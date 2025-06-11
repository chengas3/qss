###在终端下载python -m spacy download en_core_web_sm

import spacy

# 下载并加载英文模型
model_name = "en_core_web_sm"

try:
    # 尝试加载模型
    nlp = spacy.load(model_name)
    print(f"成功加载 {model_name} 模型。")
except OSError:
    # 如果模型未找到，则下载并加载
    print(f"未找到 {model_name} 模型，正在下载...")
    spacy.cli.download(model_name)
    nlp = spacy.load(model_name)
    print(f"成功加载 {model_name} 模型。")

# 待进行命名实体识别的文本
text = "Bill Gates is the founder of Microsoft. Elon Musk is the CEO of Tesla."

# 处理文本
doc = nlp(text)

# 输出命名实体
print("命名实体识别结果：")
for ent in doc.ents:
    print(f"{ent.text} ({ent.label_})")