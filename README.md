# Password Hash Script
For generating password with python

## Pre-requement

### Setup environment with poetry
```bash
cd password_generator
poetry install
```

### Setup environment with pip
```bash
cd password_generator
pip install -r requirements.txt
```

## How to use
### Options Description
* -l --length: The password length
* -s --strength: The password strength

### Get script help
```bash
python password_generator.py --help
```

### Execture without options
```bash
python password_generator.py
```

### Execture with password options
```bash
python password_generator.py -l ${PASSWORD_LENGTH} -s ${PASSWORD_STRENGTH}
```

## License
* MIT
