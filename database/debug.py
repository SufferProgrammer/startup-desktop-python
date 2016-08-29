from dbcontroller import *
import os


db = DBControl()
data = 'developer'
data2 = 'pijipirma@gmail.com'
res = db.forgetPasswdUserSpecified(data, data2)

print res