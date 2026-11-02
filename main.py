def main():
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

          print("Expense added")
          
if __name__== "__main__":
        main()

