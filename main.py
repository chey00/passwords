def check_login(names_and_passwords):
    username = input("Benutzername: ")
    password = input("Passwort:     ")

    if password == names_and_passwords[username]:
        return True
    else:
        return False

# 1) Erstellen Sie eine Methode, welche Benutzer hinzufügt. Beachten Sie, dass ein Benutzername nicht doppelt vergeben
#    werden darf. Der Methodenname ist add_user mit names_and_passwords als dict.
def add_user(names_and_passwords):
    username = input("Geben Sie den neuen Benutzernamen ein: ")

    usernames = names_and_passwords.keys()

    if username in usernames:
        print("Benutername schon vergeben")

        return False
    else:
        password = input("Geben Sie das neue Passwort ein: ")

        names_and_passwords[username] = password

        return True

# 2) Erstellen Sie eine Funktion remove_user mit dem Parameter user_and_passwords.
#    Bei Aufruf der Funktion wird der Anwender nach einem Benutzernamen gefragt.
#    Ist der Benutzer vorhanden, erscheint eine Sicherheitsabfrage, ob der Benutzername wirklich
#    gelöscht werden soll. Erst dann wird der Benutzer gelöscht. Ist der Benutzername nicht
#    vorhanden, erscheint eine Fehlermeldung.

dictionary = { "hans": "ABCD1234",
               "peter": "ABCD1234",
               "root": "2t23$&fdsgeFJZ"}

add_user(dictionary)
'''
while True:
    if check_login(dictionary):
        print("Login erfolgreich!")
        break
'''