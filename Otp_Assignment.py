#Importing requires libraries
import smtplib
import random
from twilio.rest import Client

#User and Twilio info
account_sid = 'AC1a01a4fd1cc7cdbb358e19fe12b9ce93'
auth_token = '1fbcb17dfe649c3d4476b8d0330e07dc'
client = Client(account_sid, auth_token)
twilio_num = '+16175551212'#Importing requires libraries
import smtplib
import random
from twilio.rest import Client

#User and Twilio info
account_sid = 'AC1a01a4fd1cc7cdbb358e19fe12b9ce93'
auth_token = '1fbcb17dfe649c3d4476b8d0330e07dc'
client = Client(account_sid, auth_token)
twilio_num = '+1617555121'
target = '+916006770037'

#Function to generate OTP
def generateOtp(n = 6):
    otp = ""
    for i in range(n):
        otp += str(random.randint(0, 9))
    return otp

#Function to validate mobile
def validateMobile(mobile):
    return len(mobile) == 10 and mobile.isdigit()

#Function to validate Email
def validateEmailID(receiver):
    if "@" not in receiver or "." not in receiver:
        return False
    return True

# Send OTP over mobile using Twilio
def sendOTPOverMobile(target, otp):
    if(validateMobile(target)):
        target = "+91" + target
        message = client.messages.create(
            body = "Your OTP is " + otp + ". Valid for next 15 minutes.",
            from_= twilio_num,
            to=target
        )

        print(message.body)
        print("Check Phone! Sent to ", target)
    else:
        print("Enter valid mobile number!!")

# Send OTP over email using SMTP
def sendOTPOverEmail(receiver, otp):
    body = "Your OTP is " + otp + ". Valid for next 15 minutes."

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, body)

    print("Mail sent - OTP: ", otp)


#Driver Code
if _name_ == "_main_":

    print("Welcome to Random OTP sender!!\nHere, we send random OTPs to phone number and mails.\n")

    sender = "kirankesar00@gmail.com"
    password = "090909"
    # User input for email
    receiver = input("Enter mail: ")

    #create a unique Otp
    otp = generateOtp(6)

    #Send OTP over Email
    if(validateEmailID(receiver)):"
    "
        sendOTPOverEmail(receiver, otp)
    else:
        print("Please Enter valid mail!!")


    #Send OTP over SMS
    send_twilio = input("\nDo you want to send OTP via SMS: ")
    if send_twilio.lower() == "yes":
        # User input for mobile
        target = input("Enter mobile: ")

        sendOTPOverMobile(target, otp)
        
        print("\nOTP sending program ended\n")
    else:
        print("OTP sending program ended")

    #Program Ended