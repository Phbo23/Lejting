#!/usr/bin/env python3
"""
LejTing - Rental Management System
Obligatorisk opgave 1 INNT

A simple rental management system for handling rental items and transactions.
"""

from datetime import datetime, timedelta
from typing import Dict, List, Optional
import json


class RentalItem:
    """Represents an item available for rental."""
    
    def __init__(self, item_id: str, name: str, daily_rate: float, description: str = ""):
        self.item_id = item_id
        self.name = name
        self.daily_rate = daily_rate
        self.description = description
        self.is_available = True
        self.rented_by = None
        self.rental_start = None
        self.rental_end = None
    
    def __str__(self):
        status = "Available" if self.is_available else f"Rented by {self.rented_by}"
        return f"Item: {self.name} (ID: {self.item_id}) - {self.daily_rate} kr/day - {status}"
    
    def to_dict(self):
        """Convert item to dictionary for JSON serialization."""
        return {
            'item_id': self.item_id,
            'name': self.name,
            'daily_rate': self.daily_rate,
            'description': self.description,
            'is_available': self.is_available,
            'rented_by': self.rented_by,
            'rental_start': self.rental_start.isoformat() if self.rental_start else None,
            'rental_end': self.rental_end.isoformat() if self.rental_end else None
        }


class RentalTransaction:
    """Represents a rental transaction."""
    
    def __init__(self, transaction_id: str, item_id: str, renter_name: str, 
                 start_date: datetime, end_date: datetime, total_cost: float):
        self.transaction_id = transaction_id
        self.item_id = item_id
        self.renter_name = renter_name
        self.start_date = start_date
        self.end_date = end_date
        self.total_cost = total_cost
        self.is_completed = False
    
    def __str__(self):
        status = "Completed" if self.is_completed else "Active"
        return f"Transaction {self.transaction_id}: {self.renter_name} renting item {self.item_id} - {self.total_cost} kr ({status})"


