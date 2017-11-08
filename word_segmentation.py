# coding:utf-8
# word_segmentation.py
# by Yasuhiro Taguchi and Kazutoshi Sasahara
# Last update: 2017.11.08
# Released under the MIT license

# This program segments Japanese sentences into words.
# This preprosessing is required before using J-MFD.
# Fist, you need to install Anaconda (Python3.6), MeCab, mecab-python3, and neologd.
# - Anaconda https://www.anaconda.com/
# - MeCab http://taku910.github.io/mecab/
# - mecab-python3 https://github.com/SamuraiT/mecab-python3
# - neologd https://github.com/neologd/mecab-ipadic-neologd
# Second, set neologd_path.
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
neologd_path = '/usr/local/lib/mecab/dic/mecab-ipadic-neologd'


if __name__ == '__main__':
    m = MeCab.Tagger('-d ' + neologd_path)
    segmented_str = ''

    # input texts and segment into words
    with open(fpath) as f:
        for line in f:
            m.parse('')
            node = m.parseToNode(line)
            while node:
                word = node.surface
                word = re.sub('[、,。]', '', word) # remove special character
                if word != '':
                    segmented_str += word + ' '
                node = node.next
            segmented_str += '\n'

    # output segmented texts
    with open(opath,'w') as f:
        f.write(segmented_str)
