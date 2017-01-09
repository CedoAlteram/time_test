#author aaron

import time, os, statistics, sys
import numpy as np, scipy.stats as st

x = 1

local_file = "/media/test/gentoo_root.img"
remote_loc = "/media/151/CIFS_TEST/TIFS/gentoo_root.img"

x2 = 150
y = 1
#sys.stdout=open("/media/test/stats.txt", 'w')
os.system('cp -fr /media/original_file/gentoo_root.img /media/test')
print('original file copied')
print('beginning')
while x2 < 161:
    print(x2)
    to = str("/media/") + str(x2) + str("/CIFS_TEST/TIFS/gentoo_root.img")
    #print(to)
    x2 += 1
    up = []
    down = []
    varUP = []
    varDOWN = []

    while x < 3:
        start_time = time.time()
        if os.path.isfile("/media/test/gentoo_root.img"):
            os.system('cp -fr /media/test/gentoo_root.img' + ' ' + to)
            os.sync()
        else:
            print("Error: %s file not found" % to)
        print("%s seconds" % (time.time() - start_time), "log A - UP", time.localtime())
        up.append(time.time() - start_time)
        if os.path.isfile("/media/test/gentoo_root.img"):
            os.remove("/media/test/gentoo_root.img")
        else:
            print("Error: %s file not found" % "/media/test/gentoo_root.img")
        start_time = time.time()
        os.system('cp -fr ' + to + ' /media/test/gentoo_root.img')
        os.sync()
        # down-time
        print("%s seconds" % (time.time() - start_time), "log B - DOWN", time.localtime())
        down.append(time.time() - start_time)
        x += 1
    print(up, "UP List")
    print(down, "DOWN List")

    intervalUP = st.t.interval(0.95, len(up)-1, loc=np.mean(up), scale=st.sem(up))
    print(intervalUP)
    a = (statistics.mean(up))
    print(('%.16f' % a), "meanUP")
    b = (statistics.pstdev(up))
    print(('%.16f' % b), "stdUP")
    c = (statistics.variance(up))
    print(('%.16f' % c), "varUP")

    intervalDOWN = st.t.interval(0.95, len(down) - 1, loc=np.mean(down), scale=st.sem(down))
    print(intervalDOWN)
    d = (statistics.mean(down))
    print(('%.16f' % d), "meanDOWN")
    e = (statistics.pstdev(down))
    print(('%.16f' % e), "stdDOWN")
    f = (statistics.variance(down))
    print(('%.16f' % f), "varDOWN")
    print(time.localtime(), "THIS IS TIME!!!!!")
    print('----------------------------------------')
    x = 0

print('complete')
#sys.stdout.close()