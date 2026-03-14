# test_dataflow.py
"""
Tests for DataFlow module.
"""

import unittest
from dataflow import DataFlow

class TestDataFlow(unittest.TestCase):
    """Test cases for DataFlow class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DataFlow()
        self.assertIsInstance(instance, DataFlow)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DataFlow()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
