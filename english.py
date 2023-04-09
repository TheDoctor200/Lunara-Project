import tkinter as tk
import os
import random
import webbrowser

zufallsantworten=["Oh, really", "interesting ...", "Thats a good point", "I see ..."]

reaktionsantworten = {"hello": "hello", 
                      "walk": "what do you mean by that?", 
                      "eat": "I have no sense of taste, unfortunately",
                      "What is your favorite food?": "I unfortunately have no sense of taste :(",
                      "can you drink?": "I'm afraid I can't drink :(",     
                      "emotional state": "My circuits are fine", 
                      "weather": "I think it will be sunny :)", 
                      "how do you feel about smoking?": "smoking is unhealthy :(",
                      "how are you?": "I'm fine",
                      "how are you?": "I'm fine",
                      "how are you?": "I'm fine",
                      "how are you?": "I'm fine", 
                      "what's the weather going to be like?": "I think it's going to be sunny :)"
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
    dialogfenster.insert(tk.END, "You: " + nutzereingabe + "\n")
    antwort = antwort_generieren(nutzereingabe)
    dialogfenster.insert(tk.END, "Chatbot: " + antwort + "\n\n")
    input_entry.delete(0, tk.END)
    dialogfenster.yview(tk.END)  # Automatisches Scrollen nach unten

def on_enter(event):
    antwort_senden()

def open_github():
    webbrowser.open("https://github.com/TheDoctor200/Python-Chatbot")

root = tk.Tk()
root.title("Chatbot")
root.iconbitmap('icon.ico')

input_label = tk.Label(root, text="Input of the Massage:")
input_label.pack()

input_entry = tk.Entry(root, width=50)
input_entry.pack()

antwort_button = tk.Button(root, text="Send Massage", command=antwort_senden, bg="blue", fg="white")
antwort_button.pack(pady=10)

dialogfenster = tk.Text(root, width=50, height=20)
dialogfenster.pack(side=tk.LEFT, padx=10)

dialogfenster.insert(tk.END, "Chatbot made by TheDoctor.                        Welcome, please type in your Massage:\n")

scrollbar = tk.Scrollbar(root, command=dialogfenster.yview)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)

dialogfenster.config(yscrollcommand=scrollbar.set)

about_button = tk.Button(root, text="About me", command=open_github)
about_button.pack(side=tk.BOTTOM, padx=10, pady=5)

root.bind('<Return>', on_enter)

root.mainloop()







