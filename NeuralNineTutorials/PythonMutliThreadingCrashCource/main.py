import threading
import time

done = False

def worker():
    counter = 0
    while not done:
        time.sleep(1)
        counter += 1
        print(counter)


threading.Thread(target=worker).start()

# as a daemon
#def worker():
    #counter = 0
    #while True:
        #time.sleep(1)
        #counter += 1
        #print(counter)

#threading.Thread(target=worker, daemon=True).start()

# Passing arguments
#def worker(text):
    #counter = 0
    #while True:
        #time.sleep(1)
        #counter += 1
        #print(f"{text}: {counter}")

#threading.Thread(target=worker, daemon=True, args=("ABC,")).start()
#threading.Thread(target=worker, daemon=True, args=("XYZ,")).start()

# this setup wont allow the program to get to the input because the threads are still running
#t1 = threading.Thread(target=worker, daemon=True, args=("ABC,")).start()
#t2 = threading.Thread(target=worker, daemon=True, args=("XYZ,")).start()
#t1.start()
#t2.start()
#t1.join()
#t2.join()
input("Press enter to quit\n")
done = True