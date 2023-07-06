
# Write a python program that calculate the square of a number using function
def square_number(number):
    return number**2
print(square_number)
# or
# print(square_number(7))
# print(square_number(6))
# print(square_number(9))
def square_root(num):
    return num **0.5
print(square_root)

def number_square(numb):
    if numb<6:
        print(numb**2)
        print(numb**0.5)
    else:
        print("square not found")
# def square_and_squareroot(numbers):
#     for numbers in range(50):
#         if numbers % 2==0 or numbers % 3==0:
#             print(numbers**2)
#             print(numbers**0.5)
#         # elif numbers % 5==0 or numbers % 4==0:
#         #     print(numbers**2)
#         #     print(numbers**0.5)
#         else:
#             print("Have no square and squareroot") 
# python program function to check whether a password is correct
def my_password(password):
    if password =="angethherjok@gmail":
        print("Enter password/correct password")
    else:
        print("Incorrect password")
