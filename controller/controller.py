import smtplib

class Controller():
    def __init__(self):
        self.username = 'pypijidevel@gmail.com'
        self.password = 'lolichan123'
    
    def sendMailController(self,  messageFormat,  mailTo):
        self.server = smtplib.SMTP('smtp.gmail.com:587')
        self.server.ehlo()
        self.server.starttls()
        self.server.login(self.username, self.password)

        self.fromPypiji = 'pypijidevel@gmail.com'
        self.server.sendmail(self.fromPypiji, mailTo, messageFormat)
        
