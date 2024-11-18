import time
import sys
from datetime import datetime

hourly_pay = 16
shift = 8
lunch = 1


def clock_in():
    current_time = datetime.now()
    logged_time = current_time.strftime("%H:%M")
    clocked_in = True
    current_pay = 0
    approved_ot = False
    worker_hours = 0

    print(f"You clocked in at {logged_time}")

    if clocked_in:
        while int(worker_hours + 1) <= int(shift):
            if worker_hours == 4:
                print("Take your lunch")
                start_lunch()
                worker_hours = worker_hours + 1
            else:
                worker_hours = worker_hours + 1
                # time.sleep(2)
                current_pay = hourly_pay * worker_hours
                print(current_pay)
                continue

        if int(worker_hours) > int(shift) - 1:
            print("1. Would you like overtime? ")
            print("2. Would you like to clock out? ")

            overtime_input = input("1 or 2?")

            match overtime_input:
                case 1:
                    print("Work overtime")
                case 2:
                    clock_out(logged_time)


def clock_out(logged_time):
    print(f"Clock you clocked out at {logged_time}")
    sys.exit()


def start_lunch():
    print('Start lunch')


def end_lunch():
    clock_in()
