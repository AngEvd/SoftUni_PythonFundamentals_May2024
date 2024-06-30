company_register = {}

while True:
    command_line = input()
    if command_line == "End":
        break
    else:
        company, employee_id = command_line.split(" -> ")
        if company not in company_register:
            company_register[company] = []
        if employee_id not in company_register[company]:
            company_register[company].append(employee_id)


for company, employees in company_register.items():
    print(company)
    for employee in employees:
        print(f"-- {employee}")
