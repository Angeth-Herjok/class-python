# unpack method
# names=["mercy","becky","regina","marion","anne","45","true"]
# first,second,*rest=names
# print(first)
# print(second)
# print(*rest)
# # sort
# names=["mercy","becky","regina","marion","anne"]
# names.sort()
# print(names)
# numbers=[1,6,4,5,7,8,3]
# numbers.sort()
# print(numbers)
# # reverse
# numbers.reverse()
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)
# # range
# list1=[*range(10,20)]
# print(list1)
# # del
# del(numbers[0:3])
# print(numbers)

# numbers.remove(5)
# print(numbers)

# # to remove all the value occurrences
# del(numbers(67))
# del(numbers[6])

# # to change a list to a set
# numbers=set(numbers)
# print(numbers)

# # define a function that accepts a string as input and uses the for loop to
# # iterate through the string and count the vowels

def count_vowels(stringName):
    count=0
    vowels=("a","e","i","o","u")
    for vowel in stringName:
        for n in vowels:
            # for i lowercase in name.It can't print if u one is an uppercase
            if vowel==n:
                count+=1
    return count
print(count_vowels("accessible"))

# def counting_vowel(school):
#     count=0
#     vowels="a","e","i","o","u"
#     for char in school:
#         if char in vowels:
#             count+=1
#             return count
#         school="AkiraChix"
# my_vowel=count_vowels(school)
# print(my_vowel)

def vowelcount(word):
    count=0
    vowels=["a","e","i","o","u"]
    for vowel in word:
        for i in vowels:
            if vowel==i:
                count+=1
    return count 
print(vowelcount("angeth"))
 

def sum_of_digits(num):
    sum=0
    for digit in str(num):
        sum+=int(digit)
    return sum
print(sum_of_digits(12345))

no_dups = set()
for n in range(1, 100):
  for x in range(2,10):
    if n % x == 0:
      no_dups.add(n)
print(no_dups)
print()

#nested list comprehension

result = [number for number in range(1,100) if True in [True for x in range(2,10) if number % x == 0]]
print(result)

def secondMax(list1):
    list1.sort() #sort ascending order
    return list1[len(list1)-2] # second last element is second largest
list1 = [12,322,31,43,54,76,87]
print(secondMax(list1))