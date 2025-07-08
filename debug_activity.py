#Cecilia Palau Debugging Activity

#Case 1
#Zero Devision Error, can not be devided by 0, chamnged one of the values to something other than 0
x = 10
y = 2.5
result = x/y
print("Result", result)

#Case 2
#Index out of range error, dont put i+1 becuad it will be searching for an index that does not exsist, just leave i
numbers = [1,2,3,4,5]
for i in range(len(numbers)):
    print(numbers[i])

#Case 3
#Syntax error, : is needed at the end of the fucntion
def calculate_area(radius):
   area = 3.14 * radius ** 2
   return area


#Case 4
#Syntax error after the if statement there needs to be a colon (:) as well as the else 
def is_even(number):
   if number % 2 == 0:
       return True
   else:
       return False
 
print(is_even(4))
print(is_even(7))

#Case 5
#Another syntax error, colon needed after the for loop statement
for i in range(5):
   print(i)

#Case 6 
#Syntax error, always close your quotes!  
def greet(name):
   return "Hello,  name"

#Case 7 
#Indentation error, need to have lines indented after the for loop stateme t
numbers = [1, 2, 3, 4, 5]
sum = 0
for number in numbers:
    sum += number
    print("Sum of numbers:", sum)

#Case 8
#Logical error, need to chnage n+1 to n-1 so that the math is correct
def factorial(n):
   if n == 0:
       return 1
   else:
       return n * factorial(n-1)
 
print(factorial(5))

#Case 9
#Syntax error, parenthesos are needed after the if statement
name = input("Enter your name: ")
if name == ("Alice" or "Bob"):
   print("Hello, " + name)
else:
   print("Hello, stranger!")

