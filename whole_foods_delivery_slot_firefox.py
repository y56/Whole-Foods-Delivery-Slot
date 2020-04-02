import bs4

from selenium import webdriver

import time
import os


def getWFSlot(productUrl):
   driver = webdriver.Firefox(executable_path="/home/ptt5566/Downloads/geckodriver-v0.26.0-linux64/geckodriver")
   driver.get(productUrl)           
   html = driver.page_source
   soup = bs4.BeautifulSoup(html)
   time.sleep(50)
   no_open_slots = True

   while no_open_slots:
      driver.refresh()
      print("refreshed")
      html = driver.page_source
      soup = bs4.BeautifulSoup(html)
      time.sleep(6)

      slot_pattern = 'Next available'
      try:
         print("        part1 try 1")
         next_slot_text = soup.find('h4', class_ ='ufss-slotgroup-heading-text a-text-normal').text
         print("        part1 try 2")
         if slot_pattern in next_slot_text:
            print("        part1 try 3")
            print('SLOTS OPEN!')
            #os.system('say "Slots for delivery opened!"')
            os.system('totem --play ~/Music/05.\ merry-go-round.mp3')
            no_open_slots = False
            time.sleep(1400*10)
         else:
             print("        part1 try 4")
      except AttributeError:
         print("        part1 except")
         continue
     
      try:
         print("        part2 try 1")
         no_slot_pattern = 'No delivery windows available. New windows are released throughout the day.'
         print("        part2 try 2")
         if no_slot_pattern == soup.find('h4', class_ ='a-alert-heading').text:
             print("        part2 try 3")
             print("NO SLOTS!")
         else:
             # I succeeded to reach HERE and buy my food!
             # the log was:         
             #        part1 try 1
             #        part1 try 2
             #        part1 try 4
             #        part2 try 1
             #        part2 try 2
             #        part2 try 4
             
             print("        part2 try 4")
             os.system('totem --play ~/Music/05.\ merry-go-round.mp3')
             time.sleep(12000)

      except AttributeError: 
            print("        part2 except")
            print('SLOTS OPEN!')
            #os.system('say "Slots for delivery opened!"')
            os.system('totem --play ~/Music/05.\ merry-go-round.mp3')
            time.sleep(12000)
            no_open_slots = False


getWFSlot('https://www.amazon.com/gp/buy/shipoptionselect/handlers/display.html?hasWorkingJavascript=1')


