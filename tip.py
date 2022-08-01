'''print('welcome to the tip calculator ')
bill_amount = float(input('what is the bill amount '))
percentage = float(input('what is the tip percentage that ur going to provide for waiter '))
net_amount = bill_amount * percentage/100
total_amount = net_amount + bill_amount
splitting_persons = int(input('total number of persons '))
balance = total_amount/splitting_persons
print('each person should pay', balance)
'''
import random

'''user = int(input('please enter the number '))
if type(user) == int:
    print(user)
else:
    print('input is not valid')
'''

'''marks = int(input('what is your total marks '))
if marks <= 0 or marks >= 100:
    print('enter a valid number' )
elif marks < 35:
    print('fail ')
elif marks >= 35 and marks <= 39:
    print('grade is D ')
elif marks >= 40 and marks <= 49:
    print('garde is C ')
elif marks >= 50 and marks <= 69:
    print('grade is B ')
elif marks >= 70 and marks <= 89:
    print('grade is A ')
elif marks > 90 and marks < 100:
    print('grade is A+ ')
'''

'''a = 50
b = 30
c = 20
if a > b and a > c:
    print('a is greater than both b and c ')
elif b > a and b > c:
    print ('b is greater than both a and c ')
else:
    print('c is greater than both a and b ')
'''

'''year = int(input('what is the year '))
if year % 4 == 0:
    print('its a leap year ')
else:
    print('its not a leap year ')
'''

'''a = int(input('please provide the number'))
if a % 2 == 0:
    print('its an even number')
else:
    print('its an odd number')'''

'''a = (1,2,3) 
print(a)
b = (1,1,3)
print(b)
c = [1,2,3,4]
print(c)
d = {1,2,3,4,5}
print(d)'''

'''a = int(input('please provide the  number '))

if a == 0:
    print('the number is neither even nor odd')

elif a % 2 == 0:
    print('the given number is even ')
else:
    print('the given number is odd ')
'''

'''units = 500
if units <= 100:
    print('no charges for this month')
elif units > 100 and units <= 200:
    bill_amount = int(5 * (units - 100))
    print(bill_amount)
elif units > 200:
    total = int(units - 200) * 10 + int(100 * 5)
    print(total)
'''

'''logo_name = 'Welcome To Treasure Island'
print(logo_name)
user = input('do u want to go left door or right door: ')
if user == 'right door':
    print("you fell into a hole, 'game over '")
elif user == 'left door':
    user = input("Welcome to the lake, do you want to 'swim' or 'wait': ")
    if user == 'swim':
        print('game over ')
    elif user == 'wait':
        user = input('which door do u want to enter? RED, GREEN, or BLUE ').upper()
        if user == 'GREEN':
            print('you have won ')
        else:
            print('you lost ')
'''

'''user = str(1008)
print('the last digit of given number is ', user[-1])
'''

'''user = input('enter the number ')
print(int(user[-1]) % 3 == 0)
'''

'''user = int(input('what is the cost of ur bike '))
print('user ')
if user > 100000:
    print(((int(user) / 100) * 15) + int(user))
elif user > 50000 and user <= 100000:
    print(((int(user) / 100) * 10) + int(user))
else:
    print(((int(user) / 100) * 5) + int(user))
'''
'''welcome_note = input('Welcome to SARDAR PATEL CRICKET STADIUM ')
#print('welcome_note')
a1 = 2500
a2 = 3500
a3 = 4500
a4 = 6000
a5 = 8000
user = input('do you want to go for a1 or a2 or a3 0r a4 or a5 ')
user1 = input('online_booking or advance_booking or window_booking ')
if user == 'a1':
    if user1 == 'online_booking':
        online_booking = abs(int(((a1 / 100) * 10) - a1))
        print(online_booking)
    elif user1 == 'advance_booking':
        advance_booking = abs(int(((a1 / 100) * 8) - a1))
        print(advance_booking)
    else:
        print(a1)
if user == 'a2':
    if user1 == 'online_booking':
        online_booking = abs(int(((a2 / 100) * 10) - a2))
        print(online_booking)
    elif user1 == 'advance_booking':
        advance_booking = abs(int(((a2 / 100) * 8) - a2))
        print(advance_booking)
    else:
        print(a2)
if user == 'a3':
    if user1 == 'online_booking':
        online_booking = abs(int(((a3 / 100) * 10) - a3))
        print(online_booking)
    elif user1 == 'advance_booking':
        advance_booking = abs(int(((a3 / 100) * 8) - a3))
        print(advance_booking)
    else:
        print(a3)
if user == 'a4':
    if user1 == 'online_booking':
        online_booking = abs(int(((a4 / 100) * 10) - a4))
        print(online_booking)
    elif user1 == 'advance_booking':
        advance_booking = abs(int(((a4 / 100) * 8) - a4))
        print(advance_booking)
    else:
        print(a4)
if user == 'a5':
    if user1 == 'online_booking':
        online_booking = abs(int(((a5 / 100) * 10) - a5))
        print(online_booking)
    elif user1 == 'advance_booking':
        advance_booking = abs(int(((a5 / 100) * 8) - a5))
        print(advance_booking)
    else:
        print(a5)
'''

