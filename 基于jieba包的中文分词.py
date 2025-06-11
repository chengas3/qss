import jieba

# 待分词的文本
text = "我爱自然语言处理，它是一个非常有趣的研究领域。"

# 进行分词
words = jieba.cut(text)

# 输出分词结果
print("分词结果（默认精确模式）：")
print("/ ".join(words))

# 使用全模式分词
words_full = jieba.cut(text, cut_all=True)
print("\n分词结果（全模式）：")
print("/ ".join(words_full))