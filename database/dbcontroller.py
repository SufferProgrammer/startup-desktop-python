import sqlite3 as DBS

class DBControl():
    def __init__(self):
        self.connect = DBS.connect('database/database.db')
        self.cursor = self.connect.cursor()

    def commConn(self):
        self.connect.commit()
        
    def executeQuery(self,  command):
        self.cursor.execute(command)
        
    def addUser(self,  dataGetUname,  dataGetPasswd,  dataGetMail):
        command = "INSERT INTO users(username, password, email, user_level) VALUES('%s', '%s', '%s', '2')" %(dataGetUname, dataGetPasswd,  dataGetMail)
        self.executeQuery(command)
        self.commConn()

    def loginUnameAuthenticator(self,  dataUname):
        command = "SELECT username FROM users WHERE username='%s'" %(dataUname)
        self.executeQuery(command)
        result = self.cursor.fetchone()
        return result

    def loginPasswdAutenticator(self, dataPasswd):
        command = "SELECT password FROM users WHERE password='%s'" % (dataPasswd)
        self.executeQuery(command)
        result = self.cursor.fetchone()
        return result

    def userlevelAuthenticator(self, dataUname, dataPasswd):
        command = "SELECT user_level FROM users WHERE username='%s' and password='%s'" % (dataUname, dataPasswd)
        self.executeQuery(command)
        result = self.cursor.fetchone()
        return result

    def suspendUser(self, username, email):
        command = "DELETE FROM users WHERE username='%s' AND email='%s' LIMIT 1" %(username, email)
        self.executeQuery(command)
        self.commConn()

    def getUserLevel(self, username, email):
        command = "SELECT user_level FROM users WHERE username='%s' AND email='%s' LIMIT 1" %(username, email)
        self.executeQuery(command)
        result = self.cursor.fetchone()
        return result

    def ChangeUserStatus(self, dataUname, dataPasswd, dataEmail):
        fileReadUnameFromResources = open('/tmp/project/user_name.enc', 'r')
        unameDataDecript = fileReadUnameFromResources.read()

        command = "UPDATE users SET username = '%s', password = '%s', email = '%s' WHERE username='%s'" %(dataUname, dataPasswd, dataEmail, str(unameDataDecript))
        self.executeQuery(command)
        self.commConn()

    def forgetPasswdUserSpecified(self, username, emailAddr):
        command = "SELECT password FROM users WHERE username='%s' AND email='%s' LIMIT 1" %(username, emailAddr)
        self.executeQuery(command)
        result = self.cursor.fetchone()
        return result

    def hookEmailAddr(self):
        openFileUname = open('/tmp/project/user_name.enc', 'r')
        username = openFileUname.read()
        command = "SELECT email FROM users WHERE username = '%s' LIMIT 1" %(str(username))
        self.executeQuery(command)
        result = self.cursor.fetchone()
        return result

    def connectionClose(self):
        self.connect.close()