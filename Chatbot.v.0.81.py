import tkinter as tk
import os
import random
import webbrowser
import requests
import atexit
import sys
import openai
import json

def download_file(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        content = response.content
    except requests.exceptions.RequestException as e:
        print("Fehler: Die Datei kann nicht heruntergeladen werden.", str(e))
        return
    
    # Extrahiere den Dateinamen aus dem Link
    file_name = "api_key.json"  # Setze den Dateinamen auf "api_key.json"
    
    # Bestimme den Speicherpfad im Verzeichnis des Python-Skripts
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)
    
    # Speichern der Datei als JSON im Verzeichnis des Python-Skripts
    with open(file_path, 'wb') as f:
        f.write(content)
    
    print("Die Datei wurde erfolgreich heruntergeladen:", file_path)

# Google Drive-Link zur Datei
google_drive_link = 'https://drive.google.com/uc?export=download&id=1Oa84dZEKtnEzpRGEmJpZEXQt__UGlns_'

# Datei herunterladen
download_file(google_drive_link)

zufallsantworten=["Oh, wirklich", "Interessant ...", "Das kann man so sehen", "Ich verstehe ..."]

reaktionsantworten = {"hallo": "aber Hallo", 
                      "geht": "Was verstehst du darunter?", 
                      "essen": "Ich habe leider keinen Geschmackssinn",
                      "Was ist dein Lieblingsessen?": "Ich habe leider keinen Geschmackssinn :(",
                      "Kannst du trinken?": "Ich kann leider nicht trinken :(",     
                      "gefühlslage": "Meinen Schaltkreisen geht es gut", 
                      "wetter": "Ich denke es wird sonnig :)", 
                      "Wie stehst du zu rauchen?": "Rauchen ist ungesund :(",
                      "wie gehts?": "Mir geht es gut",
                      "wie geht es dir?": "Mir geht es gut", 
                      "wie wird das wetter?": "Ich denke es wird sonnig :)"
                      }

def antwort_generieren_lokale(nutzereingabe):
    nutzereingabe = nutzereingabe.lower()
    nutzerwoerter = nutzereingabe.split()
    for reaktionswort in reaktionsantworten:
        if all(wort in nutzerwoerter for wort in reaktionswort.lower().split()):
            return reaktionsantworten[reaktionswort]
    return random.choice(zufallsantworten)

api_key = ""

def antwort_generieren_chatgpt(nutzereingabe):
    if not api_key:
        return "Die ChatGPT-API ist offline."
    
    openai.api_key = api_key
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=nutzereingabe,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
        log_level="info"
    )
    
    return response.choices[0].text.strip()

def antwort_generieren(nutzereingabe):
    if api_key:
        return antwort_generieren_chatgpt(nutzereingabe)
    else:
        return antwort_generieren_lokale(nutzereingabe)

def is_internet_available():
    try:
        response = requests.get("https://www.google.com", timeout=5)
        return True
    except requests.RequestException:
        return False

def antwort_senden():
    nutzereingabe = input_entry.get()
    dialogfenster.insert(tk.END, "Du: " + nutzereingabe + "\n")
    
    antwort = antwort_generieren(nutzereingabe)
    
    dialogfenster.insert(tk.END, "Chatbot: " + antwort + "\n\n")
    input_entry.delete(0, tk.END)
    dialogfenster.yview(tk.END)

def on_enter(event):
    antwort_senden()

def open_github():
    webbrowser.open("https://github.com/TheDoctor200/Python-Chatbot")

def set_to_english():
    os.system('python english.py')
    root.destroy()

def close_script():
    os.system('python cleanup.py')
    root.destroy()
    sys.exit()

def toggle_api_status():
    global api_key
    api_key = ""
    status_anzeigen()

def status_anzeigen():
    if api_key:
        status_label.config(text="Online", bg="green")
        toggle_button.config(text="Offline setzen")
    else:
        status_label.config(text="Offline", bg="red")
        toggle_button.config(text="Online setzen")

def get_api_key():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "api_key.json")
    
    try:
        with open(file_path) as f:
            data = json.load(f)
            return data["api_key"]
    except FileNotFoundError:
        print("Fehler: Die Datei 'api_key.json' wurde nicht gefunden.")
        return ""

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

exit_button = tk.Button(root, text="Exit", command=close_script)
exit_button.pack(side=tk.BOTTOM, padx=10, pady=5)

english_button = tk.Button(root, text="Set to English", command=set_to_english)
english_button.pack(side=tk.BOTTOM, padx=10, pady=5)

toggle_button = tk.Button(root, text="Online setzen", command=toggle_api_status)
toggle_button.pack(side=tk.BOTTOM, padx=10, pady=5)

status_label = tk.Label(root, text="Offline", bg="red")
status_label.pack(side=tk.BOTTOM, pady=5)

atexit.register(close_script)

# API-Schlüssel aus JSON-Datei lesen
api_key = get_api_key()

# Status aktualisieren
status_anzeigen()

# Enter-Taste binden
root.bind('<Return>', on_enter)

# Hauptloop starten
root.mainloop()















