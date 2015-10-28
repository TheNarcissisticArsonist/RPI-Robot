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

        # We're at this indentation...
