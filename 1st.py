#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells
#  them the year that they will turn 100 years old
user_name = str(input('name: '))
user_age = int(input('age: '))
user_age_after_100 = user_age + 100
str1 = str(user_age_after_100)
print('Mr.' + user_name +' '+'your age after 100 years will be' + ' '+ str1)



#book / author way to do the problem 
name = input("What is your name: ")
age = int(input("How old are you: "))
year = 2014 - age + 100
print(name + ", you will be 100 years old in the year " + str(year))