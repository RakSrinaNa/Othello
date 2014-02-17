from Interface import textTraitment,placer_pion

def decrypt(x):
    try:
        if x[0] == '0':
            placer_pion(int(x[1]), int(x[2]), int(x[3]))
            print("PP" + str(int(x[1]))+ str(int(x[2]))+ str(int(x[3])))
        elif x[0] == '1':
            textTraitment(x[2:], "opponent", "Neko", 'red')
    except IndexError:
        pass
