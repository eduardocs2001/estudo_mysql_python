import MySQLdb as mysql

hostname = '127.0.0.1:3306'
username = 'root'
password = 'senha'
db = 'menu'



mydb = mysql.Connect(host= hostname,
                     user= username, 
                     passwd= password, 
                     db= db)

cursor = mydb.cursor()
