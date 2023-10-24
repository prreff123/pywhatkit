import smtplib as s
ob = s.SMTP("smtp.gmail.com",587)
ob.starttls()

ob.login("priyanshujain09062003@gmail.com",'ozge talc hxyv tsig')

subject = "Sending email using python"
body = "This is a tutorial for how to send email using python"

message = "Subject:{}\n\n{}".format(subject,body)
# print(message)
listofAddress = ["pj7779732@gmail.com"]
ob.sendmail("priyanshujain09062003",listofAddress,message)
print("send successfully......")
ob.quit()