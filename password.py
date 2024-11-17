#password generator
import random
import string

def get_parameters():
    while True:
        try:
            size = int(input("Enter the length of the password: "))
            if size > 0:
                special = int(input("Enter the number of special characters: "))
                if special < size:
                    numbcount = int(input("Enter the number of numbers: "))
                    if (special + numbcount) < size:
                        return size, special, numbcount
                    else:
                        print("The sum of special characters and numbers must be less than the password length.")
                else:
                    print("Number of special characters must be less than the password length.")
            else:
                print("Password length must be greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def generate_password(size, special, numbcount):
    # Define characters
    special_chars = string.punctuation
    numbers = string.digits
    letters = string.ascii_letters

    # get random characters
    password_special = [random.choice(special_chars) for _ in range(special)]
    password_numbers = [random.choice(numbers) for _ in range(numbcount)]
    password_letters = [random.choice(letters) for _ in range(size - special - numbcount)]

    # Combine all characters
    password_list = password_special + password_numbers + password_letters

    # Puts password in random order
    random.shuffle(password_list)

    # Changes list to string
    password = ''.join(password_list)
    return password

def save_password(name, password): 
    with open('passwords.txt', 'a') as file: 
        file.write(f"{name}: {password}\n")

# Example 
size, special, numbcount = get_parameters()
password = generate_password(size, special, numbcount) 
print(f"Generated password: {password}")

name = input("Enter the name of what this password is for: ") 
# Save the password 
save_password(name, password) 
print("Password saved successfully.")
