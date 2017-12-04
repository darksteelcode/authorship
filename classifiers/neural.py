import numpy as np
import tensorflow as tf
'''
Neural Network Classifier
'''

class SimpleClassifier():
    def __init__(self, sampleLen, debug=True):
        self.debug = debug
        self.sampleLen = sampleLen
        self.feature_column = [tf.feature_column.numeric_column("x", shape=[self.sampleLen])]
        # 3 Layers
        self.classifier = tf.estimator.DNNClassifier(feature_columns=self.feature_column,
                                                hidden_units=[20, 20, 10],
                                                n_classes=3,
                                                model_dir="/tmp/authorship_classifier_model")

    def train(self, samples, authors):
        if self.debug:
            print "NeuralNetworkClassifier Training Started"

        self.train_inputs = tf.estimator.inputs.numpy_input_fn(
            x={"x": np.array(samples)},
            y=np.array(authors),
            num_epochs=None,
            shuffle=True)
        self.classifier.train(input_fn=self.train_input_fn, steps=2000)

        if self.debug:
            print "NeuralNetworkClassifier Trained Successfully"
        return self.means

    def run(self, data):
        if self.debug:
            print "NeuralNetworkClassifier Classification Started"

        if self.debug:
            print "NeuralNetworkClassifier Classification Finished"
            print "Data classified to group "
