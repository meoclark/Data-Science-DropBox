from prep import num_encoder_tokens, num_decoder_tokens

from tensorflow import keras
# Add Dense to the imported layers
from keras.layers import Input, LSTM, Dense
from keras.models import Model

# Encoder training setup
encoder_inputs = Input(shape=(None, num_encoder_tokens))
encoder_lstm = LSTM(256, return_state=True)
encoder_outputs, state_hidden, state_cell = encoder_lstm(encoder_inputs)
encoder_states = [state_hidden, state_cell]

# The decoder input and LSTM layers:
decoder_inputs = Input(shape=(None, num_decoder_tokens))
decoder_lstm = LSTM(256, return_sequences=True, return_state=True)

# Retrieve the LSTM outputs and states:
decoder_outputs, decoder_state_hidden, decoder_state_cell = decoder_lstm(decoder_inputs, initial_state=encoder_states)

# Build a final Dense layer:
decoder_dense = Dense(num_decoder_tokens, activation='softmax')

# Filter outputs through the Dense layer:
decoder_outputs = decoder_dense(decoder_outputs)


#We also need to run the output through a final activation layer,
#using the Softmax function, that will give us the probability distribution — where all probabilities sum to one — for each token.