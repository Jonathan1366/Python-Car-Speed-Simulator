class Car:
  def __init__(self, color, brand, year, speed):
    self.color = color
    self.brand = brand
    self.year = year
    self.speed = speed

  def addSpeed2(self):
    self.speed += 40

class SportCar23(Car):
  def nos(self):
    self.speed += 100

  def addSpeed2(self):
    super().addSpeed2()
    print("Be careful, your speed is increasing !!\n")

wheel4 = Car("red", "BMW", "2024", 400)
wheel4.addSpeed2()
print(f"My car's speed after 1 week is {wheel4.speed}")

wheel4fast = SportCar23("red", "BMW", "2024", 400)
wheel4fast.addSpeed2()
print(f"Your sport car speed's is {wheel4fast.speed}")
