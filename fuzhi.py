import os
import shutil

# 设置文件夹路径
folder1_path = '/media/ma/文件/jd/A101498/images/rcs'
folder2_path = '/media/ma/文件/jd/A101498/data/train/images/val'
folder3_path = '/media/ma/文件/jd/A101498/data/train/images3/val'

# 获取文件夹2中所有文件的名字
files_in_folder2 = set(os.listdir(folder2_path))

# 创建文件夹3，如果它不存在的话
if not os.path.exists(folder3_path):
    os.makedirs(folder3_path)

# 遍历文件夹1中的所有文件
for filename in os.listdir(folder1_path):
    # 检查文件夹2中是否有匹配的文件
    if filename in files_in_folder2:
        # 构建源文件和目标文件的完整路径
        source_file = os.path.join(folder1_path, filename)
        destination_file = os.path.join(folder3_path, filename)
        # 复制文件到文件夹3
        shutil.copy2(source_file, destination_file)
        print(f'文件 {filename} 已复制到文件夹3。')

print('所有匹配的文件已复制完毕。')


