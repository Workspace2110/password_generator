import string
import random

from optparse import OptionParser


def _get_parameters() -> OptionParser:
    parser = OptionParser()
    parser.add_option("-l",
                      "--length",
                      help="The password length",
                      default=16,
                      type="int",
                      dest="length")
    parser.add_option("-s",
                      "--strength",
                      help="The password strength level. 0: only letters, 1: letters and digits, 2: lettersm digits and special characters",
                      default=1,
                      type="int",
                      dest="strength")

    return parser


def gen_password(length: int, character_list: str) -> str:
    password = []
    for _ in range(length):
        random_char = random.choice(character_list)
        password.append(random_char)
    
    return "".join(password)


def main():
    # Load parameters
    parser = _get_parameters()
    (options, args) = parser.parse_args()
    
    # Set & normalize password length
    length = options.length
    length = 16 if length < 0 else length

    # Set & normalize password strength level
    strength = options.strength
    strength = 2 if strength > 2 or strength < 0 else strength

    character_list = string.ascii_letters
    if strength >= 1:
        character_list += string.digits
    if strength >= 2:
        character_list += string.punctuation

    password = gen_password(length, character_list)
    print(f"Password: {password}")


if __name__ == "__main__":
    main()
