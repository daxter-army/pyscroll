# PyScroll
Scroll your screen **up ⬆** & **down ⬇**, with the power of python. Scroll any screen infinite screen of your YouTube, Instagram, Facebook, Netflix & whatever you want.

<img src="./demo.svg" style="width: 50px;" />

## 🏃‍♂️ Demonstration
<p align="center">
<img src="./readme-media/pyscroll-demo-gif.gif" alt="demo-gif"/>
</p>

## 🛠 Requirements
* This piece of code utilizes the following listed python modules to work:
    * **pip install pyautogui** - for emulating the keyclicks on the desired object movement
    * **pip install opencv-python** - opencv for object detection and all that
    * **pip install numpy** - for internal working

## 🏎 Run
* On Windows
```sh
python scroll.py
```

* On Linux/MacOS
```sh
python3 scroll.py
```

* **NOTE** : After running the script, keep the browser tab or concerned screen in focus, which you want to scroll.
* Grab a yellow colored object in your hand, having size atleast half of your palm, and move your hand upwards or downwards, at a decent pace, to scroll up or down, respectively.
*(you can change the color to be detected, by changing the color ranges)*

## 🎨 Color Ranges
* By changing the values of the variable, you can use the color you like to work as trigger, below are some listed for you to experiment:

* Red
    * redLower = np.array([0, 50, 50])
    * redUpper = np.array([10, 255, 255])

* Green
    * greenLower = np.array([36, 25, 25])
    * greenUpper = np.array([70, 255, 255])