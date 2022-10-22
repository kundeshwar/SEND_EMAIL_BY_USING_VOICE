import smtplib as S

ob = S.SMTP("smtp.gmail.com",587)
ob.ehlo()
ob.starttls()
ob.login("kundeshwar15000@gmail.com","Kundeshwar15@")
subject = "test python code"
body = "lovely python"
msg = "subject:{}\n\n{}".format(subject,body)
list_1 = ["22m1428@iitb.ac.in"]
ob.sendmail("kundeshwar15000@gmail.com")
print("mail is sended")