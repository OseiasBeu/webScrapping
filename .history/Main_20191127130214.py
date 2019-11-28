# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import xlrd


print ('Iniciando...')

driver = webdriver.Chrome(executable_path='chromedriver.exe')