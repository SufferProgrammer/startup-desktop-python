from dbcontroller import *

db = DBControl()
data = 'developer'
data2 = 'developer'
res = db.userlevelAuthenticator(data, data2)

intRes = int(''.join(map(str, res)))

#print intRes
if intRes == 1:
    print 'admin level'

else:
    print 'user level'
