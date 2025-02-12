#Variable = A container for a value(string, integer, float, booelean)
#           A variable behaves as if it was the value it contains 

#String
# first_name = "Mustafa"
# food = "Chicken"

#Integer - Make sure they are not in quotes, then they would be a string
# age = 22
# quantity = 5
# num_of_workers = 11

#Float
# price = 19.99
# gpa = 2.56
# distance = 7

#Boolean - It is either TRUE or FALSE
# is_working = False
# for_sale = False
# is_online = False

#----------------------------------------------------------------------------

#Typecasting = The process of converting a variable from one data type to another.
#              str(), int(), float(), bool() 

# name = ""
# age = 22
# gpa = 2.5
#is_student = True

# name = bool(name)

#-----------------------------------------------------------------------------

#Input = A function that prompts the user to enter data
#        Returns the entered data as a string

#name = input("What is your name?")
#age = int(input("How old are you?"))

#Exercise 1 Rectangle Area Calculator

# length = float(input("Enter the length: "))
# width = float(input("Enter the width: "))
# area = length * width

#-----------------------------------------------------------------------------

#Exercise 2 Shopping Cart Program 

#item = input("What would you like to buy: ")
#price =  float(input("What is the price of the item: "))
#quantity = int(input("How many would you like to buy: "))
#total_pay = price * quantity

#-----------------------------------------------------------------------------

#Mad Libs game = It's a word game where you create a story by filling in blanks with random words

#team = input("Enter your favourite team (a sports team):")
#adjective1 = input("Enter an adjective (description):")
#noun1 = input("Enter a noun (person, place, thing):")
#player = input("Enter your favourite player (a player from your team):")
#adjective2 = input("Enter an adjective (description):")
#verb = input("Enter a verb (ending with -ing):")
#adjective3 = input("Enter an adjective (description):")



#print (f"Today I went to see my favourite team,{team}'s match.")
#print (f"It was absolutely {adjective1} and I had so much fun")
#print (f"I went to see the match with my {noun1}/s")
#print (f"My favourite player was {player} he made a lot of {adjective2}")
#print (f"The saddest thing was {verb} back home")
#print (f"All in all, it was a {adjective3} experience!")

#-----------------------------------------------------------------------------

#Arithmethic & math 

#friends = 10
#friends = friends + 1
#friends += 1
#friends = friends - 1
#friends -= 1
#friends = friends / 2
#friends /= 2
#friends = friends * 3
#friends *= 2
#friends = friends ** 2
#friends **= 2 
#friends = friends % 3
#friends %= 3

#x = 3.14
#y = 4
#z = 5

#result = max(x, y, z)
#result = min(x, y, z)
#result = pow(x, y)
#result = abs(y)
#result = round(x)

#-----------------------------------------------------------------------------

#import math 

#radius = float(input("Enter the radius of the circle: "))
#circumference = 2 * math.pi * radius 

#print(f"The circumference of the circle is {round(circumference, 2)}cm ")

#import math 

#radius = float(input("Enter the radius of a circle:"))
#area = math.pi * pow(radius, 2)

#print(f"The area of this circle is {round(area, 1)} cm^2")

#-----------------------------------------------------------------------------

#import math 

#a = float(input("Enter side A:"))
#b = float(input("Enter side B:"))

#c = math.sqrt (pow(a, 2) + pow(b, 2))

#print (f"Side C of a triangle is {round (c, 2)} cm)")

#-----------------------------------------------------------------------------

#IF statements = Do some code only IF some condition is True
#                Else do something else   

#age = int(input("Enter your age: "))

#if age >= 100:
    #print("You are too old to sign up!")    
#elif age >= 18:
    #print("You are eligible to sign up")
#elif age <= 0: 
    #print("You haven't born yet to sign up!")    
#else: 
    #print("You are not old enough to sign up!")  

#response = input("Would you like some food? (Y/N): ")

#if response == "Y":
#    print ("You can have some food")
#else:
#    print ("No food for you!")  

