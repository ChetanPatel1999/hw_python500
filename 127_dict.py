car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("model", "00123")
print(x)
print(car)
x = car.setdefault("color", "red")

print(x)
print(car)
x = car.setdefault("price")

print(x)
print(car)