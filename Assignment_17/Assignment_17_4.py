import schedule
import time

def Display():
    print("Namaskar...!")   


def main():
    schedule.every().day.at("09:00").do(Display)

    print("Application is in waiting state")
    while True:
        schedule.run_pending()
        time.sleep(30)
    



if __name__ == "__main__":
    main()