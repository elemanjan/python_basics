class Cat:
    paws = 4
    tail = 1

    def say(self):
        print("Meow")


class Tiger(Cat):
    color = "stripped"

    def say(self):
        print("Arrr")


sher = Tiger()

print(sher.color)
print(sher.paws)
print(sher.tail)
sher.say()
