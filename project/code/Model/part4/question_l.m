h = 1852;
ab = 5 * h;
bc = 4 * h;
bc_1 = ab * (84.4-65.2) / (84.4-24.4);
ac = sqrt(ab^2 + bc^2);
cc_1 = sqrt(bc_1 ^ 2 + (bc)^2);
arg_12 = atan(5 / 4);
arg_2 = atan(bc_1 / bc);
arg_1 = arg_12 - arg_2;
ce = cc_1 / cos(arg_1);
ee_1 = 65.2 - ce * (65.2 - 24.4) / ac;
c_1e = cc_1 * tan(arg_1);
alpha_r = atan((65.2 - ee_1) / c_1e);

theta = 120;
theta_r = deg2rad(theta); 
D0 = 65.2;

m_arg = sin(theta_r) * cos(alpha_r) * cos(alpha_r) / (cos(theta_r / 2 + alpha_r) * cos(theta_r / 2 - alpha_r));
d_sum = 0;
all_sum = [];
all_d = [];

d_max = bc_1 * cos(arg_2);
while d_sum < d_max
    k1 = 0.9 * (D0 + d_sum * tan(alpha_r)) * m_arg;
    k2 = 1 - 0.9 * tan(alpha_r) * m_arg;
    d = k1 / k2;
    d_sum = d_sum + d;
    all_d = [all_d d];
    all_sum = [all_sum d_sum];
end

all = zeros(1, length(all_sum));
for i = 1 : length(all_sum)
    all(i) = all_sum(i) / cos(arg_2);
end

len = [];
len2 = 0;

for i = 1 : length(all_sum) - 1
    len = [len (bc_1 - all(i)) * cc_1 / bc_1];
    len2 = len2 + (bc_1 - all(i)) * cc_1 / bc_1;
end

ac_1 = ab - bc_1;
final = zeros(1, length(all_sum) - 1);
for i = 1 : length(all_sum) - 1
    final(i) = ac_1 + all(i);
end