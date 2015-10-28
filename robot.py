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
# 1 | 9  #
# 2 | 10 #
# 3 | 11 #
# 4 | 12 #
# 5 | 13 #
# 6 | 14 #
# 7 | 15 #
# 8 | 16 #

# GPIO
    # Using GPIO.setmode(GPIO.BOARD)
# ? | ? #
# ? | ? #
# ? | ? #
# ? | ? #
# ? | ? #
# ? | ? #
# ? | ? #
# ? | ? #

# Motors
    # [1 2]
    # [3 4]
    # 5V is power -- 5 volts
    # GND is ground
    # + is forward
    # - is backward
# 1 5V  + | 2 5V  + #
# 1 GND + | 2 GND + #
# 1 5V  - | 2 5V  - #
# 1 GND - | 2 GND - #
# 3 5V  + | 4 5V  + #
# 3 GND + | 4 GND + #
# 3 5V  - | 4 5V  - #
# 3 GND - | 4 GND - #
