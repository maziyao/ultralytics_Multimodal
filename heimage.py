import cv2
import os

# 设置三个文件夹的路径
path="path"
folder_path1 =path+ 'rcs'
folder_path2 =path+ 'x'
folder_path3 =path+ 'y'

# 获取每个文件夹中的文件列表
files1 = sorted(os.listdir(folder_path1))
files2 = sorted(os.listdir(folder_path2))
files3 = sorted(os.listdir(folder_path3))
# print(files1,files2,files3)
# 确保三个文件夹中的文件数量相同
assert len(files1) == len(files2) == len(files3), "三个文件夹中的文件数量必须相同"

# 确保文件名相同
assert files1 == files2 == files3, "三个文件夹中的文件名必须完全相同"

# 设置目标文件夹的路径
output_folder =path+ 'he'

# 获取每个文件夹中的文件列表
files1 = sorted(os.listdir(folder_path1))

# 确保目标文件夹存在，如果不存在则创建
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历文件列表，读取、转换并合并图片
for file in files1:  # 可以使用files1, files2或files3，因为它们的文件名是相同的
    # 读取图片
    image1 = cv2.imread(os.path.join(folder_path1, file))
    image2 = cv2.imread(os.path.join(folder_path2, file))
    image3 = cv2.imread(os.path.join(folder_path3, file))
    
    # 转换为灰度图
    gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    gray_image3 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)
    
    # 将灰度图合并为一张三通道的图片
    merged = cv2.merge((gray_image1, gray_image2, gray_image3))
    
    # 保存合并后的图片到目标文件夹，保持原来的文件名
    output_path = os.path.join(output_folder, file)
    cv2.imwrite(output_path, merged)
