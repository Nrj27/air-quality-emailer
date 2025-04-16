import unittest
from aq_report.reader import read_measurement

class TestReader(unittest.TestCase):
    
    def test_read_measurement(self):
        # Example of mock data for testing purposes
        test_data = {
            "timestamp": "2025-04-16T09:15:00",
            "co2_ppm": 400,
            "humidity_RH": 45.3,
            "pm01_ugm3": 5.6,
            "pm10_ugm3": 12.7,
            "pm25_ugm3": 7.8,
            "temperature_C": 22.5,
            "voc_ppb": 100
        }
        
        result = read_measurement('W')  # Call function for a specific drive
        expected_result = [
            "16/04/25 09:15", "5.6", "7.8", "12.7", "100", "400", "45.3", "22.5"
        ]
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
