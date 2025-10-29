import os

base_path = r"E:\vscode\gradio-learning"

def print_tree(path, prefix=""):
    # 获取当前目录下的文件和文件夹
    entries = sorted(os.listdir(path))
    for i, name in enumerate(entries):
        full_path = os.path.join(path, name)
        connector = "└── " if i == len(entries) - 1 else "├── "
        print(prefix + connector + name)

        # 如果是文件夹，则递归打印其内容
        if os.path.isdir(full_path):
            new_prefix = prefix + ("    " if i == len(entries) - 1 else "│   ")
            print_tree(full_path, new_prefix)

if __name__ == "__main__":
    print(os.path.basename(base_path) + "/")
    print_tree(base_path)
