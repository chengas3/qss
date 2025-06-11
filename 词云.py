from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 示例文本
text = "自然语言处理是人工智能领域的一个重要方向，它涉及到语言的生成、理解和翻译等多个任务。"

# 生成词云
wordcloud = WordCloud(
    background_color='pink',  # 设置背景颜色
    font_path='simhei.ttf',    # 设置字体路径（确保支持中文）
    width=800, height=600,     # 设置词云图的大小
    max_words=100,             # 设置最多显示的单词数
    min_font_size=10,          # 设置最小字体大小
    max_font_size=100,         # 设置最大字体大小
).generate(text)

# 显示词云
plt.figure(figsize=(10, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()