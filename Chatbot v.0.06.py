import tkinter as tk
import os
import random
import webbrowser

zufallsantworten=["Oh, wirklich", "Interessant ...", "Das kann man so sehen", "Ich verstehe ..."]

reaktionsantworten = {"hallo": "aber Hallo", 
                      "geht": "Was verstehst du darunter?", 
                      "essen": "Ich habe leider keinen Geschmackssinn",
                      "Was ist dein Lieblingsessen?": "Ich habe leider keinen Geschmackssinn :(",
                      "Kannst du trinken?": "Ich kann leider nicht trinken :(",     
                      "gefühlslage": "Meinen Schaltkreisen geht es gut", 
                      "wetter": "Ich denke es wird sonnig :)", 
                      "Wie stehst du zu rauchen?": "Rauchen ist ungesund :(",
                      "wie gehts?": "Mir geht es geht es gut",
                      "wie geht´s": "Mir geht es geht es gut",
                      "wie geht´s?": "Mir geht es gut",
                      "wie geht es dir?": "Mir geht es gut", 
                      "wie wird das wetter?": "Ich denke es wird sonnig :)"
                      }

def antwort_generieren(nutzereingabe):
    nutzereingabe = nutzereingabe.lower()
    nutzerwoerter = nutzereingabe.split()
    for reaktionswort in reaktionsantworten:
        if all(wort in nutzerwoerter for wort in reaktionswort.lower().split()):
            return reaktionsantworten[reaktionswort]
    return random.choice(zufallsantworten)

def antwort_senden():
    nutzereingabe = input_entry.get()
    dialogfenster.insert(tk.END, "Du: " + nutzereingabe + "\n")
    antwort = antwort_generieren(nutzereingabe)
    dialogfenster.insert(tk.END, "Chatbot: " + antwort + "\n\n")
    input_entry.delete(0, tk.END)
    dialogfenster.yview(tk.END)  # Automatisches Scrollen nach unten

def on_enter(event):
    antwort_senden()

def open_github():
    webbrowser.open("https://github.com/TheDoctor200/Python-Chatbot")

def set_to_english():
    os.system('python english.py')
    root.destroy()

root = tk.Tk()
root.title("Chatbot")
root.iconbitmap('icon.ico')

input_label = tk.Label(root, text="Frage/Nachricht eingeben:")
input_label.pack()

input_entry = tk.Entry(root, width=50)
input_entry.pack()

antwort_button = tk.Button(root, text="Antwort senden", command=antwort_senden, bg="blue", fg="white")
antwort_button.pack(pady=10)

dialogfenster = tk.Text(root, width=50, height=20)
dialogfenster.pack(side=tk.LEFT, padx=10)

dialogfenster.insert(tk.END, "Chatbot made by TheDoctor.                        Wilkommen, bitte gib deine Frage/Nachricht ein:\n")

scrollbar = tk.Scrollbar(root, command=dialogfenster.yview)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)

dialogfenster.config(yscrollcommand=scrollbar.set)

about_button = tk.Button(root, text="About me", command=open_github)
about_button.pack(side=tk.BOTTOM, padx=10, pady=5)

english_button = tk.Button(root, text="Set to English", command=set_to_english)
english_button.pack(side=tk.BOTTOM, padx=10, pady=5)

root.bind('<Return>', on_enter)

root.mainloop()






