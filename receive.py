#!C:/python/python.exe
import pymysql
import cgi
print ("Content-Type: text/html \n\n")
con = pymysql.connect(host='localhost',user='root',passwd='',db='id2350504_topics')
cursor = con.cursor()
cursor.execute("SELECT Domain_name FROM Domain")
for row in cursor:
	li=[row[0]]
	s=''.join(li)
	print(s)
	print("#")
cursor.close()
con.close()