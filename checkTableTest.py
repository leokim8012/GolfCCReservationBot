import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait


from datetime import datetime, timedelta
import time

import re
  
def closest(lst, K):
  return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]


def getSeqFromForm(form):
  regex = re.compile(r"\B'\w+'\B")
  text = regex.findall(form)
  return int(text[2].replace('\'',''))


def getFormFromCalendarData(cal):
  print(cal)
  regex = re.compile('{}(.*){}'.format(re.escape('onclick="'), re.escape('" ')))
  text = regex.findall(cal)
  return text


ID = '111346'
Password = '8012'


ReservationYear = '2021'
ReservationMonth = '06'
ReservationDay = '02'

ReservationDate = ReservationYear + ReservationMonth + ReservationDay



ReservationSeq = '060'

ReservationCourse = 0



inputID = 'memberId'
inputPW = 'memberPw'

LoginURL = 'https://www.daegucc.co.kr/Member/Login'
ReservationURL = 'https://www.daegucc.co.kr/Booking/ReservationCalendar?day=' + ReservationDate
# 
Form = 'ReservationForm(\'160\', \'' + ReservationDate + '\', \'' + ReservationSeq + '\');'
ReservationOK = 'Reservation(\'ok\');'

driver = webdriver.Chrome(executable_path='chromedriver')

#Goto Login
driver.get(url=LoginURL)
#Login
idBox = driver.find_element_by_id(inputID)
idBox.send_keys(ID)
pwBox = driver.find_element_by_id(inputPW)
pwBox.send_keys(Password)
driver.execute_script('login()')

#Login alert
result = driver.switch_to_alert()
result.accept()


driver.get(url=ReservationURL)


# Get Table Datas
availableForm = []
availableSeq = []
getCalendar = "getHtmlForm(\"/Booking/AjaxGetTime\", { day: '20210604' });"
print(getCalendar)
calendarData = driver.execute_script('return ' + getCalendar)
print(calendarData)

# driver.execute_script(activeForm)
availableForm = getFormFromCalendarData(calendarData)
print(availableForm)

for form in availableForm:
  availableSeq.append(getSeqFromForm(form))

# Choose Closest Form
absolute_difference_function = lambda i : abs(availableSeq[i] - int(ReservationSeq))
closestValueIndex = min(range(len(availableSeq)), key=absolute_difference_function)
activeForm = availableForm[closestValueIndex]


driver.execute_script(activeForm)

tables = driver.find_elements_by_class_name('timeTbl')
tbody = tables[ReservationCourse].find_element_by_tag_name("tbody")
rows = tbody.find_elements_by_tag_name("tr")

for index, value in enumerate(rows):
    body=value.find_elements_by_tag_name("td")[1]
    reservBtn = body.find_element_by_class_name("reservBtn")
    attr = reservBtn.get_attribute('onclick')
    availableForm.append(attr)
    availableSeq.append(getSeqFromAttr(attr))


