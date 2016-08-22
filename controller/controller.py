import smtplib

class Controller():
    def __init__(self):
        self.username = 'pypijidevel@gmail.com'
        self.password = 'lolichan123'
    
    def sendMailController(self,  messageFormat,  mailTo):
        self.server = smtplib.SMTP('smtp.gmail.com:587')
        self.server.ehlo()
        self.server.starttls()
        self.server.login(self.password,  self.username)

        self.massage = messageFormat
        self.mailto = mailTo
        self.fromPypiji = 'pypijidevel@gmail.com'
        self.server.sendmail(self.fromPypiji, self.mailto,  self.message)
        
