# Air Quality Email Reporter 🚀

Monitor air quality from multiple LAN-connected sensors and get daily HTML reports in your inbox!

## Features
✅ Reads JSON stats from up to 4 mapped devices  
✅ Handles missing or offline drives  
✅ Generates clean, color-coded HTML tables  
✅ Sends as an email using any SMTP server  
✅ Easy to automate via Task Scheduler

## Sample Output

![Sample Email](assets/sample_email.png)

## Installation

```bash
git clone https://github.com/yourusername/air-quality-emailer.git
cd air-quality-emailer
pip install -r requirements.txt


Configuration
Edit the following in aq_report/emailer.py:

FROM_EMAIL

TO_EMAIL

SMTP server details

Run It
bash
Copy
Edit
python -m aq_report.main
Automate it with Task Scheduler on Windows.


Run It
bash
Copy
Edit
python -m aq_report.main
Automate it with Task Scheduler on Windows.

Roadmap
 Excel-imported AQI thresholds

 Web dashboard support

 Sensor discovery over LAN

 Docker image