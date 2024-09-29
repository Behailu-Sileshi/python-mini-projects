from password_generator import PasswordGenerator
def get_boolean_input(prompt):
    """Prompts the user for a yes/no input and returns a boolean."""
    while True:
        response = input(prompt).strip().lower()
        if response in ('y', 'n'):
            return response == 'y'
        print("Please enter 'y' for yes or 'n' for no.")

def get_password_length():
    """Prompts the user for a valid password length."""
    while True:
        try:
            length = int(input('Password Length (5-25): '))
            if 5 <= length <= 25:
                return length
            print('The password length should be between 5 and 25.')
        except ValueError:
            print('Invalid input. Please enter a number only.')

# Get user inputs
def main():
    password_length = get_password_length()
    lower = get_boolean_input('Include lower letters? (y/n): ')
    upper = get_boolean_input('Include upper letters? (y/n): ')
    digits = get_boolean_input('Include digits? (y/n): ')
    symbols = get_boolean_input('Include symbols? (y/n): ')

    # Generate the password
    pg = PasswordGenerator(include_digit=digits, include_upper=upper, include_lower=lower, include_symbol=symbols)
    password = pg.generate_password(password_length)
    print(f'Your password: {password}')

if __name__ == '__main__':
    main()