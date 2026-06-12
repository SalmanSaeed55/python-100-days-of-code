def format_name(first_name, last_name):
    """Takes in a first name and a last name and returns a title-case version of the name

    :param first_name: The first name of the user
    :param last_name: The last name of the user
    :return: The formatted name as title and string
    """
    if first_name == "" or last_name == "":
        return "Please enter your first and last name"
    first_name = first_name.title()
    last_name = last_name.title()
    return f'{first_name} {last_name}'  # returns an output,, allowing storage in a variable


titled_name = format_name(input("What is your first name? "), input("What is your last name? "))
print(titled_name)