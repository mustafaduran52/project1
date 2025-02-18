import time

print("Welcome to the game! 🤩")
time.sleep(2)

name = input("Please enter your baller name to start your career: ")
time.sleep(2)

print(f"☝ Okay {name.capitalize()} are you ready to be the best footballer on earth?")
time.sleep(2)

input("Press enter key to start!")
print("⚽️ After successfully competing in underage leagues, there are teams who wants to recruit you!")
time.sleep(2)
print("💡 Think carefully about your decision! Here are the teams interested:")
time.sleep(2)

print()
teams = {
    "Orduspor🟣⚪️": {"coach": "Mert Müldür", "captain": "Hasan Mustan"},
    "Barrow🔵⚪️": {"coach": "Scott Carson", "captain": "Jack Grealish"},
    "Tenerife⚪️🔵": {"coach": "Iago Aspas", "captain": "Luis Alberto"},
    "Patro Eisden🔵⚫️": {"coach": "Thorgan Hazard", "captain": "Charles de Ketelaere"}
}

for team in teams:
    print(f"{team}")


print()
time.sleep(1)
response = int(input("On which team would you like to compete for?(1/4): "))


while True:
    if response == 1:
       team = "Orduspor🟣⚪️" 
       coach = "Mert Müldür"
       captain = "Hasan Mustan"   
       print("Congrats! You are off to Turkiye to start your career")
       break
    elif response == 2:
        team = "Barrow🔵⚪️"
        coach = "Scott Carson"
        captain = "Jack Grealish"
        print("Congrats! You are off to England to start your career")
        break
    elif response == 3:
        team = "Tenerife⚪️🔵"
        coach = "Iago Aspas"
        captain = "Luis Alberto"
        print("Congrats! You are off to Spain to start your career")
        break
    elif response == 4:
        team = "Patro Eisden🔵⚫️"
        coach = "Thorgan Hazard"
        captain = "Charles de Ketelaere"
        print("Congrats! You are off to Belgium to start your career")
        break
    else: 
        response  = int(input("On which team would you like to compete for?(1/4): "))
        if response.isdigit():
            response = int(response)
        else:
            response = 0    #Forces the loop to run again if input is not a number
time.sleep(2)
print(f"Congratulations {name.capitalize()}! You have signed your first professional contract with 📝 {team}")
time.sleep(2)

print(f"Highly anticipated young player made his decision, as reports claim {name.capitalize()} signed a 4-year deal contract with: {team}!")
time.sleep(2)

print(f"Your coach {coach} wants to speak to you 🗣️")
time.sleep(2)

print("\n" + "="*50)
hint_text = f"⚠️ HINT: BE CAREFUL IN YOUR CONVERSATIONS WITH {coach}! 🔥 YOUR PLAYING TIME MIGHT BE AFFECTED BASED ON YOUR DIALOGUES."
for char in hint_text:
    print(char, end="", flush=True)
    time.sleep(0.05)  # Adjust speed (lower = faster)
print("\n")    

time.sleep(2)

print(f"{coach}: Welcome to {team}, {name.capitalize()}! I want to tell you that you made the best decision joining us\n")
time.sleep(2)

response = input(f"+: Thanks Mr.{coach}, I am excited to start and contribute.\n\n"
                 "-: Honestly, y'all are lucky I chose here, you are going to make millions off my transfer fee \n"
                 "Enter (+) or (-): ")

#Relationships

rel_coach = 5
if response == "-":
    print(f"{coach}: I am very disappointed with your approach.")
    rel_coach -= 1
elif response == "+":
    print(f"{coach}: I like your attitude. Let's keep the work going.")
    rel_coach += 1
else:
    print("Please choose a valid answer (+) or (-)")

time.sleep(2)
print(f"Your relationship with {coach} is now {rel_coach}/10\n")
print()

print(f"According to reporters, there is a meeting to be held at {team}.")
time.sleep(3)
print(f"This meeting will involve couple of the new-comers, including {name.capitalize()}, the team's captain {captain}, and {coach} ")
print()
time.sleep(3)

# The Meeting

if team == "Orduspor🟣⚪️":
    league = "Turkish Super League"

elif team == "Barrow🔵⚪️":
    league = "Premier League"

elif team == "Tenerife⚪️🔵":
    league = "La Liga"   
          
else:
    league = "Belgian Pro League"

print()
print(f"{coach}: Alright boys! I have gathered you all here to have a word with you about the upcoming season, welcome!")
time.sleep(3)
print(f"{coach}: As you are all aware as {team}, we aim to become one of the first two teams to get the promotion for the {league}")
time.sleep(3)
print()
print(f"{captain}: We will give everything for the fans {coach}, trust this group.")
time.sleep(3)
print()
response = input("+: Even though I am new, I understood this club's values from day one, we will give everything on the pitch and thrive\n\n"
                 f"-: I was wondering about my playing time {coach}, hope you can address that\n"
                 "Enter (+) or (-): ")

time.sleep(2)

rel_team = 5
if response == "-":
    rel_team -= 1

elif response == "+":
    rel_team += 1

else:
    print("Please choose a valid answer (+) or (-)")
time.sleep(2)
print(f"Your relationship with the captain {captain} is now {rel_team}/10")            
print()

if response == "-":
    print(f"{coach}: There is time and place for everything, I feel like now it was not the time to discuss this {name.capitalize()} ")
    print()
    rel_coach -= 1
elif response == "+":
    print(f"{coach}: This means a lot, hope all of the new-comers feel like you {name.capitalize()}")
    rel_coach += 1
    print()

time.sleep(2)
print(f"Your relationship with {coach} is now {rel_coach}/10\n")
print()

print(f"After a long pre-season period for {team}, they are about to play their first official game! ")
time.sleep(2)
print()

# Building the League

opp_teams = []

if response == 1:
    opp_teams = ["Manisaspor", "Ümraniyespor", "Kocaelispor", "Sakaryaspor", "Pendik", "Sariyer FK", "Erzurumspor", "Bursaspor"]

elif response == 2:
    opp_teams = ["Hull City", "Coventry", "Wigan Athletic", "West Bromwich", "Swansea", "Bristol City", "Leeds United", "Derby County"]

elif response == 3:
    opp_teams = ["Leganes", "Eibar", "Almeria", "Las Palmas", "Cadiz", "Huesca", "Real Oviedo", "Elche"] 

elif response == 4:
    opp_teams  = ["Herent", "Leisden", "Mechelen", "Drongen", "Kontich", "Moldavo", "Sporting Hasselt", "Mons"]


print(opp_teams)                 






