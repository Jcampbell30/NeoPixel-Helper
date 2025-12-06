# NeoPixel-Helper
A simple how-to on LEDs with Thonny, MicroPython, and NeoPixel.


## How to Build an executable
First setup a virtual environment for your machine

Next, Run pip install -r requirements.txt

Next, Run pyinstaller --onefile --windowed NeoPixel-Helper.py

This command should have generated a 'dist' folder. The folder will contain the .exe file to run on your machine. Create a new folder and stick the exe in it. Navigate to that folder, right click send to -> Desktop (create shortcut).
