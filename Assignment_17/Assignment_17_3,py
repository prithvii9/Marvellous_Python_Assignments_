import schedule
import time

def Display():
    print("Do Coding..!")   


def main():
    schedule.every(30).minutes.do(Display)

    print("Application is in waiting state")
    while True:
        schedule.run_pending()
        time.sleep(30)
    



if __name__ == "__main__":
    main()