#  +=================================+
#  |  MARVIN IS A LAZY SHIT v 1.0.0  |
#  +=================================+

import smtplib, ssl

print("+==============================+")
print("|   WELCOME TO MARVIN IS A     |")
print("|     LAZY SHIT V 1.0.0        |")
print("+==============================+")
input("\nYou now weild great power. Don't be a clown, use it responsibly. Press enter to continue...")

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "marvin@helium.com"
print("\nConnecting to SMTP server with " + sender_email)
password = input("Type your password and press enter:")

emails = open("email-input.txt")
messageFile = open("message.txt")
messageContents = messageFile.read()

input("\n\nOnce you pass through this command, emails will be immediately sent to every person specified on your inputs. If you're sure this is what you want to do, press enter.")


context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)



    #loop through email inputs
    emailLine = emails.readline()
    while emailLine != "":
        if len(emailLine.split()) > 1:
            receiver_email = emailLine.split()[0]
            receiver_name = " " + emailLine.split()[1]
        else:
            receiver_email = emailLine[:-1]
            receiver_name = ""
            
        message = messageContents.replace("REPLACENAME", receiver_name).replace("DONTTOUCH", receiver_email)

        #sends the email through SMTP server
        server.sendmail(sender_email, receiver_email, message)
        

        print("Email to " + receiver_email + " successful!")
        emailLine = emails.readline()
