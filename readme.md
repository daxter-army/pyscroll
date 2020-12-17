# PyScroll
Scroll your screen **up** & **down**, with the power of python. Scroll facebook, instagram, tiktok, pinterest, youtube, anything, any infinite scrolling screen.

## Working
* Grab a yellow colored object in your hand, having size atleast half of your palm's size, and move your hand upwards or downwards, at a decent pace, to scroll up or down, respectively.
*(you can change the color to be detected, by changing the color ranges)*

## Requirements
* **pip install pyautogui** - for emulating the keyclicks on the desired object movement
* **pip install opencv-python** - opencv for object detection and all that
* **pip install numpy** - for internal working

## Run
* *python main.py*
* *note : after running the script, keep the browser tab or respected concerned screen, in focus, in which you want to scroll.*

### color ranges
* redLower = np.array([0, 50, 50])
* redUpper = np.array([10, 255, 255])
* greenLower = np.array([36, 25, 25])
* greenUpper = np.array([70, 255, 255])