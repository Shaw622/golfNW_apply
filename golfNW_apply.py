#! /usr/bin/env python3

from selenium import webdriver

print('URL を入力')
url = input()
print('初期値 を入力')
number = input()
number = int(number)

browser = webdriver.Chrome()
browser.get(url)

#個人情報への同意
agree = browser.find_element_by_name('multiAnswer(ANSWER'+ str(number) +')')
agree.click()

#名前の入力
familyName = browser.find_element_by_name('singleAnswer(ANSWER'+str(number + 1)+'-1)')
familyName.send_keys('name')
lastName = browser.find_element_by_name('singleAnswer(ANSWER'+str(number + 1)+'-2)')
lastName.send_keys('name')

#性別
sex = browser.find_element_by_name('singleAnswer(ANSWER'+str(number + 2)+')')
sex.click()

#年代
age = browser.find_element_by_name('singleAnswer(ANSWER'+str(number + 3)+')')
age.click()

eMail = browser.find_element_by_name('singleAnswer(ANSWER'+str(number + 4)+')')
eMail.send_keys('eMail')

postalCode1 = browser.find_element_by_name('singleAnswer(ANSWER'+str(number +5)+'-1)')
postalCode1.send_keys('postalCode')
postalCode2 = browser.find_element_by_name('singleAnswer(ANSWER'+str(number +5)+'-2)')
postalCode2.send_keys('postalCode')

#住所
address1 = browser.find_element_by_name('singleAnswer(ANSWER'+str(number +6)+')')
address1.send_keys('address')
address2 = browser.find_element_by_name('singleAnswer(ANSWER'+str(number +7)+')')
address2.send_keys('address')
address3 = browser.find_element_by_name('singleAnswer(ANSWER'+str(number +8)+')')
address3.send_keys('address')

#電話番号
phone1 = browser.find_element_by_name('singleAnswer(ANSWER'+str(number + 10)+'-1)')
phone1.send_keys('phone')
phone2 = browser.find_element_by_name('singleAnswer(ANSWER'+str(number + 10)+'-2)')
phone2.send_keys('phone')
phone3 = browser.find_element_by_name('singleAnswer(ANSWER'+str(number + 10)+'-3)')
phone3.send_keys('phone')

#視聴方法
age = browser.find_element_by_name('singleAnswer(ANSWER'+str(number + 11)+')')
age.click()



