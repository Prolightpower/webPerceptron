import random

class Perceptron:
    def __init__(self, n_inputs, lr=0.1):
        self.weights = [random.uniform(-0.5, 0.5) for _ in range(n_inputs)]
        self.bias = random.uniform(-0.5, 0.5)
        self.lr = lr

    def activation(self, x):
        return 1 if x >= 0 else 0

    def predict(self, inputs):
        total = sum(w * i for w, i in zip(self.weights, inputs)) + self.bias
        return self.activation(total)

    def train(self, training_data, epochs=100):
        for _ in range(epochs):
            shuffled = training_data[:]
            random.shuffle(shuffled)
            for sample in shuffled:
                inputs = sample["input"]
                target = 1 if sample["output"] == "L" else 0
                output = self.predict(inputs)
                error = target - output
                for i in range(len(self.weights)):
                    self.weights[i] += self.lr * error * inputs[i]
                self.bias += self.lr * error

def classify(p, input_list):
    return "L" if p.predict(input_list) == 1 else "T"
