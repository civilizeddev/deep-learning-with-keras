from __future__ import print_function
import numpy as np
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.optimizers import SGD
from keras.utils import np_utils

np.random.seed(1671)

# 네트워크와 학습 설정
NB_EPOCH = 20
BATCH_SIZE = 128
VERBOSE = 1
NB_CLASSES = 10
OPTIMIZER = SGD()
N_HIDDEN = 128
VALIDATION_SPLIT = 0.2

# 데이터: 무작위로 섞고, 학습 데이터와 테스트 데이터로 나눔
(x_train, y_train), (x_test, y_test) = mnist.load_data()

RESHAPED = 28 * 28

x_train = x_train.reshape(60_000, RESHAPED)
x_test = x_test.reshape(10_000, RESHAPED)
x_train = x_train.astype("float32")
x_test = x_test.astype("float32")

# 정규화
x_train /= 255
x_test /= 255

print(x_train.shape[0], "train samples")
print(x_test.shape[0], "test samples")

y_train = np_utils.to_categorical(y_train, NB_CLASSES)
y_test = np_utils.to_categorical(y_test, NB_CLASSES)

model = Sequential()
model.add(Dense(N_HIDDEN, input_shape=(RESHAPED,)))
model.add(Activation("relu"))
model.add(Dense(N_HIDDEN))
model.add(Activation("relu"))
model.add(Dense(NB_CLASSES))
model.add(Activation("softmax"))
model.summary()

model.compile(
    loss="categorical_crossentropy", optimizer=OPTIMIZER, metrics=["accuracy"]
)

history = model.fit(
    x_train,
    y_train,
    batch_size=BATCH_SIZE,
    epochs=NB_EPOCH,
    verbose=VERBOSE,
    validation_split=VALIDATION_SPLIT,
)

score = model.evaluate(x_test, y_test, verbose=VERBOSE)
print("Test score:", score[0])
print("Test accuracy:", score[1])
