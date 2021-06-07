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
ReservationMonth = '06'
ReservationDay = '14'

ReservationDate = ReservationYear + ReservationMonth + ReservationDay


ReservationSeq = '023'



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




reservationDateTime = datetime(int(ReservationYear), int(ReservationMonth), int(ReservationDay), 9, 0, 0)

# targetYear = int(ReservationYear)
# targetMonth = int(ReservationMonth)
# targetDay = int(ReservationDay) - 7

targetDate = reservationDateTime - timedelta(days=7)


# targetDate = datetime(targetYear, targetMonth, targetDay, targetHour, targetMinute, targetSecond)

targetYear = targetDate.year
targetMonth = targetDate.month
targetDay = targetDate.day



now = datetime.now()
prev_time = now


print('현재 시간', now)
print('예약 시간', targetDate)
print('목표 예약 날짜', reservationDateTime)
print('목표 예약 시간', Form)
driver.get(url=ReservationURL)
while(1):
  now = datetime.now()
  countDown = targetDate - now

  if(now.second - prev_time.second >= 1):
    print('예약까지 남은 시간:', countDown)

  if(now.year == targetDate.year and now.month == targetDate.month and now.day == targetDate.day and now.hour == targetDate.hour and now.minute == targetDate.minute and now.second == targetDate.second):
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

