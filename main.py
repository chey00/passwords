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
def remove_user(user_and_passwords):
    username = input("Geben Sie einen Benutzernamen ein: ")

    if username in user_and_passwords:
        delete_username = input("Wollen Sie den Benutzer " + username + " löschen? (Ja) ")

        if delete_username == "ja" or delete_username == "Ja":
            user_and_passwords.pop(username)

            print("Benuter " + username + " gelöscht")
    else:
        print("Benuter " + username + " nicht gefunden.")

# 3) Erstellen Sie eine Funktion change_password mit dem Parameter users_and_passwords.
#    Die Funktion fragt zuerst den Benutzername ab, dessen Kennwort geändert werden soll
#    und überprüft das alte Kennwort. Ist die Eingabe korrekt gibt der Benutzer sein
#    neues Kennwort ein. Ist das Kennwort bereits bei einen anderem Nutzer gespeichert,
#    wiederholt sich die Eingabe.


dictionary = { "hans": "ABCD1234",
               "peter": "ABCD1234",
               "root": "2t23$&fdsgeFJZ"}

remove_user(dictionary)

'''
while True:
    if check_login(dictionary):
        print("Login erfolgreich!")
        break
'''