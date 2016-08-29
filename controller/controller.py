import smtplib


class Controller():
    def __init__(self):
        self.username = 'pypijidevel@gmail.com'
        self.password = 'lolichan123'
    
    def sendMailController(self, mailRecipient, emailMessage):

        message = 'Hei howdy users\nThis is yours apps developer, you have been lost yours password right ?\nBelow is yours password\n\n"%s"\n\nDont lost yours password again next time okay ;D' %(emailMessage)

        self.server = smtplib.SMTP('smtp.gmail.com:587')
        self.server.ehlo()
        self.server.starttls()
        self.server.login(self.username, self.password)
        self.fromPypiji = 'pypijidevel@gmail.com'
        self.server.sendmail(self.username, mailRecipient, message)
        
