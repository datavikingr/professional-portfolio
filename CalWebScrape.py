#!python3

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time, webbrowser, pyautogui, cv2, os, corelib, creds

# INIT #
#####################################################
# credentials stuff to login with
keyshift = input("Passkey: ") #HINT Speak 'dead' and enter
cryptuser = creds.calwebuser
cryptpass = creds.calwebpass
username = creds.caesar_decrypt(cryptuser, int(keyshift))
password = creds.caesar_decrypt(cryptpass, int(keyshift))
# Selenium driver init to control Chrome
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
prefs = {"profile.default_content_settings.popups": 0,
         "download.default_directory": r"C:\Users\ahaskins\Documents\PE Drive\Fortive\TEK-Quality Compliance - Documents\Reports\2024 ENV\Backend\CalWeb Lists\\", #IMPORTANT - ENDING SLASH V IMPORTANT
         "directory_upgrade": True,
         "download.prompt_for_download": True}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
# Let's set up for simple logging
logFileDirectory = r"C:\\Users\\ahaskins\\Documents\\PE Drive\\Fortive\\TEK-Quality Compliance - Documents\\Reports\\2024 ENV\\Backend\\Logs\\"
todayDate = datetime.now() # Get today's date
formattedDate = todayDate.strftime('%Y%m%d%H%M') # Format the date as YYYYMMDD with zero-padding
logFileName = f"{formattedDate}_logfile.txt" # Create a log file name with the formatted date
logFilePath = logFileDirectory + logFileName
# And then some various odds and ends we need later
assetfilepath = r".\\assets\\CalWeb\\"
typespeed = 0.15 # 0.35 was too slow.
listyears = ["2023", "2022", "2021", "2020", "2019", "2018"]
labList = {
    "000001": "Tektronix Baltimore",
    "000004": "Tektronix Dallas",
    #000005/Houston: records-ISH
    "000006": "Tektronix Charlotte",
    #000007/Kansas City: records
    #000008/Tulsa: consolidated to 000004/Dallas
    "000010": "Tektronix Waukesha",
    "000012": "Tektronix Seattle",
    #000013/Pittsburgh: consolidated to 000029/Billerica
    "000019": "Tektronix Strother",
    "000021": "Tektronix Andover",
    "000022": "Tektronix Danbury",
    #000024/Crestview: records
    "000026": "Tektronix Anemometers",
    "000027": "Tektronix Toronto",
    "000028": "Tektronix Phoenix",
    "000029": "Tektronix Billerica",
    "000031": "Tektronix Denver",
    "000032": "Tektronix Los Angeles",
    #000034/Orlando consolidated to 000065/Duluth
    "000038": "Tektronix Toronto Honeywell",
    "000041": "Tektronix Beckman Miami",
    "000043": "Tektronix Beaverton - MVS",
    "000044": "Tektronix Keithley Primary", 
    "000049": "Tektronix Beckman Brea",
    "000052": "Tektronix IEI",
    #000053/Buffalo: records 
    "000056": "Tektronix Denver BCTPOS",
    "000057": "Tektronix Draeger",
    "000058": "Tektronix Murrysville",#This is Philips Murrysville
    "000062": "Tektronix Chicago",
    "000063": "Tektronix Cincinnati",
    "000065": "Tektronix Duluth",
    "000066": "Tektronix Commscope",
    "000068": "Tektronix Santa Clara",
    #000071/Alcatel: records
    "000073": "Tektronix SLC",
    #000074/UTAS Phoenix: records
    "000076": "Tektronix Minneapolis",
    "000078": "Tektronix L3 Power Paragon",
    #000080/PT Billerica: records
    #000081/PT Wayne: records
    "000082": "Tektronix Bayer Pittsburgh",
    "000083": "Tektronix Ottowa Honeywell",
    "000084": "Tektronix Erie",
    "000087": "Tektronix TI Dallas", #TI-87? I see what y'all did there. 
    "30-00015": "Tektronix Austin",
    "77186-MSO": "Tektronix Mobile Service Operations"
}

