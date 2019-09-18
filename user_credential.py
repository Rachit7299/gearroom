#!c:\Python35\python.exe
import cgi
import mysql.connector
form=cgi.FieldStorage()
user=form.getvalue("t1")
pswd=form.getvalue("t2")
print("""
""")
try:
    con=mysql.connector.connect(user='root',password='root',host='localhost',database='pythondemo')
    cursor=con.cursor()
    sql="select * from register where username='{username}' and password='{password}'".format(username=user,password=pswd)
    cursor.execute(sql)
    row=cursor.fetchall()
    if(len(row)>=1):
        print("""
              <html>
              <head>
               <script>
               window.location.href="http://localhost/gearroom/home.py";
               </script>
              </head>
              </html>
""")
    else:
        print("""
              <html>
              <head>
               <script>
                window.alert("Invalid Username or Password");
                window.location.href="http://localhost/gearroom/login.html";
               </script>
              </head>
              </html>
            """)
except Exception as e:
    print(e)