#name = input("Please enter your name: ")

#if name == "":
#    print("You did not enter your name!")
#else:
#    print(f"Hello {name}")    

#online = True

#if online:
#    print("This person is online")
#else:
#    print("This person is OFFLINE!")    

#-----------------------------------------------------------------------------

# Python Calculator 

#operator = input("Enter an operator: (+ - * /) ")

#number1 = float (input("Enter your first number: "))
#number2 = float (input("Enter your second number: "))

#if operator == "+" :
#   result = number1 + number2
#   print (result)
#elif operator == "-" :
#   result = number1 - number2
#   print(result)     

#elif operator == "*" :
#   result = number1 * number2
#   print(result)     

#elif operator == "/" :
 #  result = number1 / number2
 #  print(result)     
         
#-----------------------------------------------------------------------------     

#Python Weight Converter

#weight = float(input("Enter your weight: "))
#unit = input("Kilograms or Pounds? (K or L): ")

#if unit == "K":
 #   weight = weight * 2.205
  #  unit = "lbs."
   # print (f"Your weight is {round(weight, 1)} {unit}  ")
#elif unit == "L":
 #    weight = weight / 2.205
  #   unit = "kgs."
   #  print ((f"Your weight is {round(weight, 1)} {unit} "))
#else:
 #   print(f"Your {unit} is not valid!")     

#-----------------------------------------------------------------------------

#Temperature Converter

#unit = input("The temperature's unit is (C or F): ")
#temp = float(input("The temperature is: "))

#if unit == "C":
  #  temp = round((9 * temp) / 5 + 32, 1)
 #   print(f"The temperature in Fahrenheit is {temp} °F ")
#elif unit == "F":
  #  temp = round((temp - 32) * 5/9, 1)
 #   print(f"The temperature in Celcius is {temp} °C ")
#else: 
#    print (f"Your unit {unit} is invalid!")

#-----------------------------------------------------------------------------

#Logical Operators = Evaluate multiple conditions (or, and, not)   
#                    or = at least one condition must be True
#                    and = both conditions must be True    
#                    not = inverts the condition (not False, not True)

#temp = 25
#is_raining = False

#if temp > 35 or temp < 0 or is_raining:
 #   print("Today is rainy")
#else:
 #   print("There is no rain today")    

#temp = 29
#is_sunny = True

#if temp >= 28 and is_sunny :
#    print ("It is a little bit hottoday")
 #   print("However it is sunny lowkey")
#elif temp <= 0 and is_sunny:
 #   print("It is cold outside, put ma hoodie on tight")
  #  print("It looks sunny")
#elif  28 > temp > 0 and is_sunny:
 #   print("It is warm outside")
  #  print("It is sunny!")
#elif temp >= 28 and not is_sunny :
 #   print ("It is a little bit hottoday")
  #  print("However it is cloudy lowkey")
#elif temp <= 0 and not is_sunny:
 #   print("It is cold outside, put ma hoodie on tight")
  #  print("It looks cloudy")
#elif  28 > temp > 0 and not is_sunny:
 #   print("It is warm outside")
  #  print("It is cloudy!")    

#-----------------------------------------------------------------------------

#Conditional Expressions - A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one or two values based on the condition
#                          X if condition else Y 

#score = 22
#score_list = "All Star level" if score >= 30 else "Bench Warmer"

#number = 3
#type_number = "EVEN" if number % 2 == 0 else "ODD"

#a = 6
#b = 7

#max_number = a if a > b else b 

#print(max_number)

#-----------------------------------------------------------------------------

#String Methods 

#name = input("Please enter your full name: ")

#result = len(name)
#result = name.find("u")
#result = name.rfind("z")
#name = name.capitalize()
#name = name.upper()
#name = name.lower()
#name = name.isdigit()
#name = name.isalpha()
#phone_num = input("Enter your phone number: ")
#phone_num = phone_num.count("-")
#phone_num = phone_num.replace("-", "")

