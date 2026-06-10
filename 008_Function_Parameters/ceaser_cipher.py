letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
           "v", "w", "x", "y", "z"]


def encrypt(message, shift):
    encrypted_message = ""
    for letter in message:
        if letter in letters:
            shifted_index = (letters.index(letter) + shift) % len(letters)
            new_letter = letters[shifted_index]
            encrypted_message += new_letter
        else:
            encrypted_message += letter

    return f"Here is the encoded text: {encrypted_message}"


def decrypt(message, shift):
    decrypted_message = ""
    for letter in message:
        if letter in letters:
            shifted_index = (letters.index(letter) - shift) % len(letters)
            new_letter = letters[shifted_index]
            decrypted_message += new_letter
        else:
            decrypted_message += letter

    return f"Here is the decoded text: {decrypted_message}"


print("Welcome to the Ceaser Cipher!")
ceaser_run = True

while ceaser_run:
    user_function = input("What do you want to do? 'encode' or 'decode': ")
    shift_amount = int(input("How much do you want to shift? "))
    user_message = input(f"Enter the message you want to {user_function}: ").lower()

    if user_function == "encode":
        encrypted = encrypt(user_message, shift_amount)
        print(encrypted)
    elif user_function == "decode":
        decrypted = decrypt(user_message, shift_amount)
        print(decrypted)
    else:
        print("Please enter 'encode' or 'decode'.")

    run_again = input("Do you want to run the program again? 'yes' or 'no': ")

    if run_again != "yes":
        print("Goodbye!")
        ceaser_run = False
