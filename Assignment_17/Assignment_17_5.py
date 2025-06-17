import schedule
import time

def Job():
    fobj = open('Marvellous.txt', 'a')

    fobj.write(time.asctime()+ "\n")
    print("Current time : ", time.asctime())

def main():
    fobj = open('Marvellous.txt', 'w')
    fobj.close()

    schedule.every(5).minutes.do(Job)   

    print("Application is in waiting state")
    while True:
        schedule.run_pending()
        time.sleep(1)
    



if __name__ == "__main__":
    main()