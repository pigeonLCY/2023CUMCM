import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  #导入库函数
#Loading the data again
data = pd.read_excel("附件.xlsx", header=None)

# 问题四平面图
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(10,8))
plt.imshow(data,cmap='rainbow', extent=[0,4,5,0])
plt.colorbar( label='Depth (m) ' )

#坐标轴说明
plt.title( '海水深度图' )
plt.xlabel( '东西方向(海里) ' )
plt.ylabel( '南北方向(海里) ' )
plt.show( )



plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 问题四立体图
x = np.linspace(0, 4, data.shape[1])
y = np.linspace(0, 5, data.shape[0])
X,Y = np.meshgrid(x, y)
fig = plt.figure(figsize=(11,8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, data, cmap='rainbow')
fig.colorbar(surf, ax=ax, label='深度(m) ')

#坐标轴说明
ax.set_xlabel('东西距离(m) ')
ax.set_ylabel('南北距离(m) ')
ax.set_zlabel('深度(m) ')
ax.set_title(' 3D海深度描绘图 ')
plt.show()


#问题二结果图
distance = np.array([0,0.3,0.6,0.9,1.2,1.5,1.8,2.1])
#海里
angle = np.array([0,45,90,135,180,225,270,315])# degrees
depth_values = np.array([
[415.69,466.9,516.49,566.89,617.29,677.69,718.09,768.48],
[416.12,451.79,487.47,523.14,558.81,594.50,630.16,665.84],
[416.55,416.55,416.55,416.55,416.55,416.55,416.55,416.55],
[416.12,380.45,344.77,309.10,273.42,237.75,202.08,166.40],
[415.69,365.29,314.89,264.50,214.10,163.70,113.30,62.90],
[416.12,380.44,344.77,309.10,273.42,237.75,202.08,166.40],
[416.55,416.55,416.55,416.55,416.55,416.55,416.55,416.55],
[416.12,451.79,487.47,523.14,558.81,594.50,630.16,665.84]
])
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
#Plotting
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111,projection='3d' )
X, Y = np.meshgrid(angle, distance)
ax.plot_surface(X, Y,depth_values, cmap="rainbow" )
surf = ax.plot_surface(X, Y, depth_values, cmap='rainbow')
fig.colorbar(surf, ax=ax, label='深度(m) ')
ax.set_xlabel( '角度 ( °)')
ax.set_ylabel( '距离 (m) ')
ax.set_zlabel( '深度 (m) ')
ax.set_title( '深度随角度、距离变化图' )
plt.show()


#问题三结果图

vertical_lines = [2*1852,3329.7286,2922.1109,2478.1758,1994.6875,1468.122,894.6413,
270.065,4021.66,4315.3085,4586.745,4837.6568,5069.5934,5283.9907,5482.1749,
5665.372,5834.7157,5991.2533,6135.9533,6269.71084,6393.353,6507.6460,6613.2956,
6710.955,6801.230,6884.67910378118,6961.816,7033.1214,7099.0337,7159.9617,7216.2822,7268.34374,
7316.468,7360.95,7402.0747]
sea_width = 4 * 1852
sea_length = 2 * 1852



# 设置支持中文显示的字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号'-'显示为方块的问题

# 重新绘制图形
plt.figure(figsize=(12, 7))
for line in vertical_lines:
    plt.plot([line, line], [0, sea_length], 'b-', linewidth=2.5)  # 设置线宽为2.5

plt.xlim(0, sea_width)
plt.ylim(0, sea_length)
plt.xlabel('东西方向 (m)', fontsize=14)  # 设置坐标轴标签的字体大小
plt.ylabel('南北方向 (m)', fontsize=14)
plt.title('测线实际位置', fontsize=16)  # 设置标题的字体大小
plt.xticks(fontsize=12)  # 设置x轴刻度的字体大小
plt.yticks(fontsize=12)  # 设置y轴刻度的字体大小
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()  # 调整布局，使图形适应窗口大小
plt.show()

y_lines = [6296.8,6520.63495924049,6749.44899157505,6983.35285346889,7222.45976509771,7466.88546515143,7716.74826685704,7972.16911524760,8233.27164570516,8500.18224380599,8773.03010649692,9051.94730463263,6082.49903125956,5872.76201313491,5667.49174753430,5466.59310638596,5269.97298755308,5077.54027168762,4889.20578000301,4704.88223294619,4524.48420974976,4347.92810884558,4175.13210912143,4006.01613200279,3840.50180434214,3678.51242209863,3519.97291479123,3364.80981070895,3212.95120286198,3064.32671565791,2918.86747228770,2776.50606280622,2637.17651289255,2500.81425327563,2367.35608981100,2236.74017419482,2108.90597530169,1983.79425113271,1861.34702136112,1741.50754046254,1624.22027141750,1509.43085997398,1397.08610945814,1287.13395612146,1179.52344501288,1074.20470636491,971.128932482488,870.248355124133,771.516223364797,674.886781930148,580.315249992274,487.757800416983,397.171539453055,308.514486854066,221.745556423546,136.824536974473,53.7120736942597]

x_lines = [1749.1,2010.17159958911,2295.61454474997,2607.71721266851,2948.96956089866,3322.09410337448,3730.06763064792,4176.14495874731,4663.88489612549,5197.17863586170,5780.28079963083,6417.84338110877,7114.95285961476,1529.14019123556,1326.48041303346,1139.76943449067,967.752126381097,809.272134898000,663.264108284280,528.746535206882,404.815146732568,290.636837551103,185.444065582441,88.5296923203143]




sea_width = 4 * 1852
sea_length = 5 * 1852

alpha = 0.006978502015452

# 设置支持中文显示的字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号'-'显示为方块的问题

# 重新绘制图形
plt.figure(figsize=(12, 7))
for y in y_lines:
   plt.plot([-y*2.5001,(sea_length-y)*2.5001], [0, sea_length], 'b-', linewidth=2.5)  # 设置线宽为2.5

for i in range(0,23):
   plt.plot([x_lines[i],sea_length/1.6364+x_lines[i]], [0, sea_length], 'b-', linewidth=2.5)


plt.xlim(0, sea_width)
plt.ylim(0, sea_length)
plt.xlabel('东西方向 (m)', fontsize=14)  # 设置坐标轴标签的字体大小
plt.ylabel('南北方向 (m)', fontsize=14)
plt.title('测线实际位置', fontsize=16)  # 设置标题的字体大小
plt.xticks(fontsize=12)  # 设置x轴刻度的字体大小
plt.yticks(fontsize=12)  # 设置y轴刻度的字体大小
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()  # 调整布局，使图形适应窗口大小
plt.show()