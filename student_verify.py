#!C:\Python311\python.exe
print("Content-Type:text/html\n\r")
import cgi
import pymysql

data=cgi.FieldStorage()
mydb=pymysql.Connect(host="localhost",user="root",password="Sachin@2106",database="student")
cur=mydb.cursor()

c=data.getvalue("logemail")
d=data.getvalue("logpass")

cur.execute("select * from signup_details")
sac=cur.fetchall()
for i in sac:
    if i[0]==c and i[1]==d:
        print('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Capgemini</title>
            <link rel="stylesheet" href="course.css">
        </head>
        <body>
        <div class="course">
             <nav>
              <h1 class="logo">GE<span>EK</span></h1>
              <ul>
                <li><a class="active" href="visulalogin.html">Home</a></li>
                <li><a href="#services">News</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#contact">Contact</a></li>
              </ul>
             </nav>
        
            <br><br>
            <br><br><br><center><a href='quiz1.html'<button class="block"><center><h1>ZOHO Hiring Python Developer</h1><h4>Click here to more Details</h4></center></button></center></a>
            <br><br><br><center><a href='java_open_quizz.html'<button class="block"><center><h1>Capgemini Hiring Java Developer</h1><h4>Click here to more Details</h4></center></button></center></a>
        </div>
        </body>
        </html>
    ''')
        break
    else:
        print("Inccorrect E-mail/Password")
        break

