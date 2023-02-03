#!python3
# written by Alex Haskins, 2020
# This scrapes Calweb for US-MVS OOT data in Tek SSO. These data are collated in Excel for PowerBI integration.

# Libraries
import webbrowser, pyautogui, time, cv2

# INIT
varuser = input('CalWeb username: ')
varpass = input('CalWeb password: ')
labList = {
    "Baltimore": "000001", 
    "Dallas": "000004",
    "Houston": "000005", 
    "Charlotte": "000006",
    "Tulsa": "000008",
    "Waukesha": "000010",
    "Seattle": "000012",
    "Pittsburgh": "000013",
    "Strother": "000019",
    "Danbury": "000022",
    "Anemometers": "000026",
    "Mississauga": "000027",
    "Phoenix": "000028",
    "Billerica": "000029",
    "Denver": "000031",
    "Covina": "000032",
    "Orlando": "000034",
    "Detroit": "000037",
    "Honeywell Toronto": "000038",
    "Beckman Miami": "000041",
    "Beaverton": "000043",
    "Beckman Brea": "000049",
    "IEI": "000052",
    "Kokomo": "000055",
    "BCTPOS": "000056",
    "Draeger": "000057",
    "Philips Murrysville": "000058",
    "Sayreville": "000061",
    "Chicago": "000062",
    "Cincinnati": "000063",
    "Duluth": "000065",
    "Commscope": "000066",
    "Santa Clara": "000068",
    "SLC": "000073",
    "Minneapolis": "000076",
    "L3 Power Paragon": "000078",
    "Bayer": "000082",
    "Honeywell Ottowa": "000083",
    "GETS Erie": "000084",
    "Albany": "000086",
    "Austin": "30-00015",
    "Second Kokomo": "686747-S",
    "MSO": "77186-MSO"
}

