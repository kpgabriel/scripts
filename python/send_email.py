import smtplib
import getpass

SERVER = "smtp-mail.outlook.com"
FROM = "kyle.gabriel@capgemini.com"
TO = ["kyle.gabriel@capgemini.com","kpgabriel17@gmail.com"] # must be a list

SUBJECT = "Hello! %s" % (TO[0].split('.')[0])
TEXT = """This is a email sent programatically. 
        \nYou have 3 wishes from the magic genie Fooswaldo. Fooswaldo is real. Just like your passion for FanFic +2 Creativity and +2 Charm.\n#LevelUpFam."""

# Prepare actual message
message = """From: %s\r\nTo: %s\r\nSubject: %s\r\n\

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

try:
        # Send the mail
        server = smtplib.SMTP(SERVER)
        server.connect(SERVER)
        server.ehlo()
        server.starttls()
        server.login(FROM, getpass.getpass() )
        server.sendmail(FROM, TO, message)
        server.quit()
except:
        print("Error: Password not correct")
