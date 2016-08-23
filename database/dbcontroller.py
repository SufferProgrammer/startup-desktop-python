import mysql.connector as mariaDB

class DBControl():
    def __init__(self):
        self.connect = mariaDB.connect(host = '127.0.0.1',  user='developer', password = '',  database = 'project_db' )
        self.cursor = self.connect.cursor()

        
    def commConn(self):
        self.connect.commit()
        
    def executeQuery(self,  command):
        self.cursor.execute(command)
        
    def addUser(self,  dataGetUname,  dataGetPasswd,  dataGetMail):
        command = "INSERT INTO users(username, password, email, user_level) VALUES('%s', '%s', '%s', '2')" %(dataGetUname, dataGetPasswd,  dataGetMail)
        self.executeQuery(command)
        self.commConn()

    def loginUnameAuthenticator(self,  data):
        command = "SELECT username FROM users WHERE username='%s'" %(data)
        self.executeQuery(command)
        result = self.cursor.fetchone()
        return result

    def getId(self):
        command = "SELECT id FROM users WHERE username='%s' LIMIT 1" %(unameDataDecript)
        fileReadUnameFromResources.close()
        self.executeQuery(command)
        result = self.cursor.fetchone()
        return result

    def loginPasswdAutenticator(self, data):
        command = "SELECT password FROM users WHERE username='%s'" % (data)
        self.executeQuery(command)
        result = self.cursor.fetchone()
        return result

    def userlevelAuthenticator(self, dataUname, dataPasswd):
        command = "SELECT user_level FROM users WHERE username='%s' and password='%s'" % (dataUname, dataPasswd)
        self.executeQuery(command)
        result = self.cursor.fetchone()
        return result

    def suspendUser(self, username):
        command = "DELETE FROM users WHERE username='%s' LIMIT 1" %(username)
        self.executeQuery(command)
        self.commConn()

    def ChangeUserStatus(self, dataUname, dataPasswd, dataEmail):
        fileReadUnameFromResources = open('/tmp/project/user_name.enc', 'r')
        unameDataDecript = fileReadUnameFromResources.read()

        command = "UPDATE users SET username = '%s', password = '%s', email = '%s' WHERE username='%s'" %(dataUname, dataPasswd, dataEmail, str(unameDataDecript))
        self.executeQuery(command)
        self.commConn()

    def connectionClose(self):
        self.connect.close()