
try :
    import sqlite3
except ImportError :
    print ("NO module found")
    raise
finally:
    import sqlite3

class DataBase() :
    def __init__(self,db):
        self.conection=sqlite3.connect(db)
        self.cursor=self.conection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS G2FOSSMEMBERS(id  INTEGER PRIMARY KEY  AUTOINCREMENT , firstName VARCHAR(100),lastName VARCHAR(100),cin INTEGER ,email VARCHAR(200),phone INTEGER ,birthday DATE,livingadress VARCHAR(200),studysection VARCHAR(300),workshop VARCHAR(200),status VARCHAR(100),pic VARCHAR(200),fbid VARCHAR(500),pr INTEGER,att INTEGER , par INTEGER  )")
        self.conection.commit()
    def insert(self,firstName="",lastName="",cin="",email="",phone="",birthday="",livingAdress="",studySection="",workshop="",status="",picpath="",facebook=""):
        self.cursor.execute("INSERT INTO G2FOSSMEMBERS VALUES (NULL ,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(firstName,lastName,cin,email,phone,birthday,livingAdress,studySection,workshop,status,picpath,facebook,0,0,0))
        self.conection.commit()
    def view(self):
        self.cursor.execute("SELECT * FROM G2FOSSMEMBERS")
        self.rows=self.cursor.fetchall()
        return (self.rows)
    def search(self,firstName="",lastName="",cin="",email="",phone="",birthday="",livingAdress="",studySection="",workshop="",status=""):
        self.cursor.execute("SELECT * FROM G2FOSSMEMBERS WHERE firstName=? OR lastName=? OR cin =? OR email =? OR phone =? OR birthday=? OR livingAdress =? OR studySection =? OR workshop =? OR status=? ",(firstName,lastName,cin,email,phone,birthday,livingAdress,studySection,workshop,status))
        self.row = self.cursor.fetchall()
        return (self.row)
    def update(self,id,firstName,lastName,cin,email,phone,birthday,livingAdress,studySection,workshop,status,pic,fbid):
        self.cursor.execute("UPDATE G2FOSSMEMBERS SET firstName=? , lastName=? , cin =? , email =? , phone =? , birthday=? , livingAdress =? , studySection =? , workshop =? , status=? , pic=? ,fbid=? WHERE id =? ",
                            (firstName,lastName,cin,email,phone,birthday,livingAdress,studySection,workshop,status,pic,fbid,id))
        self.conection.commit()
    def delete(self,id):
        self.cursor.execute("DELETE FROM G2FOSSMEMBERS WHERE id = ?",(id,))
        self.conection.commit()

    def __del__(self):
        self.conection.close()