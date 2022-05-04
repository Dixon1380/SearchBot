"""
Google Search Bot configuration file
Free free to configure your search bot to your liking
"""


#Changes the search url for the bot.
#Make sure you know the location for the address of the url  you wish to use before changing this.
url = 'https://google.com'

#Use pyautogui.position() to get the location of your browser icons
#Feel free to add new browsers but make sure you know their icon positions on your desktop
icon_positions = {
    'Chrome': (147, 166),
    'Firefox': (45, 958),
    'Edge': (139, 963)
}

#You can modify if the url position is different
urlbar_position = (319, 80)

#Only modify this if you change the url and need to specify the location of the website searchbar. Default values below:
searchbar_position =(0,0)

#Change the duration to anyway you like. Default values below:
keyboard_duration = 0.15
mouse_duration = 1.0

