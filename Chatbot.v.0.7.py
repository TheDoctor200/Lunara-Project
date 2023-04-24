import tkinter as tk
import os
import random
import webbrowser
import tkinter.messagebox as messagebox
import threading
import requests
import openai
import os
import json

with open('api_key.json') as f:
    data = json.load(f)
    openai.api_key = data['api_key']

zufallsantworten=["Oh, wirklich", "Interessant ...", "Das kann man so sehen", "Ich verstehe ..."]

reaktionsantworten = {"hallo": "aber Hallo", 
                      "geht": "Was verstehst du darunter?", 
                      "essen": "Ich habe leider keinen Geschmackssinn",
                      "Was ist dein Lieblingsessen?": "Ich habe leider keinen Geschmackssinn :(",
                      }

def antwort_generieren(nutzereingabe):
    nutzereingabe = nutzereingabe.lower()
    nutzerwoerter = nutzereingabe.split()

    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt=nutzereingabe,
            max_tokens=60,
            n=1,
            stop=None,
            temperature=0.5,
        )
        antwort = response.choices[0].text.strip()
    except (requests.exceptions.ConnectionError, openai.error.APIConnectionError):
        for reaktionswort in reaktionsantworten:
            if all(wort in nutzerwoerter for wort in reaktionswort.lower().split()):
                return reaktionsantworten[reaktionswort]
        antwort = random.choice(zufallsantworten)
        
    return antwort

def antwort_senden():
    nutzereingabe = input_entry.get()
    dialogfenster.insert(tk.END, "Du: " + nutzereingabe + "\n")
    antwort = antwort_generieren(nutzereingabe)
    dialogfenster.insert(tk.END, "Chatbot: " + antwort + "\n\n")
    input_entry.delete(0, tk.END)
    dialogfenster.yview(tk.END)  # Automatisches Scrollen nach unten
    
def check_internet_connection():
    try:
        requests.get("https://www.google.com")
        return True
    except:
        return False

def update_status_label():
    if check_internet_connection():
        status_label.config(text="ChatGPT API verfügbar", bg="green")
    else:
        status_label.config(text="ChatGPT API nicht verfügbar", bg="red")
    status_label.after(1000, update_status_label)
     
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

status_label = tk.Label(root, text="API wird geprüft...", bg="yellow")
status_label.pack(side=tk.BOTTOM, fill=tk.X)

update_status_label()

root.bind('<Return>', on_enter)

root.mainloop()






