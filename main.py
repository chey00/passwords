def check_login(names_and_passwords):
    username = input("Benutzername: ")
    password = input("Passwort:     ")

    if password == names_and_passwords[username]:
        return True
    else:
        return False

# 1) Erstellen Sie eine Methode, welche Benutzer hinzufügt. Beachten Sie, dass ein Benutzername nicht doppelt vergeben
#    werden darf. Der Methodenname ist add_user mit names_and_passwords als dict.

dictionary = { "hans": "ABCD1234",
               "peter": "ABCD1234",
               "root": "2t23$&fdsgeFJZ"}

while True:
    if check_login(dictionary):
        print("Login erfolgreich!")
        break
