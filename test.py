from datetime import datetime, timedelta
import time



ReservationYear = '2021'
ReservationMonth = '06'
ReservationDay = '12'
ReservationDate = ReservationYear + ReservationMonth + ReservationDay

ReservationSeq = '023'


reservationDateTime = datetime(int(ReservationYear), int(ReservationMonth), int(ReservationDay), 9, 0, 0)
targetDateTime = reservationDateTime - timedelta(days=7)

now = datetime.now()
prev_time = now
print(reservationDateTime)
print(reservationDateTime.weekday())