def calculate_overtime_pay():
    total_employees = 10
    overtime_rate = 12.00
    for i in range(total_employees):
        hours_worked = int(input(f"Enter hours worked by employee {i+1}: "))
        if hours_worked > 40:
            overtime_hours = hours_worked - 40
            pay = overtime_hours * overtime_rate
            print(f"Overtime pay for employee {i+1}: Rs. {pay:.2f}")
        else:
            print(f"No overtime pay for employee {i+1}.")

calculate_overtime_pay()