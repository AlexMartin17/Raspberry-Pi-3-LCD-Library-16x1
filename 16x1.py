import RPi.GPIO as GPIO
from time import sleep

#8 pins for display data buses
datapins = [23,24,25,8,7,12,16,20]
#2 pins for display enable/register select
setpins = [14,15]

#gpio setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(datapins, GPIO.OUT)
GPIO.setup(setpins, GPIO.OUT)

def Port(a):
    if ord(a)&1:
        GPIO.output(23, 1)
    else:
        GPIO.output(23, 0)
    if ord(a)&2:
        GPIO.output(24, 1)
    else:
        GPIO.output(24, 0)
    if ord(a)&4:
        GPIO.output(25, 1)
    else:
        GPIO.output(25, 0)
    if ord(a)&8:
        GPIO.output(8, 1)
    else:
        GPIO.output(8, 0)
    if ord(a)&16:
        GPIO.output(7, 1)
    else:
        GPIO.output(7, 0)
    if ord(a)&32:
        GPIO.output(12, 1)
    else:
        GPIO.output(12, 0)
    if ord(a)&64:
        GPIO.output(16, 1)
    else:
        GPIO.output(16, 0)
    if ord(a)&128:
        GPIO.output(20, 1)
    else:
        GPIO.output(20, 0)

def Port2(a):
    if a&1:
        GPIO.output(23, 1)
    else:
        GPIO.output(23, 0)
    if a&2:
        GPIO.output(24, 1)
    else:
        GPIO.output(24, 0)
    if a&4:
        GPIO.output(25, 1)
    else:
        GPIO.output(25, 0)
    if a&8:
        GPIO.output(8, 1)
    else:
        GPIO.output(8, 0)
    if a&16:
        GPIO.output(7, 1)
    else:
        GPIO.output(7, 0)
    if a&32:
        GPIO.output(12, 1)
    else:
        GPIO.output(12, 0)
    if a&64:
        GPIO.output(16, 1)
    else:
        GPIO.output(16, 0)
    if a&128:
        GPIO.output(20, 1)
    else:
        GPIO.output(20, 0)

def Cmd(a):
    GPIO.output(14, 0)
    Port2(a)
    GPIO.output(15, 1)
    sleep(0.005)
    GPIO.output(15, 0)

def Clear_Display():
    Cmd(1)

def Set_Cursor1():
    Cmd(0x80)

def Set_Cursor2():
    Cmd(0x80 + 0x40)

def Init():
    #Port(0);
    GPIO.output(14, 0);
    sleep(0.025)
    Cmd(0x30)
    sleep(0.005)
    Cmd(0x30)
    sleep(0.015)
    Cmd(0x30)
    Cmd(0x38)
    Cmd(0x0C)
    Cmd(0x01)
    Cmd(0x06)

def Shift_Right():
    Cmd(0x1C)

def Shift_Left():
    Cmd(0x18)

def Write_Char(a):
    GPIO.output(14, 1)
    Port(a)
    GPIO.output(15, 1)
    sleep(0.004)
    GPIO.output(15, 0)

#if display is 16 chars but divided by 2 e.g 8x2
def Write_String(a):
    for x in range(len(a)):
        if x >= 8:
            Set_Cursor2()
            Write_Char(a[x])
        else:
            Write_Char(a[x])

#if display is regular 16x1
def Write_StringR(a):
    for x in a:
        Write_Char(x)

Clear_Display()
Init()
Write_String("0123456789ABCDEF")
