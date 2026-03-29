import json
import random

# Load dataset
with open("dataset.json") as f:
    data = json.load(f)

class Perceptron:
    def __init__(self, n_inputs, lr=0.1):
        self.weights = [random.random() for _ in range(n_inputs)]
        self.bias = random.random()
        self.lr = lr

    def activation(self, x):
        return 1 if x >= 0 else 0

    def predict(self, inputs):
        total = sum(w*i for w,i in zip(self.weights, inputs)) + self.bias
        return self.activation(total)

    def train(self, training_data, epochs=10):
        for _ in range(epochs):
            random.shuffle(training_data)
            for sample in training_data:
                inputs = sample["input"]
                target = 1 if sample["output"]=="L" else 0
                output = self.predict(inputs)
                error = target - output
                for i in range(len(self.weights)):
                    self.weights[i] += self.lr * error * inputs[i]
                self.bias += self.lr * error

# Initialize Perceptron
n_inputs = len(data[0]["input"])
p = Perceptron(n_inputs)
p.train(data, epochs=20)

# Function for PyScript to call
def classify(input_list):
    result = p.predict(input_list)
    return "L" if result == 1 else "T"