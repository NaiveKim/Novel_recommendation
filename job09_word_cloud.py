from turtle import back

import background as background
import family
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import collections
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

font_path = './malgun.ttf'
font_name = font_manager.FontProperties(
    fname=font_path).get_name()
plt.rc('font', family='NanumBarunGothic')

df= pd.read_csv('./cleaned_comment_1480_one.csv')
words = df[df['cleaned_titles']=='구르미 그린 달빛 ']['cleaned_sentences']
print(words.iloc[0])
words = words.iloc[0].split()
print(words)

worddict = collections.Counter(words)
worddict = dict(worddict)
print(worddict)

wordcloud_img = WordCloud(
    background_color='white', max_words=2000,
    font_path=font_path).generate_from_frequencies(worddict)

plt.figure(figsize=(12, 12))
plt.imshow(wordcloud_img, interpolation='bilinear')
plt.axis('off')
plt.show()