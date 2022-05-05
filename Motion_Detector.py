'''
This Motion detector code senses the motion of an object and alerts the user 
with an email notification when detects motion.
'''


import RPi.GPIO as GPIO
import drivers
from time import sleep
import time
import smtplib
from datetime import datetime

ledPin = 12
sensorPin = 11
display = drivers.Lcd()

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(sensorPin, GPIO.IN)
    
    
def loop():
    while True:
        try:
            if GPIO.input(sensorPin)==GPIO.HIGH:
                GPIO.output(ledPin, GPIO.HIGH)
                now = datetime.now()
                
                print ("Motion Detected at " + now.strftime("%d/%m/%Y %H:%M:%S"))
                display.lcd_display_string("Motion Detected", 1)  # Write line of text to first line of display
                
                gmail_user = '[Enter the sender mail id]'
                gmail_password = '[Enter the password]'

                sent_from = gmail_user
                to = '[Enter the recipient mail id]'
                subject = 'Iot Research Motion Detector'
                body = 'Motion Sensed at ' + now.strftime("%d/%m/%Y %H:%M:%S")

                email_text = """\
From: %s
To: %s
Subject: %s

%s
                """ % (sent_from, ", ".join(to), subject, body)
                print(email_text)
                smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                smtp_server.ehlo()
                smtp_server.login(gmail_user, gmail_password)
                smtp_server.sendmail(sent_from, to, email_text)
                smtp_server.close()
                print ("Email sent successfully!")
                sleep(60)
                
            else:
                GPIO.output(ledPin, GPIO.LOW)
                #print ("Motion Stopped")
                display.lcd_display_string("No Motion Sensed", 1)  # Write line of text to first line of display
                #sleep(5)
            
        except Exception as e:
            print('Operation failed!')
            print('Exception message: ' + str(e))
                #exit(1)

            
def destroy():
    display.lcd_clear()
    GPIO.cleanup()

    
if __name__ == '__main__':
    print ("Program is starting...")
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()