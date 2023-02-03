#!python3
# written by Alex Haskins, 2022
# This scrapes Calweb for US-MVS OOT data in Tek SSO. These data are collated in Excel for PowerBI integration.

# Libraries
from bs4 import BeautifulSoup
from selenium import webdriver
from autoselenium import Driver, download_driver
from selenium.webdriver.common.keys import Keys
import time, pyautogui, cv2

# INIT
varuser = input('CalWeb username: ')
varpass = input('CalWeb password: ')

listyears = ["2022", "2021", "2020", "2019", "2018"]
dictlablist = {
    "000001": "false",
    "000004": "false",
    "000005": "false",
    "000006": "false",
    "000008": "false",
    "000010": "false",
    "000012": "false",
    "000013": "false",
    "000019": "false",
    "000022": "false",
    "000026": "false",
    "000027": "false",
    "000028": "false",
    "000029": "false",
    "000031": "false",
    "000032": "false",
    "000034": "false",
    "000037": "false",
    "000038": "false",
    "000041": "false",
    "000043": "false",
    "000049": "false",
    "000052": "false",
    "000055": "false",
    "000056": "false",
    "000057": "false",
    "000058": "false",
    "000061": "false",
    "000062": "false",
    "000063": "false",
    "000065": "false",
    "000066": "false",
    "000068": "false",
    "000073": "false",
    "000076": "false",
    "000078": "false",
    "000082": "false",
    "000083": "false",
    "000084": "false",
    "000086": "false",
    "30-00015": "false",
    "686747-S": "false",
    "77186-MSO": "false"
}

download_driver('chrome', version='108.0.5359.71')
for labnum in dictlablist.keys():
    with Driver('chrome') as driver:
        driver.get('https://calweb.tek.com/#!/')
        time.sleep(3)
        while True: #inpusername = driver.find_element_by_id('Username')
            try:
                inpusername = driver.find_element_by_id('Username')
            except:
                time.sleep(1)
                continue
            else:
                inpusername.send_keys(varuser)
                break
        time.sleep(.5)
        while True:
            try:
                inppassword = driver.find_element_by_id('Password')
            except:
                time.sleep(1)
                continue
            else:
                inppassword.send_keys(varpass)
                break
        time.sleep(1)
        while True:
            try:
                inplogin = driver.find_element_by_xpath('/html/body/div[2]/div/form/div/div/div/div/div[3]/div/div/div[4]/div/div/button')
            except:
                time.sleep(1)
                continue
            else:
                inplogin.click()
                break
        time.sleep(.5)
        # Page 2 
        while True: #inpqs = driver.find_element_by_id('quicksearch')
            try:
                inpqs = driver.find_element_by_id('quicksearch')
            except:
                time.sleep(1)
                continue
            else:
                inpqs.click()
                break
        # Page 3
        while True: #inpcustnum = driver.find_element_by_id('customerNumber')
            try:
                inpcustnum = driver.find_element_by_id('customerNumber')
            except:
                time.sleep(1)
                continue
            else:
                inpcustnum.send_keys(labnum)
                time.sleep(.5)
                inpcustnum.send_keys(Keys.ENTER)
                break
        time.sleep(1)
        while True: #lablink = driver.find_element_by_link_text(labnum)
            try:
                lablink = driver.find_element_by_link_text(labnum)
            except:
                time.sleep(1)
                continue
            else:
                lablink.click()
                break
        
        # Page 4
        while True: #buttdashboards = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/button[1]')
            try:
                if labnum == "686747-S":
                    buttdashboards = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/button[7]')
                else:    
                    buttdashboards = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/button[1]')
            except:
                time.sleep(1)
                continue
            else:
                buttdashboards.click()
                break

        # Page 5 - lab link check is first to ensure the page loaded, before proceeding.
        while True: #lablink = driver.find_element_by_link_text('Total OOT Events')
            try:
                lablink = driver.find_element_by_link_text('Total OOT Events')
            except:
                time.sleep(1)
                continue
            else:
                yearbox = driver.find_element_by_xpath('//*[@id="ootyear_taglist"]/input')
                time.sleep(1)
                for yearnum in listyears: #send_keys(yearnum) & Keys.ENTER
                    yearbox.send_keys(yearnum)
                    time.sleep(1)
                    yearbox.send_keys(Keys.ENTER)
                    time.sleep(1)
                time.sleep(10) #the long wait is simply required; else the db won't report back enough info.
                lablink = driver.find_element_by_link_text('Total OOT Events')
                lablink.click()
                break
        
        # Page 6 - getting into the actual data, finally.
        time.sleep(5)
        while True: #displaybox = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[4]/span[1]/span')
            try:
                displaybox = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[4]/span[1]/span')
            except:
                time.sleep(1)
                continue
            else:
                displaybox.click() #Pulls out the dropdown, so we can look with our special-OCR eyes what's inside.
                time.sleep(.5)
                displaybox.send_keys('1500')
                time.sleep(.5)
                displaybox.send_keys(Keys.ENTER)
                break
        time.sleep(10)
        while True:
            try:
                downloadbutt = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[1]/div/a[2]')
            except:
                time.sleep(1)
                continue
            else:
                break
        downloadbutt.click()
        time.sleep(1)
        if labnum == "000001":
            pyautogui.click(1350,50)
            time.sleep(.5)
            pyautogui.write('D:\PE Share Drive\Fortive\TEK-Operations-TechnicalOperations-PE - Documents\Reports\Backend Data\CalWeb Pulls', 0.1)
            pyautogui.write('\n')
            time.sleep(1)
            pyautogui.click(235,935)
            time.sleep(1)
        OOTfilename = labnum + ' OOT List.xlsx'
        pyautogui.write(OOTfilename, 0.1)
        time.sleep(.5)
        pyautogui.write('\n')
        time.sleep(1)
        pyautogui.write('y')
        time.sleep(2)
