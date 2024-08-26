import threading
import time


####################################################################################################################################################################################

# SAMPLE CONCURRENT PROGRAM

# def worker1(cc):
#     i = 0
#     while i < cc:
#         print(f'Thread {threading.current_thread().name} is running...')
#         time.sleep(1)
#         i += 1


# def worker2(cc):
#     i = 0
#     while i < cc:
#         print(f'Thread {threading.current_thread().name} is running...')
#         time.sleep(1)
#         i += 1


# th1 = threading.Thread(target=worker1, args=(3, ))
# th2 = threading.Thread(target=worker2, args=(6, ))

# Starts the Thread
# th1.start()
# th2.start()

# Call thread.join() to tell the program that it should wait for this thread to complete before it continues with the rest of the code.
# th1.join()
# th2.join()

####################################################################################################################################################################################

# SHARING DATA BETWEEN 2 THREADS

# db_inc_value = 0


# def inc():
#     global db_inc_value  # GLOBAL keywork is required to access outer variable inside a function

#     local_db_inc_value = db_inc_value
#     local_db_inc_value += 1
#     db_inc_value = local_db_inc_value


# if __name__ == "__main__":
#     t1 = threading.Thread(target=inc)
#     t2 = threading.Thread(target=inc)

#     t1.start()
#     t2.start()

#     t1.join()
#     t2.join()

#     print('End value:', db_inc_value)

####################################################################################################################################################################################

