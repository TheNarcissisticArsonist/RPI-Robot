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
