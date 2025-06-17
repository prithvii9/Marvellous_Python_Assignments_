import schedule
import time
import datetime

def Display():
    print(datetime.datetime.now())


def main():
    schedule.every(1).minute.do(Display)

    print("Application is in waiting state")
    while True:
        schedule.run_pending()
        time.sleep(30)
    



if __name__ == "__main__":
    main()