def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"{item}has been added")
            pass
        elif choice == '2':
            item = input("Enter item to remove")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed from the list")
            else:
                print(f"{item} doesn't exist in the list")
            pass
        elif choice == '3':
            if shopping_list:
                print('shopping list manager')
                for item in shopping_list:
                    print(item)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
