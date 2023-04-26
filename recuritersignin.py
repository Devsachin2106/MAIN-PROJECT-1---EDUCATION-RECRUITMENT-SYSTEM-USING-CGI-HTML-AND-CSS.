#!C:\Python311\python.exe
print("Content-Type:text/html\n\r")

import cgi
import pymysql

mydb=pymysql.Connect(host="localhost",user="root",password="Sachin@2106",database="recuriter")
cur=mydb.cursor()

print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Capgemini</title>
    <link rel="stylesheet" href="studentcss.css">
</head>
<style>
body {
  background-image: url('img08.jpg');
  background-repeat: no-repeat;
  background-attachment: fixed;  
  background-size: cover;
}
</style>
<body>
    <div class="wrapper">
        <div class="form-box login">
            <h1>SignUp</h1>
            <form action="recuriterlogin.py" method="post">
                <div class="input-box">
                    <span class="icon">
                        <ion-icon name="person-circle-outline"></ion-icon>
                    </span>
                    <input Type="text" name="user"required>
                    <label>Username</label>
                </div>
                <div class="input-box">
                    <span class="icon">
                        <ion-icon name="mail-outline"></ion-icon>
                    </span>
                    <input Type="email"  name="mail" required>
                    <label>Email</label>
                </div>
                <div class="input-box">
                    <span class="icon"><ion-icon name="lock-closed-outline"></ion-icon>
                    </span>
                    <input Type="password" name="password"required>
                    <label>Password</label>
                </div>
                <button type="submit" class="bton">SingUp</button>
                <div class="login-register">
                    <p>Already have a account ? <a 
                    href="recuriterlogin.py" class="register-link">LogIn</a></p>
        </div>
    </div>
    <script type="module" src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.esm.js"></script>
    <script nomodule src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.js"></script>

</body>
</html>
''')
