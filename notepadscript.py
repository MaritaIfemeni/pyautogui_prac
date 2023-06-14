import pyautogui
import time
import pygetwindow as gw
#import datetime

# Find the application window
app_window = gw.getWindowsWithTitle("AssisDent")[0]
time.sleep(5)

# Activate the application window
app_window.activate()

# Find time block
select_time_block = 'time_block.png'
select_time_block_location = pyautogui.locateCenterOnScreen(select_time_block)

if select_time_block_location is not None:
    pyautogui.rightClick(select_time_block_location)
    time.sleep(2)
else:
    print("Time block not found on the screen.")

# Open customer from the time block
open_customer = 'open_customer.png'
open_customer_location = pyautogui.locateCenterOnScreen(open_customer)

if open_customer_location is not None:
    pyautogui.click(open_customer_location)
    time.sleep(3)
else:
    print("Open customer not found on the screen.")

print("All the code has been run")

# # Task 1
# # open chrome
# pyautogui.press('win')
# pyautogui.typewrite('chrome')
# pyautogui.press('enter')

# time.sleep(4)

# # Find and click the link using image recognition
# guest_user_image = 'guest_user_link.png'
# guest_user_location = pyautogui.locateCenterOnScreen(guest_user_image)

# if guest_user_location is not None:
#     pyautogui.click(guest_user_location)
#     time.sleep(2)
# else:
#     print("Guest User link not found on the screen.")

# # type url to the browser
# pyautogui.typewrite('https://www.google.com')
# pyautogui.press('enter')
# time.sleep(2)
# print("URL typed successfully.")

# # Task 2
# # check what date it is today
# curent_date = datetime.datetime.now()
# yesterday = curent_date - datetime.timedelta(days=1)
# print(yesterday.strftime("%d/%m/%Y"))

# # open notepad
# pyautogui.press('win')
# pyautogui.typewrite('notepad')
# pyautogui.press('enter')
# time.sleep(4)
# pyautogui.typewrite(yesterday.strftime("%d/%m/%Y"))
# time.sleep(4)

# # # Save the file
# pyautogui.hotkey('ctrl', 's')
# time.sleep(3)  # Wait for the save dialog to open

# # # Type the file name and save
# filename = yesterday.strftime("%d/%m/%Y") + 'my text file'
# pyautogui.typewrite(filename)
# pyautogui.press('enter')
# time.sleep(2)

# # # Close Notepad
# pyautogui.hotkey('alt', 'f4')
