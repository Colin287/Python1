#Branch bird for programming assignment #8
class bird:

    #attributes
    color = "blue"
    size = "small"
    status = "cool"

    #set name
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def name(self):
        print("My name is {}".format(self.name))

    #other function
    def type(self):
        print("I am this kind of bird {}".format(self.type))

#Child class
class user_bird(bird):
    def __init__(self, name, type):
        self.name = name
        self.type = type

        bird.__init__(self, name, type)

    def attr(self):
        print("//Name Method//")
        print("My name is {}".format(self.name))
        print("//Type Method//")
        print("My type is {}".format(self.type))



#Create two instances of the bird calss
a = user_bird('Eric', 'Sparrow')
b = user_bird('Mordecai', 'Blue Jay')

#Prompt user to name both birds


#prompt user to do anything else (type)


#display each bird to the console, prining all of its attributes and method names
a.attr()
print()
b.attr()

