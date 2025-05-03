#Defining a Function

#1.
def print_codanics():
    print("hello world")
    print("hello world")
    print("hello world")
print_codanics()

#2.
def print_codanics():
    text=("Hello world")
    print(text)
    print(text)
    print(text)
print_codanics()



#3.
def print_codanics(text):
    print(text)
    print(text)
    print(text)

print_codanics("we are learning python.")


#5. Defining a function using if, elif, else statements.

def school_calculator(age):
    if age==5:
        print("congratulation! Hammad can join the school.")
    elif age< 5:
        print("Hammad is still a baby.")
    else:
        print("Hammad shoud join the higher school")

school_calculator(3)

#6. Defining a future function
def future_age(age):
    new_age=age+20
    return new_age
    print(new_age)
future_predicted_age=future_age(10)
print(future_predicted_age)