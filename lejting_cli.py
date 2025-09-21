#!/usr/bin/env python3
"""
LejTing Interactive CLI
Obligatorisk opgave 1 INNT

Interactive command-line interface for the LejTing rental management system.
"""

from lejting import LejTingSystem
import sys


def print_menu():
    """Display the main menu options."""
    print("\n=== LejTing - Rental Management System ===")
    print("1. List all items")
    print("2. List available items only")
    print("3. Add new item")
    print("4. Remove item")
    print("5. Rent item")
    print("6. Return item")
    print("7. View item details")
    print("8. List transactions")
    print("9. List active transactions")
    print("10. Save data")
    print("11. Load data")
    print("0. Exit")
    print("=" * 45)


def get_input(prompt: str, input_type=str):
    """Get user input with type conversion and error handling."""
    while True:
        try:
            user_input = input(prompt).strip()
            if input_type == str:
                return user_input
            else:
                return input_type(user_input)
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")
        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit(0)


def main():
    """Main interactive CLI function."""
    system = LejTingSystem()
    
    print("Welcome to LejTing - Rental Management System!")
    print("Obligatorisk opgave 1 INNT")
    
    # Try to load existing data
    system.load_data()
    
    while True:
        try:
            print_menu()
            choice = get_input("Select an option (0-11): ", int)
            
            if choice == 0:
                print("Thank you for using LejTing! Goodbye!")
                break
            
            elif choice == 1:
                system.list_items()
            
            elif choice == 2:
                system.list_items(available_only=True)
            
            elif choice == 3:
                print("\n--- Add New Item ---")
                item_id = get_input("Enter item ID: ")
                if not item_id:
                    print("Item ID cannot be empty!")
                    continue
                
                name = get_input("Enter item name: ")
                if not name:
                    print("Item name cannot be empty!")
                    continue
                
                daily_rate = get_input("Enter daily rate (kr): ", float)
                description = get_input("Enter description (optional): ")
                
                system.add_item(item_id, name, daily_rate, description)
            
            elif choice == 4:
                print("\n--- Remove Item ---")
                item_id = get_input("Enter item ID to remove: ")
                system.remove_item(item_id)
            
            elif choice == 5:
                print("\n--- Rent Item ---")
                item_id = get_input("Enter item ID to rent: ")
                renter_name = get_input("Enter renter's name: ")
                if not renter_name:
                    print("Renter name cannot be empty!")
                    continue
                
                days = get_input("Enter rental period (days): ", int)
                system.rent_item(item_id, renter_name, days)
            
            elif choice == 6:
                print("\n--- Return Item ---")
                item_id = get_input("Enter item ID to return: ")
                system.return_item(item_id)
            
            elif choice == 7:
                print("\n--- View Item Details ---")
                item_id = get_input("Enter item ID: ")
                system.get_item_info(item_id)
            
            elif choice == 8:
                system.list_transactions()
            
            elif choice == 9:
                system.list_transactions(active_only=True)
            
            elif choice == 10:
                filename = get_input("Enter filename (press Enter for default): ")
                if filename:
                    system.save_data(filename)
                else:
                    system.save_data()
            
            elif choice == 11:
                filename = get_input("Enter filename (press Enter for default): ")
                if filename:
                    system.load_data(filename)
                else:
                    system.load_data()
            
            else:
                print("Invalid option! Please select a number between 0 and 11.")
            
            if choice != 0:
                input("\nPress Enter to continue...")
        
        except KeyboardInterrupt:
            print("\n\nExiting LejTing system...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()