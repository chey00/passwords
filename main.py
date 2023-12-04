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