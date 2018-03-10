import MySQLdb as mysql 

# Dictionary mit Login-Infos -> Kapselung der Daten
dbConfig = {
    'user': 'Teemo', 
    'password': '1234',
    'host': '127.0.0.1'
    }

# Verbindungs-test mit der DB
# conn = mysql.connect(**dbConfig) 
# print(conn)  
# conn.close()