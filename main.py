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

ID = '111346'
Password = '8012'


ReservationYear = '2021'
ReservationMonth = '05'
ReservationDay = '18'

ReservationDate = ReservationYear + ReservationMonth + ReservationDay



ReservationSeq = '024'



inputID = 'memberId'
inputPW = 'memberPw'

LoginURL = 'https://www.daegucc.co.kr/Member/Login'
ReservationURL = 'https://www.daegucc.co.kr/Booking/ReservationCalendar?day=' + ReservationDate
# 
Form = 'ReservationForm(\'160\', \'' + ReservationDay + '\', \'' + ReservationSeq + '\');'
ReservationOK = 'Reservation(\'ok\');'
# Form = 'ReservationForm('160','20210512','001');'

# driver = webdriver.Chrome(executable_path='chromedriver')

# #Goto Login
# driver.get(url=LoginURL)
# #Login
# idBox = driver.find_element_by_id(inputID)
# idBox.send_keys(ID)
# pwBox = driver.find_element_by_id(inputPW)
# pwBox.send_keys(Password)
# driver.execute_script('login()')

# #Login alert
# result = driver.switch_to_alert()
# result.accept()




# #Goto Reservation
# driver.get(url=ReservationURL)


targetYear = int(ReservationYear)
targetMonth = int(ReservationMonth)
targetDay = int(ReservationDay) - 7
targetHour = 9
targetMinute = 0
targetSecond = 0

targetDate = datetime(targetYear, targetMonth, targetDay, targetHour, targetMinute, targetSecond)

# print(targetDate.minute-now.minute, '분 ', targetDate.second - now.second, '초 뒤 예약을 시작합니다.')


now = datetime.now()
prev_time = now


while(1):
  now = datetime.now()
  countDown = targetDate - now


  print('예약까지 남은 시간:', countDown)

  prev_second = now.second

  if(now.date == targetDate):
    #Send Form
    # driver.execute_script(Form)
    # driver.execute_script(ReservationOK)
    break

