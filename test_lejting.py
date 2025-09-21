#!/usr/bin/env python3
"""
LejTing System Tests
Obligatorisk opgave 1 INNT

Basic tests for the LejTing rental management system.
"""

import unittest
from datetime import datetime, timedelta
import os
import tempfile
from lejting import LejTingSystem, RentalItem


class TestRentalItem(unittest.TestCase):
    """Test cases for RentalItem class."""
    
    def test_rental_item_creation(self):
        """Test creating a rental item."""
        item = RentalItem("TEST001", "Test Item", 50.0, "Test description")
        
        self.assertEqual(item.item_id, "TEST001")
        self.assertEqual(item.name, "Test Item")
        self.assertEqual(item.daily_rate, 50.0)
        self.assertEqual(item.description, "Test description")
        self.assertTrue(item.is_available)
        self.assertIsNone(item.rented_by)
    
    def test_rental_item_string_representation(self):
        """Test string representation of rental item."""
        item = RentalItem("TEST001", "Test Item", 50.0)
        expected = "Item: Test Item (ID: TEST001) - 50.0 kr/day - Available"
        self.assertEqual(str(item), expected)
    
    def test_rental_item_to_dict(self):
        """Test converting rental item to dictionary."""
        item = RentalItem("TEST001", "Test Item", 50.0, "Test description")
        item_dict = item.to_dict()
        
        self.assertEqual(item_dict['item_id'], "TEST001")
        self.assertEqual(item_dict['name'], "Test Item")
        self.assertEqual(item_dict['daily_rate'], 50.0)
        self.assertEqual(item_dict['description'], "Test description")
        self.assertTrue(item_dict['is_available'])


class TestLejTingSystem(unittest.TestCase):
    """Test cases for LejTingSystem class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.system = LejTingSystem()
    
    def test_add_item(self):
        """Test adding items to the system."""
        result = self.system.add_item("TEST001", "Test Item", 50.0, "Test description")
        
        self.assertTrue(result)
        self.assertIn("TEST001", self.system.items)
        self.assertEqual(self.system.items["TEST001"].name, "Test Item")
    
    def test_add_duplicate_item(self):
        """Test adding duplicate item IDs."""
        self.system.add_item("TEST001", "Test Item", 50.0)
        result = self.system.add_item("TEST001", "Another Item", 75.0)
        
        self.assertFalse(result)
        self.assertEqual(len(self.system.items), 1)
    
    def test_remove_item(self):
        """Test removing items from the system."""
        self.system.add_item("TEST001", "Test Item", 50.0)
        result = self.system.remove_item("TEST001")
        
        self.assertTrue(result)
        self.assertNotIn("TEST001", self.system.items)
    
    def test_remove_nonexistent_item(self):
        """Test removing non-existent item."""
        result = self.system.remove_item("NONEXISTENT")
        self.assertFalse(result)
    
    def test_remove_rented_item(self):
        """Test removing a currently rented item."""
        self.system.add_item("TEST001", "Test Item", 50.0)
        self.system.rent_item("TEST001", "Test Renter", 3)
        result = self.system.remove_item("TEST001")
        
        self.assertFalse(result)
        self.assertIn("TEST001", self.system.items)
    
    def test_rent_item(self):
        """Test renting an item."""
        self.system.add_item("TEST001", "Test Item", 50.0)
        transaction_id = self.system.rent_item("TEST001", "Test Renter", 3)
        
        self.assertIsNotNone(transaction_id)
        self.assertFalse(self.system.items["TEST001"].is_available)
        self.assertEqual(self.system.items["TEST001"].rented_by, "Test Renter")
        self.assertIn(transaction_id, self.system.transactions)
    
    def test_rent_nonexistent_item(self):
        """Test renting non-existent item."""
        result = self.system.rent_item("NONEXISTENT", "Test Renter", 3)
        self.assertIsNone(result)
    
    def test_rent_already_rented_item(self):
        """Test renting an already rented item."""
        self.system.add_item("TEST001", "Test Item", 50.0)
        self.system.rent_item("TEST001", "First Renter", 3)
        result = self.system.rent_item("TEST001", "Second Renter", 2)
        
        self.assertIsNone(result)
    
    def test_rent_item_invalid_days(self):
        """Test renting item with invalid rental period."""
        self.system.add_item("TEST001", "Test Item", 50.0)
        result = self.system.rent_item("TEST001", "Test Renter", 0)
        
        self.assertIsNone(result)
        self.assertTrue(self.system.items["TEST001"].is_available)
    
    def test_return_item(self):
        """Test returning a rented item."""
        self.system.add_item("TEST001", "Test Item", 50.0)
        transaction_id = self.system.rent_item("TEST001", "Test Renter", 3)
        result = self.system.return_item("TEST001")
        
        self.assertTrue(result)
        self.assertTrue(self.system.items["TEST001"].is_available)
        self.assertIsNone(self.system.items["TEST001"].rented_by)
        self.assertTrue(self.system.transactions[transaction_id].is_completed)
    
    def test_return_nonexistent_item(self):
        """Test returning non-existent item."""
        result = self.system.return_item("NONEXISTENT")
        self.assertFalse(result)
    
    def test_return_available_item(self):
        """Test returning an item that isn't rented."""
        self.system.add_item("TEST001", "Test Item", 50.0)
        result = self.system.return_item("TEST001")
        
        self.assertFalse(result)
    
    def test_rental_cost_calculation(self):
        """Test rental cost calculation."""
        self.system.add_item("TEST001", "Test Item", 50.0)
        transaction_id = self.system.rent_item("TEST001", "Test Renter", 3)
        
        transaction = self.system.transactions[transaction_id]
        expected_cost = 50.0 * 3
        self.assertEqual(transaction.total_cost, expected_cost)
    
    def test_save_and_load_data(self):
        """Test saving and loading system data."""
        # Create temporary file
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
            temp_filename = f.name
        
        try:
            # Add some test data
            self.system.add_item("TEST001", "Test Item", 50.0, "Test description")
            self.system.add_item("TEST002", "Another Item", 75.0)
            
            # Save data
            self.system.save_data(temp_filename)
            
            # Create new system and load data
            new_system = LejTingSystem()
            new_system.load_data(temp_filename)
            
            # Verify data was loaded correctly
            self.assertIn("TEST001", new_system.items)
            self.assertIn("TEST002", new_system.items)
            self.assertEqual(new_system.items["TEST001"].name, "Test Item")
            self.assertEqual(new_system.items["TEST001"].daily_rate, 50.0)
            self.assertEqual(new_system.items["TEST002"].daily_rate, 75.0)
        
        finally:
            # Clean up temporary file
            if os.path.exists(temp_filename):
                os.unlink(temp_filename)


