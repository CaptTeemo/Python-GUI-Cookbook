# Grundaufbau Cursor anlegen und am Schluss wieder löschen ist gleich
# einzig das Kommando in .execute("") ist entsprechendes SQL
# if __name__ == '__main__':  Erlaubt das Testen einer Klasse im selben File!!!


import MySQLdb as mysql 
import DB_config as guiConf 

class MySQL():
    # class variable
    GUIDB  = 'GuiDB'   
     
    #------------------------------------------------------
    def connect(self):
        # Verbinden mit der DB -> entpacken des Wörterbuchs mit (**)
        conn = mysql.connect(**guiConf.dbConfig)
    
        # Cursor auf die DB erzeugen
        cursor = conn.cursor()    
            
        return conn, cursor
    
    #------------------------------------------------------    
    def close(self, cursor, conn):        
        # Cursor löschen + verbindung beenden
        cursor.close()
        conn.close()    

    #------------------------------------------------------        
    def showDBs(self):
        # connect to MySQL
        conn, cursor = self.connect()        
        
        # Datenbanken anzeigen
        cursor.execute("SHOW DATABASES")
        print(cursor)
        print(cursor.fetchall())

        # Cursor löschen + Verbindung trennen
        self.close(cursor, conn)
                   
    #------------------------------------------------------
    def createGuiDB(self):
        # connect to MySQL
        conn, cursor = self.connect()
        
        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(MySQL.GUIDB))
        except mysql.Error as err:
            print("Failed to create DB: {}".format(err))        

        # Cursor löschen + Verbindung trennen
        self.close(cursor, conn) 

    #------------------------------------------------------
    def dropGuiDB(self):
        conn, cursor = self.connect()
        try:
            cursor.execute(
                "DROP DATABASE {}".format(MySQL.GUIDB))
        except mysql.Error as err:
            print("Failed to drop DB: {}".format(err))        

        # close cursor and connection
        self.close(cursor, conn) 
             
    #------------------------------------------------------        
    def useGuiDB(self, cursor):
        # Erwartet Verbindung zur GUI
        cursor.execute("USE guidb")
                      
    #------------------------------------------------------
    def createTables(self):
        conn, cursor = self.connect()
    
        self.useGuiDB(cursor)
        
        # Tabelle Books erzeugen
        cursor.execute("CREATE TABLE Books (       \
              Book_ID INT NOT NULL AUTO_INCREMENT, \
              Book_Title VARCHAR(25) NOT NULL,     \
              Book_Page INT NOT NULL,              \
              PRIMARY KEY (Book_ID)                \
            ) ENGINE=InnoDB")
        
        # Tabelle Quotations erzeugen
        cursor.execute("CREATE TABLE Quotations ( \
                Quote_ID INT AUTO_INCREMENT,      \
                Quotation VARCHAR(250),           \
                Books_Book_ID INT,                \
                PRIMARY KEY (Quote_ID),           \
                FOREIGN KEY (Books_Book_ID)       \
                    REFERENCES Books(Book_ID)     \
                    ON DELETE CASCADE             \
            ) ENGINE=InnoDB")   
            
        # Schließen
        self.close(cursor, conn) 
        
    #------------------------------------------------------
    def createTablesNoFK(self):
        conn, cursor = self.connect()
    
        self.useGuiDB(cursor)
        
        # create Table inside DB
        cursor.execute("CREATE TABLE Books (       \
              Book_ID INT NOT NULL AUTO_INCREMENT, \
              Book_Title VARCHAR(25) NOT NULL,     \
              Book_Page INT NOT NULL,              \
              PRIMARY KEY (Book_ID)                \
            ) ENGINE=InnoDB")
                
        # create second Table inside DB -- 
        # No FOREIGN KEY relation to Books Table
        cursor.execute("CREATE TABLE Quotations ( \
                Quote_ID INT AUTO_INCREMENT,      \
                Quotation VARCHAR(250),           \
                Books_Book_ID INT,                \
                PRIMARY KEY (Quote_ID)            \
            ) ENGINE=InnoDB")   
            
        # close cursor and connection
        self.close(cursor, conn) 
          
    #------------------------------------------------------
    def dropTables(self):
        conn, cursor = self.connect()
    
        self.useGuiDB(cursor)
        # Löschen der Tabellen
        cursor.execute("DROP TABLE quotations")
        cursor.execute("DROP TABLE books")   
    
        # close cursor and connection
        self.close(cursor, conn)    

    #------------------------------------------------------
    def showTables(self):
        conn, cursor = self.connect()
    
        # Namen der Tabellen ausgeben
        cursor.execute("SHOW TABLES FROM guidb") 
        print(cursor.fetchall())
        
        self.close(cursor, conn)          
            
    #------------------------------------------------------        
    def insertBooks(self, title, page, bookQuote):
        conn, cursor = self.connect()
        
        self.useGuiDB(cursor)
        
        # NEue DAten einfügen
        cursor.execute("INSERT INTO books (Book_Title, Book_Page) VALUES (%s,%s)", (title, page))

        # Schlüssel_ID automatisch hochzählen
        keyID = cursor.lastrowid 
                
        cursor.execute("INSERT INTO quotations (Quotation, Books_Book_ID) VALUES (%s, %s)", \
                       (bookQuote, keyID))
                
        # Commit -> Wichtig, damit Änderungen übernommen werden 
        conn.commit ()

        # close cursor and connection
        self.close(cursor, conn)

    #------------------------------------------------------              
    def showBooks(self):
        # connect to MySQL
        conn, cursor = self.connect()    
        
        self.useGuiDB(cursor)    
        
        # print results
        cursor.execute("SELECT * FROM Books")
        allBooks = cursor.fetchall()
        print(allBooks)

        # close cursor and connection
        self.close(cursor, conn)   
        
        return allBooks     

    #------------------------------------------------------        
    def showColumns(self):
        conn, cursor = self.connect()   
        
        self.useGuiDB(cursor)      
         
        #cursor.execute("SHOW COLUMNS FROM quotations")
        #print(cursor.fetchall())
        
        #Schönere Darstellung:
        print('\n Pretty Print:\n--------------') 
        from pprint import pprint
        cursor.execute("SHOW COLUMNS FROM quotations")
        pprint(cursor.fetchall())

        self.close(cursor, conn) 
        
    #------------------------------------------------------        
    def showData(self):
        conn, cursor = self.connect()   
        self.useGuiDB(cursor)      
         
        cursor.execute("SELECT * FROM books")
        print(cursor.fetchall())

        cursor.execute("SELECT * FROM quotations")
        print(cursor.fetchall())
        
        self.close(cursor, conn) 
        
    #------------------------------------------------------        
    def showDataWithReturn(self):
        conn, cursor = self.connect()       
        self.useGuiDB(cursor)      
         
        cursor.execute("SELECT * FROM books")
        booksData = cursor.fetchall()

        cursor.execute("SELECT * FROM quotations")
        quoteData = cursor.fetchall()
        
        self.close(cursor, conn) 
        
        # print(booksData, quoteData)
        for record in quoteData:
            print(record)
        
        return booksData, quoteData
        
    #------------------------------------------------------        
    def updateGOF(self):
        conn, cursor = self.connect()          
        self.useGuiDB(cursor)      
         
        # Update des Zitats
        cursor.execute("SELECT Book_ID FROM books WHERE Book_Title = 'Design Patterns'")
        primKey = cursor.fetchall()[0][0]

        cursor.execute("SELECT * FROM quotations WHERE Books_Book_ID = (%s)", (primKey,))
        
        cursor.execute("UPDATE quotations SET Quotation = (%s) WHERE Books_Book_ID = (%s)", \
                       ("Pythonic Duck Typing: If it walks like a duck and talks like a duck it probably is a duck...", primKey))

        conn.commit ()            
        cursor.execute("SELECT * FROM quotations WHERE Books_Book_ID = (%s)", (primKey,))
        
        self.close(cursor, conn) 
 
    #------------------------------------------------------        
    def deleteRecord(self):
        conn, cursor = self.connect()        
        self.useGuiDB(cursor)      
        
        try: 
            # Eintrag in Tabelle löschen
            cursor.execute("SELECT Book_ID FROM books WHERE Book_Title = 'Design Patterns'")
            primKey = cursor.fetchall()[0][0]
            
            cursor.execute("DELETE FROM books WHERE Book_ID = (%s)", (primKey,))
    
            conn.commit ()
        except:
            pass
               
        # close cursor and connection
        self.close(cursor, conn)     
        
                                           
