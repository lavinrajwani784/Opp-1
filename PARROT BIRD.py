class parrot:

    # class altribute
    species = "bird"

    # intance altribute
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sing(self,song):
        return f"{self.name} sings {song}"

    def dance(self):
        return f"{self.name} is now dancing"

# instantiate the parrot class
blu = parrot("blu" ,14)
woo = parrot("woo" ,25)

print(f"blu is a {blu.species}")
print(f"woo is a {woo.species}")

print(f"{blu.name} is {blu.age} years old")
print(f"{woo.name} is {woo.age} years old")

print(blu.sing("happy"))
print(woo.dance())