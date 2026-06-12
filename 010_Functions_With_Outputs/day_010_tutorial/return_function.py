def format_name(first_name, last_name):
    first_name = first_name.title()
    last_name = last_name.title()
    return f'{first_name} {last_name}'  # returns an output,, allowing storage in a variable


titled_name = format_name('salman', 'saeed')
new_titled_name = format_name('SALMAN', 'sAeEd')

print(titled_name)
print(new_titled_name)


def function_1(text):
    return text + text


def function_2(text):
    return text.title()


print(function_1('hello'))
print(function_2('hello'))

print(function_2(function_1('hello')))