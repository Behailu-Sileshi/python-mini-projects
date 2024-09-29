import string
from random import choice, shuffle

def random_lower():
    return choice(string.ascii_lowercase)

def random_upper():
    return choice(string.ascii_uppercase)

def random_digit():
    return choice(string.digits)

def random_symbol():
    return choice(string.punctuation)

random = {
    'lower': random_lower,
    'upper': random_upper,
    'digit': random_digit,
    'symbol': random_symbol
}

class PasswordGenerator:
    """
    A class used to generate passwords based on the specified character sets.

    Parameters:
    -----------
    include_lower : bool
        If True, include lowercase letters in the password (default is False).
    include_upper : bool
        If True, include uppercase letters in the password (default is False).
    include_digit : bool
        If True, include digits (0-9) in the password (default is False).
    include_symbol : bool
        If True, include symbols (e.g., !, @, #) in the password (default is False).
        
    Methods:
    --------
    generate_password(length: int) -> str:
        Generates a random password of the specified length.
    """
    
    def __init__(self, include_lower: bool = False, include_upper: bool = False, 
                 include_digit: bool = False, include_symbol: bool = False):
        self.include_lower = include_lower 
        self.include_upper = include_upper
        self.include_digit = include_digit
        self.include_symbol = include_symbol
        self.include = self._contains()

    def _contains(self):
        """Private method to determine which character sets to include."""
        return [key for key in random if getattr(self, f'include_{key}')]

    def generate_password(self, length: int) -> str:
        """
        Generates a random password of the specified length.

        Parameters:
        -----------
        length : int
            The length of the password to be generated.

        Returns:
        --------
        str
            A randomly generated password.

        Raises:
        -------
        ValueError
            If no character sets are included.
        """
        if not self.include:
            raise ValueError("At least one character set must be selected to generate a password.")

        password_chars = [random[choice(self.include)]() for _ in range(length)]
        shuffle(password_chars)  # Optional: shuffle the characters for randomness
        return ''.join(password_chars)
