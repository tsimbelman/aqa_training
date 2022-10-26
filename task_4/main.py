
import human

def main():

    # Input employer data
    name = input('Input name:')
    gender = input('Input gender:')
    position = input('Input position:')
    salary_per_hour = int(input('Input salary per hour: $:'))

    employee_1 = human.Employee(name, gender, position, salary_per_hour)

    # Display the employer data
    print(employee_1.get_name())
    print(employee_1.get_gender())
    print(employee_1.get_salary_per_hour())
    print(employee_1.get_position())
    print()

    # Employee start working day
    employee_1.wake_up()
    employee_1.to_work()
    log_time = int(input(f"Enter login time for employee name {employee_1.get_name()} on position {employee_1.get_position()}:"))
    employee_1.log_time(log_time)
    salary = log_time * employee_1.get_salary_per_hour()
    print()

    # Executed some actions
    print(f"{employee_1.get_name()} on position {employee_1.get_position()} do some work for {log_time} hours and earned {salary}$" )
    print()

    # Employer end working day
    employee_1.sit_down()
    print()
    employee_1.to_rest()

main()








