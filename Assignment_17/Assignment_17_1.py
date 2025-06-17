import schedule
import time

def Display():
    print("Jay Ganesh")


def main():
    schedule.every(2).seconds.do(Display)

    print("Application is in waiting state")
    while True:
        schedule.run_pending()
        time.sleep(2)
    



if __name__ == "__main__":
    main()