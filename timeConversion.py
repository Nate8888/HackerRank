def timeConversion(s):
    if s[8:] == "PM" and int(s[0:2]) != 12:
        return(str((int(s[0:2])+12))+s[2:8])
    elif s[8:] == "AM" and int(s[0:2]) == 12:
        return("00"+s[2:8])
    return(s[:8])