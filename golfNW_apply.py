#! /usr/bin/env python3

from selenium import webdriver

default = webdriver.Chrome()
default.get("https://www.golfnetwork.co.jp/campaign/")

print('URL を入力')
url = input()

# 個人情報規約に同意する　の部分を参照
print('初期値 を入力')
number = input()
number = int(number)

browser = webdriver.Chrome()
browser.get(url)

#個人情報への同意
browser.find_element_by_name('multiAnswer(ANSWER'+ str(number) +')').click()

#Name
browser.find_element_by_name('singleAnswer(ANSWER'+str(number + 1)+'-1)').send_keys('name')
browser.find_element_by_name('singleAnswer(ANSWER'+str(number + 1)+'-2)').send_keys('name')

#Sex
browser.find_element_by_name('singleAnswer(ANSWER'+str(number + 2)+')').click()

#Age
browser.find_element_by_name('singleAnswer(ANSWER'+str(number + 3)+')').click()

browser.find_element_by_name('singleAnswer(ANSWER'+str(number + 4)+')').send_keys('eMail')

#ZIP
browser.find_element_by_name('singleAnswer(ANSWER'+str(number +5)+'-1)').send_keys('postalCode')
browser.find_element_by_name('singleAnswer(ANSWER'+str(number +5)+'-2)').send_keys('postalCode')

#Address
browser.find_element_by_name('singleAnswer(ANSWER'+str(number +6)+')').send_keys('yourAddress1')
browser.find_element_by_name('singleAnswer(ANSWER'+str(number +7)+')').send_keys('yourAddress2')
browser.find_element_by_name('singleAnswer(ANSWER'+str(number +8)+')').send_keys('yourAddress3')

#Phone
browser.find_element_by_name('singleAnswer(ANSWER'+str(number + 10)+'-1)').send_keys('phone#1')
browser.find_element_by_name('singleAnswer(ANSWER'+str(number + 10)+'-2)').send_keys('phone#2')
browser.find_element_by_name('singleAnswer(ANSWER'+str(number + 10)+'-3)').send_keys('phone#3')

#Way
browser.find_element_by_name('singleAnswer(ANSWER'+str(number + 11)+')').click()



