# -*- coding: utf-8 -*-
import schedule
import time
import toolbox.middleware as middleware
import toolbox.integracoes_h as integracoes_h

middleware.middleware()
integracoes_h.integracoes_h()

# def Main():

#   middleware.middleware()

# schedule.every(10).minutes.do(Main)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
