import numpy as np
import tensorflow as tf
'''
Neural Network Classifier
'''

class NeuralNetworkClassifier():
    def __init__(self, sampleLen, numAuthors, debug=True):
        self.debug = debug
        self.sampleLen = sampleLen
        self.numAuthors = numAuthors
        self.feature_column = [tf.feature_column.numeric_column("x", shape=[self.sampleLen])]
        # 3 Layers
        self.classifier = tf.estimator.DNNClassifier(feature_columns=self.feature_column,
                                                hidden_units=[6, 12, 24, 6],
                                                n_classes=self.numAuthors,
                                                model_dir="/tmp/authorship_classifier_model")

    def train(self, samples, authors):
        if self.debug:
            print "NeuralNetworkClassifier Training Started"

        self.train_inputs = tf.estimator.inputs.numpy_input_fn(
            x={"x": np.array(samples)},
            y=np.array(authors),
            num_epochs=None,
            shuffle=True)
        for i in range(50):
            self.classifier.train(input_fn=self.train_inputs, steps=800)
            if self.debug:
                print "Trained " + str((i+1)*800) + " steps"

        if self.debug:
            print "NeuralNetworkClassifier Trained Successfully"

    def run(self, data):
        if self.debug:
            print "NeuralNetworkClassifier Classification Started"

        self.predict_input = tf.estimator.inputs.numpy_input_fn(
            x={"x": np.array([data])},
            num_epochs=1,
            shuffle=False)
        classification = self.classifier.predict(input_fn=self.predict_input)
        classification = list(classification)[0]['classes'][0]
        if self.debug:
            print "NeuralNetworkClassifier Classification Finished"
        return int(classification)

    def getPredictions(self, data):
        if self.debug:
            print "NeuralNetworkClassifier Classification Started"

        self.predict_input = tf.estimator.inputs.numpy_input_fn(
            x={"x": np.array(data)},
            num_epochs=1,
            shuffle=False)
        classification = list(self.classifier.predict(input_fn=self.predict_input))
        probabilities = []
        for s in classification:
            probabilities.append(s['probabilities'])
        if self.debug:
            print "NeuralNetworkClassifier Classification Finished"
        return probabilities

    def testAccuracy(self, samples, authors):
        if self.debug:
            print "NeuralNetworkClassifier Accuracy Evaluation Started"
        self.test_input = tf.estimator.inputs.numpy_input_fn(
            x={"x": np.array(samples)},
            y=np.array(authors),
            num_epochs=1,
            shuffle=False)
        accuracy = self.classifier.evaluate(input_fn=self.test_input)["accuracy"]

        print "Accuracy " + str(accuracy)
        if self.debug:
            print "NeuralNetworkClassifier Accuracy Evauation Successfully"
        return accuracy
