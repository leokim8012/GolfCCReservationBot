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

ID = '111763'
Password = '3359'


inputIDElement = 'memberId'
inputPWElement = 'memberPw'

LoginURL = 'https://www.daegucc.co.kr/Member/Login'

driver = webdriver.Chrome(executable_path='chromedriver')

#Goto Login
driver.get(url=LoginURL)
#Login
idBox = driver.find_element_by_id(inputIDElement)
idBox.send_keys(ID)
pwBox = driver.find_element_by_id(inputPWElement)
pwBox.send_keys(Password)
driver.execute_script('login()')

#Login alert
result = driver.switch_to_alert()
result.accept()




ReservationYear = '2021'
ReservationMonth = '06'
ReservationDay = '20'
ReservationDate = ReservationYear + ReservationMonth + ReservationDay

ReservationURL = 'https://www.daegucc.co.kr/Booking/ReservationCalendar?day=' + ReservationDate


# 2021/06/07 주문 20일(일) seq 14, 20(7:31, 8:13) 예약
ReservationSeq = '020'
Form = 'ReservationForm(\'160\', \'' + ReservationDate + '\', \'' + ReservationSeq + '\');'
ReservationOK = 'Reservation(\'ok\');'


reservationDateTime = datetime(int(ReservationYear), int(ReservationMonth), int(ReservationDay), 9, 0, 0)

if(reservationDateTime.weekday() == 6):
  targetDateTime = reservationDateTime - timedelta(days=12)
elif(reservationDateTime.weekday() == 5):
  targetDateTime = reservationDateTime - timedelta(days=11)
else:
  targetDateTime = reservationDateTime - timedelta(days=7)

now = datetime.now()
prev_time = now

print('목표 예약 날짜', reservationDateTime)
print('목표 예약 시간', Form)

print('예약 실행 시간', targetDateTime)
print('현재 시간', now)

driver.get(url=ReservationURL)



while(1):
  now = datetime.now()
  countDown = targetDateTime - now

  if(now.second - prev_time.second >= 1):
    print('예약까지 남은 시간:', countDown)

  if(now.year == targetDateTime.year and now.month == targetDateTime.month and now.day == targetDateTime.day and now.hour == targetDateTime.hour and now.minute == targetDateTime.minute and now.second == targetDateTime.second):
    startingTime = now
    print('시작 시간', startingTime)


    #Goto Reservation
    print('폼 입력 중')
    #Send Form
    print(Form)
    driver.execute_script(Form)
    print('폼 작성 완료')

    print('예약 확인 중')

    print(ReservationOK)
    driver.execute_script(ReservationOK)
    print('예약 완료')
    
    result = driver.switch_to_alert()
    result.accept()

    endTime = now
    print('종료 시간', endTime)
    print('총 소요 시간: ', endTime - startingTime)
    break

  prev_time = now

