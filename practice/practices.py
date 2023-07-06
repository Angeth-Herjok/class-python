def addition(a,b):
    sum=a+b
    print(sum)

def substraction(c,d):
    difference=c-d
    print(difference)    
def multiplication(e,f):
    product=e*f
    print(product)

def division(g,h):
    dividend=g/h
    print(dividend)
def modulus(i,j):
    remainder=i%j
    return(remainder)
def exponentiation(k,l):
    exponent=k**l
    print(exponent)
def floor_division(m,n):
    whole_numberdivision=m//n
    return(whole_numberdivision)

def greet():
    print("Hey my people")
    print("welcome to kenya")
greet()
# print function takes an input but a call(greet)
# function does not take an input but to make it more useful we use arguments
def greet(first_name,last_name):
    print(f"{first_name} {last_name}" )
    print("welcome to USA")
greet("Angeth","Ajak")
greet("Angeth","It is your time to shine")

def greetings(name):
    return f"Hello {name}" 
message=greetings("Becky")
print(message)

# keword arguments
def nums(num1,by):
    return num1+by
answer=nums(21,3)
print(answer)

# alternative
def num(num2,num3):
    return num2+num3
print(num(32,8))
#  to make this code more readable we use keyword arguments
def number(num4,by1):
    return num4 + by1
print(number(num4=24,by1=20))

# default arguments all parameters you pass at first are required by default

def numbers(numb,numbs=2):
    return numb+numbs
print(numbers(9))

# or
def numbers(num5=2,numbs1=3):
    return num5+numbs1
print(numbers())
# or
def numbers(num5=2,numbs1=3):
    return num5+numbs1
print(numbers(12,4))
print(numbers(40,30))

# args,wait,what
def multiply(v,b):
    return v*b
print(num(2,5))

# to make it to take many arguments you use args which can allow you take more numbers
# Then you later use a list[] and tuples()to create objects  this can allow us to loop 
# through them but tuple cannot be change,list and tuple are iterable
def multiply(*numbers):
    total=1
    for number in numbers:
        # total=total*number
        total*=number
    return total
print(multiply(23,3))

def sum(*numbs):
    sum1=0
    for numb in numbs:
        sum1+=numb
        return sum1
    print(sum(6,7))
        

def product(*nums):
    totalProduct=1
    for num in nums:
        totalProduct*=num
    return totalProduct
print(product(21,5))

def add(*numbs):
    sum=0
    for numb in numbs:
        sum+=numb
    return sum
print(add(39,14))

def substract(*numbers):
    difference=0
    for number in numbers:
        difference-=number
    return difference
print(substract(9,2))

def division(*numms):
    divide=1
    for numm in numms:
        divide/=numm
    return divide
print(division(9,3))


# **kwargs
# when using double asterisk we can pass in multiple keywords arguments(dictionary)
def my_self(**me):
    print(me)
    print(me["name"])
    print(me["number"])
    print(me["age"])
my_self(name="Angeth",number=30,age=23)

# scope where a variable are define

message="a"
def greet(name):
    global message
    # if you want to get b  use global message
    message="b"
    # b is a local variable and will not be printed
greet("Becky")
print(message)

# control flow

def temperature_measurement():
    temperature=35
    if temperature>=30:
        print("it is warm")
    elif temperature<30:
        print("It's cold")
    else:
        print("Nice one")

def person_age():
    age=25
    if age>=18:
        print("Eligible")
    else:
        print("Not Eligible")

def addit(a,b):
    summation=a+b
    print(summation)

# num = 123456789 
# >>> sum_of_digits = 0 
# >>> for digit in str(num): 
# ...     sum_of_digits += int(digit) 
# ... 
# >>> sum_of_digits 
# 45 
# A more advanced solution would eschew the loop and use a generator expression. There’s still a loop in there, but sum_of_digits is computed all in one go, so we don’t have to set it to 0 first:

# >>> num = 123456789 
# >>> sum_of_digits = sum(int(digit) for digit in str(num)) 
# >>> sum_of_digits 
# 45 

def sum_of_digits(num):
    sum=0
    for digit in str(num):
        sum+=int(digit)
    return sum
print(sum_of_digits(54))

class AnkaraFabric:
     def __init__(self,mood,temperature):
          self.mood=mood
          self.temperature=temperature
     def predict_design(self,design):
          if self.temperature in range(5,25) and self.mood=="happy":
               return f"Pattern changes to {design}"
          elif self.temperature in range(30,40) and self.mood=="sad":
               return f"pattern changes to {design}"
          else:
               return f"pattern to none"
