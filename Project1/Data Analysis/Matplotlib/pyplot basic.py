from matplotlib import pyplot as plt
import random

x = range(2,26,2)
y = range(1,13)
x2 = [random.randint(1,24) for i in range(5)]
y2 = [random.randint(1,24) for e in range(5)]
# 图片大小
plt.figure(figsize=(20,8), dpi=100)
# 绘图
plt.plot(x,y,label='set1',color='orange',linestyle=':',linewidth=3)
plt.plot(x2,y2,label='set2',color='cyan',linestyle='-.',linewidth=3)
# xy轴刻度设置
plt.xticks(range(2,25))
plt.yticks(range(min(y),max(y)+1))
# 保存
# plt.savefig('draw.png')
# 添加描述信息
plt.xlabel('time')
plt.ylabel('Speed')
plt.title('Chart')
# 添加网格
plt.grid(alpha=0.1) #alpha=透明度
# 添加图例
plt.legend(prop='Calibri',loc='upper left')
# 展示
plt.show()