#print(phone_num)

#Validate user input Exercise -- 1.Username is no more than 12 characters 2-Username must not contain spaces  3-Username must not contain digits

#user_name = input("Please enter your username: ")

#if len(user_name) > 12:
 #  print ("Username cannot be longer than 12 characters!")
#elif not user_name.find(" ") == -1:
 #  print("Username cannot include spaces!")    
#elif not user_name.isalpha():
 #  print("Username cannot have digits!")   
#else: 
 #  print(f"Welcome {user_name}")    
  
#-----------------------------------------------------------------------------

#Indexing = Accessing elements of a sequence using [] (indexing operator)
#                        [start : end : step]

#credit_num = "1234-567-8903"
#print(credit_num[7])
#print(credit_num[:4])
#print(credit_num[5:])
#print(credit_num[-1])
#print(credit_num [::3])
#last_digits = credit_num[-4: 13]
#print(last_digits)
#print(credit_num[::-1])

#card_number = "5265-789-0123"

#last_digits = card_number[-4:]

#print(f"xxxx-xxx-{last_digits}")

#-----------------------------------------------------------------------------

#Format Specifiers = {value: flags} format a value based on what flags are inserted 

#price1 = 3000.147823
#price2 = -1276.59
#price3 = 2500.9826

#print(f"Price 1 is £{price1:+,.2f}")
#print(f"Price 2 is £{price2:+,.2f}")
#print(f"Price 3 is £{price3:+,.2f}")

#-----------------------------------------------------------------------------

#While Loop = Execute some code WHILE some condition remains true

#name = input("Enter your name: ")

#while name == "":
 #   print ("You did not enter your name!") 
  #  name = input("Enter your name: ")    
#print(f"Hello {name}")

#age = int(input("Enter your age: "))

#while age < 0 or age > 100: 
 #   print ("Your age cannot be negative or more than 100!")
  #  age = int(input("Enter your age: "))
#print(f"You are {age} years old.")

#food = input("Enter a food you like (press q to exit): ")

#while not food == "q":
 # print(f"You like {food}" )
  #food = input("Enter another food you like (press q to exit): ")

#print("bye")

#-----------------------------------------------------------------------------

#Python compound interest calculator

#principle = 0
#rate = 0
#time = 0

#while principle <= 0: 
 #   principle = float(input(("Please enter the principal value: ")))
  #  if principle <= 0:
   #   print("Principle cannot be less or equal to zero.")

#while rate <= 0: 
 #   rate = float(input(("Please enter the interest rate: ")))
  #  if rate <= 0:
   #   print("Rate cannot be less or equal to zero.")

#while time <= 0: 
 #   time = int(input(("Please enter the time (year): ")))
  #  if time <= 0:
   #   print("Time cannot be less or equal to zero.")


#total = principle * pow ((1 + rate / 100), time)

#print(f"Your balance after {time} year/s is ${total:.2f}")

#-----------------------------------------------------------------------------

#For Loops = Execute a block of code a fixed number of times
#            You can itirate over a range, string, sequence etc. 

#for x in range (1,18):
 # if x == 13:
  #  break
  #print(x)

#credit_num = "1234 - 5678 - 9012 - 3456"
#for x in credit_num:
 # print(x)

#Countdown Timer Program

#import time

#my_time = int(input( "Please enter the seconds: ")) 

#for x in range(my_time, 0, -1 ):
 #   time.sleep(1)
  #  seconds = x % 60
   # minutes = int(x / 60) % 60
    #hours = int(x / 3600)
    #print(f"{hours:02}:{minutes:02}:{seconds:02}")

#-----------------------------------------------------------------------------    

#Nested Loop = A loop within another loop (outer, inner) 
#              outer loop:
#                  inner loop:

#rows = int(input("Enter the # of rows: ")) 
#columns = int(input("Enter the # of columns: "))
#symbol = input("Enter the symbol of your choice: ")

