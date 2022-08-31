class Animal:
    def __init__(self):
        self.num_eye=2
        self.num_feet=4

    def breathe(self):
        print("inhale and exhale ")


class Fish(Animal):
    def __init__(self):
        super().__init__()
        self.num_feet=0

    def breathe(self):
        super().breathe()
        return "🌿🌿🌿🌿change origin method🌿🌿🌿🌿"

nemo=Fish()
print(f"num_feet = {nemo.num_feet} and method={nemo.breathe()}")