class TestIntegration(unittest.TestCase):
    """Integration tests for the complete rental workflow."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.system = LejTingSystem()
    
    def test_complete_rental_workflow(self):
        """Test a complete rental workflow from start to finish."""
        # Add items
        self.system.add_item("BIKE001", "Mountain Bike", 50.0, "High-quality bike")
        self.system.add_item("CAR001", "Compact Car", 300.0, "Fuel-efficient car")
        
        # Check initial state
        self.assertEqual(len(self.system.items), 2)
        self.assertTrue(self.system.items["BIKE001"].is_available)
        self.assertTrue(self.system.items["CAR001"].is_available)
        
        # Rent bike
        bike_transaction = self.system.rent_item("BIKE001", "Anna Nielsen", 3)
        self.assertIsNotNone(bike_transaction)
        self.assertFalse(self.system.items["BIKE001"].is_available)
        
        # Rent car
        car_transaction = self.system.rent_item("CAR001", "Lars Andersen", 2)
        self.assertIsNotNone(car_transaction)
        self.assertFalse(self.system.items["CAR001"].is_available)
        
        # Check that both items are rented
        self.assertEqual(len([item for item in self.system.items.values() if not item.is_available]), 2)
        
        # Return bike
        self.assertTrue(self.system.return_item("BIKE001"))
        self.assertTrue(self.system.items["BIKE001"].is_available)
        self.assertFalse(self.system.items["CAR001"].is_available)
        
        # Verify transaction states
        self.assertTrue(self.system.transactions[bike_transaction].is_completed)
        self.assertFalse(self.system.transactions[car_transaction].is_completed)
        
        # Return car
        self.assertTrue(self.system.return_item("CAR001"))
        self.assertTrue(self.system.items["CAR001"].is_available)
        
        # Check final state
        self.assertEqual(len([item for item in self.system.items.values() if item.is_available]), 2)
        self.assertTrue(all(transaction.is_completed for transaction in self.system.transactions.values()))


def run_tests():
    """Run all tests and display results."""
    print("Running LejTing System Tests...")
    print("=" * 50)
    
    # Discover and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(__import__(__name__))
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "=" * 50)
    if result.wasSuccessful():
        print("All tests passed! ✅")
    else:
        print(f"Tests failed: {len(result.failures)} failures, {len(result.errors)} errors ❌")
    
    return result.wasSuccessful()


if __name__ == "__main__":
    run_tests()