import smtplib
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_email = "bludhound221@gmail.com"
x = "kandarpparikh97@gmail.com"
receiver_email = []
receiver_email.append(str(x))
receiver_email.append("15it065@charusat.edu.in")
password = "<Password>"

message = MIMEMultipart("alternative")
message["Subject"] = "Vaccine Notifier test"
message["From"] = sender_email
message["To"] = ", ".join(receiver_email)

# Create the plain-text and HTML version of your message
#mymessage = "Center Name : "+str(i['name']) + "\n" + "Pincode : "+str(i['pincode']) + "\n" +"Vaccines Available : "+ \
                #str(i['available_capacity']) + "\n"
part1 = MIMEText("Hi kandarp", "plain")
message.attach(part1)
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
