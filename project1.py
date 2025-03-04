import time
import random

print("Welcome to the game! 🤩")


name = input("Please enter your baller name to start your career: ")


print(f"☝ Okay {name.capitalize()} are you ready to be the best footballer on earth?")


input("Press enter key to start!")
print("⚽️ After successfully competing in underage leagues, there are teams who wants to recruit you!")

print("💡 Think carefully about your decision! Here are the teams interested:")


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

opp_teams = []

if response == 1:
    opp_teams = ["Manisaspor", "Ümraniyespor", "Kocaelispor", "Sakaryaspor", "Pendik", "Sariyer FK", "Erzurumspor"]

elif response == 2:
    opp_teams = ["Hull City", "Coventry", "Wigan Athletic", "West Bromwich", "Swansea", "Bristol City", "Leeds United"]

elif response == 3:
    opp_teams = ["Leganes", "Eibar", "Almeria", "Las Palmas", "Cadiz", "Huesca", "Real Oviedo",] 

elif response == 4:
    opp_teams  = ["Herent", "Leisden", "Mechelen", "Drongen", "Kontich", "Moldavo", "Sporting Hasselt"]
     


print(f"Congratulations {name.capitalize()}! You have signed your first professional contract with 📝 {team}")


print(f"Highly anticipated young player made his decision, as reports claim {name.capitalize()} signed a 4-year deal contract with: {team}!")


print(f"Your coach {coach} wants to speak to you 🗣️")


print("\n" + "="*50)
hint_text = f"⚠️ HINT: BE CAREFUL IN YOUR CONVERSATIONS WITH {coach}! 🔥 YOUR PLAYING TIME MIGHT BE AFFECTED BASED ON YOUR DIALOGUES."
for char in hint_text:
    print(char, end="", flush=True)
    time.sleep(0.05)  # Adjust speed (lower = faster)
print("\n")    



print(f"{coach}: Welcome to {team}, {name.capitalize()}! I want to tell you that you made the best decision joining us\n")


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


print(f"Your relationship with {coach} is now {rel_coach}/10\n")
print()

print(f"According to reporters, there is a meeting to be held at {team}.")

print(f"This meeting will involve couple of the new-comers, including {name.capitalize()}, the team's captain {captain}, and {coach} ")
print()


# The Meeting

if team == "Orduspor🟣⚪️":
    your_team = "Orduspor🟣⚪️"
    league = "Turkish Super League"

elif team == "Barrow🔵⚪️":
     your_team = "Barrow🔵⚪️"
     league = "Premier League"

elif team == "Tenerife⚪️🔵":
    your_team = "Tenerife⚪️🔵"
    league = "La Liga"   
          
else:
    your_team = "Patro Eisden🔵⚫️"
    league = "Belgian Pro League"
    

print()
print(f"{coach}: Alright boys! I have gathered you all here to have a word with you about the upcoming season, welcome!")

print(f"{coach}: As you are all aware as {team}, we aim to become one of the first two teams to get the promotion for the {league}")

print()
print(f"{captain}: We will give everything for the fans {coach}, trust this group.")

print()
response = input("+: Even though I am new, I understood this club's values from day one, we will give everything on the pitch and thrive\n\n"
                 f"-: I was wondering about my playing time {coach}, hope you can address that\n"
                 "Enter (+) or (-): ")



rel_team = 5
if response == "-":
    rel_team -= 1

elif response == "+":
    rel_team += 1

else:
    print("Please choose a valid answer (+) or (-)")

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


print(f"Your relationship with {coach} is now {rel_coach}/10\n")
print()

print(f"After a long pre-season period for {team}, they are about to play their first official game! ")

print()

# Building the League

played_matches = []  # Step 1: Create an empty list to track played teams

for _ in range(len(opp_teams)):  # Step 2: Loop through opp_teams' length (play each team once)
    opponent = random.choice([team for team in opp_teams if team not in played_matches])  
    played_matches.append(opponent)  # Step 3: Add the chosen opponent to played_matches
    print(f"{your_team} vs {opponent}")  # Step 4: Print the match


while opp_teams:
    opponent = random.choice(opp_teams)
chances_ingame = 0
match_fixture = []
match_actions = ("goal ⚽️ ", "assist 🤝 ", "foul 🤕 ", "dribbling 💨 ", "tackle 🛝 ", "bad pass 👎🏽 " )

for opponent in opp_teams:
    match = f"{team} vs {opponent}"
    match_fixture.append(match)

for match in match_fixture:
    print(match)    


if rel_coach <= 3:
    print(f"You are on the bench for this match! 🪑 ")
    chances_ingame = random.randint(1, 5)

elif 4 <= rel_coach <= 8:
    print(f"You are starting the game! 🏃🏽‍♂️ ")
    chances_ingame = random.randint(6, 10)

else:
    print(f"Your coach is starting you as the vice captain! Ⓒ ")
    chances_ingame = random.randint(3, 7)

    

print(f"We are ready to proceed with the {match}, for the first game of the season! ")


print("The referee blew the whistle and the game has started! ⌚️ ") 

num_events = random.randint(3, chances_ingame)

for _ in range(num_events):
    time.sleep(1)

    #DECISION MAKING
    if random.random() < 0.4:
        print("You have the ball, what are you going to do?")
        choice = int(input("1: Pass 🤜 , 2: Shoot 💥 , 3: Dribble ⛹🏻‍♂️ "  ("Enter 1, 2 or 3") ))

        if choice == 1: #Pass
            outcome = random.choice(["Successful pass ✅", "Intercepted pass ❌"])
            if outcome == "Successful pass ✅":
                rel_team += 1 #Team likes your playstyle
                rel_coach += 1 #Coach approves your playstyle
            elif outcome == "Intercepted pass ❌":
                rel_team -= 0.5  #Team is not happy with your playstyle
                rel_coach -= 0.5  #Coach does not approve your your playstyle    

        elif choice == 2: #Shoot
            outcome = random.choice(["GOALLL ⚽︎🎁", "Wide off the target ❌", "Hits the post! 🥅"])    
            if outcome == "GOALLL ⚽︎🎁":
                rel_team += 1 #Your teammates are impressed with your shooting power
                rel_coach += 1 #Your coach thinks your hard work has paid off
            elif outcome == "Wide off the target ❌":
                  rel_team -= 0.5 #Your teammates think you should pass them more
                  rel_coach -= 0.5 #Your coach is disappointed with your skills
            else:
                rel_team = 0 #Your teammates think your were unlucky there
                rel_coach = 0 #Your coach thinks you were unlucky with the shot

        elif choice == 3: #Dribble
            outcome = random.choice(["NUTMEG! ⛹🏾‍♂️", "Dribbled past two players! 🤌🏼", "Strong tackle! ❌", "Intercepted by the defense 🥊" ]) 
            if outcome == "NUTMEG! ⛹🏾‍♂️":
                rel_team += 0.75 #Your teammates are impressed with your skills
                rel_coach += 0.75 #Your coach is amazed by your joga bonito
            elif outcome == "Dribbled past two players! 🤌🏼":
                rel_team += 1.5 #Your teammates love your take on's!
                rel_coach += 1.5 #Your coach is a fan of your dribbling
            elif outcome == "Strong tackle! ❌":
                rel_team -= 0.5 #Your teammates were open, waiting for your pass
                rel_coach -= 0.5 #Your coach wants you to be more efficient with the ball
            else:
                rel_team -= 0.5 #Your teammates think you had better options than dribbling
                rel_coach -= 0.5 #Your coach wants you to be more decisive with your actions  


