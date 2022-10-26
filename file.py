import random
import os
import fontstyle
from datetime import date


os.system("cls")

intro = fontstyle.apply("Hi user.\nI am PARTH.\nPARTH stands for 'Personal Artificial Rocking and Trustworthy Helper'.\nI am a text based program made by Mr Krishna Anand.", "bold/white/italic")

computer_specifications = fontstyle.apply("Device name: DESKTOP-11U57QR\n Processor: Intel(R) Core(TM) i7 -8700 CPU @ 3.20GHz 3.19 GHz\nnstalled RAM: 8.00 GB (Can't tell how much RAM is left)\nDevice ID: 3AE627FF-4915-4BF2-B50D-E992697924F8\nProduct ID: 00330-52236-95497-AAOEM\nSystem type: 64-bit operating system, x64-based processor\nPen and touch: No pen or touch input is available for this display", " blue/bold/underline")


today = date.today()
todate = fontstyle.apply(f"Date: {today.day}-{today.month}-{today.year}", "white/bold")

txt_power_on = fontstyle.apply("Power ON\nActivated PARTH", "green/bold/underline")
power_on = (f"{txt_power_on}\n{intro}\n{todate}")

options = fontstyle.apply("")

 