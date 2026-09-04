# test_vibeember.py
"""
Tests for VibeEmber module.
"""

import unittest
from vibeember import VibeEmber

class TestVibeEmber(unittest.TestCase):
    """Test cases for VibeEmber class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = VibeEmber()
        self.assertIsInstance(instance, VibeEmber)
        
    def test_run_method(self):
        """Test the run method."""
        instance = VibeEmber()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
