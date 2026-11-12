from file_manager import save_expenses, load_expenses
from datetime import datetime

def main():
    expenses = load_expenses()
   
    print("Expense Tracker")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Filter by category")
    print("4. Filter by data")
    print("5. Exit")

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
    elif choice == "3":
     # filter expenses by category
     category = input("Enter category: ")

     for expense in expenses:
         if expense[2].lower()  == category.lower():
               print(expense)
    elif  choice == "4":
         # filter expenses by date
         start_date = input("Enter start date: ")
         end_date = input("Enter end date ")

         start = datetime.strptime(start_date, "%m/%d/%Y")
         end = datetime.strptime(end_date, "%m/%d/%Y")

         for expense in expenses:
              expense_date = datetime.strptime(expense[0], "%m/%d/%Y")

              if start <= expense_date <= end:
                   print(expense)
                         
if __name__== "__main__":
        main()

