# plate
A simple Shanghai plate program written in python

1. The main file is panic_buying/control/main.py
2. The first step is running panic_buying\mouse_key\soft_key.py to get the locations for the numbers(from 0 ~ 9) in the virtual keyboard of Win7.
3. After running, there will be file named softkey.conf.
4. Copy softkey.conf into panic_buying\control
5. Enter the website of Shanghai Plate, Run setConfig.py to get the locations of buttons, input windows, auth code rectangle.
6. Don't move the IE application, run main.py, it will read from the config_file created by setConfig.py.
7. Press "F2" to try it, see if it can work normally.

Reminder: This project depends on python and some libs, need to install these applications: http://pan.baidu.com/s/1eRvNHhK
