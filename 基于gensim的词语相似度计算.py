from gensim.models import Word2Vec
import numpy as np

# 示例语料
sentences = [
    ["cat", "say", "meow"],
    ["dog", "say", "woof"],
    ["bird", "fly", "sky"],
    ["fish", "swim", "water"],
]

# 训练 Word2Vec 模型
model = Word2Vec(sentences, vector_size=100, min_count=1)

# 计算词语相似度
similarity = model.wv.similarity('cat', 'dog')
print(f"词语 'cat' 和 'dog' 的相似度: {similarity}")

# 使用预训练的词向量模型
from gensim.models import KeyedVectors

# 加载预训练的词向量模型（如 Google News 词向量）
model_path = 'C:\\Users\\20938\\Desktop\\自然语言处理大礼包\\自然语言处理大礼包\\项目架构示例\\models\\GoogleNews-vectors-negative300.bin'
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

# 计算词语相似度
similarity = model.similarity('cat', 'dog')
print(f"使用预训练模型计算的词语 'cat' 和 'dog' 的相似度: {similarity}")