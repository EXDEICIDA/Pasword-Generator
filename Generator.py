import random
import string
import os


def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_numbers=True, use_special=True):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("No character types selected for password generation")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def save_password(password, description):
    with open("passwords.txt", "a") as file:
        file.write(f"{description}: {password}\n")


def load_passwords():
    if not os.path.exists("passwords.txt"):
        print("No passwords saved yet.")
        return
    with open("passwords.txt", "r") as file:
        for line in file:
            print(line.strip())


def main():
    while True:
        print("\nPassword Generator")
        print("1. Generate a new password")
        print("2. View saved passwords")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            length = int(input("Enter password length: "))
            use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
            use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
            use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
            use_special = input("Include special characters? (y/n): ").lower() == 'y'

            try:
                password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special)
                print(f"Generated password: {password}")
                save_option = input("Do you want to save this password? (y/n): ").lower()
                if save_option == 'y':
                    description = input("Enter a description for this password: ")
                    save_password(password, description)
                    print("Password saved.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '2':
            load_passwords()

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