'''sum of all the digits given by user '''

'''letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password_generator = input('how many letter do u want in your password? ')
password_generator1 = input('how many number do u want to use in your password? ')
password_generator2 = input('how many symbols do u want to use in your password? ')
i = 0
while i < int(password_generator):
    i = i + 1
    print(letters[i])
i = 0
while i < int(password_generator1):
    i = i + 1
    print(numbers[i])
i = 0
while i <int(password_generator2):
    i = i + 1
    print(symbols[i])
'''

'''print the fibonacci numbers'''
# 0 1 1 2 3 5 8 13 21 34
# 10
'''user = int(input("give the number = "))
first_pos = 0
sec_pos = 1
i = 0
while(i<user):
    current_pos = first_pos + sec_pos
    print(first_pos, end=" ")
    first_pos = sec_pos
    sec_pos = current_pos
    i +=1'''

''' 5 = 5*4*3*2*1 = 
ask the user about the number
user = (n-1)
n<1
'''
'''i = 0
while i < 10:
    i = i + 1
    print('asif shahrukh ')
'''

'''i = 1
while i < 8:
    print(i)
    if i == 7:
        break
    i += 1
'''

'''i = 0
while i < 4:
    i += 1
    if i == 2:
        continue
    print(i)
'''
'''sum of natural numbers eg 1+2+3+......+n'''

'''n = int(input('provide the number '))
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i + 1
    print("the sum is", sum)
'''
'''VN2solutions.com'''
'''i = 0
a = 'VN2solutions.com'
while i < len(a):
    if a[i] == '2' or a[i] == '.':
        i += 1
        continue
    print('current letters', a[i])
    i += 1
'''

'''x = 5
y = 7
print('before swapping: ')
print('value of x : ', x, ' and y: ', y)
x, y = y, x
print('after swapping: ')
print('value of x: ', x, ' and y: ', y) 
'''

'''a = 2
b = 3
a,b =b,a
print(a,b)
'''

'''for i in range(1500,2700):
    if (i % 7 == 0) and (i % 5 == 0):
        print(i)
'''

'''a = "asif"
print(a[::-1])
'''
'''def my_reverse(a):
    return a[::-1]
reverse = my_reverse('my name is asif shahrukh')
print(reverse)
'''

'''def divisible(n1,n2):
    for i in range(n1,n2):
        if i % 5 == 0 and i % 7 == 0:
            print(i)

divisible(1500,3001)
''''''
list = [1,2,3,4,]
tuple = (1,2,3,4)
dictionary = {1:2,3:4,5:6}
set = {1,3,6,7}
'''

'''from collections import Counter
name = 'shahrukh'
print(Counter(name))
'''
'''
def odd_even(n):
    if n > 0:
        if n % 2 == 0:
            print('the number is even')
        else:
            print('the number is odd')
    else:
        print('the number is neither even or odd')
odd_even(0)
'''
'''list1 = [1,2,3,4,5]
list1.reverse()
print(list1)
'''
'''def odd_even(n1,n2):
    even = []
    odd = []
    for i in range(n1,n2):
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    print('the even list numbers are', even)
    print('the odd list numbers are', odd)
odd_even(500,550)
'''
'''def addition(n1,n2):
    return (n1 + n2)
print('the above addition value is',addition(65,78))
'''

'''def sum(n1,n2):
    return (n1 + n2)

def odd_even():
    num1 = int(input('give us the first number: '))
    num2 = int(input('give us the second number: '))
    additions = num1 + num2
    print(additions)
    even = []
    odd = []
    for i in range(additions):
        if i % 2 == 0:
            even.append(i)
        else:
             odd.append(i)
    print(even)
    print(odd)
odd_even()
'''
'''def reversing(n):
    return(n[::-1])
reverse = reversing('my name is asif shahrukh')
print(reverse)
'''

#print the string which are in capital and small and swap cases
'''def swap(n):
    return(n.swapcase())
swaps = swap('HeLlo woRlD')
print(swaps)
'''

