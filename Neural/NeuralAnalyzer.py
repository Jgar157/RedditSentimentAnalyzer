"""
Name: NeuralAnalyzer
Desc: Creates a Neural Network based on a file location and sets up all the weights.
        Also includes the tokenizer for the Neural network.
        Takes text inputs and returns a corresponding value based on the input.
Author: Jairo Garciga
"""

import tensorflow as tf
import pickle
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


class NeuralAnalyzer:
    """
    Creates a Neural Network based on a file location and sets up all the weights.
        Also includes the tokenizer for the Neural network.
        Takes text inputs and returns a corresponding value based on the input.
    """

    def __init__(self, neural_network_loc, tokenizer_loc, name="Neural Network"):
        """
        Constructor for the Neural Network analyzer
        :param neural_network_loc: The location of the neural network in the files
        :param tokenizer_loc: The location of the tokenizer in the files
        :param name: The name of the neural network
        """

        # The name of the Neural Network could be useful when having multiple neural networks and managing them all
        self.name = name

        # We first get the location of the neural network and tokenizer from the parameters
        self.neural_network_loc = neural_network_loc
        self.tokenizer_loc = tokenizer_loc

        # The file locations from the neural network and tokenizer are used to load the model and tokenizer
        self.neural_network = keras.models.load_model(self.neural_network_loc)
        with open(self.tokenizer_loc, 'rb') as handle:
            self.tokenizer = pickle.load(handle)
        # Creation of the Neural Network is done

    def predict_text(self, text, max_length=150, padding_type='post', trunc_type='post'):
        """
        Outputs a value for the text based on the Neural Network model
        :param max_length: The max length of the text, defaults to 150 but can be higher.
        :param padding_type: Where the padding takes place, 'pre' or 'post'
        :param trunc_type: Where the text is cut off at, 'pre' or 'post'
        :param text: The text that the neural network is predicting
        :return: A double
        """

        # We first tokenize the text into what the neural network understands.
        # Then the sequence is padded and truncated
        # Finally the neural network generates a prediction
        sequences = self.tokenizer.texts_to_sequences(text)
        padded = pad_sequences(sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)
        prediction = self.neural_network.predict(padded)

        return prediction[0]
