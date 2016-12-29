import time, os, shutil


x = 1

local_file = "/media/test/0060.tif"

while x < 20000000:
    start_time = time.time()
    if os.path.isfile("/media/test/0060.tif"):
        shutil.copy("/media/test/0060.tif", "/media/Isilon/Isilon_Packages/test/move_test/0060.tif")
    else:
        print("Error: %s file not found" % "/media/test/0060.tif")
    print("%s seconds" % (time.time() - start_time), "log A - UP", time.localtime())
    if os.path.isfile("/media/test/0060.tif"):
        os.remove("/media/test/0060.tif")
    else:
        print("Error: %s file not found" % "/media/test/0060.tif")
    start_time = time.time()
    shutil.copy("/media/Isilon/Isilon_Packages/test/move_test/0060.tif", "/media/test/0060.tif")
    print("%s seconds" % (time.time() - start_time), "log B - DOWN", time.localtime())
    x = x + 1

print('complete')
