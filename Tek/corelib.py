#!python3
import pyautogui, time

def tryfind(findAssetFilePath, leftadj, topadj): # while(try/except) loop to find the image
    i = 0
    findtarget = None
    while True:
        findtarget = pyautogui.locateOnScreen(findAssetFilePath, confidence=0.80)
        try:
            pyautogui.click(findtarget.left + leftadj, findtarget.top + topadj)
        except:
            i += 1
            time.sleep(0.5)
            if i >= 20:
                tryfind(findAssetFilePath, leftadj, topadj)
            continue
        else:
            time.sleep(0.5)
            break
    return

def tryhoverandclick(findAssetFilePath,leftadj, topadj): #while(try/except) loop after finding an image revealed in a hidden drawer
    i = 0
    findtarget = None
    while True:
        findtarget = pyautogui.locateOnScreen(findAssetFilePath, confidence=0.80) #60% literally went sideways - just thought it was funny how bad it missed, and that my guess about it was correct.
        try:
            pyautogui.moveTo(findtarget.left + leftadj, findtarget.top + topadj, duration=0.15)
            time.sleep(0.1)
            pyautogui.click()
        except:
            i += 1
            time.sleep(0.5)
            if i >= 20:
                tryhoverandclick(findAssetFilePath,leftadj, topadj)
            continue
        else:
            time.sleep(0.5)
            break
    return

def tryMaximizeWindow(WindowTitle): # while(try/except) loop to Maximize the window
    targetWindow = None
    while True:
        targetWindow = pyautogui.getWindowsWithTitle(WindowTitle)
        try:
            targetWindow[0].moveTo(0, 0)
        except:
            time.sleep(0.5)
            continue
        else:
            time.sleep(0.5)
            targetWindow[0].maximize()
            break
    return

def tryfinddoubleclick(findAssetFilePath, leftadj, topadj): # while(try/except) loop to find the image
    i = 0
    findtarget = None
    while True:
        findtarget = pyautogui.locateOnScreen(findAssetFilePath, confidence=0.80)
        try:
            pyautogui.click(findtarget.left + leftadj, findtarget.top + topadj)
            time.sleep(0.1)
            pyautogui.click(findtarget.left + leftadj, findtarget.top + topadj)
        except:
            i += 1
            time.sleep(0.5)
            if i >= 20:
                tryfinddoubleclick(findAssetFilePath, leftadj, topadj)
            continue
        else:
            time.sleep(0.5)
            break
    return