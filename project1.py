import time

print("Welcome to the game! 🤩")
time.sleep(1)

name = input("Please enter your baller name to start your career: ")
time.sleep(1)

print(f"☝ Okay {name} are you ready to be the best footballer on earth?")
time.sleep(1)

input("Press enter key to start!")
print("⚽️ After successfully competing in underage leagues, there are teams who wants to recruit you!")
time.sleep(1)
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

print(f"Congratulations {name}! You have signed your first professional contract with 📝 {team}")
time.sleep(2)

print(f"Highly anticipated young player made his decision, as reports claim {name} signed a 4-year deal contract with: {team}!")
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

print(f"{coach}: Welcome to {team}, {name}! I want to tell you that you made the best decision joining us\n")
time.sleep(2)

response = input(f"+: Thanks Mr.{coach}, I am excited to start and contribute.\n\n"
                 "-: Honestly, y'all are lucky I chose here, you are going to make millions off my transfer fee \n"
                 "Enter (+) or (-): ")

rel_coach = 5
if response == "-":
    print(f"{coach}: I am very disappointed with your approach")
    rel_coach -= 1
elif response == "+":
    print(f"{coach}: I like your attitude. We are all thrilled by your talents, let's begin")
    rel_coach += 1
else:
    print("Please choose a valid answer (+) or (-)")

time.sleep(2)
print(f"Your relationship with {coach} is now {rel_coach}/10\n")
print()

print(f"According to reporters, there is a meeting to be held at {team}.")
time.sleep(2)
print(f"This meeting will involve couple of the new-comers, including {name}, {captain}, and {coach} ")
time.sleep(2)

# The Meeting

if team == "Orduspor🟣⚪️":
    league = "Turkish Super League"

elif team == "Barrow🔵⚪️":
    league = "Premier League"

elif team == "Tenerife⚪️🔵":
    league = "La Liga"   
          
else:
    league = "Belgian Pro League"


print(f"{coach}: Alright boys! I have gathered you all here to have a word with you about the upcoming season, welcome!")
time.sleep(2)
print(f"{coach}: As you are all aware as {team}, we aim to become one of the first two teams to get the promotion for the {league}")





