#!C:/python/python.exe
import cgi
print ("Content-Type: text/html \n\n")
formData=cgi.FieldStorage()
firstname = formData.getvalue("name")
import pymysql
conn = pymysql.connect(host= "localhost",user="root",passwd="",db="id2350504_topics")
x = conn.cursor()
try:
   x.execute("""INSERT INTO Domain VALUES (%s,%s)""",(8,firstname))
   conn.commit()
except:
   conn.rollback()
conn.close()