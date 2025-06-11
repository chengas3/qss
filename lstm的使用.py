import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Input
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# 生成更复杂的数据
def generate_data():
    data = np.sin(np.linspace(0, 100, 1000)).reshape((10, 100, 1))
    target = np.cos(np.linspace(0, 100, 1000)).reshape((10, 100))
    return data, target

data, target = generate_data()

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=42)

# 构建 LSTM 模型
model = Sequential()
model.add(Input(shape=(100, 1)))
model.add(LSTM(50, activation='relu', return_sequences=True))
model.add(LSTM(50, activation='relu'))
model.add(Dense(100))
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), loss='mse')

# 使用回调函数
early_stopping = EarlyStopping(monitor='loss', patience=10, min_delta=0.001)
model_checkpoint = ModelCheckpoint('best_model.h5', monitor='loss', save_best_only=True, mode='min')

# 训练模型
model.fit(X_train, y_train, epochs=100, callbacks=[early_stopping, model_checkpoint], verbose=0)

# 加载最佳模型
model.load_weights('C:\\Users\\20938\\Desktop\\自然语言处理大礼包\\自然语言处理大礼包\\项目架构示例\\data\\best_model.h5')

# 进行预测并评估
y_pred = model.predict(X_test, verbose=0)
mse = mean_squared_error(y_test, y_pred)
print(f"测试集均方误差: {mse}")