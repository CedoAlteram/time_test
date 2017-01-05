#author aaron
import time, os, shutil, statistics


x = 1

local_file = "/media/test/1GBa.txt"
remote_loc = "/media/151/CIFS_TEST/TIFS/1GBa.txt"

x2 = 150
y = 1

while x2 < 160:
    print(x2)
    to = str("/media/") + str(x2) + str("/CIFS_TEST/TIFS/1GBa.txt")
    #print(to)
    x2 += 1
    #x2 = x2 + 1
    up = []
    down = []
    varUP = []
    varDOWN = []

    while x < 10:
        os.system('dd if=/dev/urandom of=/media/test/1GBa.txt bs=64 count=16 iflag=fullblock')
        start_time = time.time()
        if os.path.isfile("/media/test/1GBa.txt"):
            #print(to)
            shutil.copy("/media/test/1GBa.txt", to)
            os.sync()
            #print('I copied a file up')
        else:
            print("Error: %s file not found" % to)
        #uptime
        #print("%s seconds" % (time.time() - start_time), "log A - UP", time.localtime())
        up.append(time.time() - start_time)
        if os.path.isfile("/media/test/1GBa.txt"):
            os.remove("/media/test/1GBa.txt")
        else:
            print("Error: %s file not found" % "/media/test/1GBa.txt")
        start_time = time.time()
        shutil.copy(to, "/media/test/1GBa.txt")
        os.sync()
        #print('I copied a file down')
        # down-time
        #print("%s seconds" % (time.time() - start_time), "log B - DOWN", time.localtime())
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
