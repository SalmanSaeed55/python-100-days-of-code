from student_data import student_db


def main_menu():
    """Displays the main menu and options for the user, looping continuously until a valid option is selected. Returns the user's choice as an integer.

    :return: The user's choice as an integer.
    """
    while True:
        try:
            print("Select what you want to do:", end="")
            choice = int(input("""
            1. Add Student
            2. View Class Average
            3. Review Performance on Specific Tests
            4. Exit
            >> """))

            if 1 <= choice <= 5:
                print(f"Proceeding with option {choice}\n")
                return choice
            else:
                print("Invalid option, please try again\n")
        except ValueError:
            print("Please enter a numeric input\n")


def add_student(data):
    """Adds a student to the database.

    :param data: The student database to add the new student to
    :return: None
    """
    name = input("Enter the student's name: ")
    scores = []
    for i in range(3):
        while True:
            try:
                score = float(input(f"Enter score for test {i + 1}: "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("Score must be between 0 and 100. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    average = sum(scores) / len(scores)
    if average >= 50:
        if 91 <= average <= 100:
            grade = "A"
        elif 81 <= average <= 90:
            grade = "B"
        elif 71 <= average <= 80:
            grade = "C"
        else:
            grade = "Pass"
    else:
        grade = "Fail"
    data.append({"name": name, "scores": scores, "average": average, "grade": grade})
    print(f"Student {name} added successfully with average score {average:.2f} and grade {grade}.\n")


def class_average(data):
    """Calculates the average grade for the entire class, based on each individual's average.

    :param data: The entire database to calculate the average for.
    :return: The calculated average.
    """
    total_average = 0
    if not data:
        print("No student data available to calculate class average.\n")
        return None

    for i in range(len(data)):
        total_average += data[i]["average"]

    return total_average / len(data)


def specific_test_performance(data):
    """Calculates the class average on a specific test, based on the scores of each individual. Prompts the user to
    select which test to analyse.

    :param data: The entire database to calculate the class average for.
    :return: The calculated average and the test number.
    """
    class_total = 0
    while True:
        try:
            test_performance = int(input("Which test would you like to analyse? [1], [2] or [3]  "))
            if 1 <= test_performance <= 3:
                print("Processing Class performance on Test", test_performance)
                break
            else:
                print("Invalid option, please try again\n")
        except ValueError:
            print("Please enter a numeric input\n")

    for i in range(len(data)):
        class_total += data[i]["scores"][test_performance - 1]

    return class_total / len(data), test_performance


if __name__ == "__main__":
    print(f"Welcome to Student Performance Tracker\n{"-" * 100}\n")

    while True:
        option_select = main_menu()

        if option_select == 1:
            add_student(student_db)
        elif option_select == 2:
            class_average = class_average(student_db)
            print(f"Average Grade:\t {class_average:.2f}\n")
        elif option_select == 3:
            specific_test = specific_test_performance(student_db)
            print(f"The average grade for test {specific_test[1]} is {specific_test[0]:.2f}\n")
        else:
            break
