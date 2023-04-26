#!C:\Python311\python.exe
print("Content-Type:text/html\n\r")
import cgi
import pymysql

mydb=pymysql.Connect(host="localhost",user="root",password="Sachin@2106",database="recuriter")
cur=mydb.cursor()
data=cgi.FieldStorage()
value=0

q1=data.getvalue("a")
q2=data.getvalue("b")
q3=data.getvalue("c")
q4=data.getvalue("d")
q5=data.getvalue("e")
q6=data.getvalue("f")
q7=data.getvalue("g")
q8=data.getvalue("h")
q9=data.getvalue("i")
q10=data.getvalue("j")

if q1==".py":
    value+=1
else:
    value+=0
if q2=="None of the mentioned":
    value+=1
else:
    value+=0
if q3=="def":
    value+=1
else:
    value+=0
if q4=="Class":
    value+=1
else:
    value+=0
if q5=="eval":
    value+=1
else:
    value+=0
if q6=="Built-in function & User defined function":
    value+=1
else:
    value+=0
if q7=="Preferred Installer Program":
    value+=1
else:
    value+=0
if q8=="Indentation":
    value+=1
else:
    value+=0
if q9=="All of the mentioned":
    value+=1
else:
    value+=0
if q10=="Yes":
    value+=1
else:
    value+=0
query="insert into quiz_value values(%s)"
values=[value]
cur.execute(query,values)
mydb.commit()

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
	    <br><br><br<br><br><h1><center><ins>Congrats.....!</ins> <br>You are eligible for our Online Course!</center></h1><br>
	    <br><br><br><br><br><center><a href='content1.html'><button class="black"><center><h2 style:"color:white"><ins>Click Here to Start Online Course</ins></h2></center></button></center></a>
        </div>
      </body>
</html>
''')
