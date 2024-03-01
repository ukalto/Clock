from datetime import datetime


def main():
    now = datetime.now()
    first_sec = now.strftime("%S")
    while True:
        now = datetime.now()
        new_sec = now.strftime("%S")
        if first_sec != new_sec:
            first_sec = new_sec
            current_time = now.strftime("%H:%M:%S")
            print("Current Time =", current_time)


if __name__ == "__main__":
    main()
