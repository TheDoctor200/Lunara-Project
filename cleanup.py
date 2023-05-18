import os

def delete_file():
    # Datei löschen
    file_name = "api_key.json"
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    if os.path.exists(file_path):
        os.remove(file_path)
        print("Die Datei wurde erfolgreich gelöscht:", file_path)

# Aufrufen der Funktion zum Löschen der Datei
delete_file()
