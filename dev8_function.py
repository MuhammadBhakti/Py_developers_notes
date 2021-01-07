#Simple function

def myfunc():
    print("firts function")

myfunc()

#Function wih argument
def argfunc(x):
    print("My name is"+x)

argfunc("bhakti")

#function with double arg and more...
def double_arg(name1, name2):
    print("namanya adalah "+name1+" dan "+name2)

double_arg("Andi", "Taufan")

#Function with unkown number of argumen (Gunakan *argumen)
def unkown_arg(*nama):
    print("Nama ketiga dari list adalah "+nama[2])

unkown_arg("Barry","yudhi","irwan","randy","faisal")

#Function with default parameter value
def default_par(negara="Indonesia"):
    print("Saya berasal dari "+negara)

default_par("China")
default_par("USA")
default_par("Malaysia")

#Function to print member of list
def print_list(food):
    for i in food:
        print(i)

meals =["Rice", "Fruits", "Chicken", "beef"]
print_list(meals)

#function using return to assign value 
def return_func(x):
    return 5*x

print(return_func(10))