import time, os, shutil, statistics


x = 1

local_file = "/media/test/0060.tif"
remote_loc = "/media/151/CIFS_TEST/TIFS/0060.tif"

x2 = 150
y = 1

while x2 < 160:
    print(x2)
    to = str("/media/") + str(x2) + str("/CIFS_TEST/TIFS/0060.tif")
    #print(to)
    x2 += 1
    #x2 = x2 + 1
    up = []
    down = []
    varUP = []
    varDOWN = []

    while x < 1000:
        start_time = time.time()
        if os.path.isfile("/media/test/0060.tif"):
            #print(to)
            shutil.copy("/media/test/0060.tif", to)
        else:
            print("Error: %s file not found" % to)
        #uptime
        up.append(time.time() - start_time)
        if os.path.isfile("/media/test/0060.tif"):
            os.remove("/media/test/0060.tif")
        else:
            print("Error: %s file not found" % "/media/test/0060.tif")
        start_time = time.time()
        shutil.copy(to, "/media/test/0060.tif")
        # down-time
        down.append(time.time() - start_time)
        x += 1
    print(up)
    print(down)
    a = (statistics.pstdev(up))
    print(('%.16f' % a), "stdUP")
    b = (statistics.variance(up))
    print(('%.16f' % b), "varUP")
    c = (statistics.pstdev(down))
    print(('%.16f' % c), "stdDOWN")
    d = (statistics.variance(down))
    print(('%.16f' % d), "varDOWN")

    x = 0

print('complete')
