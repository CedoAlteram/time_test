import time


x = 1
start_time = time.time()
while x < 10000:
    x = x+1
    #do something

print('complete')
print("--- %s seconds ---" % (time.time() - start_time))