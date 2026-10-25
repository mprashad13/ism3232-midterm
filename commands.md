# Cloudstep Software - Terminal Commands

This file documents the terminal commands used to create, inspect, test, and manage the project. The outputs shown below are copied directly from the Ubuntu terminal.
## 1. Python Interpreter

Command:
```bash
which python3
```

Output:
```/home/gp151/ism3232-midterm/.venv/bin/python3
```
## 2. Project Folder Structure

Command:
```bash
tree -L 2
```

Output:
```├── README.md
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
├── test_business_rules.py
│   ├── __pycache__
│   └── test_business_rules.py
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py
```
## 3. Python Function Definitions

Command:
```bash
rg 'def '
```

Output:
```text
main.py
11:def main():

business_rules.py
14:def calculate_license_cost(seat_price: float, seats: int) -> float:
```
## 4. Files Containing Print Statements

Command:
```bash
rg -l 'print'
```

Output:
```main.py
```
## 5. Git Commit History

Command:
```bash
git log --oneline
```

Output:
```bc2d324 (HEAD -> main, origin/main) Complete business rules and order report
9fc26b9 Initialize midterm project structure
```
## 6. File and Folder Creation Commands

This section documents the Ubuntu terminal commands used to create the project files and folders.

Commands:
```mkdir ism3232-midterm
```

Output:
```no output displayed
```
### File Creation Using VS Code

I used the mkdir command in my Ubuntu terminal to create my project directory. After creating the folder, I used Visual Studio Code's Explorer panel to create and organize my Python files, including business_rules.py, main.py, and my test file. I also used VS Code to create README.md and commands.md.