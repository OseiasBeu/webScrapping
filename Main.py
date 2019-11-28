# -*- coding: utf-8 -*-
import schedule
import time
import toolbox.middleware as middleware


def Main():

  middleware.middleware()

schedule.every(1).minutes.do(Main)

while True:
    schedule.run_pending()
    time.sleep(1)