#for x in range(rows):
 #   for y in range(columns):
  #    print(symbol, end="")
   # print()

#-----------------------------------------------------------------------------    

# Collection = Single "variable" used to store multiple values 
#   List = [] ordered and changable. Duplicates OK
#   Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangable. Duplicates OK. FASTER

# fruits = ["apple", "banana", "peach", "coconut"]

# fruits.pop()

# print(fruits.count("apple"))
# print(fruits.index("coconut"))
#fruits.clear()
# fruits.sort()
# fruits.reverse()

# fruits.insert(0, "orange")
# fruits.remove("banana")

# fruits.append("pineapple")
# print(fruits)
# fruits[1] = "avocado"

# print("berry" in fruits) 
# print("apple" in fruits) 
# print(len(fruits))
# print(dir(fruits))
# print(help(fruits))

# print(fruits)

# for fruit in fruits: 
 #   print(fruit) 

#-----------------------------------------------------------------------------

# Shopping Cart Program 

#foods = []
#prices = []
#total = 0

#while True:
 #   food = input("Enter a food you like (press q to quit): ")
  #  if food.lower() == "q":
   #     break
    #else:
     #   price = float(input(f"Enter the price of the {food} you like: $"))
      #  foods.append(food)
       # prices.append(price)

#print("----- YOUR CART -----")

#for food in foods:
 #   print(food, end=" ")
#for price in prices: 
 #   total += price

#print()
#print(f"Your total is:$ {total} ")    

#-----------------------------------------------------------------------------

#2d Collections 

#fruits = ["banana, apple, pear, watermelon"]
#vegetables = ["carrot, tomato, onion"]
#meats = ["chicken, beef, fish"]

#groceries = [fruits, vegetables, meats]

#print(groceries[0])

#groceries = [["banana", "apple", "pear", "watermelon"],
 #            ["carrot", "tomato", "onion"],
  #           ["chicken", "beef", "fish"]]

#print(groceries[0][1])

#Number Pad

#num_pad = ((1, 2, 3),
 #          (4, 5, 6),
  #         (7, 8, 9), 
   #        ("#", 0, "*"))

#for row in num_pad:
 #   for num in row:
  #      print(num, end=" ")
   # print()    

#-----------------------------------------------------------------------------

#Python Quiz Game

#questions = ("Who is the greatest player of all time?: ",
 #            "What is Kobe Bryant's nickname?: ",
  #           "Who are the founding members of Mamba&Rose Industries?: ",
   #          "How many goals Messi has scored in 2012?: ",
    #         "In what season Derrick Martell Rose was crowned the MVP?: " )

#options = (("A. Johan Cruyff ", "B. Lionel Messi ", "C. Thierry Henry ", "D. Alex De Souza "), 
 #          ("A. King of LA ", "B. Beast ", "C. Black Mamba ", "D. Proud daddy of lebron "), 
  #         ("A. Mustafa Duran & Umut Tengiz ", "B. Kobe Bryant & Derrick Rose ", "C. Franklin & Oso ", "D. Ned Stark "),
   #        ("A.88 ", "B.89 ", "C.90 ", "D.91 "),
    #       ("A.08-09 ", "B.09-10 ", "C.10-11 ", "D.11-12 "))

#answers = ("B", "C", "A", "D", "C")
#guesses = []
#score = 0
#question_num = 0

#for question in questions:
 #   print("§§§§§§§§§§§§§§§")
  #  print(question)
   # for option in options[question_num]:  
#        print(option)
 #   guess = input("Enter A,B,C,D: ").upper()   
  #  guesses.append(guess)
   # if guess == answers[question_num]:
    #    score += 1
     #   print("Correct")
    #else: 
#      print("Incorrect") 
 #     print(f"{answers[question_num]} is the correct answer")   
  #  question_num += 1

#print("§§§§§§§§§§§§§§§")
#print("     RESULTS    ")
#print("§§§§§§§§§§§§§§§")

