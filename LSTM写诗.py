import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

# 加载更大的诗歌数据集
with open('C:\\Users\\20938\\Desktop\\自然语言处理大礼包\\自然语言处理大礼包\\项目架构示例\\models\\poetry.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# 构建字符映射
chars = sorted(list(set(text)))
char_to_int = dict((c, i) for i, c in enumerate(chars))
int_to_char = dict((i, c) for i, c in enumerate(chars))

# 准备训练数据
seq_length = 40
dataX = []
dataY = []
for i in range(0, len(text) - seq_length, 1):
    seq_in = text[i:i + seq_length]
    seq_out = text[i + seq_length]
    dataX.append([char_to_int[char] for char in seq_in])
    dataY.append(char_to_int[seq_out])

# 转换数据格式并归一化
X = np.reshape(dataX, (len(dataX), seq_length, 1))
X = X / float(len(chars))
y = to_categorical(dataY)

# 构建 LSTM 模型
model = Sequential()
model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2])))
model.add(Dense(y.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')

# 使用回调函数
early_stopping = EarlyStopping(monitor='loss', patience=10, min_delta=0.001)
model_checkpoint = ModelCheckpoint('C:\\Users\\20938\\Desktop\\自然语言处理大礼包\\自然语言处理大礼包\\项目架构示例\\data\\best_poetry_model.h5', monitor='loss', save_best_only=True, mode='min')

# 训练模型
model.fit(X, y, epochs=2, batch_size=32, callbacks=[early_stopping, model_checkpoint], verbose=1)

# 加载最佳模型
model.load_weights('C:\\Users\\20938\\Desktop\\自然语言处理大礼包\\自然语言处理大礼包\\项目架构示例\\data\\best_poetry_model.h5')

# 生成诗歌
def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

start = np.random.randint(0, len(dataX) - 1)
pattern = dataX[start]
print("Seed:")
print("\"", ''.join([int_to_char[value] for value in pattern]), "\"")

# 生成 100 个字符
for i in range(100):
    x = np.reshape(pattern, (1, len(pattern), 1))
    x = x / float(len(chars))
    prediction = model.predict(x, verbose=0)
    index = sample(prediction[0], temperature=0.5)
    result = int_to_char[index]
    seq_in = [int_to_char[value] for value in pattern]
    print(result, end="")
    pattern.append(index)
    pattern = pattern[1:len(pattern)]