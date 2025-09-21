# LejTing - Rental Management System
**Obligatorisk opgave 1 INNT**

A comprehensive rental management system implemented in Python for handling rental items, transactions, and customer interactions.

## Overview

LejTing is a simple yet functional rental management system that allows you to:
- Manage rental items (add, remove, list)
- Handle rental transactions (rent items, return items)
- Track rental history and active rentals
- Persist data to JSON files
- Interactive command-line interface

## Features

### Core Functionality
- **Item Management**: Add, remove, and list rental items
- **Rental Transactions**: Rent items to customers with automatic cost calculation
- **Return Processing**: Handle item returns and transaction completion
- **Data Persistence**: Save and load system data to/from JSON files
- **Interactive CLI**: User-friendly command-line interface

### Item Properties
- Unique item ID
- Name and description
- Daily rental rate
- Availability status
- Current renter information
- Rental period tracking

### Transaction Management
- Automatic transaction ID generation
- Rental period calculation
- Cost calculation based on daily rates
- Transaction history tracking
- Active vs. completed transaction status

## Installation and Usage

### Prerequisites
- Python 3.6 or higher

### Running the System

#### 1. Demo Mode (Automated)
Run the main system with pre-populated sample data:
```bash
python3 lejting.py
```

#### 2. Interactive CLI Mode
Use the interactive command-line interface:
```bash
python3 lejting_cli.py
```

#### 3. Run Tests
Execute the test suite to verify functionality:
```bash
python3 test_lejting.py
```

## System Architecture

### Classes

#### `RentalItem`
Represents an individual rental item with properties:
- `item_id`: Unique identifier
- `name`: Item name
- `daily_rate`: Cost per day in kr
- `description`: Item description
- `is_available`: Availability status
- `rented_by`: Current renter name
- `rental_start/end`: Rental period dates

#### `RentalTransaction`
Manages rental transaction details:
- `transaction_id`: Unique transaction identifier
- `item_id`: Associated item
- `renter_name`: Customer name
- `start_date/end_date`: Rental period
- `total_cost`: Calculated rental cost
- `is_completed`: Transaction status

#### `LejTingSystem`
Main system class providing:
- Item management methods
- Rental operation handling
- Transaction processing
- Data persistence
- System state management

## Usage Examples

### Basic Operations

```python
from lejting import LejTingSystem

# Create system instance
system = LejTingSystem()

# Add rental items
system.add_item("BIKE001", "Mountain Bike", 50.0, "High-quality mountain bike")
system.add_item("CAR001", "Compact Car", 300.0, "Fuel-efficient city car")

# List available items
system.list_items(available_only=True)

# Rent an item
transaction_id = system.rent_item("BIKE001", "Anna Nielsen", 3)

# Return an item
system.return_item("BIKE001")

# Save data
system.save_data("my_rental_data.json")
```

### Interactive CLI Commands

The interactive CLI provides these options:
1. List all items
2. List available items only
3. Add new item
4. Remove item
5. Rent item
6. Return item
7. View item details
8. List transactions
9. List active transactions
10. Save data
11. Load data
0. Exit

## File Structure

```
├── lejting.py          # Core system implementation
├── lejting_cli.py      # Interactive command-line interface
├── test_lejting.py     # Comprehensive test suite
├── README.md           # This documentation
└── lejting_data.json   # Data persistence file (created when saving)
```

## Testing

The system includes comprehensive tests covering:
- Unit tests for individual classes
- Integration tests for complete workflows
- Error handling validation
- Data persistence testing

Run all tests:
```bash
python3 test_lejting.py
```

## Sample Data

The demo mode includes sample rental items:
- **Mountain Bike** (50 kr/day) - High-quality mountain bike for outdoor adventures
- **Compact Car** (300 kr/day) - Fuel-efficient compact car for city driving
- **Camping Tent** (25 kr/day) - 4-person camping tent, waterproof
- **Power Drill Set** (75 kr/day) - Professional power drill with accessories

## Data Format

The system saves data in JSON format with the following structure:
```json
{
  "items": {
    "ITEM_ID": {
      "item_id": "ITEM_ID",
      "name": "Item Name",
      "daily_rate": 50.0,
      "description": "Item description",
      "is_available": true,
      "rented_by": null,
      "rental_start": null,
      "rental_end": null
    }
  },
  "transaction_counter": 1
}
```

## Error Handling

The system includes robust error handling for:
- Invalid item IDs
- Duplicate item registration
- Rental of unavailable items
- Invalid rental periods
- File I/O operations
- User input validation

## Future Enhancements

Potential improvements for future versions:
- Web-based user interface
- Database integration
- Advanced reporting features
- Multiple location support
- Payment processing integration
- Customer management system
- Email notifications
- Mobile application

## Assignment Requirements

This implementation fulfills the requirements for "Obligatorisk opgave 1 INNT" by providing:
- Complete rental management functionality
- Object-oriented design with proper class structure
- Data persistence and retrieval
- User interaction capabilities
- Comprehensive testing
- Detailed documentation
- Error handling and validation

## License

This project is created for educational purposes as part of INNT coursework.
