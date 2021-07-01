def getPhotoNumber():
    f = open("photoNumber", "r")
    i = int(f.read().replace(" ", ""))
    # print(i)
    f.close()
    return(i)

def setPhotoNumber(num):
    f = open("photoNumber", "w")
    f.write(str(num))
    f.close()