# Password Hash Script
For generating password with python

## Prerequisites

* ### Setup environment with uv venv
  ```bash
  cd password_hash
  uv venv
  uv sync
  ```

* ### Setup environment with pip
  ```bash
  cd password_generator
  pip install -r requirements.txt
  ```

## How to use

* ### Options Description
  * -l --length: The password length
  * -s --strength: The password strength
    * 0: only letters
    * 1: letters and digits
    * 2: lettersm digits and special characters

* ### Get script help
  ```bash
  python password_generator.py --help
  ```

* ### Execture without options
  ```bash
  python password_generator.py
  ```

* ### Execture with password options
  ```bash
  python password_generator.py -l ${PASSWORD_LENGTH} -s ${PASSWORD_STRENGTH}
  ```

## Example

* ### Execture with password options via uv
  ```bash
  uv run python password_generator.py -l 12 -s 1
  ```

* ### Execture with password options via vanilla python
  ```bash
  python password_generator.py -l 12 -s 1
  ```

## References:
* [uv official website](https://docs.astral.sh/uv/)

## License
* MIT
