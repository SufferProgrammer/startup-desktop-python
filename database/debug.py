from dbcontroller import *
import os


db = DBControl()
data = 'developer'
data2 = 'developer'
res = db.userlevelAuthenticator(data, data2)

intRes = int(''.join(map(str, res)))
data = intRes
data3 = db.getId()

print data3

if intRes == 1:
    print 'admin level'

else:
    print 'user level'
