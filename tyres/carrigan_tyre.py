from tyre import Tyre

class CarriganTyre(Tyre):

    def __init__(self, tyre_life):
        self.tyre_life = tyre_life

    def needs_service(self):
        return max(self.tyre_life) > 0.9