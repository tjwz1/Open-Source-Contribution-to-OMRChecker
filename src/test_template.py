import unittest
from unittest.mock import MagicMock
from src.template import Template 

class TestFillOutputColumns(unittest.TestCase):

    def setUp(self):
        """Set up a minimal Template instance with required attributes only."""
        self.template = Template.__new__(Template)  # Bypass __init__

        # Manually set necessary attributes
        self.template.output_columns_array = []  # Used in CUSTOM sorting
        self.template.output_columns = []

    def test_alphabetical_sorting(self):
        """Test ALPHABETICAL sorting in ascending order."""
        self.template.sort_type = "ALPHABETICAL"
        self.template.sort_order = "ASC"

        non_custom = ["Zebra", "apple", "banana"]
        custom = ["mango", "Cherry"]

        self.template.fill_output_columns(non_custom, custom)

        expected_output = ["apple", "banana", "Cherry", "mango", "Zebra"]
        self.assertEqual(self.template.output_columns, expected_output)

    def test_alphanumeric_sorting(self):
        """Test ALPHANUMERIC sorting in ascending order."""
        self.template.sort_type = "ALPHANUMERIC"
        self.template.sort_order = "ASC"

        def custom_sort_output_columns(value):
            return int(''.join(filter(str.isdigit, value))) if any(char.isdigit() for char in value) else value

        self.template.fill_output_columns(["item10", "item2", "item1"], ["item3", "item20"])

        expected_output = ["item1", "item2", "item3", "item10", "item20"]
        self.assertEqual(self.template.output_columns, expected_output)

    def test_custom_sorting(self):
        """Test CUSTOM sorting based on predefined order."""
        self.template.sort_type = "CUSTOM"
        self.template.sort_order = "ASC"
        self.template.output_columns_array = ["banana", "Cherry", "apple", "Zebra", "mango"]

        non_custom = ["Zebra", "apple", "banana"]
        custom = ["mango", "Cherry"]

        self.template.fill_output_columns(non_custom, custom)

        expected_output = ["banana", "Cherry", "apple", "Zebra", "mango"]
        self.assertEqual(self.template.output_columns, expected_output)

    def test_sort_order_desc(self):
        """Test ALPHABETICAL sorting in descending order."""
        self.template.sort_type = "ALPHABETICAL"
        self.template.sort_order = "DESC"

        non_custom = ["Zebra", "apple", "banana"]
        custom = ["mango", "Cherry"]

        self.template.fill_output_columns(non_custom, custom)

        expected_output = ["Zebra", "mango", "Cherry", "banana", "apple"]
        self.assertEqual(self.template.output_columns, expected_output)

if __name__ == "__main__":
    unittest.main()
