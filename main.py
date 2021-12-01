import smtplib, ssl

port = 465  # For SSL
password = "cSwkMTPKRF"

# Create a secure SSL context
context = ssl.create_default_context()

FROM = "no-reply@gabrielmarin.com.ar"
TO = ["soldebenedet@gmail.com"]
SUBJECT = "CRON TEST"
TEXT = "This message was sent with Python's smtplib."
mail_message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

with smtplib.SMTP_SSL("vps-1831058-x.dattaweb.com", port, context=context) as server:
    server.login("no-reply@gabrielmarin.com.ar", password)
    # TODO: Send email here
    server.sendmail("no-reply@gabrielmarin.com.ar","soldebenedet@gmail.com",mail_message)
    server.quit()