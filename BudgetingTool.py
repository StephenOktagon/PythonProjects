class BudgetingTool:
    def __init__(self):
        self.income = 0
        self.expenses = []

    def get_income(self):
        try:
            self.income = float(input("Enter your monthly income: $"))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            self.get_income()

    def get_expenses(self):
        num_expenses = int(input("How many expenses do you want to add? "))
        for _ in range(num_expenses):
            expense_name = input("Enter expense name: ")
            try:
                expense_amount = float(input(f"Enter monthly {expense_name} expense: $"))
                self.expenses.append((expense_name, expense_amount))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                self.get_expenses()

    def calculate_budget(self):
        total_expenses = sum(expense[1] for expense in self.expenses)
        budget = self.income - total_expenses
        return budget

    def display_budget(self):
        print("\n--- Budget Summary ---")
        print(f"Monthly Income: ${self.income:.2f}")
        print("Expenses:")
        for expense_name, expense_amount in self.expenses:
            print(f"- {expense_name}: ${expense_amount:.2f}")
        print(f"Total Expenses: ${sum(expense[1] for expense in self.expenses):.2f}")
        budget = self.calculate_budget()
        print(f"Remaining Budget: ${budget:.2f}")

    def run(self):
        print("Welcome to the Budgeting Tool!")
        self.get_income()
        self.get_expenses()
        self.display_budget()


if __name__ == "__main__":
    budget_tool = BudgetingTool()
    budget_tool.run()
