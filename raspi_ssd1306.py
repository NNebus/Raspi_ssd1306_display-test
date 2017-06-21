#!/usr/bin/python
# coding=utf-8
# Python Version 3
# raspi_ssd1306.py
#------------------------------------------------------------
 
# Einbindung der notwendigen Grundbibliotheken
import os, sys, time, threading
 
# Einbindung 0,96 Zoll OLED Display 128x64 Pixel
import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont



# Display einrichten
 
# Raspberry Pi pin configuration:
RST = 24
 
# Display 128x64 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
 
# Initialize library.
disp.begin()
 
# Clear display.
disp.clear()
disp.display()


# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)


# Load default font.
font = ImageFont.load_default() # Wenn keine eigene Schrift vorhanden ist!!!! 


# Write one line of text.
draw.text((0,0), 'Line 1', font=font, fill=255)
draw.text((0,10), 'Line 2', font=font, fill=255)
draw.text((0,20), 'Line 3', font=font, fill=255)


# Display image.
disp.image(image)
disp.display()