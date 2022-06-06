import pyautogui, time

#Alot to learn... I would like to be able to traverse the websites
# as needed. Unsure if this will be the way to do that though. 
# At the very least, this is pretty interesting :)


 # Moves mouse in a square
 for i in range(10):
     pyautogui.moveTo(100, 100, duration=0.25)
     pyautogui.moveTo(200, 100, duration=0.25)
     pyautogui.moveTo(200, 200, duration=0.25)
     pyautogui.moveTo(100, 200, duration=0.25)

# Waits 5 seconds, then draws a neat rectangle-esque pattern
# time.sleep(5)
# pyautogui.click()    # Click to make the window active.
# distance = 300
# change = 20

# while distance > 0:
#     pyautogui.drag(distance, 0, duration=0.2)   # Move right.
#     distance = distance - change
#     pyautogui.drag(0, distance, duration=0.2)   # Move down.
#     pyautogui.drag(-distance, 0, duration=0.2)  # Move left.
#     distance = distance - change
#     pyautogui.drag(0, -distance, duration=0.2)  # Move up.

#ShutDown PC Script
pyautogui.moveTo(30,1160, duration=.50)
pyautogui.click()
pyautogui.moveTo(970,70, duration=.50)
pyautogui.click()
pyautogui.write("shut")
pyautogui.moveTo(970,125, duration=.50)
pyautogui.click()
pyautogui.moveTo(1100,670, duration=.25)
pyautogui.click()
