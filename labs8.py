import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login("prajwalbiradar75@gmail.com", "prajwalkfi") 
  
# message to be sent 
message = "hi,how r you "
  
# sending the mail 
s.sendmail("prajwalbiradar75@gmail.com", "vishnusharmananda@gmail.com", message) 
  
# terminating the session 
s.quit() 