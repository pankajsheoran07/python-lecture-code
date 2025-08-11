'''Ask the user for a number. Depending on whether the number is
 even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?'''
user_input = int(input('give your number: '))
if(user_input % 2 == 0):
    print('your number is even')

else:
    print('your input is not a even number')

    #author way to do this 
33num = input("Enter a number: ")
mod = num % 2
if mod > 0:
    print("You picked an odd number.")
else:
    print("You picked an even number.")