#print("answers: ", end ="")
#for answer in answers:
 #   print (answer, end =" ")
#print()    

#print("guesses: ", end ="")
#for guess in guesses:
 #   print (guess, end =" ")
#print()

#score = int(score / len(questions) * 100)
#print(f"Your score is {score} %")

#-----------------------------------------------------------------------------

#Dictionary = A collection of {key:value} pairs 
 #            ordered and changable. No duplicates. 

# capitals = {"USA": "Washington D.C.",
#           "Turkiye": "Ankara", 
 #          "England": "London",
 #          "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))

# print(capitals.get("Japan"))
# print(capitals.get("England"))

# if capitals.get("Japan"):
#    print("That capital exists!")
# else:
#    print("That capital does not exist!")    

# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "New York"})
# capitals.pop("Russia")
# capitals.popitem()

# keys = capitals.keys()
# for key in capitals.keys():
#    print(key)

# values = capitals.values()
# for value in capitals.values():
#    print(value)

# items = capitals.items()
# for key, values in capitals.items():
#    print(f"{key}, {values}")

#-----------------------------------------------------------------------------

# Concession Stand Game  

# menu = {"pizza": 3.00,
#        "coke": 1.50,
#        "popcorn": 4.20,
#       "fries": 2.00,
#       "candy": 1.20,
#        "chocolate": 1.80,
#        "slushy": 3.50,}
                     

# cart = []
# total = 0
 
# print("----- MENU ------ ")    

# for key, value in menu.items():
#    print(f"{key:10}: ${value:.2f}")

# print("----------------- ")

# while True:
#    food = input("Select items from the menu(q to quit):").lower()
#    if food == "q":
#      break  
#    elif menu.get(food) is not None:
#      cart.append(food)
    
# print("---- YOUR ITEMS ----")

# for food in cart:
#    total += menu.get(food)

#    print(food, end=" ")      

# print()
# print(f"Your total is: ${total:.2f}")

# print("--------------------")

#-----------------------------------------------------------------------------

# import random 

# low = 1 
# high = 100
# options = ("rock", "paper", "scissors")
# cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "Q", "A" ]

# number = random.randint(low,high)
# number = random.random()
# option = random.choice(options)
# random.shuffle(cards)

# print(cards)

#-----------------------------------------------------------------------------

# Number Guessing Game

# import random

# lowest_num = 1
# highest_num = 100
# answer = random.randint(lowest_num, highest_num)
# guesses = 0 
# is_running = True

# print("Welcome to Mustafa's number guesser!")
# print(f"Select a number between {lowest_num} and {highest_num}")

# while is_running:

#    guess = input("Enter your guess: ")

#    if guess.isdigit(): 
#        guess = int(guess)
#        guesses += 1
    
#        if guess < lowest_num or guess > highest_num: 
#              print("Your answer is out of range!") 
#              print(f"Enter a number between {lowest_num} and {highest_num}") 
#        elif guess < answer:
#              print("Too low!")      
#        elif guess > answer:  
#              print("Too high!")
#        else: 
#            print(f"CORRECT The answer was {answer}")     
#            print(f"Number of guesses: {guesses}")   
#            is_running = False    
#    else:
#        print("Invalid guess") 
#        print(f"Select a number between {lowest_num} and {highest_num}")  

#-----------------------------------------------------------------------------

# Rock, Paper, Scissors Game 

# import random

# options = ("rock", "paper", "scissors")
# running = True

# while running:
  
#  player = None
#  computer = random.choice(options)
  
#  while player not in options:
#      player = input("Enter your choice(rock, paper, scissors): ")

#  print(f"Player: {player}")
#  print(f"Computer: {computer}")

#  if player == computer:
#          print("It's a tie")
#  elif player == "rock" and computer == "scissors":    
#          print("You win") 
#  elif player == "paper" and computer == "rock":    
#          print("You win") 
#  elif player == "scissors" and computer == "paper":    
#          print("You win")
#  else:
#          print("You lose")      

