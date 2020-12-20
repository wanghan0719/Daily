"""
文本分词
"""
import nltk.tokenize as tk
import numpy as np

doc = "Are you curious about tokenization? " \
      "Let's see how it works! " \
      "We need to analyze a couple of sentences " \
      "with punctuations to see it in action."
print(doc)
print('-' * 15)
# 按句子拆分
tokens = tk.sent_tokenize(doc)  # 返回拆分后的list
print(tokens)
# for i, token in enumerate(tokens):
#     print("%2d" % (i + 1), token)
print('-' * 15)
# 按单词拆分
tokens = tk.word_tokenize(doc)  # 返回拆分后的list
print(tokens)
# for i, token in enumerate(tokens):
#     print("%2d" % (i + 1), token)
print('-' * 15)
#  把样本按单词进行拆分 创建分词器对象
tokenizer = tk.WordPunctTokenizer()  # 创建分词器对象
tokens = tokenizer.tokenize(doc)  # 返回拆分后的list
print(tokens)
# for i, token in enumerate(tokens):
#     print("%2d" % (i + 1), token)

"""
词干提取
"""
import nltk.stem.porter as pt
import nltk.stem.lancaster as lc
import nltk.stem.snowball as sb

words = ['table', 'probably', 'wolves', 'playing',
         'is', 'dog', 'the', 'beaches', 'grounded',
         'dreamt', 'envision']
pt_stemmer = pt.PorterStemmer()  # 波特词干提取器，偏宽松
lc_stemmer = lc.LancasterStemmer()  # 朗卡斯特词干提取器，偏严格
sb_stemmer = sb.SnowballStemmer('english')  # 思诺博词干提取器，偏中庸
for word in words:
    pt_stem = pt_stemmer.stem(word)
    lc_stem = lc_stemmer.stem(word)
    sb_stem = sb_stemmer.stem(word)
    # print('%8s %8s %8s %8s' % (
    #     word, pt_stem, lc_stem, sb_stem))
print('-' * 15)

"""
词性还原
"""
import nltk.stem as ns

words = ['table', 'probably', 'wolves', 'playing',
         'is', 'dog', 'the', 'beaches', 'grounded',
         'dreamt', 'envision']
# 获取词性还原器对象
lemmatizer = ns.WordNetLemmatizer()
for word in words:
    # 把单词word按照名词进行还原
    n_lemma = lemmatizer.lemmatize(word, pos='n')
    # 把单词word按照动词进行还原
    v_lemma = lemmatizer.lemmatize(word, pos='v')
    print('%8s %8s %8s' % (word, n_lemma, v_lemma))
print('-' * 15)

"""
 词袋模型
"""
import nltk.tokenize as tk
import sklearn.feature_extraction.text as ft
import sklearn.preprocessing as sp

doc = 'The brown dog is running. ' \
      'The black dog is in the black room. ' \
      'Running in the room is forbidden.'
print(doc)
sentences = tk.sent_tokenize(doc)
print(sentences)
# 构建词袋模型对象
cv = ft.CountVectorizer()
# 训练模型，把句子中所有可能出现的单词作为特征名，每一个句子为一个样本，单词在句子中出现的次数为特征值。
bow = cv.fit_transform(sentences).toarray()
print(bow)
words = cv.get_feature_names()
print(words)
print('-' * 15)

"""
词频（TF）
    单词在句子中出现的次数除以句子的总词数称为词频。
"""
tf = sp.normalize(bow, norm='l1')  # 对词袋矩阵进行归一化处理
print(tf)
print('-' * 15)

"""
文档频率（DF）
    含有某个单词的文档样本数/总文档样本数  DF越高，语义贡献越小
逆文档频率（IDF）
    总样本数/含有某个单词的样本数  IDF越高，语义贡献越大
词频-逆文档频率(TF-IDF)
    词频矩阵中的每一个元素乘以相应单词的逆文档频率，其值越大说明该词对样本语义的贡献越大，根据每个词的贡献力度，构建学习模型。
"""
tt = ft.TfidfTransformer()
tfidf = tt.fit_transform(bow).toarray()
print(np.round(tfidf, 2))
words = cv.get_feature_names()
print(words)