#==========================================================
if __name__ == '__main__': 
    # Objekt erzeugt
    mySQL = MySQL()
    
    #Methoden zum Testen der Funktionalität

    #--Tabellen verwalten--#
#    mySQL.showTables()
#    mySQL.dropTables()
#    mySQL.createTables()
#    mySQL.showTables()
    
    #--Datebanken erstellen--#
#    mySQL.showDBs()
#    mySQL.createGuiDB()
#    mySQL.showDBs()
     
    #--Datenbank löschen--#
#    mySQL.dropGuiDB()
#    mySQL.showDBs()
    
    #--Datenbank neu anlegen--#
    mySQL.createGuiDB()
    mySQL.dropTables()
    mySQL.createTables()
    mySQL.showTables()
     
    #--Bücher in der DB anzeigen--#
#    mySQL.showBooks()
    
    #--Attribute einer Tabelle ausgeben--#
#    mySQL.showColumns()
    
    #--Einfügen eigener Daten--#
#    mySQL.insertBooks('Design Patterns', 7, 'Programming to an Interface, not an Implementation')
#    mySQL.insertBooks('xUnit Test Patterns', 31, 'Philosophy of Test Automation')
#    mySQL.showData()
      
    #--Alle Tabellen + Inhalt anzeigen--#
#    mySQL.showData()
    
    #--Update eines Zitats--#
#    mySQL.updateGOF()
    
    #--Daten in Variablen speeichern--#
#    book, quote = mySQL.showData()  
#    book, quote = mySQL.showDataWithReturn()
#    print(book, quote)

    #--Tabellen löschen + Neue Testdaten einfügen--#
#    mySQL.dropTables()
#    mySQL.createTablesNoFK()
#    mySQL.showTables()
    
#    mySQL.insertBooks('Design Patterns', 7, 'Programming to an Interface, not an Implementation')
#    mySQL.insertBooks('xUnit Test Patterns', 31, 'Philosophy of Test Automation')
#    mySQL.showData()    

    #--Eintrag aus Tabellen löschen
#    mySQL.deleteRecord()
    
    #------------------------
#    mySQL.deleteRecord()    
    mySQL.showData()
    