salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
    return x*20/100 + x

for salary in salaries:
    print(new_salary(salary))

null_list = []

for salary in salaries:
    null_list.append(new_salary(salary))

for salary in salaries:
    if salary > 3000:
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(salary*2))

[salary * 20 if salary < 3000  else salary * 0 for salary in salaries ]

[new_salary(salary * 20) if salary < 3000  else salary * 0 for salary in salaries ]

students = ["Johm", "Mark", "Venessa", "Mariam"]

stu_no = ["John", "Venessa"]

[student.lower() if student in stu_no else student.upper() for student in students]