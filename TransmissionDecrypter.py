from Interface import textTraitment,placer_pion,getLastPos,getLastChat

def decrypt(x):
    try:
        if x[0] == '0': #0_col_x_y
            #placer_pion(int(x[1]), int(x[2]), int(x[3]))
            return "OK " + str(int(x[1]))+ str(int(x[2])) + str(int(x[3]))
        elif x[0] == '1': #1_user&mess
            #textTraitment(x[x.find('&') + 1:]), "opponent", x[1:x.find('&')], 'red')
            return "OK " + str(x[x.find('&') + 1:]) + "opponent"  + str(x[1:x.find('&')]) + 'red'
        elif x[0] == '8':
            x = x[1:]
            while x.find('£') > -1:
                x = x[1:]
                y = x
                if(x.find('£') > -1):
                    print(decrypt(y[:y.find('£')]))
                    x = x[
                        x.find('£'):]
                else:
                    print(decrypt(x))
            return "OK 8"
        elif x[0] == '9':
            mess = '8'
            s = getLastPos()
            if s != '': mess += "£0" + s
            i = 0
            l = getLastChat()
            for s in l:
                i += 1
                if(i == 1): continue
                mess += '£1' + l[0] + "&" + s
            return mess
    except IndexError as e:
        print(e)
        pass
    return "Error " + x
