import time
import sys
from datetime import datetime

hourly_pay = 16
shift = 9
lunch = 1


def clock_in():
    current_time = datetime.now()
    logged_time = current_time.strftime("%H:%M")
    clocked_in = True
    worker_hours = 0

    print(f"You clocked in at {logged_time}")

    if clocked_in:
        while int(worker_hours) <= int(shift):
            if worker_hours == 2 or worker_hours == 8:
                time.sleep(2)
                break_time()
                time.sleep(2)
                worker_hours = worker_hours + 1
            elif worker_hours == 5:
                time.sleep(2)
                start_lunch()
                time.sleep(2)
                end_lunch()
                time.sleep(2)
                worker_hours = worker_hours + 1
            else:
                print("Working...")
                time.sleep(2)
                # current_pay = hourly_pay * worker_hours
                worker_hours = worker_hours + 1

        if int(worker_hours) > int(shift):
            overtime_input = input("Would you like overtime? y/n ")

            if overtime_input == 'y':
                ot_approval = input("Is overtime approved? y/n ")
                approved_ot = True

                match ot_approval:
                    case 'y':
                        print("Work overtime")
                        overtime(hourly_pay, approved_ot)
                    case 'n':
                        clock_out(logged_time)
                        sys.exit()
            else:
                print("Overtime denied")
                clock_out(logged_time)
                sys.exit()


def clock_out(logged_time):
    print(f"You clocked out at {logged_time}")
    sys.exit()


def start_lunch():
    print('Start lunch')


def end_lunch():
    print('End lunch')


def break_time():
    print("On break")
    return None


def overtime(pay, approved):
    current_time = datetime.now()
    logged_time = current_time.strftime("%H:%M")
    oth = int(1)
    ot_hours = int(input('How many overtime hours are you working? '))

    if ot_hours > 4:
        print("You can only work 4 hours over")
        clock_out(logged_time)
    else:
        while approved:
            if oth <= ot_hours:
                ot_pay = pay + pay/2
                time.sleep(2)
                print(f"Worked {oth} overtime hour...")
                oth = oth + 1
                time.sleep(1)
            else:
                approved = False

        final_ot = ot_hours * ot_pay
        print(final_ot)


def work():
    clock_in()
