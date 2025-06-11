import nltk
from nltk import word_tokenize, pos_tag

# 下载必要的语料库
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

# 待进行词性标注的文本
text = "I love natural language processing and machine learning."

# 分词
tokens = word_tokenize(text)

# 词性标注
tagged = pos_tag(tokens)

print("词性标注结果：")
print(tagged)