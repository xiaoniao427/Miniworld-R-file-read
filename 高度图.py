import ast
import numpy as np
from PIL import Image

# 读取并解析数据文件
with open('出云', 'r', encoding='utf-8') as f:
    data = ast.literal_eval(f.read())

# 提取所有x和z坐标以确定范围
x_coords = [point[0] for point in data]
z_coords = [point[1] for point in data]

x_min = min(x_coords)
x_max = max(x_coords)
z_min = min(z_coords)
z_max = max(z_coords)

# 计算图像的宽度和高度
width = x_max - x_min + 1
height = z_max - z_min + 1

# 初始化图像数组为全黑（0）
image_array = np.zeros((height, width), dtype=np.uint8)

# 填充每个数据点到图像数组
for point in data:
    x, z, k,h = point
    # 转换坐标到图像的行和列
    col = x - x_min
    row = z_max - z  # 使得较大的z值位于图像上方
    # 确保行列在有效范围内
    if 0 <= row < height and 0 <= col < width:
        gray_value = max(0, min(255, h - 62))
        image_array[row, col] = gray_value

# 创建并保存灰度图像
img = Image.fromarray(image_array, mode='L')
img.save('height_map.png')