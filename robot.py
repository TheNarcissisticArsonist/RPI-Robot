# WIRING AND PIN INFORMATION

# Relays
# 1 | 16 #
# 2 | 15 #
# 3 | 14 #
# 4 | 13 #
# 5 | 12 #
# 6 | 11 #
# 7 | 10 #
# 8 | 9  #

# Breadboard
# Row | Relay | GPIO
# 01 | 15 | 11
# 02 | 13 | 13
# 03 | 11 | 15
# 04 | 9  | 29
# 05 | 7  | 31
# 06 | 5  | 33
# 07 | 3  | 35
# 08 | 1  | 37
# 09 | 16 | 12
# 10 | 14 | 16
# 11 | 12 | 18
# 12 | 10 | 22
# 13 | 8  | 32
# 14 | 6  | 36
# 15 | 4  | 38
# 16 | 2  | 40

# Pi
# -- | -- #
# -- | -- #
# -- | -- #
# -- | -- #
# -- | -- #
# 11 | 12 #
# 13 | -- #
# 15 | 16 #
# -- | 18 #
# -- | -- #
# -- | 22 #
# -- | -- #
# -- | -- #
# -- | -- #
# 29 | -- #
# 31 | 32 #
# 33 | -- #
# 35 | 36 #
# 37 | 38 #
# -- | 40 #

# GPIO
    # Using GPIO.setmode(GPIO.BOARD)
# 37 | 12 #
# 40 | 11 #
# 35 | 16 #
# 38 | 13 #
# 33 | 18 #
# 36 | 15 #
# 31 | 22 #
# 32 | 29 #

# Motors
    # [1 2]
    # [3 4]
    # 12V is power -- 12 volts
    # GND is ground
    # + is forward
    # - is backward
# 1 12V + | 2 12V + #
# 1 GND + | 2 GND + #
# 1 12V - | 2 12V - #
# 1 GND - | 2 GND - #
# 3 12V + | 4 12V + #
# 3 GND + | 4 GND + #
# 3 12V - | 4 12V - #
# 3 GND - | 4 GND - #

# Pins -> Motors
# Motor 1 +      -
    # 37 low    high
    # 40 low    high
    # 35 high   low
    # 38 high   low
# Motor 2 +      -
    # 12 low    high
    # 11 low    high
    # 16 high   low
    # 13 high   low
# Motor 3 +      -
    # 33 low    high
    # 36 low    high
    # 31 high   low
    # 32 high   low
# Motor 4 +      -
    # 18 low    high
    # 15 low    high
    # 22 high   low
    # 29 high   low

# BE CAREFUL WITH THESE VALUES!!!!!
RELAYS = [None, 37, 40, 35, 38, 33, 36, 31, 32, 29, 22, 15, 18, 13, 16, 11, 12]
# Indexes: 0  , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10, 11, 12, 13, 14, 15, 16
# The None in index 0 makes it easier to use -- relay 1 is RELAYS[1], relay 7 is RELAYS[7], etc.

#import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BOARD)
#for i in range(1,18):
#    print i
#    print RELAYS[i]
#    GPIO.setup(RELAYS[i], GPIO.OUT)
#    GPIO.output(RELAYS[i], True)
try:
    while True:
        motorFile = open("motor_instructions.txt", "r")
        cont = motorFile.read()
        if cont != "":
            cont = cont.split()
            print cont #cont is an array of strings
            for i in range(0, 4):
                if cont[i] == "true":
                    cont[i] = True
                elif cont[i] == "false":
                    cont[i] = False
                else:
                    cont[i] = None
                    print cont #cont is an array of booleans or NoneTypes
                    print "\n"

                if cont[0] == True:
                    # 37, 40 low  &  35, 38 high
                elif cont[0] == False:
                    # 37, 40 high  &  35, 38 low
                else:
                    # 37, 40, 35, 38 high

                if cont[1] == True:
                    # 12, 11 low  &  16, 13 high
                elif cont[1] == False:
                    # 12, 11 high  &  16, 13 low
                else:
                    # 12, 11, 16, 13 high

                if cont[2] == True:
                    # 33, 36 low  &  31, 32 high
                elif cont[2] == False:
                    # 33, 36 high  &  31, 32 low
                else:
                    # 33, 36, 31, 32 high

                if cont[3] == True:
                    # 18, 15 low  &  22, 29 high
                elif cont[3] == False:
                    # 18, 15 high  &  22, 29 low
                else:
                    # 18, 15, 22, 29 high
except:
    print "Detected exception!"
    # GPIO.cleanup()
