import nltk
from nltk.corpus import gutenberg, brown

# 下载更多语料库
nltk.download('gutenberg')
nltk.download('brown')

# 获取并输出更多单词
emma = gutenberg.words('austen-emma.txt')
print("Gutenberg Emma 前 50 个单词:")
print(emma[:50])

brown_words = brown.words()
print("\nBrown 语料库前 50 个单词:")
print(brown_words[:50])