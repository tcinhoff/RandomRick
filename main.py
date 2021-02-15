import time
from random import randint
import tkinter
from tkinter import messagebox
import json

from selenium import webdriver

staffel = randint(1, 4)

if (staffel == 1):
    folge = randint(1, 11)
else:
    folge = randint(1, 10)

root = tkinter.Tk()
root.withdraw()


driver = webdriver.Chrome()
driver.maximize_window()

with open('Login.json', 'r') as loginFile:
    login = json.load(loginFile)

driver.get('https://www.netflix.com/de/login')
driver.find_element_by_xpath('//*[@id="id_userLoginId"]').send_keys(login["username"])
driver.find_element_by_xpath('//*[@id="id_password"]').send_keys(login["password"])
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div[1]/form/button').submit()

time.sleep(2)

driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[4]/div/a/div/div').click()

time.sleep(3)

driver.get('https://www.netflix.com/browse?jbv=80014749')


staffel = randint(1, 4)

if (staffel == 1):
    folge = randint(1, 11)
else:
    folge = randint(1, 10)

root = tkinter.Tk()
root.withdraw()

messagebox.showinfo('Random Rick', "You have to watch \nSeason: " + str(staffel) + "\nEpisode: " + str(folge))