#print the lenghth of the function using function
'''def length(n):
    return(len(n))
lengths = length('asif shahrukh')
print(lengths)

#count the character of string
def counting(n):
    for i in n:
        print(i + '\t\t' + str(n.count(i)))
counting('my name is asif shahrukh')
'''
#count the character in strings in oops concept
'''class Occurences:
    def __init__(self,string):
        self.string = string
    def occurence_of_character(self):
        occurence_of_char = {}
        for each_char in self.string:
            if each_char in occurence_of_char:
                occurence_of_char[each_char] += 1
            else:
                occurence_of_char[each_char] = 1
        print(occurence_of_char)

occ = Occurences('welcome to python')
occ.occurence_of_character()
'''
#to display a number with comma seperator
'''n = int(input('give us the number: '))
print('original number: ',n)
print('The number after being Formatted is: '+'{:,}'.format(n))
'''

#to format a number with percentage
'''def percentage(n1):
    if n1 == float(n1):
        print('before formatting: ', n1)
        print('after formatting: '+'{:.2%}'.format(n1))
    else:
        print('print the valid number')
percentage(.032)
'''

#to count the occurences of a sub string in a string
'''def substring(n1):
    print(n1[:8])
substring('welcome to my world')

#print the index of the character in a string
def index(a):
    print(a[:1])
index('asif')
'''
#swap commas with dots
'''
def swapping(a):
    print(a.replace(',','.'))
swapping('500,201,302')

#count and display the vowels in a string
def vowels(a):
    vowel_character = 'aeiou'
    vowel_count = {}
    for each_character in a:
        for vowel in vowel_character:
            if each_character == vowel:
                if each_character in vowel_count:
                    vowel_count[each_character] += 1
                else:
                    vowel_count[each_character] = 1

    print(vowel_count)

vowels('mother of all evils is alchohal')

#remove spaces from given string
def close_spaces(n):
    new_string = ''
    for each_character in n:
        if each_character == " ":
            new_string += ""
        else:
            new_string += each_character
    print(new_string)
close_spaces("my name is asif shahrukh")

#move spaces to the front of a given string

def move_spaces(n):
    n = ('welcome to python')
    c = n.count(' ')
    n = n.replace(' ','')
    n = '    ' * c + n
    print(n)
move_spaces('welcome to python')

#swap comma and dot in a string

def swapping(a):
    print(a.replace(',','.'))
swapping('welcome,to,python')
'''
'''#sum of elements in lists
def addition(n1,n2):
    n1 = [1, 2, 4, 5, 5]
    n2 = [2, 2, 4, 3, 2]
    n4 = sum(n1) + sum(n2)
    print('the sum of the elements are: ', n4)

addition([1, 2, 4, 5, 5],[2, 2, 4, 3, 2])

#product of element in lists
import math
n = [2, 3, 4, 6, 3]
n1 = math.prod(n)
print('the product of the list: ',n1)

#largest number from the list

def largest_number(a):
    a = [23, 43, 51, 67, 298]
    print(max(a))
largest_number([23, 43, 51, 67, 298])

#smallest number from the list

def smallest_number(s):
     print('the smallest element in the list s is: ',min(s))
smallest_number([0, 3, 6, 90])

#remove common elements in the lists

def remove(list1,list2):
    common_ele = []
    for i in list1:
        for j in list2:
            if i == j:
                common_ele.append(i)
    print(common_ele)
remove([1,2,3,4,5],[1,2,3,6,5])

#remove duplicate elements from the list

def remove_duplicates(l1):
    unique_ele = []
    for each_ele in l1:
        if each_ele not in unique_ele:
            unique_ele.append(each_ele)
    print(unique_ele)

remove_duplicates([1,3,5,6,3,4,8,2,3,8])

#check list is whether empty or not
def empty_or_not(l1):
    l1 = []
    if len(l1) == 0:
        print('the list is empty')
    else:
        print('the list: ', l1)
empty_or_not([])

#clone or copy in python
def cloning(l1):
    l2 = []
    for i in l1:
        l2.append(i)
    print(l2)

cloning([1,4,7,23,5678])
'''
#remove specified index from list and print
'''
def remove_index(l1, index):
    l1.pop(index)
    print(l1)
remove_index([1, 4, 5, 7, 90], 2)
'''
'''l1 =['anusha', 'asif', 'ashwini']
l1.pop(0)
print(l1)
'''
'''
#remove even elements in list
l1 = [30, 49, 67, 22, 98]
l2 = []
for i in l1:
    if i % 2 == 0:
        print(l2.append(i))
print(l2)
'''
'''
from random import shuffle
class random_shuffling:
    def __init__(self,shuffle):
        self.shuffle = shuffle
    def shuffling(self):
        shuffle(self.shuffle) 
        print(self.shuffle)
list1 = random_shuffling([20,90,76])
list1.shuffling()
'''
'''
#difference between two list
def differences(list1,list2):
    print(list(set(list1) - set(list2)) + list(set(list2) - set(list1)))
differences([21, 43, 78],[34, 87, 90])
'''
'''
#to access the index of the list
def indexing(l1,ind):
    print(l1[ind])
indexing([32, 56, 78, 89, 1000], 4)
'''
'''
#list of characters into string
def converting(l1):
    print(''.join(l1))
converting(['a', 's', 'i', 'f'])
'''
'''
#finding index of an item in a specified list
 
def indexing(l1):
    print(l1.index('shahrukh'))
indexing(['asif', 'shahrukh', 'ashwin', 'santhosh'])
'''
'''
#flatten a shallow
def flatten_num(num):
    i = []
    for x in num:
        for y in x:
            i.append(y)
    print(i)
flatten_num([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])

#write a program to create a class by name students and initialise attributes like name age and grade

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def student(self):
        print(self.name)
        print(self.age)
        print(self.grade)
afrid = Student('afrid', 17, '11th')

afrid.student()

#class for dog
class Dog:
    animal = 'Dog'
    def __init__(self, breed, colour):
        self.breed = breed
        self.colour = colour
sultan = Dog('german shepherd' , 'brown')
sheru = Dog('bulldog' ,'white')

print('sultan details: ')
print('sultan is a ', sultan.animal)
print('breed: ', sultan.breed)
print('colour: ', sultan.colour)

print('\n sheru details: ')
print('sheru is a ', sheru.animal)
print('breed: ', sheru.breed)
print('colour: ', sheru.colour)

print(Dog.animal)


def prime_numbers(n1):
    for i in range(2,n1):
        if n1 % i == 0:
            print('number is not prime')
            break
    else:
        print('number is prime')

prime_numbers(7)

#append list into another list

colours = ['red' , 'blue' , 'purple' , 'yellow']
flowers = ['rose' , 'orchids' , 'december' , 'sunflower']
mixing = colours.extend(flowers)
print('after appending the colours: ', mixing)
print(colours)

def append_list(list1,list2):
    for i in list2:
        list1.append(i)
    return list1

append_list(['red', 'blue', 'yelow', 'black'],['rose', 'sunflower', 'mariegold', 'hibuscuss'])

#select randomly from the list
def random_selection(l1):
    print(random.choice(l1))
random_selection([1,23,54,67,8976,55,56584353,])

#check circularly identical in two lists
def circularly_identical(list1,list2):
    list1.extend(list1)
    for i in range(len(list1)):
        if list2 == list1[i: 1 + len(list2)]:
            print('true')
        print('false')


list1 = [10, 20, 30, 5, 3]
list2 = [20, 30, 3, 5, 10]
list3 = [20, 30, 6, 5, 10]


if circularly_identical(list1,list2):
    print('it is circularly identical')
else:
    print('its not circularly identical')

if circularly_identical(list2,list3):
    print('it is circularly identical')
else:
    print('its not circularly identical')
'''
#finding a second smallest number

