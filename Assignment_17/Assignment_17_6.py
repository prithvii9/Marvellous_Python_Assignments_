import schedule
import time

def Lunch():
    print("Lunch Time")   

def WrapUp():
    print("Wrap up work")

def main():
    schedule.every().day.at("13:00").do(Lunch)
    schedule.every().day.at("18:00").do(WrapUp)

    print("Application is in waiting state")
    while True:
        schedule.run_pending()
        time.sleep(30)
    



if __name__ == "__main__":
    main()