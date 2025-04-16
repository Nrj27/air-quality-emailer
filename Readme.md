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


Clone the repository:

```
git clone https://github.com/yourusername/air-quality-emailer.git
cd air-quality-emailer
pip install -r requirements.txt
```


Create a virtual environment (optional but recommended):

```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`


```

Install the required dependencies:

```
pip install -r requirements.txt


```
## Configuration
1. Edit the following in `aq_report/emailer.py`:

2. Update ```FROM_EMAIL```,```TO_EMAIL```and ``SMTP server details``

#### 🚀 Install Python and Virtual Environment
Set up a virtual environment (recommended):
Using a virtual environment keeps dependencies isolated from other projects on your system. To set it up:

Navigate to your project folder in the terminal:
```
cd path/to/your/air-quality-emailer
```
Create a virtual environment:
```
python -m venv venv
```
Activate the virtual environment:

>> On Windows:
```
venv\Scripts\activate
```
>>On macOS/Linux:
```
source venv/bin/activate
```
#### 🚀 Install Dependencies
```
pip install -r requirements.txt

```


#### 🚀 Configure the Email Settings

```
FROM_EMAIL = "your-email@example.com"
TO_EMAIL = "recipient-email@example.com"
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587  # For example, 587 is the default for Gmail
SMTP_USER = "your-email@example.com"
SMTP_PASSWORD = "your-email-password"

```
#### 🚀 Create a sample JSON file


#### 🚀 Run the Script

```
python -m aq_report.main
```
Automate it with Task Scheduler on Windows.

#### 🚀 Verify the Email
Check the recipient email inbox for the report. It should contain a color-coded table with the air quality measurements from the devices. If you used mock data for one of the drives, some columns will have a "-" value.


#### 🚀 Automate the Script (Optional)
To automate this task, you can set it up to run periodically using a task scheduler.

**Windows: Task Scheduler :** 
1. Open **Task Scheduler** from the Start menu.
2. Click **Create Task**.
3. Under **General**, provide a name like "Air Quality Email Report".       
4. Under **Triggers**, set the frequency (e.g., daily, weekly).
5. Under **Actions**, click **New** and select **Start a Program**. Browse for `python.exe` and set the path to your `main.py` script in the **"Add arguments"** field.

Example:
```
"C:\path\to\python.exe" "C:\path\to\air-quality-emailer\aq_report\main.py"
```
6 .Save the task, and it will run automatically based on your schedule.


## Roadmap
* Excel-imported AQI thresholds

* Web dashboard support

* Sensor discovery over LAN

* Docker image