class LejTingSystem:
    """Main rental management system."""
    
    def __init__(self):
        self.items: Dict[str, RentalItem] = {}
        self.transactions: Dict[str, RentalTransaction] = {}
        self.transaction_counter = 1
    
    def add_item(self, item_id: str, name: str, daily_rate: float, description: str = "") -> bool:
        """Add a new rental item to the system."""
        if item_id in self.items:
            print(f"Error: Item with ID {item_id} already exists!")
            return False
        
        self.items[item_id] = RentalItem(item_id, name, daily_rate, description)
        print(f"Added item: {name} (ID: {item_id})")
        return True
    
    def remove_item(self, item_id: str) -> bool:
        """Remove an item from the system."""
        if item_id not in self.items:
            print(f"Error: Item with ID {item_id} not found!")
            return False
        
        item = self.items[item_id]
        if not item.is_available:
            print(f"Error: Cannot remove item {item_id} - it is currently rented!")
            return False
        
        del self.items[item_id]
        print(f"Removed item: {item.name} (ID: {item_id})")
        return True
    
    def list_items(self, available_only: bool = False):
        """List all items in the system."""
        if not self.items:
            print("No items in the system.")
            return
        
        print("\n--- Rental Items ---")
        for item in self.items.values():
            if available_only and not item.is_available:
                continue
            print(item)
    
    def rent_item(self, item_id: str, renter_name: str, days: int) -> Optional[str]:
        """Rent an item to a customer."""
        if item_id not in self.items:
            print(f"Error: Item with ID {item_id} not found!")
            return None
        
        item = self.items[item_id]
        if not item.is_available:
            print(f"Error: Item {item_id} is already rented!")
            return None
        
        if days <= 0:
            print("Error: Rental period must be at least 1 day!")
            return None
        
        # Calculate rental details
        start_date = datetime.now()
        end_date = start_date + timedelta(days=days)
        total_cost = item.daily_rate * days
        
        # Create transaction
        transaction_id = f"T{self.transaction_counter:04d}"
        self.transaction_counter += 1
        
        transaction = RentalTransaction(
            transaction_id, item_id, renter_name, start_date, end_date, total_cost
        )
        
        # Update item status
        item.is_available = False
        item.rented_by = renter_name
        item.rental_start = start_date
        item.rental_end = end_date
        
        # Store transaction
        self.transactions[transaction_id] = transaction
        
        print(f"Rental successful!")
        print(f"Transaction ID: {transaction_id}")
        print(f"Item: {item.name}")
        print(f"Renter: {renter_name}")
        print(f"Period: {days} days ({start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')})")
        print(f"Total cost: {total_cost} kr")
        
        return transaction_id
    
    def return_item(self, item_id: str) -> bool:
        """Return a rented item."""
        if item_id not in self.items:
            print(f"Error: Item with ID {item_id} not found!")
            return False
        
        item = self.items[item_id]
        if item.is_available:
            print(f"Error: Item {item_id} is not currently rented!")
            return False
        
        # Find the active transaction
        active_transaction = None
        for transaction in self.transactions.values():
            if transaction.item_id == item_id and not transaction.is_completed:
                active_transaction = transaction
                break
        
        if active_transaction:
            active_transaction.is_completed = True
        
        # Update item status
        renter_name = item.rented_by
        item.is_available = True
        item.rented_by = None
        item.rental_start = None
        item.rental_end = None
        
        print(f"Item {item.name} (ID: {item_id}) returned by {renter_name}")
        return True
    
    def list_transactions(self, active_only: bool = False):
        """List all transactions."""
        if not self.transactions:
            print("No transactions found.")
            return
        
        print("\n--- Rental Transactions ---")
        for transaction in self.transactions.values():
            if active_only and transaction.is_completed:
                continue
            print(transaction)
    
    def get_item_info(self, item_id: str):
        """Get detailed information about a specific item."""
        if item_id not in self.items:
            print(f"Error: Item with ID {item_id} not found!")
            return
        
        item = self.items[item_id]
        print(f"\n--- Item Details ---")
        print(f"ID: {item.item_id}")
        print(f"Name: {item.name}")
        print(f"Description: {item.description}")
        print(f"Daily Rate: {item.daily_rate} kr")
        print(f"Status: {'Available' if item.is_available else 'Rented'}")
        
        if not item.is_available:
            print(f"Rented by: {item.rented_by}")
            print(f"Rental period: {item.rental_start.strftime('%Y-%m-%d')} to {item.rental_end.strftime('%Y-%m-%d')}")
    
    def save_data(self, filename: str = "lejting_data.json"):
        """Save system data to a JSON file."""
        data = {
            'items': {item_id: item.to_dict() for item_id, item in self.items.items()},
            'transaction_counter': self.transaction_counter
        }
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"Data saved to {filename}")
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def load_data(self, filename: str = "lejting_data.json"):
        """Load system data from a JSON file."""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Restore items
            self.items = {}
            for item_id, item_data in data.get('items', {}).items():
                item = RentalItem(
                    item_data['item_id'],
                    item_data['name'],
                    item_data['daily_rate'],
                    item_data['description']
                )
                item.is_available = item_data['is_available']
                item.rented_by = item_data['rented_by']
                
                if item_data['rental_start']:
                    item.rental_start = datetime.fromisoformat(item_data['rental_start'])
                if item_data['rental_end']:
                    item.rental_end = datetime.fromisoformat(item_data['rental_end'])
                
                self.items[item_id] = item
            
            self.transaction_counter = data.get('transaction_counter', 1)
            print(f"Data loaded from {filename}")
            
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with empty system.")
        except Exception as e:
            print(f"Error loading data: {e}")


def main():
    """Main function to demonstrate the LejTing system."""
    print("=== LejTing - Rental Management System ===")
    print("Obligatorisk opgave 1 INNT\n")
    
    # Create system instance
    system = LejTingSystem()
    
    # Add some sample items
    print("Adding sample rental items...")
    system.add_item("BIKE001", "Mountain Bike", 50.0, "High-quality mountain bike for outdoor adventures")
    system.add_item("CAR001", "Compact Car", 300.0, "Fuel-efficient compact car for city driving")
    system.add_item("TENT001", "Camping Tent", 25.0, "4-person camping tent, waterproof")
    system.add_item("TOOLS001", "Power Drill Set", 75.0, "Professional power drill with accessories")
    
    print("\nListing all available items:")
    system.list_items()
    
    print("\n--- Rental Transactions ---")
    
    # Demonstrate rental transactions
    print("\nRenting mountain bike to Anna for 3 days:")
    system.rent_item("BIKE001", "Anna Nielsen", 3)
    
    print("\nRenting camping tent to Lars for 7 days:")
    system.rent_item("TENT001", "Lars Andersen", 7)
    
    print("\nListing available items after rentals:")
    system.list_items(available_only=True)
    
    print("\nListing all transactions:")
    system.list_transactions()
    
    print("\nGetting detailed info for mountain bike:")
    system.get_item_info("BIKE001")
    
    print("\nReturning the mountain bike:")
    system.return_item("BIKE001")
    
    print("\nListing active transactions:")
    system.list_transactions(active_only=True)
    
    print("\nFinal state - all items:")
    system.list_items()
    
    # Save data
    print("\nSaving system data...")
    system.save_data()
    
    print("\n=== LejTing System Demo Complete ===")


if __name__ == "__main__":
    main()