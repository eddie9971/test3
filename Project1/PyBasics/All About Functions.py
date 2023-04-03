# 1. 读取文件中每一行数据，将包含特定关键词数据选出来，并以列表的形势返回
import os


def select_content(file_path, key):
    if not os.path.exists(file_path):
        return
    data_list = []
    with open (file_path, mode='r', encoding='utf-8') as file_object:
        for line in file_object:
            if key in line:
                data_list.append(line)
    return data_list


result = select_content('F:\Eddie\小红书数据', '纽约')
# if result == None:
#     print('File does not exist')
# else:
#     print(result)


# 2. 替换敏感词
def change_string(text):
    sensitive_words = ['fuck', 'shit']
    for word in sensitive_words:
        text = text.replace(word, '**')
    return text

text = 'fuck this shit that cunt cock asshole'
changed_text = change_string(text)
print(changed_text)