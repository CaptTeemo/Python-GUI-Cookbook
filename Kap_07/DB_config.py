import MySQLdb as mysql 

# Dictionary mit Login-Infos
dbConfig = {
    'user': 'Teemo', 
    'password': 'deluxe22',
    'host': '127.0.0.1'
    }

# Verbindungs-test mit der DB
# conn = mysql.connect(**dbConfig) 
# print(conn)  
# conn.close()