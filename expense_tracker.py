import json
from datetime import datetime

FILE_NAME = "expenses.json"


def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    print("\n--- Add Expense ---")

    description = input("Enter description: ")

    while True:
        try:
            amount = float(input("Enter amount: $"))

            if amount <= 0:
                print("Amount must be greater than 0.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    category = input("Enter category (Food, Transport, Education, Entertainment, Other): ")

    expense = {
        "description": description,
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully!")


def view_expenses(expenses):
    print("\n--- Your Expenses ---")

    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. "
            f"{expense['description']} | "
            f"${expense['amount']:.2f} | "
            f"{expense['category']} | "
            f"{expense['date']}"
        )


def view_total(expenses):
    print("\n--- Total Spending ---")

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"Total spent: ${total:.2f}")


def search_expenses(expenses):
    print("\n--- Search Expenses ---")

    search = input("Enter a description or category to search: ").lower()

    found = False

    for index, expense in enumerate(expenses, start=1):
        if (
            search in expense["description"].lower()
            or search in expense["category"].lower()
        ):
            print(
                f"{index}. "
                f"{expense['description']} | "
                f"${expense['amount']:.2f} | "
                f"{expense['category']} | "
                f"{expense['date']}"
            )
            found = True

    if not found:
        print("No matching expenses found.")


def delete_expense(expenses):
    print("\n--- Delete Expense ---")

    if len(expenses) == 0:
        print("No expenses to delete.")
        return

    view_expenses(expenses)

    while True:
        try:
            number = int(input("Enter the expense number to delete: "))

            if number < 1 or number > len(expenses):
                print("Please enter a valid expense number.")
            else:
                removed = expenses.pop(number - 1)
                save_expenses(expenses)

                print(
                    f"Deleted: {removed['description']} "
                    f"(${removed['amount']:.2f})"
                )
                break

        except ValueError:
            print("Please enter a whole number.")


def show_category_totals(expenses):
    print("\n--- Spending By Category ---")

    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    categories = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    for category, total in categories.items():
        print(f"{category}: ${total:.2f}")


def display_menu():
    print("\n=================================")
    print("       STUDENT EXPENSE TRACKER")
    print("=================================")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total")
    print("4. Search Expenses")
    print("5. Delete Expense")
    print("6. Spending By Category")
    print("7. Exit")
    print("=================================")


def main():
    expenses = load_expenses()

    while True:
        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            view_total(expenses)

        elif choice == "4":
            search_expenses(expenses)

        elif choice == "5":
            delete_expense(expenses)

        elif choice == "6":
            show_category_totals(expenses)

        elif choice == "7":
            print("Thank you for using Student Expense Tracker!")
            break

        else:
            print("Invalid choice. Please select 1-7.")


main()