#  if not input("Do you want to play again? (y/n): ").lower() == "y":
#      running = False

# print("Thanks for playing bro!")   

#-----------------------------------------------------------------------------   
              
# Dice Roller Program 

# import random 

# ● ┌ ─ ┐ │ └ ┘ 

#  "┌─────────┐"
#  "│         │"
#  "│         │"
#  "│         │"
#  "└─────────┘"

# dice_art = {  
#    1: ("┌─────────┐", 
#        "│         │", 
#        "│    ●    │", 
#        "│         │", 
#        "└─────────┘"), 
#    2: ("┌─────────┐", 
#        "│ ●       │", 
#        "│         │", 
#        "│      ●  │", 
#        "└─────────┘"), 
#    3: ("┌─────────┐", 
#        "│ ●       │", 
#        "│    ●    │", 
#        "│       ● │", 
#        "└─────────┘"), 
#    4: ("┌─────────┐", 
#        "│ ●     ● │", 
#        "│         │", 
#        "│ ●     ● │", 
#        "└─────────┘"), 
#    5: ("┌─────────┐", 
#        "│ ●     ● │", 
#        "│    ●    │", 
#        "│ ●     ● │", 
#        "└─────────┘"), 
#    6: ("┌─────────┐", 
#        "│ ●     ● │", 
#        "│ ●     ● │", 
#        "│ ●     ● │", 
#        "└─────────┘")                 
#}    

# dice = []
# total = 0
# num_of_dice = int(input("How many dice?: "))

# for die in range(num_of_dice):
#     dice.append(random.randint(1,6))

# for die in range(num_of_dice):
#    for line in dice_art.get(dice[die]):
#        print(line)  

# for line in range(5):
#    for die in dice:
#        print(dice_art.get(die)[line], end="")
#    print()        

# for die in dice: 
#    total += die
#print(f"total: {total}")       

#-----------------------------------------------------------------------------
  
# Functions = A block of reusable code 
#             place () after the function name to invoke it

# def happy_birthday(name, age):

#    print(f"Happy birthday to {name}")
#    print(f"You are {age} years old")
#    print("Happy birthday to you")

# happy_birthday("Umut", "23")
# happy_birthday("Mustafa", "23")
# happy_birthday("Sebo", "27")

# def display_invoice(username, amount, due_date):

#    print(f"Hello {username}, your bill of ${amount} is due on {due_date}")

# display_invoice("MustafaD", "800", "Monday")    

#-----------------------------------------------------------------------------

# Return 

# def add(x, y):
#    z = x + y
#    return z
# def subtract(x, y):
#    z = x - y
#    return z
# def multiply(x, y):
#    z = x * y
#    return z
# def divide(x, y):
#    z = x / y          
#    return z

# print(add(8,5))
# print(subtract(3,5))
# print(multiply(8,5))
# print(divide(12,6))

# def create_name(first, second):
#    first = first.capitalize()
#    second = second.capitalize()
#    return first + " " + second

# full_name = create_name("lionel", "messi") 

# print(full_name)

#-----------------------------------------------------------------------------

# Default Arguements = A default value for certain parameters 
#                      default is used when that arguement is omitted
#                      make your functions more flexible, reduces # of arguements
#                      1.positional 2.DEFAULT 3.keyword 4.arbitrary 

# import time 

# def net_price(price, discount=0, tax=0.5):
#  return price + (1 - discount) * (1 + tax)

# print(net_price(725))

# def count(start, end):
#  for x in range(start, end):
#      print(x)
#      time.sleep(1)
# count(0, 10)
# print(count)

#-----------------------------------------------------------------------------

# Keyword Arguements = An arguement preceded by an identifier 
#                      helps with readability 
#                      order of arguements doesn't matter
#                      1.positional 2.default 3.KEYWORD 4.arbitrary  

# def get_num(country, area, first, last):
#    return f"{country}-{area}-{first}-{last}"

