def greet():
    print("Hello, dear World!")
    print("End of the greet function.")

    greet()

    name1= "Thor"
    name2= "Joel"
    list_of_names = ["Katja", "Olga", "Tim"]

    # name = parameter
    def greet_person(name):
        print("Hello, ", name)
        print("End of the greet_person function.")

        #  the named argument
        greet_person(name=name1)
        # name1 = argument
        greet_person(name1)
        # name2 = argument
        greet_person(name2)

        greet_person(name="Najat")

        greet_person("Hanno")

    print("Hello, Theo")
    print("Hello, Olga")
    print("Hello, Tim")

# some other code

print("Other Code 1.")

print("Hello, World!")

# some other code

print("Other Code 2.")

print("Hello, World!")