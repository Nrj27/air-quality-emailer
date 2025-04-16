import unittest
from unittest.mock import patch
from aq_report.emailer import send_email

class TestEmailer(unittest.TestCase):
    
    @patch("smtplib.SMTP")
    def test_send_email(self, MockSMTP):
        mock_smtp = MockSMTP.return_value
        html_content = "<html><body><h2>Test Email</h2></body></html>"
        send_email(html_content)  # Test email sending
        mock_smtp.send_message.assert_called_once()  # Ensure send_message was called

if __name__ == "__main__":
    unittest.main()
