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
    "Orduspor🟣⚪️🇹🇷": {"coach": "Mert Müldür", "captain": "Mehmet Öz"},
    "Barrow🔵⚪️🏴": {"coach": "Scott Carson", "captain": "Liam Delap"},
    "Tenerife⚪️🔵🇪🇸": {"coach": "Iago Aspas", "captain": "Andres Parejo"},
    "Patro Eisden🔵⚫️🇧🇪": {"coach": "Thorgan Hazard", "captain": "Jan Vertonghen"}
}

for team in teams:
    print(f"{team}")


print()
time.sleep(1)
response = int(input("On which team would you like to compete for?(1/4): "))


while True:
    if response == 1:
       team = "Orduspor🟣⚪️ 🇹🇷" 
       coach = "Mert Müldür"   
       print("Congrats! You are off to Turkiye to start your career")
       break
    elif response == 2:
        team = "Barrow🔵⚪️ 🏴󠁧󠁢󠁥󠁮󠁧󠁿"
        coach = "Scott Carson"
        print("Congrats! You are off to England to start your career")
        break
    elif response == 3:
        team = "Tenerife⚪️🔵🇪🇸"
        coach = "Iago Aspas"
        print("Congrats! You are off to Spain to start your career")
        break
    elif response == 4:
        team = "Patro Eisden🔵⚫️🇧🇪"
        coach = "Thorgan Hazard"
        print("Congrats! You are off to Belgium to start your career")
        break
    else: 
        response  = int(input("On which team would you like to compete for?(1/4): "))

print(f"Congratulations {name}! You have signed your first professional contract with 📝 {team}")
time.sleep(1)

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

time.sleep(1)
rel_coach = 5
if response == "-":
    rel_coach - 1
elif response == "+":
    rel_coach + 1
else:
    print("Please choose a valid answer (+) or (-)")

response = input(f"{coach}: Welcome to the family {name}! I would like to tell you that you made the best decision choosing {team}.\n\n"
                 "Choose your answer \n"
                 "+: Honestly coach, y'all are lucky to have me on this team\n"
                 "-: I'm excited on this journey and I would like to start as soon as possible!\n"
                 "Enter (+) or (-):" )




