from tyre import Tyre

class OctoprimeTyre(Tyre):

    def __init__(self, tyre_life):
        self.tyre_life = tyre_life

    def needs_service(self):
        return sum(self.tyre_life) > 3