from keras.layers import LSTM, Dense
from keras.models import Sequential
from keras.utils.vis_utils import plot_model

class Rnn():
    def __init__(self, feature_size, time):
        self.model = Sequential()
        self.model.add(LSTM(3, batch_input_shape=(None, time, feature_size), return_sequences=True))
        self.model.add(LSTM(3, batch_input_shape=(None, time, feature_size), return_sequences=True))
        self.model.add(LSTM(3, activation='relu'))
        self.model.add(Dense(3))
        self.model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

    def fit(self, x, y):
        self.model.fit(x, y, epochs=1000)
        plot_model(self.model, to_file='model.png', show_shapes=True, show_layer_names=True)

    def predict(self, x):
        return self.model.predict(x)

    def evaluate(self, x, y):
        return self.model.evaluate(x, y)