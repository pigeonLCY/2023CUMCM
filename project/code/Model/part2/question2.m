numdis = 8; 
numarg = 8;
haili = 1852;
W = zeros(numarg, numdis);

%角度定义与求解
theta = 120;
alpha = 1.5;
theta_r = deg2rad(theta); 
alpha_r = deg2rad(alpha);
beta = [0, 45, 90, 135, 180, 225, 270, 315];
beta_r = zeros(1, numarg);
for i = 1 : numarg
    beta_r(i) = deg2rad(beta(i));
end
alpha_s = zeros(1, numarg);%alpha'
for i = 1 : numarg
    alpha_s(i) = atan(tan(alpha_r) * sin(beta_r(i)));
end

%航行距离定义
dis0 = 0.3 * haili;
dis = [0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1];
dis_s = zeros(1, numdis);
for i = 1 : numdis
    dis_s(i) = dis(i) * haili;
end

%深度定义
D0 = 120;
D_s = zeros(numarg, numdis);
for i = 1 : numarg
    for j = 1 : numdis
        D_s(i, j) = D0 + dis_s(j) * cos(beta_r(i)) * tan(alpha_r);
    end
end

%计算覆盖宽度
for i = 1 : numarg
    for j = 1 : numdis
        W(i, j) = D_s(i, j) * sin(theta_r) * cos(alpha_s(i)) * cos(alpha_s(i)) / (cos(theta_r / 2 + alpha_s(i)) * cos(theta_r / 2 - alpha_s(i)));
    end
end

