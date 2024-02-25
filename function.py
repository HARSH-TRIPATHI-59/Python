def my_function(**kid): # act when we have to use a dict to call
    print("My last name is " + kid["lname"])

my_function(fname = "Harsh", lname = "Tripathi")

def name_function(*name):  # used when we have to use a tuple to call 
    print("My name is " + name[2])

name_function("Saurabh", "Shlok", "Harsh")

def class_section(section = "S4" ,/):# ,/ positional argument, while calling cant assign value back to the varibles, in the above example while calling class_section() as class_section(section = "s5") will give you an error TO SOLVE THE ABOVE ERRRO WE USE KEYWORD ONLY ARGUMENT(*,)
    print("I am from " + section)

class_section("S1")
class_section("S2")
class_section("S3")
class_section()

