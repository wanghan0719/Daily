# GovRptWordCloudv2.py
import jieba
import wordcloud
from imageio import imread

mask = imread("chinamap.jpg")
excludes = {}
f = open("新时代中国特色社会主义.txt", "r", encoding="utf-8")
t = f.read()
f.close()

ls = jieba.lcut(t)
jieba.suggest_freq('的', False)
txt = " ".join(ls)
w = wordcloud.WordCloud(width=1000, height=700, background_color="white",
                        font_path="msyh.ttc", mask=mask
                        )
w.generate(txt)
w.to_file("grwordcloudm.png")
