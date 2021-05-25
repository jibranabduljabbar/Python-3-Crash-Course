#                                                  What Is Python?

"""

+ Python Is a Popular Programming Language. It was created by Guido van Rossum, And Released In 1991.
+ Python Is a Interpreted Language.

+ It Is Used For: 
+                  1): Web Development (Server-Side),
+                  2): Software Development,
+                  3): Mathematics,
+                  4): System Scripting.

#                                                What can Python do?   
 
+ Python can be used on a server to create web applications.
+ Python can be used alongside software to create workflows.
+ Python can connect to database systems. It can also read and modify files.
+ Python can be used to handle big data and perform complex mathematics.
+ Python can be used for rapid prototyping, or for production-ready software development.

#                                                   Why Python?

+ Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).
+ Python has a simple syntax similar to the English language.
+ Python has syntax that allows developers to write programs with fewer lines than some other programming languages.
+ Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick.
+ Python can be treated in a procedural way, an object-oriented way or a functional way.

#                                Python Syntax compared to other programming languages:
 
+ Python was designed for readability, and has some similarities to the English language with influence from mathematics.
+ Python uses new lines to complete a command, as opposed to other programming languages which often use semicolons or parentheses.
+ Python relies on indentation, using whitespace, to define scope; such as the scope of loops, functions and classes. Other programming languages often use curly-brackets for this purpose.

#                                           Installing Python Setup: 

+ Download Anaconda Navigator Website_Name Go(https://www.anaconda.com/products/individual#Downloads). Then Selected Option (Window, MacOS, Linux).
+ Download Completed Then Opon Anaconda Then Accept All Argrements Then Open Anaconda Then Launch ((Jupyter)NoteBook) Version(6.3.0).
+ Then Open Jupyter in Google then Press New Button then Select Option (Python 3)
+ Then Your Browser In Always Open This Https: (http://localhost:8888/notebooks/Untitled1.ipynb?kernel_name=python3)
+ Then Write Your Coading Inside (In[]: Input) 

# For Example:

                                              Press Run Button
                                                    ⬇️
* print("Hello World")                             ===>                             Output Is: (Hello World)

#                                                No Need:

+ No need of var int or double in python.
+ variable declearation.
+ variable initiallization.

#                                                Variable:

+ Variables are containers for storing data values.
+ A variable is created the moment you first assign a value to it.
+ Variables do not need to be declared with any particular type, and can even change type after they have been set.

# For Example:

 (a) Is a Variable Name 
    Equal (Operator) 
      (5) Is Value Of (a) Variable

 ⬇️⬇️⬇️ 

* a = 5                                           ===>                             Varible Inside Value.
* print(a)                                        ===>                             Print (a) Variable Value.  

#                                                Work On:

*                                                                                  VariableName = Value

#                                           String Expression:

* populor_string = "This Is String Value"
* print(populor_string)

#                                            Math Expression:

* populor_number = 5
* print(populor_number)

#                                   Math Expression: Familiar Operators:

# Addition:

* addition = 5 + 5
* print(addition) # 10

# Subtraction:

* subtraction = 15 - 5
* print(subtraction) # 10

# MultipliCation:

* multipliCation = 5 * 2
* print(multipliCation) # 10

# Division:

* division = 15 / 5
* print(division) # 3.0

# Module:

* module = 20 % 6
* print(module) # 2

# Decimal Value:

* num = .075  ===> This Is a Decimal Value.
* total = num + 200 ===> Concatenating.
* print(total) ===> 200.075

#                                   Variable Names Legal & Illegal:

+ You've already learned three rules about naming a variable:

1. You can't enclose it in quotation marks.
2. You can't have any spaces in it.
3. It can't be a number or begin with a number.

+ In addition, a variable can't be any of Python's reserved words, also known as
keywords—the special words that act as programming instructions, like print.
Here’s a list of them.

# and                                           False                                          not
# as                                            finally                                        or
# assert                                        for                                            pass
# break                                         from                                           print
# class                                         global                                         raise
# continue                                      if                                             return
# def                                           import                                         True
# del                                           in                                             try
# elif                                          is                                             while
# else                                          lambda                                         with
# except                                        none                                           yield
#                                               nonlocal

#                                               Code:

* a = 5
* a = a+1
* print(a) ===> Output Is: (6)

#                                             Same Work: 

* a = 10
* a += 2
* print(a) ===> Output Is: (12)

#                               Math Expresstion: Eliminating Ambiguity(DMAS Rule):

* dmas = 1 + 3 * 4
* print(dmas) ===> Output Is: (13)

* dmas = (1 + 3) * 4
* print(dmas) ===> Output Is: (16)

* dmas = (1 + 3) * 4 / 2
* print(dmas) ===> Output Is: (8.0)

* dmas = (1 + 3) * 4 // 2
* print(dmas) ===> Output Is: (8)

#                                          Assignment No_(1):

+ Step_(1):

*                 print("Twinkle, twinkle, little star, ")
*                 print("           How I wonder what you are!")
*                 print("                       Up above the world so high, ")
*                 print("                       Like a diamond in the sky. ")
*                 print("Twinkle, twinkle, little star,")
*                 print("           How I wonder what you are")

+ Second Optioin(One print Of Code)

* print("Twinkle, twinkle, little star,\n           How I wonder what you are!\n                       Up above the world so high, \n                       Like a diamond in the sky. \nTwinkle, twinkle, little star,\n           How I wonder what you are")

+ Step_(2):

* version = "3.8.8 (default, Apr 13 2021, 15:08:07) [MSC v.1916 32 bit (Intel)]"
* print(version)

+ Output Is:

+ 3.8.8 (default, Apr 13 2021, 15:08:07) [MSC v.1916 32 bit (Intel)]

+ Second Option("Import Sys")

* import sys
* print(sys.version)

+ Output Is:

+ 3.8.8 (default, Apr 13 2021, 15:08:07) [MSC v.1916 32 bit (Intel)]

+ Step_(3):
 
* text = "Current Date And Time: "
* date = "2021-05-16 04:12:38"
* print(text)
* print(date)

+ Output Is:

+ Current Date And Time: 
+ 2021-05-16 04:12:38

+ Second Option("Import DateTime")

* import datetime
* now = datetime.datetime.now()
* print("Current Date And Time: ")
* print(now.strftime("%Y-%m-%d %H:%M:%S"))
 
+ Output Is:

+ Current Date And Time: 
+ 2021-05-16 04:12:38

+ Step_(4): 

* 

+ Step_(5): 

* firstname = "Mark"
* lastname = "Myers"
* print("Fullname Is: " + lastname +" "+ firstname)

+ Output Is:

+ Fullname Is: Myers Mark

+ Second Option("Input Throw")

* firstname = input("Enter your Firstname: ")
* lastname = input("Enter your Lastname: ")
* print("Fullname Is: " + lastname +" "+ firstname)

+ Output Is:

+ Fullname Is: Myers Mark

+ Step_(6): 

* num1 = 18
* num2 = 2
* print(num1+num2)

+ Output Is:

+ 20

+ Second Option("Input Throw")

* num1 = input("Enter your num1: ")
* num2 = input("Enter your num2: ")

* print(int(num1)+int(num2))

+ Output Is:

+ 20

#                                                  Assignment No_(1) Is Completed

#                                                         Concatenation

* str = "Jibran"
* str1 = "Abdul Jabbar"
* punc = "!"
* print(str + ' ' + str1 + " " + punc)

#                                                      Arithmetic Operation

* () / * + - ** // %

*  >>> 20 / 2 
* 10.0 (a float?)
* >>> 3/0
+ ZeroDivisonError: division by Zero
* >>> 5 + 3.0
* 8.0
* >>> 2 ** 3 >>> Powered Discuss
* 8

+ Powered Discuss (**)

* num = 5
* num1 = 2
* print(num ** num1)

+ Output Is: 

+ 25

+ Second Option(**)

* num = 3
* num1 = 2
* print(num ** num1)

+ Output Is: 

+ 9

+ Third Option(**)

* num = 4
* num1 = 2
* print(num ** num1)

+ Output Is: 

+ 16

#                                                    Arithmetic Operation_(Cont)

* >>> 15.0 // 2.0   (floor division)

* 7

* >>> 15.0 % 2.0    (remainder) 

* 1

#                                                         String (Theory)

+ A String is created by entering a text between two double quotations or two single quotes.

* >>> 'We are Programmers'

'We are Programmers'
* Three Quotes String
  '''Whatever I write here
  will be displayed
  as it is'''

+ String Is a Group Of Character.

#                                                         String (Cont)

>>> print('one,' + ' two,' + ' three')

+ Output Is:

+ one, two, three

>>> '5' + '3'

+ Output Is:

+ 53     (not 8)

>>> '1' + 5

+ Output Is: 

+ TypeError: unsupported operand types

>>> print(" Hello World " * 5)

+ Output Is:

+ Hello World Hello World Hello World Hello World Hello World

>>> print(5 * " Hello World ")

+ Output Is:

+ Hello World Hello World Hello World Hello World Hello World

>>> print(" Hello World " * 5.0)

+ Output Is:

+ TypeError

>>> print('Hello' * 'World')

+ Output Is:

+ TypeError

#                                                        Simple Input/Output

>>> print('Python is cool')

+ Output Is: 

+ Python is cool

#                                                     Line Break In Python Print

>>> print('You are \n Welcome')

+ Output Is: 

+ You are 
+ Welcome

#                                                          Variable Input

+ Input Always take the Values as String.

* x = input("Enter your age: ")
+ Enter your age: 8
>>> print(x)

+ Output Is:

* 8

#                                                    Format Function In Python

* marks = "79"
* percentage =  "80.0000000%"
* print("Marks: {} - Percentage: {}".format(marks , percentage))

+ Output Is:

+ Marks: 79 - Percentage: 80.0000000%

#                                                             Float

* x = input("Enter your value: ")
* y = 18
* z = float(x) + y
* print(z)

+ Output Is:

+ Enter your value: 5
+ 23.0

+ Second Option(Use Float ==> input)

* x = float(input("Enter your value: "))
* y = 18
* z = x + y
* print(z)

+ Output Is:

+ Enter your value: 5
+ 23.0


#                                                    Integer(int ===> Keyword)

+ Use Int() Function to Convert String into Integer.

* x = input("Enter your value: ")
* y = 18
* z = int(x) + y
* print(z)

+ Output Is:

+ Enter your value: 5
+ 23

+ Second Option(Use Integer ==> input)

* x = int(input("Enter your value: "))
* y = 18
* z = x + y
* print(z)

+ Output Is:

+ Enter your value: 5
+ 23

#                                                     Single Line Comment (#)

# This Is Single Line Comment TexT

#                                                   Multi Line Comment (""" """)


* This Is Multi Line Comment TexT ===> """  """


#                                                   IF/Else Statement In Python

* age = int(input("Enter your age: "))

* if age >= 15 :
*     print("You are Allowed To This Ride")
* else :
*     print("You are Not Allowed to This Ride")

+ Output Is: 

+ Enter your age: 17
+ You are Allowed To This Ride

+ Second Condition

* if 2+2 == 4 :
*    print("2 + 2 Is Equal To 4")

+ Output Is:

+ 2 + 2 Is Equal To 4

#                                                     Comparison Operators

* a = 5
* b = 15
* c = 5
* d = 5

* if a+d == b-c :
*    print("Your Answer Is Correct..!")
 
* else :
*    print("Your Answer Is WronG..!")

+ Output Is:

+ Your Answer Is Correct..!

#                                                    Not Equal To Operator

* a = 5
* b = 15 ==> 22
* c = 5 
* d = 5 ==> 20

* if a+d != b-c :
*    print("Your Answer Is Correct..!")
 
* else :
*    print("Your Answer Is WronG..!")

+ Output Is:

+ Your Answer Is WronG..!

+ Here are 4 more comparison operators, usually used to compare numbers.

+ > Is Greater than

+ < Is Lass than

+ >= Is Greater than or Equal to 

+ <= Is Less than or Equal to

+ In the Examples below, all the Conditions are True. 

* if 1 > 0 :

* if 0 < 1 :

* if 1 >= 0 :

* if 1 >= 1 : 

* if 0 <= 1 :

* if 1 <= 1 : 

#                                                       Else/ElIF Statement

* course_name = input("Enter Your CourSe Name: ")

* if course_name == "Python" :
*     print("Python Is Cool")
* elif course_name == "JavaScript" :
*     print("JavaScript Is Cool")
* elif course_name == "HTML & CSS" :
*     print("HTML & CSS")
* else : 
*     print("All Courses Is COOL..!")

+ Output Is: 

+ Enter Your CourSe Name: Python

+ Python Is Cool

#                                      (IF/Else/ElIF) Statement Percentage Example Uses (and/or)

* percent = int(input("Enter Your Percent: "))
 
* if percent >= 80 and percent <= 100 :
*     print("A+")
 
* elif percent >= 70 and percent <= 80 :
*     print("A")
 
* elif percent >= 60 and percent <= 70 :
*     print("B")
     
* elif percent >= 50 and percent <= 60 :
*     print("C")
 
* elif percent >= 40 and percent <= 50 :
*     print("D")
 
* elif percent >= 33 and percent <= 40 :
*     print("E")
 
* elif percent >= 0 and percent <= 33 :
*     print("Fail")
 
* else :
*     print("You have given Inapproperiate Percentage_(%) ")

#                                  (IF/Else/ElIF) Statement Simple CalCulator Example Uses (and/or)

* num1 = int(input("Enter Your Num1: "))
* operator = input("Enter Your Operator: ")
* num2 = int(input("Enter Your Num2: "))
  
* if operator == "+" : 
*     print("Answer Is: ", num1 + num2)
* elif operator == "-" : 
*     print("Answer Is: ", num1 - num2)
* elif operator == "*" : 
*     print("Answer Is: ", num1 * num2)
* elif operator == "/" : 
*     print("Answer Is: ", num1 / num2)
* elif operator == "%" : 
*     print("Answer Is: ", num1 % num2)
* else :
*       print("Make a Mistake!")

#                                  (IF/Else/ElIF) Statement Prize Bond Example Uses (and/or)

* ticket_luck = int(input("Enter your Ticket No: "))

* if ticket_luck == 18341 :
*     print("Congratulations (1st Prize) Price: ($50000)")
* elif ticket_luck == 18342 :
*     print("Congratulations (2nd Prize) Price: ($30000)")
* elif ticket_luck == 18343 :
*     print("Congratulations (3rd Prize) Price: ($10000)")
* else :
*     print("Bad Luck Next Time Try Again")

#                                              Nested (IF/Else/ElIF) Statement:

* a = 5;
* b = 6;
* c = 7;
* d = 7;
* e = 9;
* g = 10;
* f = 11;
* x = 12;
* y = 12;
* h = 0;

*  if (x == y or a == b) and c == d : ==> ( (x == y ==> 12 == 12) or (a == b ==> 5 == 6) ) and (c == d ==> 7 == 7)
*     g = h
*     print(g)

* else :
*     e = f
*     print(e)

# Second Condition Same Condition (Nested (IF/Else/ElIf))

* a = 5;
* b = 6;
* c = 7;
* d = 7;
* e = 9;
* g = 10;
* f = 11;
* x = 12;
* y = 12;
* h = 0;

* if c == d :
*     if a == b :
*         g = h
*         print(g)
*     elif x == y :
*         g = h
*         print(g)
*     else :
*         e = f
* else: 
*     e = f

#                                                      List (Array)

+ We can store one or more elements in the list.
+ List & Array Is a Group of Element.
+ Each element in the list has a unique id through which we see the value of that ID.
+ Lists are created using square brackets:

* arr = ["Array",1,False,"List",1.33,True]
* print(arr)

+ Output Is: 

+ ['Array', 1, False, 'List', 1.33, True]

#                                                     Array_(Indexs)

* arr = ["Array",1,False,"List",1.33,True]
* print(arr[3]) 

+ Output Is:

+ List

#                                            Find the Length of List in Python_(len)

* list = ["HTML","CSS","JavaScript","EcmaScript","React Js","Redux","React Native","Firebase","Github","Bootstrap","Linux"]
* print(len(list))

+ Output Is:

+ 11

#                                               Element Add Inside List_(append)

* arr = ["Array",1,False,"List",1.33,True]
* arr.append("React")
* print(arr)

+ Output Is:

+ ['Array', 1, False, 'List', 1.33, True, 'React']

#                                              Multiples Elements Added Inside List

* arr1 = arr + ["JavaScript","HTML & CSS"]
* print(arr1)

+ Output Is:

+ ['Array', 1, False, 'List', 1.33, True, 'React', 'JavaScript', 'HTML & CSS']

#                                           Get the largest number from a Numeric list_(max).

* largest = [65,34,23,67,98,56,87]
* print(max(largest))

+ Output Is:

* 98  

+ Second Option:

* largest = [65,34,23,67,98,56,87]
* largest.sort()
* print(largest[-1])

+ Output Is:

+ 98

#                                              List_(Array) Inside Insert Elements

* arr1.insert(2, "Redux")
* print(arr1)

+ Output Is:

+ ['Array', 1, 'Redux', False, 'List', 1.33, True, 'React', 'JavaScript', 'HTML & CSS']

#                                             Array_(List) Inside Replace/Add Value

* arr1[5] = 1.34
* print(arr1)

+ Output Is: 

+ ['Array', 1, 'Redux', False, 'List', 1.34, True, 'React', 'JavaScript', 'HTML & CSS']

#                                              List_(Array) Inside Slice Elements

+ Slicing Is a Flexible tool to Build new Lists Out of an Existing List.
+ The Slice() Function returns a Slice Object that can use Used to Slice Strings, lists, tuple etc.
+ To Access a Range of items in a List, you need to Slice a List.

+ Syntex:

* arr2 = arr1[2 : 5] # 5 Means Index No 4 ('List')
* print(arr2)

+ Output Is:

+ ['Redux', False, 'List']

#                                       Copy Element One Array To Second Array_(Short Cut): 

* arr = ["Array",1,False,"List",1.33,True]
* arr.append("React")
* print(arr)
* arr3 = arr[:6]
* print(arr3)

+ Output Is:

+ ['Array', 1, False, 'List', 1.33, True, 'React']
+ ['Array', 1, False, 'List', 1.33, True]

#                                              List_(Array) Inside (DELETE Method)  

+ Definition & Usage:

+ The del keyword is used to delete objects. In Python everything is an object, so the del keyword can also be used to delete variables, lists, or parts of a list etc.

+ Syntex:

* arr = ["Array",1,False,"List",1.33,True]

* del arr[2]
* print(arr)

+ Output Is:

+ ['Array', 1, 'List', 1.33, True]

#                                              List_(Array) Inside (Remove Method)

+ Definition & Usage:

+ remove() is an inbuilt function in Python programming language that removes a given object from the list. It does not return any value.
+ Remove the "Banana" element of the fruit list:

* fruits = ['Apple','Banana','Cherry']
* fruits.remove("Banana")
* print(fruits)

+ Output Is: 

+ ['Apple', 'Cherry']

#                                               List_(Array) Inside (Pop Method)

+ Definition & Usage:

+ Pop method is used to remove the last element of the list.
+ Pop () This remove the last element of the list
+ Remove the second element of the fruit list:

* fruits = ['Apple','Banana','Cherry']
* fruits.pop(1)
* print(fruits)

+ Output Is: 

+ ['Apple', 'Cherry']

+ Second Example_(Push)

+ We can also use pop to cover values from one list to another: 

* list5 = [1,2,3,4,5]
* list6 = list5.pop()
* print(list6)

+ Output Is:

+ 5

#                                      List_(Array) Inside (Sort List Alphanumerically Method)

+ Definition & Usage: 

+ List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

+ Sort the list numerically:

* sort_method = [3,5,1,4,2,9,6,10,8,7]
* sort_method.sort()
* print(sort_method)

+ Output Is:

+ [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

+ Sort the list alphabetically:

* sort_method = ["Banana","Apple","Cherry","Watermillon","Orange"]
* sort_method.sort()
* print(sort_method)

+ Output Is:

+ ['Apple', 'Banana', 'Cherry', 'Orange', 'Watermillon']

#                                              List_(Array) Inside (Copy Method)

+ Definition & Usage: 

+ You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
+ There are ways to make a copy, one way is to use the built-in List method copy().
+ Make a copy of a list with the copy() method:

* copy_method = ["Banana","Apple","Cherry","Watermillon","Orange"]
* copy_method1 = copy_method.copy()
* print(copy_method1)

+ Output Is:

+ ['Banana', 'Apple', 'Cherry', 'Watermillon', 'Orange']

#                                             List_(Array) Inside (List Method)

+ Definition & Usage: 

+ Another way to make a copy is to use the built-in method list().
+ Make a copy of a list with the list() method:

* list_method = ["Banana","Apple","Cherry","Watermillon","Orange"]
* list_method1 = list(list_method)
* print(list_method1)

+ Output Is: 

+ ['Banana', 'Apple', 'Cherry', 'Watermillon', 'Orange']

#                                             List_(Array) Inside (Sum Method)      

+ Definition & Usage:

+ Add all items in a list, and return the result:

+ Example:

* Sum = [10,5,15,40,10,20]
* print(sum(Sum))

+ Output Is:

+ 100

#                                            List_(Array) Inside (extend Method)

+ Definition & Usage: 

+ Or you can use the extend() method, which purpose is to add elements from one list to another list:
+ Use the extend() method to add list2 at the end of list1:

* list1 = [1,2,3,4,5]
* list2 = [6,7,8,9,10]
* list1.extend(list2)
* print(list1)

+ Output Is:

+ [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#                                            List_(Array) Inside (Clear Method)

+ Definition & Usage: 

+ Remove all elements from the fruits list:

* list = [1,2,3,4,5,6,7,8,9,10]
* print(list)
* list.clear()
* print(list)

+ Output Is:

+ [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
+ [] # This Is Empty List.

#                                                    Assignement No_(2):

+ Step No_(1):

* sub1 = int(input("Enter your English Subject Marks: "))
* sub2 = int(input("Enter your Physics Subject Marks: "))
* sub3 = int(input("Enter your Chemistry Subject Marks: "))
* sub4 = int(input("Enter your Bio Science Subject Marks: "))
* sub5 = int(input("Enter your Math Subject Marks: "))
 
* total = (sub1+sub2+sub3+sub4+sub5)/5
 
* if total >= 80 and total <= 100 :
*     print("A+")
* elif total >= 70 and total < 80 :
*     print("A")
* elif total >= 60 and total < 70 :
*     print("B")
* elif total >= 50 and total < 60 :
*     print("C")
* elif total >= 40 and total < 50 :
*     print("D")
* elif total >= 33 and total < 40 :
*     print("E")
* elif total >= 0 and total < 33 :
*     print("You are Fail!")

+ Output Is:

+ Enter your English Subject Marks: 30
+ Enter your Physics Subject Marks: 90
+ Enter your Chemistry Subject Marks: 70
+ Enter your Bio Science Subject Marks: 40
+ Enter your Math Subject Marks: 60
+ C

+ Step No_(2):

* user = int(input("Enter your Number "))
* if user % 2 == 0 :
*     print("This Is Even Number")
* else :
*     print("This Is Odd Number")

+ Output Is:

+ Enter your Number 152
+ This Is Even Number

+ Step No_(3):

* list = ["HTML","CSS","JavaScript","EcmaScript","React Js","Redux","React Native","Firebase","Github","Bootstrap","Linux"]
* print(len(list))

+ Output Is:

+ 11

+ Step No_(4):

* Sum = [10,5,15,40,10,20]
* print(sum(Sum))

+ Output Is:

+ 100 

+ Step No_(5):

* largest = [65,34,23,67,98,56,87]
* print(max(largest))

+ Output Is:

* 98  

+ Second Option:

* largest = [65,34,23,67,98,56,87]
* largest.sort()
* print(largest[-1])

+ Output Is:

+ 98

+ Step No_(6):

* a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
* for i in a :
*     if i < 5 :
*         print(i)

+ Output Is:

+ 1
* 1
* 2
* 3

#                                                 Assignment_No_(2) Is Completed

#                                                            Tuples

+ Definition & Usage: 

+ Tuples are used to store multiple items in a single variable.
+ Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
+ A tuple is a collection which is ordered and unchangeable.
+ Tuples are written with round brackets.

+ Example: 

* tp = ("I","Learned","Python","In",2,"Hours",True)
* print(tp)

+ Output Is:

+ ('I', 'Learned', 'Python', 'In', 2, 'Hours', True)

#                                                         Tuples Index 

* tp = ("I","Learned","Python","In",2,"Hours",True)
* print(tp[2])

+ Output Is:

+ Python

+ Tuples allow duplicate values:

* thistuple = ("apple", "banana", "cherry", "apple", "cherry")
* print(thistuple[3])

+ Output Is: 

+ apple

#                                                   List & Tuple Difference

* List Is Changeble.
* But Tuples Is Not Changeble. 

#                                                      Python For Loop

+ Definition & Usage:

+ A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
+ This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
+ With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

+ Example:

* list = [1,2,3,4,5,6,7,8,9,10]
* print(list)
* for i in list :
*     print(i)

+ Output Is:

+ [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
+ 
+ 1
+ 2
+ 3
+ 4
+ 5
+ 6
+ 7
+ 8
+ 9
+ 10

+ Second Example_(String):

* fruits = ["Apple","Mango","Orange","Banana","Watermillon","Cherry","Strawberry"]
* for iteration in fruits :
*     print(iteration)

+ Output Is:

* Apple
* Mango
* Orange
* Banana
* Watermillon
* Cherry
* Strawberry

#                                                     For_Loop_(Break Method)

+ Definition & Usage

+ The break keyword is used to break out a for loop

+ Example

* cleanest_City = ["Karachi","Lahore","Faisalabad","Islamabad","Hyderabad"]
* user_City = input("Enter Your City Name: ")
* for City in cleanest_City :
*     if user_City == City :
*         print(user_City,"Is Cleanest City.")
*         break
* else :
*     print(user_City,"Is Not Cleanest City.")

+ Output Is:

+ Enter Your City Name: Karachi
+ Karachi Is Cleanest City.

#                                                     Nested Loop In Python

+ Definition & Usage:

+ A nested loop is a loop inside a loop.
+ The "inner loop" will be executed one time for each iteration of the "outer loop":

+ Example: 

* First_Name = ["Ghouse ","Basit","Muhammad Ali","Muhammad","Mark"]
* Last_Name = ["Ahmed","Ahmed","Mughal","Umair","Myers"]
* Full_Name = []

* for Fe_First_Name in First_Name : # Outer For Loop
*     for Fe_Last_Name in Last_Name : # Inner For Loop
*         Full_Name.append(Fe_First_Name + " " + Fe_Last_Name)
*     
* print(Full_Name)

+ Output Is:

* ['Ghouse  Ahmed', 'Ghouse  Ahmed', 'Ghouse  Mughal', 'Ghouse  Umair', 'Ghouse  Myers', 'Basit Ahmed', 'Basit Ahmed', 'Basit  Mughal', 'Basit Umair', 'Basit Myers', 'Muhammad Ali Ahmed', 'Muhammad Ali Ahmed', 'Muhammad Ali Mughal', 'Muhammad Ali Umair',  'Muhammad Ali Myers', 'Muhammad Ahmed', 'Muhammad Ahmed', 'Muhammad Mughal', 'Muhammad Umair', 'Muhammad Myers', 'Mark Ahmed',  'Mark Ahmed', 'Mark Mughal', 'Mark Umair', 'Mark Myers']

#                                                        While Loop In Python

*  num = 0
* while(num <= 10) :
*     print(num)
*     num = num +1

+ Output Is:

+ 0
+ 1
+ 2
+ 3
+ 4
+ 5
+ 6
+ 7
+ 8
+ 9
+ 10

#                                                  Table Generate Using While Loop

*  num = 1
* while(num <= 10) :
*     print("2" +" "+ "x" +" "+ str(num) +" "+ "=" +" "+ str(2*num) )
*     num = num + 1

+ Output Is:

+ 2 x 1 = 2
+ 2 x 2 = 4
+ 2 x 3 = 6
+ 2 x 4 = 8
+ 2 x 5 = 10
+ 2 x 6 = 12
+ 2 x 7 = 14
+ 2 x 8 = 16
+ 2 x 9 = 18
+ 2 x 10 = 20

#                                         Integer Number Convert Into Float Number(float,int)

+ Example: 

* a = 10
* b = float(a)
* print(b)

+ Output Is:

+ 10.0

#                                         Integer Number Convert Into String_("10") Number(str)

* a = 10
* b = str(a)
* c = 15
* d = b + c
* print(d)

+ Output Is:

+ TypeError: can only concatenate str (not "int") to str

#                                        Changing Case_(LowerCase , UpperCase , CapitalizeCase , Title)

+ Definition & Usage: 

+ In the Changing Case We Talk About The Lower Case & The Upper Case.
* lower()- Return a copy of the string with all the cased characters converted to lowercase.
* upper()- Return a copy of the string with all the cased characters converted to uppercase.
* capitalize()- Return a copy of the string with its first character capitalized and the rest lowercased.

+ Example_(UpperCase):

* a = "MarK"
* print(a.upper())

+ Output Is: 

+ MARK

+ Example_(LowerCase):

* a = "MarK"
* print(a.lower())

+ Output Is: 

+ mark

+ Example_(CapitalizeCase):

* a = "MarK"
* print(a.capitalize())

+ Output Is: 

+ Mark

+ Example_(Title Same Work (CapitalizeCase)):

* a = "MarK"
* print(a.title())

+ Output Is: 

+ Mark

#                                                        Dictionary_In_Python

+ Dictionary is an object that represent is an key/value.
+ The Dictionary can be declared by using curly braces {}.
+ And each key-value pair is separated by the commas(,).

+ Dictionary_Syntex:

+ var dictionary = {                                     ===>                   #  dictionary = {                 
+   "Name": "ExamPle_Name",                              ===>                   #    "Key" : "Value",                            
+   "Roll_No": "1897",                                   ===>                   #    "Key" : "Value",                      
+   "Contact_No": "+92111111111"                         ===>                   #    "Key" : "Value",                       
+ };                                                     ===>                   #  }; ===>                 (SemiColon(;))    

+ Example: 

* fruit = {1: "Apple", 2: "Mango", 3: "OranGe", 4: "Banana", 5: "WaterMelon"};
* print(fruit)

+ Output Is: 

+ {1: 'Apple', 2: 'Mango', 3: 'OranGe', 4: 'Banana', 5: 'WaterMelon'}

#                                             Access Particular Property Inside Dictionary: 

* Student = {"Firstmame": "Jibran", "Lastname": "Abdul Jabbar", "Roll no": 1834, "Coaching": "BMJ_(Bantva Memon Jamat Education)", "Contact no": "+921111111122"};
* print(Student["Coaching"])

+ Output Is:

+ BMJ_(Bantva Memon Jamat Education)

#                                              Dictionary Inside Edit Any Property Value

* Student = {"Firstmame": "Jibran", "Lastname": "Abdul Jabbar", "Roll no": 1834, "Coaching": "BMJ_(Bantva Memon Jamat Education)", "Contact no": "+921111111122"};
* Student["Coaching"] = "Saylani Mass IT Training Program"
* print(Student)

+ Output Is: 

+ {'Firstmame': 'Jibran', 'Lastname': 'Abdul Jabbar', 'Roll no': 1834, 'Coaching': 'Saylani Mass IT Training Program', 'Contact no': '+921111111122'}

#                                              Dictionary Inside Add Any Property Value

* Student = {"Firstmame": "Jibran", "Lastname": "Abdul Jabbar", "Roll no": 1834, "Coaching": "BMJ_(Bantva Memon Jamat Education)", "Contact no": "+921111111122"};
* Student["Batch"] = "5th"
* print(Student)      

+ Output Is:

+ {'Firstmame': 'Jibran', 'Lastname': 'Abdul Jabbar', 'Roll no': 1834, 'Coaching': 'BMJ_(Bantva Memon Jamat Education)', 'Contact no': '+921111111122', 'Batch': '5th'}

#                                               Dictionary Inside Remove Any Property

* Student = {"Firstmame": "Jibran", "Lastname": "Abdul Jabbar", "Roll no": 1834, "Coaching": "BMJ_(Bantva Memon Jamat Education)", "Contact no": "+921111111122"};
* Student["Batch"] = "5th"
* print(Student)      
* del Student["Batch"]
* print(Student)  

+ Output Is:

* {'Firstmame': 'Jibran', 'Lastname': 'Abdul Jabbar', 'Roll no': 1834, 'Coaching': 'BMJ_(Bantva Memon Jamat Education)', 'Contact no': '+921111111122', 'Batch': '5th'}
* {'Firstmame': 'Jibran', 'Lastname': 'Abdul Jabbar', 'Roll no': 1834, 'Coaching': 'BMJ_(Bantva Memon Jamat Education)', 'Contact no': '+921111111122'}

#                                        Print All Keys Inside (Dictionary) Using_(For Loop)

* Student = {"Firstmame": "Jibran", "Lastname": "Abdul Jabbar", "Roll no": 1834, "Coaching": "BMJ_(Bantva Memon Jamat Education)",  "Contact no": "+921111111122"};
* for keys in Student.keys() :
*         print(keys)

+ Output Is:

+ Firstmame
+ Lastname
+ Roll no
+ Coaching
+ Contact no

#                                       Print All Values Inside (Dictionary) Using_(For Loop)

* Student = {"Firstmame": "Jibran", "Lastname": "Abdul Jabbar", "Roll no": 1834, "Coaching": "BMJ_(Bantva Memon Jamat Education)", "Contact no": "+921111111122"};
* for values in Student.values() :
*         print(values)

+ Output Is:

+ Jibran
* Abdul Jabbar
* 1834
* BMJ_(Bantva Memon Jamat Education)
* +921111111122

#                                                 Creating a List Of Dictionary

+ Example:

* Questions = [
*     {
*         "S no.": 1,
*         "Question1": "What Is Your City Name: ",
*         "Options": ["Karachi","Lahore","Islamabad","Faisalabad","Hyderabad"],
*         "Answer": "Karachi"
*     },
*     {
*         "S no.": 2,
*         "Question2": "What Is Your Batch No: ",
*         "Options": ["5th","4th","3rd","1st","2nd"],
*         "Answer": "5th"
*     },
*     {
*         "S no.": 3,
*         "Question3": "What Is Your Age: ",
*         "Options": ["18","7","32","23","12"],
*         "Answer": "7"
*     },
*     {
*         "S no.": 4,
*         "Question4": "What Is Your Country Name: ",
*         "Options": ["Pakistan","India","America","U.S","Afghanistan"],
*         "Answer": "Pakistan"
*     },
*     {
*         "S no.": 5,
*         "Question5": "Gender: ",
*         "Options": ["Male","Female","Other"],
*         "Answer": "Male"
*     }
* ]

* print(Questions[0])

+ Output Is:

+ {'S no.': 1, 'Question1': 'What Is Your City Name: ', 'Options': ['Karachi', 'Lahore', 'Islamabad', 'Faisalabad', 'Hyderabad'], 'Answer': 'Karachi'}

#                                         Dictionary Inside Get Any Property For Example:

* print(Questions[0]["Question1"])

+ Output Is:

+ What Is Your City Name: 

#                                          Append a new Dictionary in a list of Dictionaries


* Questions = [
*     {
*         "S no.": 1,
*         "Question1": "What Is Your City Name: ",
*         "Options": ["Karachi","Lahore","Islamabad","Faisalabad","Hyderabad"],
*         "Answer": "Karachi"
*     },
*     {
*         "S no.": 2,
*         "Question2": "What Is Your Batch No: ",
*         "Options": ["5th","4th","3rd","1st","2nd"],
*         "Answer": "5th"
*     },
*     {
*         "S no.": 3,
*         "Question3": "What Is Your Age: ",
*         "Options": ["18","7","32","23","12"],
*         "Answer": "7"
*     },
*     {
*         "S no.": 4,
*         "Question4": "What Is Your Country Name: ",
*         "Options": ["Pakistan","India","America","U.S","Afghanistan"],
*         "Answer": "Pakistan"
*     },
*     {
*         "S no.": 5,
*         "Question5": "Gender: ",
*         "Options": ["Male","Female","Other"],
*         "Answer": "Male"
*     }
* ]
 
* new_Dictionary = {
*     "S no.": 6,
*     "Question6": "What Is Your Qualification",
*     "Options": ["Associate","Certificate","B.A.","BArch","BM"],
*     "Answer": "Certificate"
* }

* Questions.append(new_Dictionary)

* print(Questions[5])

+ Output Is:

+ {'S no.': 6, 'Question6': 'What Is Your Qualification', 'Options': ['Associate', 'Certificate', 'B.A.', 'BArch', 'BM'], 'Answer': 'Certificate'}

+ List Inside Dictionary Inside Value List Inside Get Any Value Throw Index:

* print(Questions[5]["Options"][1])

+ Output Is:

+ Certificate

+ Insert & Append Method:

* Questions.append(new_Dictionary)
* Questions.insert(2,new_Dictionary)

#                                               Dictionary of Dictionaries

+ Example: 

* Students_Data = {
*     0: {
*         "Name": "Basit Ahmed",
*         "Roll_No": "1875",
*         "Batch": "2nd",
*         "Coaching": "Saylani Mass IT Training Program"
*     },
*     1: {
*         "Name": "Muhammad Ali Mughal",
*         "Roll_No": "1876",
*         "Batch": "2nd",
*         "Coaching": "Saylani Mass IT Training Program"
*     },
*     2: {
*         "Name": "Ghouse Ahmed",
*         "Roll_No": "1877",
*         "Batch": "2nd",
*         "Coaching": "Saylani Mass IT Training Program"
*     },
*     3: {
*         "Name": "Muhammad Umair",
*         "Roll_No": "1878",
*         "Batch": "2nd",
*         "Coaching": "Saylani Mass IT Training Program"
*     },
* }
 
* print(Students_Data[0])

+ Output Is:

+ {'Name': 'Basit Ahmed', 'Roll_No': '1875', 'Batch': '2nd', 'Coaching': 'Saylani Mass IT Training Program'}

#                            Quiz AppliCation Using List Of Dictionary || For Loop || IF Else Condition

* Quiz_AppliCation = [
*     {
*         "S no.": "Q_1",
*         "Question": "Who was the first President of the Constitution Assembly of Pakistan?",
*         "Options": ["Quaid-e-Azam","Sardar Abdur Rab Nishtar","Liaquat Ali Khan","Moulvi Tameez-ud-Din"],
*         "Answer": "Quaid-e-Azam"
*     },
*     {
*         "S no.": "Q_2",
*         "Question": "After how many years did Pakistan got its first Constitution?",
*         "Options": ["9 years","7 years","5 years","11 years"],
*         "Answer": "9 years"
*     },
*     {
*         "S no.": "Q_3",
*         "Question": "Who was Mohammad Ali Bogra?",
*         "Options": ["Prime Minister","Foreign Minister","Parliament Minister","Law Minister"],
*         "Answer": "Prime Minister"
*     },
*     {
*         "S no.": "Q_4",
*         "Question": "When first constitution of Pakistan was enforced?",
*         "Options": ["23rd March 1956","8th June 1956","14th August 1956","25th December 1956"],
*         "Answer": "23rd March 1956"
*     },
*     {
*         "S no.": "Q_5",
*         "Question": "What official name was given to Pakistan in 1956 constitution?",
*         "Options": ["Islamic Republic of Pakistan","United States of Pakistan","Islamic Pakistan","Republic of Pakistan"],
*         "Answer": "Islamic Republic of Pakistan"
*     },
*     {
*         "S no.": "Q_6",
*         "Question": "What is the other name of Mohammad Ali Bogra Formula?",
*         "Options": ["Constitutional Formula","New Law of Pakistan","Pakistan Report","Third Report"],
*         "Answer": "Constitutional Formula"
*     },
*     {
*         "S no.": "Q_7",
*         "Question": "Who was the Prime Minister of Pakistan during enforcement of first constitution?",
*         "Options": ["Choudhry Mohammad Ali","Mohammad Ali Bogra","Khwaja Nazim Uddin","Ibrahim Ismail Chundrigar"],
*         "Answer": "Choudhry Mohammad Ali"
*     },
*     {
*         "S no.": "Q_8",
*         "Question": "What document was firstly drafted to give pace to constitution making process?",
*         "Options": ["Objective Resolution","Pakistan Act","Independence Act","Representative Act"],
*         "Answer": "Objective Resolution"
*     },
*     {
*         "S no.": "Q_9",
*         "Question": "What age was prescribed for President in 1956 constitution?",
*         "Options": ["40 years","55 years","45 years","50 years"],
*         "Answer": "40 years"
*     },
*     {
*         "S no.": "Q_10",
*         "Question": "In respect of religion what term was set for President and Prime Minister in 1956 constitution?",
*         "Options": ["He must be a Muslim","He may be a Muslim","He must not be Christian","He must not be Hindu"],
*         "Answer": "He must be a Muslim"
*     }
* ]
* 
* Score = 0
* 
* for Quiz in Quiz_AppliCation :
*     Data = Quiz["S no."] + ": " + Quiz["Question"] + "\n" + "* Give your answer in the input field!" + "\n" +"1): "+ Quiz["Options"]* [0] + "\n" +"2): "+ Quiz["Options"][1] + "\n" +"3): "+ Quiz["Options"][2] + "\n" + "4): "+ Quiz["Options"][3] + "\n" + "\n"
*     User_Answer = input(Data)
*     if User_Answer == Quiz["Answer"] :
*         Score += 1
*         
*         print("Your Score Is: " + str(Score) + "\n")

#                                                    Predefined Function 

+ For Example:

* print(),
* input(),
* insert(),
* sort(),
* append(),
* ETC.

#                                              User Defined Functions In Python

+ Definition & Usage:

+ A Function is a block of code which only runs when it is called.
+ You can pass data, known as parameters, into a function.
+ A function can return data as a result.
+ Function Is a Very Important Milestone In Any Programming Language.

#                                                    Creating a Function

+ In Python a function is defined using the def keyword:

* def funcname() :
*     val = "I am Learning"
*     val1 = "Python Function"
*     val2 = "Live now...!"
*     complete_val = val +" "+ val1 +" "+ val2
*     print(complete_val)
     
* funcname() 

+ Output Is:

+ I am Learning Python Function Live now...!

+ Second Example:

* def addition() :
*     num_1 = 5
*     num_2 = 10
*     total = num_1 + num_2
*     print(total)
*     
* addition()

+ Output Is:

+ 15

#                                       Parameters & Arguments In User Defined Function

* def addition(num_1 , num_2) : ===> This Is Parameters.
*     total = num_1 + num_2
*     print(total)
*     
* addition(15 , 5) ===> This Is Arguments.

+ Output Is:

+ 20

+ Second Example_(Parameters & Arguments):

* def addition(num_1 , num_2) : # This Is Parameters
*     total = num_1 + num_2                                          <==    ==>   This Is indentation
*     print(total)
     
* User_1 = int(input("Enter Your Number: "))
* User_2 = int(input("Enter Your Number1: "))    
     
* addition(User_1 , User_2) # This Is Argument

+ Output Is:

+ Enter Your Number: 60
+ Enter Your Number1: 10
+ 70

#                                                  Positional Arguments

* def Full_name(First_name , Last_name) :
*     Complete_name = First_name +" "+ Last_name
*     print(Complete_name)
*     
* Full_name("Jibran","Khan")

+ Output Is:

+ Jibran Khan

+ Second Example_(Positional Argument Mistake):

* def Full_name(Last_name , First_name) :
*     Complete_name = First_name +" "+ Last_name
*     print(Complete_name)
*     
* Full_name("Jibran","Khan")

+ Output Is:

+ Khan Jibran

#                                                  Keyword Arguments

* def Full_name(Last_name , First_name) :
*     Complete_name = First_name +" "+ Last_name
*     print(Complete_name)
*     
* Full_name(First_name = "Jibran", Last_name = "Khan")

+ Output Is:

+ Jibran Khan

#                                                Theory Base Examples:

* num_1 = 10
* num_2 = 5
 
* def addition(Ten , Five) : 
*     Total = Ten - Five 
*     print(Total)
     
* addition(num_1, num_2) 

+ Output Is:

+ 5

#                                              Global Data & Local Data

* First_num = 10 ===> This Is Global Scope Variable.
 
* def theory(Ten , Tweenty = 20) :
*     Total = Ten + Tweenty
*     print(Total)
     
* theory(First_num)

+ Output Is:

+ 30

+ Second Example_(Default, Gloabl, Call Function)

* Inst = "By myself" ===> Global Scope Variable.
 
* def Course_detail(Inst , dur , lang = "Python Programming") : ===> Language Parameter Is a Default Value. 
*     print(Inst +" "+ lang +" "+ dur)

* Course_detail(Inst, dur = "1 Week") ===> Call the Function then Push Duration Argument Value.

+ Output Is:

+ By myself Python Programming 1 Week

#                                              ToDo AppliCation In Python

* elements = []
 
* while True :
*     print("Element In Our List: ")
*     for element in elements :
*         print(" ===> " + element)
      
*     print("\n" + "Option: ")
*     print("1): Add Element.")
*     print("2): Delete Element.")
*     print("3): Delete All Element.")
*     print("4): Exit.")
*     print("Note: Please Give Input In Number e.g 1, 2, 3, 4")
 
*     inp = input("Enter Your Choice: ")
 
*     if inp == '1':
*         elements.append(input("Enter Your Item: "))
*     elif inp == '2':
*         elements.remove(input("Enter Item To Delete: "))
*     elif inp == '3':
*         elements.clear()
*     elif inp == '4':
*         break
*     else:
*           print("Invalid Syntex")
             
*     print("\n ------------------------------------------------------------------------------------------------------ \n")

#                                    OBJECT Oriented Programming Classes In Python

# Classes - Template
# OBJECT - Instance Of the Class

# DRY - Do not repeat Yourself

+ Get_no_of_films(table) ===> Table Filmstar Is Not Exit.

# Definition & Usage:

+ Python is an object oriented programming language.
+ Almost everything in Python is an object, with its properties and methods.
+ A Class is like an object constructor, or a "blueprint" for creating objects.
+ To create a class, use the keyword class:

+ Example:

* class Student:
*     pass
 
* Student_1 = Student()
 
* Student_1.name = "Object Oriented Programming...!"
* Student_1.Learner = "Jibran Abdul Jabbar"
 
* print(Student_1.name)
* print(Student_1.Learner)

+ Output Is: 

+ Object Oriented Programming...!
+ Jibran Abdul Jabbar                                                                                     """
  
#        !... Complete Python Programming With Definition With Explanation With Docs With Assignment With Coding & UsaGe ...!

#           !... Complete OBJECT OREINTED PROGRAMMING With Definition With Explanation With Docs With Coding & UsaGe ...!           