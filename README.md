# Cloudstep Software - License Order Report
## Project Description

This project is a Python-based license order reporting system for Cloudstep Software. It calculates software license costs based on the number of seats purchased, applies discounts for qualifying customers, and determines whether onboarding fees are required.

The program also identifies customers who need contract reviews or dedicated trainers. It generates a report showing each customer's final license total, along with a summary of all orders.
## Business Rules

The program follows these rules when processing customer orders:

1. **License Cost:** The original cost is calculated by multiplying the seat price by the number of seats purchased.

2. **Discounts:**
   - Fewer than 10 seats: No discount.
   - 10–49 seats: 7% discount.
   - 50 or more seats: 16% discount for educational customers and 7% for non-educational customers.

3. **Onboarding Fee:** A $60 onboarding fee is added when the discounted license cost is $400 or less.

4. **Contract Review:** A contract review is required when the final license total exceeds $5,000.

5. **Dedicated Trainer:** A trainer is assigned when a customer purchases 25 or more seats or the license total exceeds $3,000.
## How to Run the Program

This project uses Python 3 and was developed using VS Code with Ubuntu (WSL).

To run the program:

1. Open the project folder in VS Code.
2. Open the Ubuntu terminal.
3. Activate the virtual environment:

   ```bash
   source .venv/bin/activate
   ```

4. Run the program:

   ```bash
   python3 main.py
   ```

The program displays all eight customer orders, their final license totals, and a summary report.
## Testing Instructions

This project uses pytest to verify that the business rules work correctly.

To run all tests, enter:

```bash
python3 -m pytest -v
```

The test suite includes 25 tests covering license costs, discounts, onboarding fees, contract reviews, trainer assignments, and report formatting.

To check code quality using Ruff, enter:

```bash
ruff check .
```

To check code formatting, enter:

```bash
ruff format --check .
## Project Files

- **business_rules.py** — Contains the eight functions used to calculate license costs, discounts, onboarding fees, contract reviews, trainer assignments, and order summaries.

- **main.py** — Contains the eight customer orders and generates the Cloudstep Software order report.

- **test_business_rules.py** — Contains the pytest tests used to verify the business rules and calculations.

- **README.md** — Provides project information, business rules, and instructions for running and testing the program.

- **commands.md** — Records the terminal commands and their actual outputs used during development.
## AI Use Statement

I did not use AI.

I reviewed the code, ran the program in Ubuntu, and verified the test results. All 21 pytest tests passed.