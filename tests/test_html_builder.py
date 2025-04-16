import unittest
from aq_report.html_builder import create_html_table

class TestHTMLBuilder(unittest.TestCase):
    
    def test_create_html_table(self):
        # Sample input data
        results = {
            "Office": ["16/04/25 09:15", "5.6", "7.8", "12.7", "100", "400", "45.3", "22.5"],
            "Bedroom": ["16/04/25 09:15", "-", "-", "-", "-", "-", "-", "-"]
        }
        
        html = create_html_table(results)
        self.assertIn("<th>Location</th>", html)  # Check if header is present
        self.assertIn("<td>Office</td>", html)   # Check if office data is included

if __name__ == "__main__":
    unittest.main()

