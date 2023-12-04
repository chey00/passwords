# Übung
# Erstellen Sie ein Dictionary als Telefonbuch.

phonebook = { "Peter Mayer": "01711234567",
              "Franz Huber": "+49(0)911987654",
              "Sabine Schmidt": "789456"}

phonebook["Sebastian"] = "876535"
phonebook["Sebastian"] = "921123"

phonebook.pop("Franz Huber")

print(phonebook)
print(phonebook.keys())
print(phonebook.values())
print(phonebook["Sebastian"])
