numboat = 10;
d0 = 200;
d = [-1000, -800, -600, -400, -200, 0, 200, 400, 600, 800];
D = zeros(1, numboat);
W = zeros(1, numboat);
W1 = zeros(1, numboat);
W2 = zeros(1, numboat);
over_l = zeros(1, numboat);
over_p = zeros(1, numboat);
D(5) = 70;
theta = 120;
alpha = 1.5;
theta_r = deg2rad(theta);
alpha_r = deg2rad(alpha);

%深度
for i = 1 : numboat
    D(i) = 70 - d(i) * tan(alpha_r);
end

%覆盖宽度
for i = 1 : numboat
    W1(i) = D(i) * sin(theta_r / 2) / cos(theta_r / 2 + alpha_r);
    W2(i) = D(i) * sin(theta_r / 2) / cos(theta_r / 2 - alpha_r);
    %W(i) = (W1(i) + W2(i)) * cos(alpha_r);
    W(i) = D(i) * sin(theta_r) * cos(alpha_r) * cos(alpha_r) / (cos(theta_r / 2 + alpha_r) * cos(theta_r / 2 - alpha_r));
end

%重叠率
for i = 2 : numboat
    over_l(i) = W2(i - 1) + W1(i);
    %over_p(i) = 1 - d0 / W(i);
    over_p(i) = 1 - d0 / (over_l(i) * cos(alpha_r));
end