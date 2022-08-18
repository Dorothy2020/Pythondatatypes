from re import A


def my_function():
    print("Hello World")


my_function()

# Number of Arguments
def my_function(fname,lname):
    print(fname + " " + lname)

my_function("Rez","Kem")


# concatenating strings
hi="Hello there"
name="Akoth"
greeting=hi+" "+ name

print(greeting)

# casting(specifying or converting variable type)
y=int("3")
print(y)

x=float(3)
print(x)

# Input (Takes input from the user and returns it)
x=input("Enter your name: ")
print("Hello," + x )


# use of elif

a=33
b=33

if b > a:
   print("b is greater than a")
elif a==b:
    print("a and be are equal")


    # while loop
    i=1
    while i<6:
        print(i)
        break
        i=+1

for i in range (10):
    print(i)

    # slicing in python(use of index)
    s="abcdefgh"
    s[1:6]
    print(s)
