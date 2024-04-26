import time


def countdown():
    condition = True

    while condition is not False:
        try:
            user_time = int(input("Set the timer (In Seconds)? "))

            for x in range(user_time, 0, -1):
                seconds = x % 60
                minutes = int(x / 60) % 60
                hours = int(x / 3600)  # Add modulus % 24 if working with days
                print(f"{hours:02}:{minutes:02}:{seconds:02}")
                time.sleep(1)  # sleeps for 1 second

            print("TIME'S UP!")
            condition = False

        except ValueError:
            print("Incorrect input, try again")


countdown()
