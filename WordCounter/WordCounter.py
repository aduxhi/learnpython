from os import path
from wordcloud import WordCloud
from collections import Counter
import jieba

d = path.dirname(__file__)

f = open(path.join(d, '十九大报告.txt')).read()
words = list(jieba.cut(f))
data = dict (Counter(words).most_common(50))

with open ("十九大词频.txt",'w',encoding= 'utf-8') as fw:
	for k,v in data.items():
		fw.write("%s\t%d\n" %(k,v))

a = []

for word in words:
	if len(word)>1:
		a.append(word)
		
txt = r' '.join(a)
fpath= '/Library/Fonts/Songti.ttc'
wordcloud = WordCloud(font_path=fpath).generate(txt)

import matplotlib.pyplot as plt
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis("off")
plt.show()
		