def find_length(list1):
    length = len(list1)
    list1.sort()
    print('largest element is: ', list1[-1])
    print('smallest element is: ', list1[0])
    print('second largest element is: ', list1[-2])
    print('second smallest element is: ', list1[1])

list1 = [12, 45, 2, 41, 31, 10, 8, 6, 4]
find_length(list1)
largest = find_length(list1)

#find unique element in the list

def unique_number(list1):
    unique_element =[]
    for i in list1:
        if i not in unique_element:
            unique_element.append(i)
    for i in unique_element:
        print('unique_number are: ', i)


unique_number([20,40,20,40,30,50,60,50])

#another method
from collections import Counter


def unique_elements(list):
    print('the unique_elements in the list are: ', *Counter(list))
unique_elements([1,2,3,1,2,3,4,5,6,6,7,9,])

#check the frequency of the elements

def frequency_elements(list1):
    frequency = {}
    for i in list1:
        if i in frequency:
            frequency[i] += i
        else:
            frequency[i] = i

    print(frequency)


frequency_elements([1,1,1,1,2,2,2,2,3,3,4,5,6,7,9])

#another method

def frequency(list1):
    import collections
    frequencies = collections.Counter(list1)
    print(dict(frequencies))

frequency(['a', 'a', 'b', 'b', 'c', 'd', 'd', 'a', 'd'])

#counting a number of elements in a specified range

def counting(list1, l, r):
    a = 0
    for i in list1:
        if i >= 1 and i <= r:
            a += 1
    return a

list1 = [10, 20, 30, 40, 50, 40, 40, 60, 70]
l = 40
r = 80
print('the number of elements in the specified range is: ',counting(list1, l, r))

#another method

def count(list1, l, r):
    c = 0
    return(len(list(x for x in list1 if 1 <= x <= r)))

list1 = [10, 20, 30, 40, 50, 40, 40, 60, 70]
l = 40
r = 80
print(count(list1, l, r))




