# coding:utf-8
# word_segmentation.py
# by Yasuhiro Taguchi and Kazutoshi Sasahara
# Last update: 2018.06.22 Released under the MIT license

# This program segments Japanese sentences into words.
# This preprosessing is required before using J-MFD.
# Fist, install Anaconda (Python3.6) https://www.anaconda.com/
# Second, install MeCab related packages:
# In the case of Ubuntu: sudo apt-get install mecab libmecab-dev mecab-ipadic-utf8; pip install mecab-python3
# In the case of Mac (Homebrew): brew install mecab mecab-ipadic; pip install mecab-python3
# Then, type
# python word_segmentation.py -f input.txt

import MeCab
import re
import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument('-f','--file',required=True)
fpath = parser.parse_args().file
opath = fpath.split('.')[0] + '_segmented.txt'

# change this based on your environment
# ipadic_path = '/usr/local/lib/mecab/dic/ipadic'

dic_words = ['等価物' ,'先入主' ,'先取権' ,'生活共同体' ,'同盟国' ,'利己主義' ,'諜報部員' ,'恐怖政治' ,'入国管理' ,'創始者' ,'資本家階級' ,'有産階級' ,'社会的地位' ,'最高位' ,'聖職者' ,'危険人物' ,'不従順' ,'運動員' ,'法律違反' ,'尻軽女' ,'不敬虔' ,'嘔吐物' ,'無差別' ,'変質者']

def execute_Mecab(segmented_str, text):

    m.parse('')
    node = m.parseToNode(text)
    while node:
        word = node.surface

        if word != '':
            segmented_str += word + ' '
        node = node.next

    return segmented_str

if __name__ == '__main__':
    m = MeCab.Tagger('-d ' + ipadic_path)
    segmented_str = ''



    # input texts and segment into words
    with open(fpath, encoding='utf-8') as f:

        for line in f:

            print(line)
            line = re.sub('[、,。]', '', line) # remove special character
            for i, word in enumerate(dic_words):

                line = re.sub(word, '\n。' + word + '\n', line)

            split = line.split('\n')
            print(split)

            for s in split:

                if len(split) > 1 and len(s) > 0 and s[0] == '。':
                    segmented_str += s[1:] + ' '

                else:
                    segmented_str = execute_Mecab(segmented_str, s)


            segmented_str += '\n'

    # output segmented texts
    with open(opath,'w', encoding='utf-8') as f:
        f.write(segmented_str)
