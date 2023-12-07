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


# Erstellen Sie ein Dictionary mit Mitarbeitern und Gehalt.
employee_and_salary = dict()

employee_and_salary["Franz Mayer"] = 2123.76
employee_and_salary["Hans Petersen"] = 3421.45

add_employee(employee_and_salary)
add_employee(employee_and_salary)

print(employee_and_salary)