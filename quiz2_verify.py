#!C:\Python311\python.exe
print("Content-Type:text/html\n\r")
import cgi
import pymysql

mydb=pymysql.Connect(host="localhost",user="root",password="Sachin@2106",database="recuriter")
cur=mydb.cursor()
data=cgi.FieldStorage()
value=0

a1=data.getvalue("a")
b1=data.getvalue("b")
c1=data.getvalue("c")
d1=data.getvalue("d")
e1=data.getvalue("e")
f1=data.getvalue("f")
g1=data.getvalue("g")
h1=data.getvalue("h")
i1=data.getvalue("i")
j1=data.getvalue("j")

if a1=="7":
    value+=1
else:
    value+=0
if b1=="4":
    value+=1
else:
    value+=0
if c1=="512, 64, 512":
    value+=1
else:
    value+=0
if d1=="print()":
    value+=1
else:
    value+=0
if e1=="false":
    value+=1
else:
    value+=0
if f1=="4":
    value+=1
else:
    value+=0
if g1=="abc":
    value+=1
else:
    value+=0
if h1=="_str_()":
    value+=1
else:
    value+=0
if i1=="eval":
    value+=1
else:
    value+=0
if j1=="(1,2,3)":
    value+=1
else:
    value+=0
query="insert into final_quiz values(%s)"
values=[value]
cur.execute(query,values)
mydb.commit()

cur.execute("select * from final_quiz details")
sac=cur.fetchall()
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
        background-image: url('img04.jpg');
        background-repeat: no-repeat;
        background-attachment: fixed;  
        background-size: cover;
        }
        nav{
    	display: flex;
    	align-items: center;
    	justify-content: space-between;
    	padding-top: 45px;
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
         height: 400px;
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
        </html>

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
            <div class="block">
	      <h1><center><ins>Congratulation.....!</ins> <br><br>You are Sucessfully complete the Assesment!</center></h1><br>
	      <br><h2><center>Thank you for showing your interst our recuriter review your
	      <br>Profile and Contack as soon...</center></h2><br>''')
for i in sac:
    print("<h1><center>The final quiz value is :",i[0],"<h1></center>")
    break

print('''	      
            </div>
            <button type="submit" class="btn">Log Out</button>
        </div>	
       </form>
      </body>
      </html>
      ''')


