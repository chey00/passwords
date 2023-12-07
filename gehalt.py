# 2) Erweitern Sie das Programm wiefolgt:
#    Programmieren Sie eine Funktion add_employee. Die Funktion erhält als Prameter das
#    dict employee_and_salery. In das Dictonary wird ein neuer Mitarbeitername und das Gehalt eingefügt.
#    Zuerst prüft es aber, ob der Mitarbeitername schon vergeben ist.
def add_employee(employee_and_salary):
    employee = input("Geben Sie den Namen des Mitarbeiters ein: ")

    if employee in employee_and_salary:
        print("Der Benutzer existiert bereits.")

        overwrite = input("Möchten Sie das Gehalt ändern (J/N)?")

        if overwrite == "J" or overwrite == "j":
            salary = float(input("Geben Sie das neue Gehalt ein: "))

            employee_and_salary[employee] = salary
        else:
            print("Es werden keine Änderungen am Gehalt vorgenommen.")
    else:
        salary = float(input("Geben Sie das neue Gehalt ein: "))

        employee_and_salary[employee] = salary

# 3) Erstellen Sie eine Funktion remove_employee mit dem Parameter dictionary.
#    In der Funktion werden ehemalige Mitarbeiter aus dem Parameter gelöscht.
#    Es soll eine Sicherheitsabfrage stattfinden, ob der Mitarbeiter wirklich
#    gelöscht werden soll.
def remove_employee(dictionary):
    employee = input("Welchen Mitarbeiter möchten Sie entfernen? ")

    if employee in dictionary:
        confirm = "JahA"
        output_text = "Möchten Sie den Mitarbeiter " + employee + " wirklich löschen (" + confirm + ")? "
        overwrite = input(output_text)

        if overwrite == confirm:
            dictionary.pop(employee)

# 4) Deklarien Sie eine Funktion sum_of_values mit dem Parameter employee_and_salary.
#    Die Funktion bildet die Summe über alle im Wörterbuch hinterlegten Gehälter.
def sum_of_values(employee_and_salary):
#    return sum(employee_and_salary.values())
    sum = 0.0

    for salary in employee_and_salary.values():
        sum += salary

    return sum

# 5) Erstellen Sie eine Textausgabe der Gehältern und Namen der Mitarbeiter in aufsteingender
#    Reihenfolge. Die Funktion heisst print_salary mit dem Parameter dictionary.
def print_salary(dictionary):
#    print(dict(sorted(dictionary.items(), key=lambda x: x[1])))
    salaries = dictionary.values()

    sorted_salaries = sorted(salaries)

    for salary in sorted_salaries:
        for employee in dictionary.keys():
            if dictionary[employee] == salary:
                print(salary, ":", employee)

# 1) Erstellen Sie ein Dictionary mit Mitarbeitern und Gehalt.
employee_and_salary = dict()

employee_and_salary["Franz Mayer"] = 2123.76
employee_and_salary["Hans Petersen"] = 3421.45
employee_and_salary["Hans Franz"] = 1421.45
employee_and_salary["Hans Mayer"] = 5421.45

print_salary(employee_and_salary)
