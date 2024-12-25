# 读取 Markdown 文件并提取标题和正文

def read_markdown(file_path):
    """
    读取 Markdown 文件，将第一行赋值给标题变量，其余内容赋值给正文变量。
    :param file_path: Markdown 文件路径
    :return: 标题和正文
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 提取标题和正文
    title = lines[0].strip() if lines else ""
    body = "".join(lines[1:]).strip() if len(lines) > 1 else ""

    return title, body

# 示例用法
if __name__ == "__main__":
    file_path = "C:\\Users\\23512\Desktop\\Stellar-Code-Dreams-KCL\\digital-signal-processing-7ccemdsp\\note.md"  # 替换为你的 Markdown 文件路径
    title, body = read_markdown(file_path)

    print("标题:", title)
    print("正文:", body)