# phone_num = get_num(country=1, area=23, first=456, last=7890)
# print(phone_num)

#-----------------------------------------------------------------------------

# *args = Allows you to pass multiple non-key arguements
# **kwargs = Allows you to pass multiple keyword arguements
#           *unpacking operator
#           1.positional 2.default 3.keyword 4.ARBITRARY
# The name you are giving is not as important as the unpacking operator (*)

# def add(*args):
#  total = 0
#  for arg in args:
#    total += arg
#  return total  

# print(add(1,2,3,4,5,6))

# def display_name(*args):
#    for arg in args:
#        print(arg, end=" " )

# display_name("Coder","Baller", "Mustafa", "Duran") 

# def print_address(**kwargs):
#    for key, value in kwargs.items():
#        print(f"{key}: {value}")

# print_address(city="Istanbul",
#         district="Umraniye", 
#         alley="Madenler", 
#         areacode="34764")        

# def shipping_point(*args, **kwargs):
#    for arg in args:
#      print(arg, end=" ")
#    print()  
  
#    if "num" in kwargs:
#        print(f"{kwargs.get("city")} {kwargs.get("num")}")
#    else: 
#        print(f"{kwargs.get("city")}")     
#    print(f"{kwargs.get("district")} {kwargs.get("alley")} {kwargs.get("street")}")   
  
# shipping_point("MVP", "Derrick", "Martell", "Rose",
#              city="Istanbul",
#              district="Umraniye",
#              alley="Madenler",         
#              street="Ozlem",
#              num="5/B")  

#-----------------------------------------------------------------------------

# Iterables = An object/collection that can return its elements one at a time, 
#             allowing it to be iterated over in a loop

# numbers = [1,2,3,4,5]

# for number in reversed(numbers):
#    print(number, end=" ")

# fruits = {"banana", "pear", "orange", "melon"}

# for fruit in fruits:
#    print(fruit)

# name = "Derrick Martell Rose"

# for character in name:
#    print(character, end=" ")

# my_dictionary = {"A": 1, "B": 2, "C": 3}

# for key, value in my_dictionary.items():
#    print(f"{key} = {value}")

#-----------------------------------------------------------------------------

# Membership Operators = Used to test whether a value or variable is found in sequence
#                        (string, list, tuple, set, or dictionary)
#                        1.in   2.not in 

# word = "ROSE".lower()

# letter = input("Enter a letter: ")

# if letter not in word:
#    print(f"The letter {letter} was not found on this word") 
# else:
#     print(f"Correct! The letter {letter} is found in this word")    

# players = {"durant", "steph", "kyrie", "derrick", "kobe"}

# player = input("Enter the name of a player: ")

# if player in players:
#    print(f"{player} is in this list")

# else: 
#    print(f"{player} is not on this list")    

# ranking = {"durant": "D", 
#            "steph": "E", 
#            "kyrie": "C", 
#            "derrick": "A", 
#            "kobe": "B" }

# player = input("Enter the name of a player: ")

# if player in ranking:
#    print(f"{player} has the ranking {ranking[player]}")

# else:
#    print(f"{player} is not found on this list")    
             
#-----------------------------------------------------------------------------

# List Comprehension = A concise way to crate lists in python 
#                      Compact and easier to read than traditional loops.
#                      [expression for value in iterable if condition]  

#doubles = [x * 2 for x in range (1,11)]
#triples = [y * 3 for y in range (1,11)]
#squares = [z * z for z in range (1,11)]

#print(squares)
#print(triples)
#print(doubles) 

# fruits = ("apple", "banana", "strawberry", "melon")
# fruit_chars = [fruit[0].upper() for fruit in fruits] 

# print(fruit_chars)

# numbers = [1, -2, 3, -4, 5, -6, 8]
# positive_nums = [num for num in numbers if num >= 0]
# negative_nums = [num for num in numbers if num < 0]
# even_nums = [num for num in numbers if num % 2 == 0]
# odd_nums = [num for num in numbers if num % 2 == 1]

