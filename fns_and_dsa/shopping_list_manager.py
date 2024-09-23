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
        choice = input("Enter your choice: ")

        if choice == '1':
            add_item = input("What would you like to add: ")
            shopping_list.append(add_item)
        elif choice == '2':
            rem_item = input("what item would you like to remove: ")
            if rem_item not in shopping_list:
                print("Item not found!")
            else:
                shopping_list.remove(rem_item)    
        elif choice == '3':
            print(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
