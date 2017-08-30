# Headphone_Tester
This is an android app to test out your Bluetooth headphones

Required Downloads 
-------------------
<br> http://vpython.org/contents/download_windows.html                  - Link to python 2.7 and vPython (get both in 32 bit, vPython is optional)
<br> http://www.pygame.org/download.shtml                               - Pygame 1.9.1 (get the one that says pygame-1.9.1.win32-py2.7.msi) 
<br> http://www.oracle.com/technetwork/java/javase/downloads/index.html - JDK (Java Development Kit) 
<br> https://github.com/renpytom/rapt-pygame-example                    - RAPT (download the Step 2 file, the .zip they mention)
<br> Android SDK link included in the RAPT instructions 

Usage
------
<br> Write your script using pygame 
<br> Go into the command prompt and cd your way to the RAPT folder
<br> Type:
<br>    python android.py configure ***folder name***
<br> Replace ***folder name*** with the name of the folder 
<br> Answer the questions (sample questions included in the RAPT github link) 
<br> Type:
<br>     python android.py --launch build ***folder name***  release
<br> Get your .apk from the bin folder and test it out on your phone! 

NOTE:
------
<br> A lot of guides say to use the android library for mapping keys or whatever
<br> DON"T DO IT IF YOU"RE USING THESE LINKS HERE
<br> There is no android library for this version of RAPT.  Here is an example of how to manage key inputs:
<br> https://github.com/renpytom/rapt-pygame-example/blob/master/main.py 

Debugging
---------
<br> From your phone enable Debugging mode (see link below)
<br> Plug it into your comp. 
<br> Navigate to the rapt/android-sdk ######.##>.#>#/platform-tools folder
<br> type:
<br>     adb devices 
<br> to see if your device is there
<br> type:
<br>     adb logcat
<br> to start viewing your phone's logs
<br> Run the app and when it crashes hit ctrl + c to stop logging
<br> Scroll up and look for the python lines showing the error 
<br> 
<br> https://www.kingoapp.com/root-tutorials/how-to-enable-usb-debugging-mode-on-android.htm     - Debug mode on Android
