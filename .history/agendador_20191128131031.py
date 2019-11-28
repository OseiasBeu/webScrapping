import schedule
import time
import Main as Main



schedule.every(1).minutes.do(Main.Main())
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)
# print("Final do arquivo")

while True:
    schedule.run_pending()
    time.sleep(1)