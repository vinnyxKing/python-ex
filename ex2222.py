def display():
    for staff in employees:
        fields = staff.split(',')
        for field in fields:
            print(field, end="\t")
        print()

def display_old():
    for staff in employees:
        fields = staff.split(',')
        date = fields[2]
        parts = date.split('/')
        if parts[2] <= "2020":
            for field in fields:
                print(field, end="\t")
            print()

def change_salary(id,newsalary):
    for staff in employees:
        fields = staff.split(',')
        if staff[0:8] == id:
            fields[3] = newsalary
            new_rec = ",".join(fields)
            employees.remove(staff)
            employees.append(new_rec)
            break

def change_salary2(id,newsalary):
    idx = 0
    for staff in employees:
        if staff[0:8] == id:
            oldsalary = staff.split(',')[3]
            employees[idx] = employees[idx].replace(oldsalary,newsalary)
            break
        idx +=1

employees = ["22334455,Jane White                    ,22/04/2021,1300.50",
             "11223344,Joe Black                     ,22/04/2021,1300.50",
             "66778899,Alice Purple                  ,22/04/2021,1300.50",
             "99887766,Robert Claymore               ,22/04/2021,1300.50"]

print("\nAll employees")
display()

print("\nOld employees")
display_old()

change_salary("66778899","2500.00")
print("\nAll employee after salary change")

change_salary2("11223344","3500.00")
print("\nAll employees after salary change 2".upper())
display()