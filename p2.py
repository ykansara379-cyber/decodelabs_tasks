
import json
import os
from datetime import date

DATA_FILE = "expenses.json"


def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=2)


def add_expense(expenses):
    desc = input("Description: ").strip()
    while True:
        try:
            amount = float(input("Amount (₹): ").strip())
            break
        except ValueError:
            print("Please enter a valid number.")
    category = input("Category (e.g. food, travel, rent): ").strip() or "general"

    expense = {
        "date": str(date.today()),
        "description": desc,
        "amount": amount,
        "category": category,
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added.\n")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    print(f"\n{'Date':<12}{'Category':<12}{'Description':<20}{'Amount':>10}")
    print("-" * 54)
    total = 0
    for e in expenses:
        print(f"{e['date']:<12}{e['category']:<12}{e['description']:<20}{e['amount']:>10.2f}")
        total += e["amount"]
    print("-" * 54)
    print(f"{'Total':<44}{total:>10.2f}\n")


def view_by_category(expenses):
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    totals = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]

    print("\nSpending by category:")
    for cat, amt in sorted(totals.items(), key=lambda x: -x[1]):
        print(f"  {cat:<15}₹{amt:.2f}")
    print()


def main():
    expenses = load_expenses()

    menu = """
1 Expense Tracker 
1. Add expense
2. View all expenses
3. View totals by category
4. Exit
"""

    while True:
        print(menu)
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_by_category(expenses)
        elif choice == "4":
            print("see you soon!")
            break
        else:
            print("Invalid choice, try again.\n")


if __name__ == "__main__":
    main()