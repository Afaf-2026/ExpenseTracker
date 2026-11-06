from file_manager import save_expenses, load_expenses

def main():
    expenses = load_expenses()
   
    print("Expense Tracker")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Exit")

    choice = input("Enter your choice: ")
    print("You chose:", choice)
    if choice == "1":
          date = input("Enter date: ")
          amount = input("Enter amount: ")
          category = input("Enter category: ")
          description = input("Enter description: ")
          # store the expense in the list
          expense = [date, amount, category, description]
          expenses.append(expense)
          save_expenses(expenses)
          print("Expense added")
    elif choice == "2":
          # show all expenses
          for expense in expenses:
                print(expense)
          
if __name__== "__main__":
        main()

