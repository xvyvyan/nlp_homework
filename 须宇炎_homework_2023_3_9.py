'''
作业：
读一个文本，该文本每一行前半部分为中文，后半部分为英文，用空格做分隔符
具体需求如下：
1. 输出两个 list，一个存放中文，一个存放英文（如果有某一行没有英文或没有中文，将这一行忽略）
2. 对中文的每个汉字做一个映射（word to index），key是汉字，value是对应的索引,索引从0开始
3. 对英文做一个字典，key是出现的英文字母，value 是该字母在文本中出现的次数
'''

import os

def get_data(file):
    with  open(file, encoding='utf-8') as f:
        all_data = f.read().split('\n')

    chinese_data, english_data = [], []
    for data in all_data:
        try:
            ch, en = data.split(' ')
        except:
            continue
        chinese_data.append(ch)
        english_data.append(en)

    return chinese_data, english_data

def build_chinese_vocab(chinese_data):
    chinese_vocab={}

    for sentence in chinese_data:
        for ch in sentence:
            chinese_vocab[ch]=chinese_vocab.get(ch,len(chinese_vocab))

    return chinese_vocab

def count_en_num(english_data):
    english_dict = {}

    for sentence in english_data:
        for ch in sentence:
            english_dict[ch]=english_dict.get(ch,0)+1
    return english_dict


if __name__ == '__main__':
    chinese_data, english_data = get_data(os.path.join('.', 'data', 'text.txt'))

    chinese_vocab=build_chinese_vocab(chinese_data)

    english_dict=count_en_num(english_data)








