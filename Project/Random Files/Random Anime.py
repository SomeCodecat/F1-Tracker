import random

anime = ["A Certain Scientific Index / A Certain Scientific Railgun / A Certain Scientific Railgun S (Gibt Mehr Brauchen Reihenfolge)",
         "A Chivalry of a Failed Knight",
         "Akame Ga Kill",
         "Assasination Classroom",
         "Bahamut chronicles",
         "Bakemonogatari",
         "BNA",
         "Boku no Hero Academia",
         "Charlotte",
         "Death Note",
         "Dr. Stone",
         "Food Wars! Shokugeki no Soma",
         "Gun Gale Online",
         "Heavy Object",
         "High-Rise Invasion",
         "High School Prodigies Have It Easy Even In Another World",
         "How To Raise A Boring Girlfriend",
         "Kakegurui",
         "Kill la Kill",
         "Kiznaiver",
         "No Game No Life",
         "Noragami",
         "Overlord",
         "Rising of The Shield Hero",
         "Rosario to Vampire",
         "Sentouin, Hakenshimasu!",
         "Shigatsu Wa Kimi No Uso",
         "Steinsgate",
         "Toradora",
         "Violet Evergarden",
         "Wonder Egg Priority",
         "Youjo Senki",
         "Your Name"]

n = random.randint(0, len(anime)-1)
x = anime[n]

print(x)
input()
