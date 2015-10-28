while True:
    motorFile = open("motor_instructions.txt", "r")
    cont = motorFile.read()
    if cont != "":
        cont = cont.split()
        print cont #cont is an array of strings
