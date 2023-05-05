import numpy as np
import matplotlib.pyplot as plt

# 准备数据
x_labels = ['protein/defect&&etest', 'drug/tispc', 'disease/label', 'drug-disease/tispc-label', 'drug-protein/tispc-defect&etest','protein-protein/none','disease-protein/label-defect&etest']
x = np.arange(len(x_labels))
y1 = [5008, 610, 264, 5130, 6823,38034,528]
y2 = [800, 200, 100, 5000, 34000,0,17000]

# 计算并列柱状图的横坐标
bar_width = 0.35
x_position = x - bar_width / 2

# 绘制柱状图
plt.bar(x_position, y1, width=bar_width, label='药物疾病数据')
plt.bar(x_position + bar_width, y2, width=bar_width, label='半导体领域数据')

# 设置x轴刻度标签
plt.xticks(x, x_labels)
#plt.xticks(fontsize=4)
plt.tight_layout()

# 添加标签和标题
plt.xlabel('数据类型')
plt.ylabel('数值')
plt.title('数据对比')

# 添加图例
plt.legend()

# 显示图像
plt.show()

# 保存图片
plt.savefig('bar_chart_compare.png')
