from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from datetime import datetime as dt
import winsound

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
try_again = True

driver.get("https://bmvs.onlineappointmentscheduling.net.au/oasis/Search.aspx")
input_id = driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$txtHAPID")
input_id.send_keys("Replace it with your HAP ID")

input_given_name = driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$txtFirstName")
input_given_name.send_keys("Replace it with your given name")

input_family_name = driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$txtSurname")
input_family_name.send_keys("Replace it with your surname")

input_dob = driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$txtDOB")
input_dob.send_keys("Replace it with your DOB")

time.sleep(1)
search_button = driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$btnSearch")
search_button.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_repAppointments_divButton2_0"))
)

time.sleep(1)
modify_date = driver.find_element(By.ID, "ContentPlaceHolder1_repAppointments_divButton2_0")
modify_date.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_btnCont" ))
)

next_button = driver.find_element(By.ID, "ContentPlaceHolder1_btnCont")
next_button.click()

while try_again:
    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, '//button[@data-val="0"]'))
        )
        earliest_date = driver.find_element(By.XPATH, '//button[@data-val="0"]')
        earliest_date = earliest_date.get_attribute("data-value")
        # pywhatkit.sendwhatmsg_instantly(phone, "testing")
        # print("Testing")
        if dt.strptime(earliest_date, "%d/%m/%Y") >= dt.strptime("2024-02-07", "%Y-%m-%d") :
            print("no earlier date available")
            time.sleep(7*60)
            driver.refresh()
            
        elif dt.strptime(earliest_date, "%d/%m/%Y") < dt.strptime("2024-02-07", "%Y-%m-%d"): 
            print("Earlier date available!")
            try_again = False
            winsound.MessageBeep()
            # pywhatkit.sendwhatmsg_instantly(phone, msg)
            time.sleep(60*5)
            
            print("Msg send successfully!")
    except TimeoutException:
        print ("no available time")
        time.sleep(7*60)
        driver.refresh()

time.sleep(10)

driver.quit()