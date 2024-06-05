D0 = 110;
h = 1852;

theta = 120;
alpha = 1.5;
theta_r = deg2rad(theta); 
alpha_r = deg2rad(alpha);

m_arg = sin(theta_r) * cos(alpha_r) * cos(alpha_r) / (cos(theta_r / 2 + alpha_r) * cos(theta_r / 2 - alpha_r));
d_sum = 0;
all_sum = [];
all_d = [];
while d_sum < 2 * h
    k1 = 0.9 * (D0 - d_sum * tan(alpha_r)) * m_arg;
    k2 = 1 + 0.9 * tan(alpha_r) * m_arg;
    d = k1 / k2;
    d_sum = d_sum + d;
    all_d = [all_d d];
    all_sum = [all_sum d_sum];
end

all = zeros(1, length(all_sum));
for i = 1 : length(all_sum)
    all(i) = all_sum(i) + 2 * h;
end
