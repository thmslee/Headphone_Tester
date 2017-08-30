# Headphone_Tester
This is an android app to test out your Bluetooth headphones

Required Downloads 
-------------------
http://vpython.org/contents/download_windows.html                  - Link to python 2.7 and vPython (get both in 32 bit, vPython is optional)
http://www.pygame.org/download.shtml                               - Pygame 1.9.1 (get the one that says pygame-1.9.1.win32-py2.7.msi) 
http://www.oracle.com/technetwork/java/javase/downloads/index.html - JDK (Java Development Kit) 
https://github.com/renpytom/rapt-pygame-example                    - RAPT (download the Step 2 file, the .zip they mention)

Usage
------
Write your script using pygame 
Go into the command prompt and cd your way to the RAPT folder
Type:
    python android.py configure <<<<folder name>>>>> 
^ Replace <<<<folder name>>>>> with the name of the folder 
Answer the questions (sample questions included in the RAPT github link) 
Type:
    python android.py --launch build <<<<folder name>>>>>  release
Get your .apk from the bin folder and test it out on your phone! 

NOTE:
------
A lot of guides say to use the android library for mapping keys or whatever
DON"T DO IT IF YOU"RE USING THESE LINKS HERE
There is no android library for this version of RAPT.  Here is an example of how to manage key inputs:
https://github.com/renpytom/rapt-pygame-example/blob/master/main.py 

Debugging
---------
From your phone enable Debugging mode (see link below)
Plug it into your comp. 
Navigate to the rapt/android-sdk ######.##>.#>#/platform-tools folder
type:
    adb devices 
to see if your device is there
type:
    adb logcat
to start viewing your phone's logs
Run the app and when it crashes hit ctrl + c to stop logging
Scroll up and look for the python lines showing the error 

https://www.kingoapp.com/root-tutorials/how-to-enable-usb-debugging-mode-on-android.htm     - Debug mode on Android
