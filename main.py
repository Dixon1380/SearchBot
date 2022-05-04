import pyautogui
import time
from googlesearchbot_config import url, icon_positions
from googlesearchbot_config import keyboard_duration, mouse_duration

is_search_complete = False
#DO NOT modify these function
def get_current_mouse_pos():
    return pyautogui.position()

def left_click():
    pyautogui.leftClick()

def enter():
    pyautogui.press('enter')

def double_click():
    # pyautogui.click(click= 2, button='left')
    pyautogui.doubleClick(button='left')

def type(text):
    pyautogui.typewrite(text, keyboard_duration)

#Only modify this function if you are having issues with the time.sleep function
def search():
    time.sleep(3)
    type(search_input)
    enter()

#Modify this function and add as many browsers to this functions
def open_browser(browser_choice):
    time.sleep(2)
    print("Searching now......")
    try:
        if get_current_mouse_pos() != icon_positions[browser_choice]:
            pyautogui.moveTo(icon_positions[browser_choice][0], icon_positions[browser_choice][1],mouse_duration)
            double_click()
    #move mouse to address bar to type url
            pyautogui.moveTo(319, 80, mouse_duration)
            left_click()
            type(url)
            enter()
        elif get_current_mouse_pos() == icon_positions[browser_choice]:
            double_click()
            pyautogui.moveTo(319, 80, mouse_duration)
            left_click()
            type(url)
            enter()
        else:
            print("The browser_choice you selected doesn't not have a position.")
    except:
        print("An error has occured: Must type the browser selection as prompted.")
        browser_choice = input("Type 'Chrome' for Chrome, 'Firefox' for Firefox or 'Edge' for Edge: ")
        #open_browser(browser_choice)


#Takes your search input as a string
search_input = input("What do you want to search for?: ")
#Takes your choice as a string and pass it into "icon_positions"
browser_choice = input("Type 'Chrome' for Chrome, 'Firefox' for Firefox or 'Edge' for Edge: ")


while not is_search_complete:
    open_browser(browser_choice)
    search()
    is_search_complete = True
print("Your search has been completed.")