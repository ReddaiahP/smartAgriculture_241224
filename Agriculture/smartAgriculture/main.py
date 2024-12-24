import mysql.connector
import random
import time
from twilio.rest import Client

# Connect to MySQL server

connection = mysql.connector.connect(
    host="database1.cdosgqg2ixnv.us-east-1.rds.amazonaws.com",
    user="admin",
    password="adminadmin",
    database="Agriculture"
)

# Create a cursor object to execute SQL queries

cursor = connection.cursor()
motor_status =''

while 1:

    t = random.randint(1,50)
    h = random.randint(1, 50)
    m = random.randint(1, 100)


    # if m<30:

        # account_sid = 'ACc6ee1400a2cda41f282868ec45f70a00'
        # auth_token = '8ac974ef114f03b2f6217d7f3ef0cbb9'
        # client = Client(account_sid, auth_token)
        #
        # message = client.messages.create(
        #     from_='+12512410914',
        #     body='Hello your crop is running out of water please visit once..',
        #     to='+919550284810'
        # )



    if m > 50:
        motor_status = "OFF"
    else:
        motor_status = "ON"

    insert_query = "INSERT INTO myApp_agriculture (motor, temp, humidity, soil_moisture) VALUES (%s, %s, %s, %s)"
    data_to_insert = (motor_status, t, h, m)

    cursor.execute(insert_query, data_to_insert)
    connection.commit()

    print(f'motor_status: {motor_status} Temperature: {t}  Humidity: {h}  Moisture: {m}')
    time.sleep(1)

cursor.close()
connection.close()



