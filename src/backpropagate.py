class GradientDescent:
    def __init__(self, learning_rate=0.01):
        self.learning_rate = learning_rate

    def update(self, weights, gradients):
        """
        Update the weights using the computed gradients.

        :param weights: Current weights of the model.
        :param gradients: Gradients computed from the loss function.
        :return: Updated weights.
        """
        return weights - self.learning_rate * gradients

    def compute_gradients(self, loss, weights):
        pass

class SGD(GradientDescent):
    pass

class Momentum(GradientDescent):
    pass
