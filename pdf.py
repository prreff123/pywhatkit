from pdf_mail import sendpdf

file = sendpdf("priyanshujain09062003@gmail.com",
               "pj7779732@gmail.com",
               "######sender_email######",
               "pdf document",
               "body of message",
               "Priyanshu_Jain Resume",
               "C:/Users/asus/Downloads/pywhatkit/Priyanshu_Jain Resume")
file.email_send()