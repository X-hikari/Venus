def read_and_convert_md(file_path):
    # 打开文件并读取所有内容
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 将换行符替换为 '\n'
    content_with_newline = content.replace('\n', '\\n')
    
    return content_with_newline

# 例如，调用函数并传入文件路径
md_file_path = './article2.md'
converted_content = read_and_convert_md(md_file_path)

# 输出结果
print(converted_content)
