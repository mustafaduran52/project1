import time

print("Welcome to the game! 🤩")
time.sleep(3)

name = input("Please enter your baller name to start your career: ")
time.sleep(3)

print(f"☝ Okay {name} are you ready to be the best footballer on earth?")
time.sleep(3)

input("Press enter key to start!")
print("⚽️ After successfully competing in underage leagues, there are teams who wants to recruit you!")
time.sleep(3)
print("💡 Think carefully about your decision! Here are the teams interested:")
time.sleep(3)

print()
teams = ("1.Orduspor 🇹🇷 (Turkish League 2nd division)",
         "2.Barrow 🏴󠁧󠁢󠁥󠁮󠁧󠁿 (English League 3rd division)",
         "3.Tenerife 🇪🇸 (Spanish League 3rd division)",
         "4.Patro Eisden 🇧🇪 (Belgian League 2nd division)")

for team in teams:
    print(f"{team}")

print()
response = input("On which team would you like to compete for?(1/4): ")

if response == "1":
    print("Congratulations! You are off to Turkiye to start your career!")

elif response == "2":
    print("Congratulations! You are off to England to start your career!")    

elif response == "3":
    print("Congratulations! You are off to Spain to start your career!")
    
elif response == "4":
    print("Congratulations! You are off to Belgium to start your career!")


while response != "1" or "2" or "3" or "4":
    print("Your answer is invalid, please read again!")
    response = input("On which team would you like to compete for?(1/4): ")
    if response == "1" or "2" or "3" or "4":
    break         

    



