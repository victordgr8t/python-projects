import smtplib

# Set up the SMTP server
server = smtplib.SMTP('smtp-mail.outlook.com', 587)
server.starttls()
server.login("creativedirector01@outlook.com", "President101")

# Set the email content
subject = "Hello from Nnamdi"
body = "This is a test mail Dont get it twister."
msg = f"Subject: {subject}\n\n{body}"

# Send the email
server.sendmail("creativedirector01@outlook.com",
                "nnamdimodebe@gmail.com", msg)

# Disconnect from the server
server.quit()
