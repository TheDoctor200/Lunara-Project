# -*- coding: utf-8 -*-
import os
os.system('color B') # sets the background to blue
import random
zufallsantworten=["Oh, wirklich", "Interessant ...", "Das kann man so sehen", "Ich verstehe ..."]

reaktionsantworten = {"hallo": "aber Hallo", 
					  "geht": "Was verstehst du darunter?", 
					  "essen": "Ich habe leider keinen Geschmackssinn :("
					  }

# Print Bold and Underlined Text
import os
os.system("color")
print('\033[1;4m' + 'Wilkommen beim Chatbot' + '\033[0m')

print("Worüber würden Sie gerne heute sprechen?")
print("Zum beenden einfach 'bye' eintippen")
print("v.0.02")
print("")

import webbrowser
webbrowser.open("https://github.com/TheDoctor200")

nutzereingabe = ""
while nutzereingabe != "bye":
    nutzereingabe = ""
    while nutzereingabe == "":
        nutzereingabe = input("Frage/Antwort eingeben: ")
        
    nutzereingabe = nutzereingabe.lower()
    nutzerwoerter = nutzereingabe.split()
    
    intelligenteAntworten = False
    for einzelwoerter in nutzerwoerter:
        if einzelwoerter in reaktionsantworten:
            print(reaktionsantworten[einzelwoerter])
            intelligenteAntworten = True
    if intelligenteAntworten == False:
        print(random.choice(zufallsantworten))
    print("")
print("Einen schönen Tag wünsche ich Dir. Bis zum nächsten Mal")