# print(odd_nums)
# print(even_nums)
# print(positive_nums)
# print(negative_nums)

# grades = [80, 67, 45, 32, 52, 75, 96, 21]

# passing_grades = [grade for grade in grades if grade >= 60]

# print(passing_grades)

#-----------------------------------------------------------------------------

# Match-case Statements = An alternative to using many 'elif' statements
#                         Execute some code if a value matches a case 
#                         Benefits => Cleaner and syntax is more readable

# def is_weekend(day):
#    match(day):
#      case "Saturday" | "Sunday":
#          return True
#      case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
#          return False

# print(is_weekend("Friday"))

#-----------------------------------------------------------------------------

# Module = A file containing code you want to include in your program 
#          Use 'import' to include a module (built-in or your own)
#          useful to break up a large program reusable seperate files 

# import math 
# import math as m
# from math import pi
# print(pi)

# a, b, c, d, e = 1, 2, 3, 4, 5 

# print(math.e ** a)
# print(math.e ** b)
# print(math.e ** c)
# print(math.e ** d)
# print(math.e ** e)

# Banking Program

# def show_balance(balance):
#    print(f"Your balance is ${balance:.2f}")

# def deposit():
#    amount = float(input("Enter amount to deposit: "))

#    if amount < 0:
#        print("Invalid amount")
#        return 0
#    else: 
#        return amount    

# def withdraw(balance):
#    amount = float(input("Enter an amount to withdraw: "))

#    if amount > balance: 
#        print("YOU'RE BROKE")
#    elif amount < 0:
#        print("Must be bigger than 0")
#        return 0
#    else:
#        return amount 
                         
# def main():
#  balance = 0 
#  is_running = True 

#  while is_running:
#      print("Banking Program")
#      print("A.Show balance")
#      print("B.Deposit")
#      print("C.Withdraw")
#      print("D.Exit")

#      choice = input("Enter your choice (A-D): ")

#      if choice == 'A':
#          show_balance(balance)
#      elif choice == 'B':    
#        balance += deposit()
#      elif choice == 'C':
#        balance -= withdraw(balance)
#      elif choice == 'D':
#          is_running = False
#      else:
#          print("Invalid")

#  print("Bye bro") 
#if __name__ == '__main__':
   # main()      

#-----------------------------------------------------------------------------       

# Slot Machine

# import random

# def spin_row():
#    symbols = ["🍒", "🍉", "🍋", "☎️", "⭐️"]

#    return[random.choice(symbols)for symbol in range(3)]
    
# def print_row(row):
#    print(" -- ".join(row))

# def get_payout(row, bet):
#    if row[0] == row[1] == row[2]:
#        if row[0] == '🍒':
#            return bet * 4
#    elif row[0] == '🍉':
#         return bet * 5
#    elif row[0] == '🍋':
#          return bet * 6
#    elif row[0] == '☎️':
#          return bet * 10
#    elif row[0] == '⭐️':
#          return bet * 15   
    
#    return 0
    

# def main():
#    balance = 100

#    print("Welcome to the game")  
#    print("Symbols: 🍒 🍉 🍋 ☎️ ⭐️") 

#    while balance > 0:
#        print(f"Current balance: ${balance}")

#        bet = input("Place your bet")

#        if not bet.isdigit():
#              print("Enter a valid amount piç")
#              continue 

#        bet = int()

#        if bet > balance:
#            print("Broke ass")
#            continue

#        if bet <=0:
#            print("Bet must be valid")
#            continue    
        
#        balance -= bet

#        row = spin_row()
#        print("Spinning...")
#        print_row(row)

#        payout = get_payout(row, bet)

#        if payout > 0:
#            print(f"You won ${payout}")
#        else: 
#            print("Bohoo you lost")

#        balance += payout


# if __name__ == '__main__':
#   main() 

#-----------------------------------------------------------------------------