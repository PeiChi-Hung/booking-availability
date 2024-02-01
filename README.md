## Automated Appointment Scheduling Script
This Python script utilizes Selenium to automate the process of checking and scheduling appointments on the BMVS online appointment scheduling platform. The script interacts with the website, inputs personal information, and checks for the earliest available appointment date.

### Prerequisites
Python installed on your machine
Chrome browser installed
Chromedriver executable in the project directory (replace "chromedriver.exe" with the appropriate version for your operating system)

### Installation
Clone the repository:

git clone https://github.com/yourusername/automated-appointment-scheduler.git
cd automated-appointment-scheduler
Install the required Python packages:

pip install selenium
Replace the placeholder values in the script:

Replace **"Replace it with your HAP ID"** with your actual HAP ID.
Replace **"Replace it with your given name"** with your actual given name.
Replace **"Replace it with your surname"** with your actual surname.
Replace **"Replace it with your DOB"** with your actual date of birth.
Adjust the target date in the script ("2024-02-07") as needed.
Run the script:
```
```
python main.py
```
```
### Notes
The script uses the Chrome browser and requires the Chromedriver executable. Make sure to update it based on your operating system.

Ensure that you have a stable internet connection for the script to work correctly.

The script will notify you with a beep sound and a console message when an earlier date is available. You can customize the notification method according to your preferences.

