#!C:\Python311\python.exe
print("Content-Type:text/html\n\r")
import cgi
import pymysql

data=cgi.FieldStorage()
mydb=pymysql.Connect(host="localhost",user="root",password="Sachin@2106",database="recuriter")
cur=mydb.cursor()

c=data.getvalue("verifymail")
d=data.getvalue("verifypass")
cur.execute("select * from login_details")
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
        </head>
<style>
body{
        background-image: url('img22.jpg');
        background-repeat: no-repeat;
        background-attachment: fixed;  
        background-size: cover;
        }
        nav{
    	display: flex;
    	align-items: center;
    	justify-content: space-between;
    	padding-top: 30px;
    	padding-left: 8%;
    	padding-right: 8%;
        }

        .logo{
    	color: white;
    	font-size: 35px;
	letter-spacing: 1px;
	cursor: pointer;
        }
        span{
    	color: #f9004d;
        }
        nav ul li{
    	list-style-type: none;
    	display: inline-block;
    	padding: 10px 25px;
        }
        nav ul li a{
    	color: white;
    	text-decoration: none;
    	font-weight: bold;
    	text-transform: capitalize;
        }
        nav ul li a:hover{
	color: #f9004d;
    	transition: .4s;
        }
        .block{
         position: relative;
         width: 800px;
         height: 440px;
         right:-250px;
         top:-10px;
         color: white;
         background: transparent;
         border: 2px solid rgba(255, 255, 255, .5);
         border-radius: 20px;
         backdrop-filter: blur(20px);
         box-shadow: 0 0 30px rgba(0, 0, 0, .5);
        
         }
         .block .form-box{
	  width: 100%;
	  padding: 40px;
	  }
	  .block h1{
	  right:10%;

	  }
          .btn{
            width: 10%;
            height: 45px;
            background: white;
            border: 2px solid transparent;
            font-weight: bold;
            font-size: 1rem;
            color: black;
            cursor: pointer;
            padding: 10px 10px;
            margin: 2px 580px;
            border-radius: 30px;
            transition: transform.4s;
            }
            .btn:hover{
             transform: scale(1.2);
            }
</style>
      <body>
       <form action=visulalogin.html>
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
        </div>
       </form>
      </body>
      </html>
      ''')
    break
cur.execute("select * from final_quiz details")
sac=cur.fetchall()
for i in sac:
    quiz_mark=i[0]
    print('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <title>Webpage Design</title>
        <link rel="stylesheet" href="python_student_final.css">
<style>
        th,td{
	border:1px solid black;
	border-collapse:collapse;
	background-color:white;
	border-radius:10px;
	border-style:ridge;
	border-color:blue;
	color: black;
	padding:15px;
	border-spacing:40px;
        }
        tr:nth-child(even){
	background-color:black;
        }
        .btn{
            width: 10%;
            height: 45px;
            background: white;
            border: 2px solid transparent;
            font-weight: bold;
            font-size: 1rem;
            color: black;
            cursor: pointer;
            padding: 10px 10px;
            margin: 2px 580px;
            border-radius: 30px;
            transition: transform.4s;
            }
            .btn:hover{
             transform: scale(1.2);
            }
</style>
        </head>
        <body>
        <form action=visulalogin.html>
        <table style="width:100%">
	<br><br><br><h1 style="color:white"><center>Student Details</center></h1>
	<tr style="height:50px">
		<th style="width:20%;height:50%">Student Name</th>
		<th>Student Mail Id</th>
		<th>Student Mobile Number</th>
		<th>Student Entrance Quiz Score</th>
		<th>Student Final Quiz Score</th>
	</tr>
	<tr>
	''')
    break
cur.execute("select * from quiz_value details")
vei=cur.fetchall()
for i in vei:
    enter_quiz=i[0]
for i in i[0]:
    print("<td><center>K.Sachinpandi</center></td>")
    print("<td><center>sachinpandi6444@gmail.com</center></td>")
    print("<td><center>6385560918</center></td>")
    print("<td><center>",enter_quiz,"</center></td>")
    print("<td><center>",quiz_mark,"</center></td>")
    print('''
        </tr>
        </table>
    	<br><br><br><button type="submit" class="btn">Log Out</button>
    	</form>
        </body>
        </html>
        ''')



