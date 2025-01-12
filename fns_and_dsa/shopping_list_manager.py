def display_menu():
    """
    Display the menu options for the shopping list manager.
    """
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    """
    Main function to manage the shopping list.
    """
    # Define the shopping list as an array
    shopping_list = []
    
    while True:
        # Call the display_menu function
        display_menu()

        # Ensure choice input is taken as a number
        try:
            choice = int(input("Enter your choice (1-4): ").strip())
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            # Add item
            item = input("Enter the name of the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to the shopping list.")
            else:
                print("Item name cannot be empty.")
        
        elif choice == 2:
            # Remove item
            item = input("Enter the name of the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"'{item}' was not found in the shopping list.")
        
        elif choice == 3:
            # View list
            if shopping_list:
                print("\nCurrent Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("The shopping list is currently empty.")
        
        elif choice == 4:
            # Exit
            print("Goodbye!")
            break
        
        else:
            # Handle invalid input
            print("Invalid choice. Please select a number between 1 and 4.")

# Ensure this block is properly aligned with no indentation issues
if __name__ == "__main__":
    main()
