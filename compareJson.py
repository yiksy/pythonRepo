import os

def search_files(folder_path, search_term):
    # 遍历文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            with open(file_path, 'r') as file:
                try:
                    content = file.read()
                    if search_term in content:
                        # 找到匹配的数据
                        print(f"在文件 {file_path} 中找到匹配的数据")
                except UnicodeDecodeError:
                    print(f"无法解码文件 {file_path}")

# 指定文件夹路径和要搜索的字符串
folder_path = './data'  # 替换为实际的文件夹路径
search_term = '014243762'
file_path="params.json"


def read_file_to_list(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
    return lines

search_files(folder_path, file_path)




