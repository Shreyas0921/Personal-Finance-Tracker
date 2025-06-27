# finance_tracker.py

def print_welcome():
    print("Welcome to the Personal Finance Tracker!")

# Step 2: Add an expense
def add_expense(data):
    try:
        description = input("Enter expense description: ").strip()
        if not description:
            raise ValueError("Description cannot be empty.")

        category = input("Enter category: ").strip()
        if not category:
            raise ValueError("Category cannot be empty.")

        amount_str = input("Enter amount: ").strip()
        amount = float(amount_str)

        # Store as a tuple
        expense = (description, amount)

        # Add to the category list
        if category in data:
            data[category].append(expense)
        else:
            data[category] = [expense]

        print("✅ Expense added successfully.")
    except ValueError:
        print("❌ Invalid amount or empty input. Please enter valid data.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

# Step 3: View all expenses
def view_expenses(data):
    if not data:
        print("No expenses recorded yet.")
        return

    for category, expenses in data.items():
        print(f"\nCategory: {category}")
        for desc, amount in expenses:
            print(f"  - {desc}: ${amount:.2f}")

# Step 4: View summary by category
def view_summary(data):
    if not data:
        print("No expenses recorded yet.")
        return

    print("\nSummary:")
    for category, expenses in data.items():
        total = sum(amount for _, amount in expenses)
        print(f"{category}: ${total:.2f}")

# Step 6: Main menu logic
def main():
    data = {}
    print_welcome()

    while True:
        print("\nWhat would you like to do?")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            add_expense(data)
        elif choice == '2':
            view_expenses(data)
        elif choice == '3':
            view_summary(data)
        elif choice == '4':
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")

main()