# CalWeb Set Up #
#####################################################
print(f"Initializing run on {formattedDate}.")
driver.get("http://calweb.tek.com//#!/") #init chrome
wait = WebDriverWait(driver, timeout=30, poll_frequency=0.5) #NOTE this is for `= wait.until(EC.presence_of_element_located(By.ID, "foobar"))`
# log in
userLoginField = driver.find_element(By.ID, "Username")
userLoginField.send_keys(username)
passwordLoginField = driver.find_element(By.ID, "Password")
passwordLoginField.send_keys(password)
time.sleep(typespeed)
time.sleep(3) #Let's see if this helps click the button every time.
loginButton = driver.find_element(By.NAME, "Submit")
loginButton.click()
time.sleep(3)
# quick search; placed outside the loop below, because the loop handles the other version of this button down at the end the loop. Why are there two? Because Tektronix developers have no idea what they're doing, that's why.
quickSearchButton = wait.until(EC.element_to_be_clickable((By.ID, "quicksearch"))) # Gotta make sure the button exists 
quickSearchButton.click() # click it
time.sleep(2) # Selenium moves so fast for this Java-based schlock-show; gotta get it to breathe a little

# CalWeb Lab Data Loop; now reporting log files! #
#####################################################
with open(logFilePath, 'w') as logfile:
    logfile.write(f"Initialized run on {formattedDate}.\n\n") # init log file
    startRunTime = datetime.now() # Get timestamp for RUN start
    for labnumber in labList.keys(): # loop through the labs found in labList{}, starting with 000001
        startLabTime = datetime.now() # Get timestamp for LAB start
        formattedLabStartTime = startLabTime.strftime('%Y%m%d%H%M') # formatted for log/console output
        print(f"{formattedLabStartTime} - {labnumber}: ", end=' ') # debugging string with pretty single-line console output.
        customerNumberField = wait.until(EC.presence_of_element_located((By.ID, "customerNumber"))) #gotta find the customer number field to dump lab numbers into
        customerNumberField.send_keys(labnumber) # send it
        time.sleep(typespeed) # brief wait because Java
        customerNumberField.send_keys(Keys.ENTER)
        time.sleep(5) # 2 seconds was too fast.
    # My old pyautogui hyjinks, because nothing ever works right in this shitty company and Selenium + their Angular framework = don't work
        assetfile = os.path.join(assetfilepath, 'custnum2.png') #this is column header on the bottom of the page
        corelib.tryfind(assetfile, 20, 87) # clicks the approximate position of the first entry in the list; Works deecently
        time.sleep(typespeed) # brief wait because Java
        assetfile = os.path.join(assetfilepath, 'dashboards2.png') #dashboards button, pretty clear
        corelib.tryfind(assetfile, 10, 10) #clicks dashboard button
        time.sleep(typespeed) # brief wait because Java
        assetfile = os.path.join(assetfilepath, 'year3.png')
        corelib.tryfind(assetfile, 100, 5) # finds input box for years in listyears
        for year in listyears: #dumps 2023-2018 into the box so we have 100% of the OOTs required, because CalWeb is more than a little out of pocket sometimes.
            pyautogui.write(year, typespeed) #writes the year
            time.sleep(typespeed) #typing speed wait because Java
            pyautogui.write('\n') #this is simply pressing enter
            time.sleep(typespeed) #typing speed wait because Java
        time.sleep(0.5)
        assetfile = os.path.join(assetfilepath, 'total.PNG') # Selenium find(By.XPATH) was an abysmal failure, reverting.
        corelib.tryfind(assetfile, 15, 5) # Opens Total-OOT list
    # Pyautogui method for the rows reported up to 1500, so we can get everything in one file download
        time.sleep(5) # let the itemsinlist.png positioning settle, so I don't misclick when the UI moves again.
        assetfile = os.path.join(assetfilepath, 'itemsinlist.png') # this sets up the line below, similar to the XPath business above.
        corelib.tryfind(assetfile, 10, 5) # finding and clicking the display rows box, so we can set it.
        time.sleep(typespeed) # opens dropdown
        pyautogui.write('1500', typespeed) # set it
        time.sleep(typespeed) # brief wait because java
        pyautogui.write('\n') # hit enter
        time.sleep(30) #omg let it load, because holy shit this front end sucks. 20 seconds worked on the old version of this.
    # Click on the Download button then Save As
        assetfile = os.path.join(assetfilepath, 'download.png')
        corelib.tryfind(assetfile, 20, 5) # opens Save As Dialog
        time.sleep(typespeed)
    # Open & max Save As dialog box; save the file
        corelib.tryMaximizeWindow('Save As') #make it big, so we know where to click; presumes 1920x1080 screen resolution
        time.sleep(1)
        if labnumber == "000001":
            pyautogui.click(1350,50) # pyautogui is weird about the y axis. Places 0 in a bloody weird position. Hence this bloody weird number.
            time.sleep(typespeed) # brief wait because letters getting dropped here is the absolute worst possible scenario for the script
            pyautogui.write(r'C:\Users\ahaskins\Documents\PE Drive\Fortive\TEK-Quality Compliance - Documents\Reports\2024 ENV\Backend\CalWeb Lists', typespeed) #this is where we're saving this
            time.sleep(typespeed) # brief wait because letters getting dropped here is the absolute worst possible scenario for the script
            pyautogui.write('\n') # press enter to actually pull up the correct folder in the dialog box, because bloody windows problems.
            time.sleep(typespeed)
            pyautogui.click(235,935) #click back into the filename field
        time.sleep(2)
    # File name; easy-peasy
        OOTfilename = labnumber + ".xlsx" # simple enough naming convention results in '000001.xlsx' etc
        pyautogui.write(OOTfilename, typespeed) # send it
        time.sleep(typespeed) #brief wait
        pyautogui.write('\n') # press enter
        time.sleep(typespeed) #brief wait
        pyautogui.write('y') #would you liek to overwrite? Yes, I would, that's the point.
    # That should close the dialog box; Setting up for the next lab-entry
        assetfile = os.path.join(assetfilepath, 'Account.png') # find the Accounts button
        corelib.tryfind(assetfile, 5, 5) # try/find to click it; see corelib for more details
        pyautogui.click() # gonna click it again. I could make the above a hover instead, but this accomplishes the same goal: reveal Quick Search
        time.sleep(0.5) # brief wait
        assetfile = os.path.join(assetfilepath, 'quicksearchfromdrawer.png') # find the different Quick Search button (I dunno why it's different either)
        corelib.tryhoverandclick(assetfile, 5, 5) #this'll get the mouse over the QS button and click it, so we can proceed to the next lab in the list.
        endLabTime = datetime.now()
        formattedLabEndTime = endLabTime.strftime('%Y%m%d%H%M')
        deltaLabTime = endLabTime - startLabTime
        labDuration = round(deltaLabTime.total_seconds() / 60, 2) # Convert duration to hundredths of a minute
        print(f"\033[92mSuccess!\033[0m Completed in {labDuration} minutes.") # console output for debugging. Shows up green.
        logfile.write(f"{formattedLabStartTime} - {labnumber}: Completed in {labDuration} minutes.\n") # write timestamp, lab #, status to log file.
    logfile.write("\n\n")
    endRunTime = datetime.now()
    deltaRunTime = endRunTime - startRunTime
    runDuration = round(deltaRunTime.total_seconds() / 60, 2) # Convert duration to hundredths of a minute
    logfile.write(f"Run completed in {runDuration} minutes.\n\n")
# Real talk, that should be enough for the loop to continue on with the next lab.
time.sleep(5) # give that last download a moment to settle before we shut Chrome down.
driver.close() # close the window, so Chrome doesn't eat our RAM
driver.quit() # close the Chrome-controller-driver itself, so it doesn't eat our CPU

#TODO Openpyxl Data Processing Time#
#####################################################
