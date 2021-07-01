import schedule
import time
import instragram
import photoNumber

schedule.every().monday.at("12:00").do(instragram.start)
schedule.every().monday.at("15:00").do(instragram.start)
schedule.every().monday.at("18:00").do(instragram.start)

schedule.every().tuesday.at("12:00").do(instragram.start)
schedule.every().tuesday.at("15:00").do(instragram.start)
schedule.every().tuesday.at("18:00").do(instragram.start)

schedule.every().wednesday.at("12:00").do(instragram.start)
schedule.every().wednesday.at("15:00").do(instragram.start)
schedule.every().wednesday.at("18:00").do(instragram.start)

schedule.every().thursday.at("12:00").do(instragram.start)
schedule.every().thursday.at("15:00").do(instragram.start)
schedule.every().thursday.at("18:00").do(instragram.start)

schedule.every().friday.at("12:00").do(instragram.start)
schedule.every().friday.at("15:00").do(instragram.start)
schedule.every().friday.at("18:00").do(instragram.start)

schedule.every().saturday.at("12:00").do(instragram.start)
schedule.every().saturday.at("15:00").do(instragram.start)
schedule.every().saturday.at("18:00").do(instragram.start)

schedule.every().sunday.at("12:00").do(instragram.start)
schedule.every().sunday.at("15:00").do(instragram.start)
schedule.every().sunday.at("18:00").do(instragram.start)

# schedule.every(1).minutes.do(instragram.start)

while True and (photoNumber.getPhotoNumber()>=744):
    schedule.run_pending()
    time.sleep(1)