# main loop
for labnumber in labList.values():

    # Open and maximize CalWeb, for standardized mouse positions against the standard 1920x1080 laptop screen
    webbrowser.open('https://calweb.tek.com/#!/')
    time.sleep(20)
    CalWeb = pyautogui.getActiveWindow()
    time.sleep(.1)
    CalWeb.maximize()
    time.sleep(.5)

    # Log in
    userbox = pyautogui.locateOnScreen(r'Assets\username.png', confidence=0.8)
    pyautogui.click(userbox.left, userbox.top + 2)
    time.sleep(.5)
    pyautogui.write(username, 0.1)
    pyautogui.write(['tab'])
    pyautogui.write(password, 0.1)
    pyautogui.write('\n')
    time.sleep(5)

    # Quick search Button
    quickbox = pyautogui.locateOnScreen(r'Assets\quicksearch.png', confidence=0.8)
    pyautogui.click(quickbox.left,quickbox.top)
    time.sleep(2)
    
    # input lab number
    custbox = pyautogui.locateOnScreen(r'Assets\custnum.png', confidence=0.8)
    pyautogui.click(custbox.left + 250, custbox.top + 10)
    time.sleep(.1)
    pyautogui.write(labnumber, 0.1) 
    pyautogui.write('\n')
    time.sleep(2)
    
    # actually select the lab, because this was absolutely genius front-end design
    cust2box = pyautogui.locateOnScreen(r'Assets\custnum2.png', confidence=0.8)
    pyautogui.click(cust2box.left + 30, cust2box.top + 90)
    time.sleep(5)
    
    # find and select the dashboards button - beause, charmingly, they're changing the godsdamned thing, again, AND IT MOVES, AND IS MULTIPLE BUTTONS
    try:
        dashbox = pyautogui.locateOnScreen(r'Assets\dashboards.png', confidence=0.8)
    except:
        dashbox = pyautogui.locateOnScreen(r'Assets\dashboards2.png', confidence=0.8)
    time.sleep(1)
    pyautogui.click(dashbox.left + 10, dashbox.top + 10)
    time.sleep(5)
    
    # Click in the year box of the OOTs dashboard space, input timeframe, open list
    yearbox = pyautogui.locateOnScreen(r'Assets\year2.png', confidence=0.8)
    pyautogui.click(yearbox.left + 100 ,yearbox.top + 5)
    time.sleep(.1)
    # 2022 Grab
    pyautogui.write('2022', 0.1)
    time.sleep(.1)
    pyautogui.write('\n')
    time.sleep(.25)
    # 2021 Grab
    pyautogui.write('2021', 0.1)
    time.sleep(.1)
    pyautogui.write('\n')
    time.sleep(.25)
    # 2020 Grab
    pyautogui.write('2020', 0.1)
    time.sleep(.1)
    pyautogui.write(['down'])
    time.sleep(.1)
    pyautogui.write('\n')
    time.sleep(.25)
    # 2019 Grab
    time.sleep(.1)
    pyautogui.write('2019', 0.1)
    time.sleep(.1)
    pyautogui.write(['down'])
    time.sleep(.1)
    pyautogui.write('\n')
    time.sleep(.25)
    #2018 Grab
    pyautogui.write('2018', 0.1)
    time.sleep(.1)
    pyautogui.write(['down'])
    time.sleep(.1)
    pyautogui.write('\n')
    time.sleep(3)
    
    # This is the old method, grabbing Opens.
    #openbox = pyautogui.locateOnScreen(r'C:\Users\ahaskins\Desktop\OOTScrape\open.png', confidence=0.8)
    #pyautogui.click(openbox.left + 5, openbox.top + 3)
    #time.sleep(20)
    
    # BETA TEST; IF BAD THEN GRAB OPENS INSTEAD
    openbox = pyautogui.locateOnScreen(r'Assets\total.PNG', confidence=0.8)
    pyautogui.click(openbox.left + 15, openbox.top + 5)
    time.sleep(15)
    openbox = pyautogui.locateOnScreen(r'Assets\itemsinlist.png', confidence=0.8)
    pyautogui.click(openbox.left + 10, openbox.top + 5)
    time.sleep(3)
    pyautogui.click(openbox.left + 10, openbox.top - 15)
    #try: # Raw find 1500
    #    openbox = pyautogui.locateOnScreen(r'C:\Users\ahaskins\Desktop\OOTScrape\1500.png')
    #    pyautogui.click(openbox.left + 10, openbox.top + 5)
    #except: # This'll anchor the click to the top of the drop up menu, and go up from there
    #    openbox = pyautogui.locateOnScreen(r'C:\Users\ahaskins\Desktop\OOTScrape\itemsinlist.png', confidence=0.8)
    #    pyautogui.click(openbox.left + 10, openbox.top - 15)
    time.sleep(20)
    
    # Click on the download button, save as
    downloadbox = pyautogui.locateOnScreen(r'Assets\download.png', confidence=0.8)
    time.sleep(.1)
    pyautogui.click(downloadbox.left + 20, downloadbox.top + 5)
    time.sleep(10)
    
    # maximize the Save As window to ensure constant mouse positions
    SaveAs = pyautogui.getWindowsWithTitle('Save As')
    time.sleep(1)
    SaveAs[0].maximize()
    time.sleep(.1)
    
    # Filepath interaction
    pyautogui.click(1350,50)
    time.sleep(.1)
    pyautogui.write('D:\PE Share Drive\Fortive\TEK-Operations-TechnicalOperations-PE - Documents\Reports\Backend Data\CalWeb Pulls', 0.1)
    pyautogui.write('\n')
    time.sleep(.1)
    pyautogui.click(235,935)
    time.sleep(.1)
    OOTfilename = labnumber + ' OOT List.xlsx'
    pyautogui.write(OOTfilename, 0.1)
    time.sleep(.1)
    pyautogui.write('\n')
    time.sleep(1)
    pyautogui.write('y')
    time.sleep(5)
    closetabbox = pyautogui.locateOnScreen(r'Assets\closetab.png')
    time.sleep(.1)
    pyautogui.click(closetabbox.left + 3, closetabbox.top + 3)
    time.sleep(3)
