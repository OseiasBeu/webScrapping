# -*- coding: utf-8 -*-


import toolbox.middleware as middleware

schedule.every(1).minutes.do(Main.Main())

def Main():

  middleware.middleware()
