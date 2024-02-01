# Automated Appointment Scheduling Script
## Overview
This Python script automates the process of checking and scheduling visa medical appointments on the BMVS online platform. Given the high demand for visa applications, the earliest available appointment time is often a month later. However, visa applicants must complete their medical check within 28 days after submitting the visa application.

## Project Purpose
The primary aim of this project is to address the challenge of tracking appointment availability on the website regularly. Manual tracking can be cumbersome, and it's easy to forget to refresh the page due to other tasks at hand. This automated solution simplifies the process by regularly checking for available dates, notifying you when an earlier date is found, and allowing you to schedule your visa medical appointment within the required timeframe.

## Prerequisites
Python installed on your machine
Chrome browser installed
Chromedriver executable in the project directory (replace "chromedriver.exe" with the appropriate version for your operating system)

## Installation
Clone the repository:
```
git clone https://github.com/yourusername/automated-appointment-scheduler.git
cd automated-appointment-scheduler
```
Install the required Python packages:
```
pip install selenium
```

Replace the placeholder values in the script:
- Replace **"Replace it with your HAP ID"** with your actual HAP ID.
- Replace **"Replace it with your given name"** with your actual given name.
- Replace **"Replace it with your surname"** with your actual surname.
- Replace **"Replace it with your DOB"** with your actual date of birth.
- Adjust the target date in the script ("2024-02-07") as needed.
  
Run the script:
```
python main.py
```
### Notes
The script uses the Chrome browser and requires the Chromedriver executable. Make sure to update it based on your operating system.

Ensure that you have a stable internet connection for the script to work correctly.

The script will notify you with a beep sound and a console message when an earlier date is available. You can customize the notification method according to your preferences.

