from app.data.modelo.tipos_platos import Plato

class Platazos:

    def select_all(self,db) -> list[Plato]:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM Comidas')
        platos_en_db = cursor.fetchall()
        platos : list[Plato]= list()
        for plato_en_db in platos_en_db:
            platos.append(Plato(plato_en_db[0], plato_en_db[1], plato_en_db[2], plato_en_db[3]))

        cursor.close()
        return platos


    def select_uno(self,db,nombre) -> Plato:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM Comidas where nombre = %s',[nombre])
        platos_en_db = cursor.fetchall()
        if (platos_en_db == []):
            return None
        plato_en_db = platos_en_db[0]        
        plato = Plato(plato_en_db[0], plato_en_db[1], plato_en_db[2], plato_en_db[3])
        cursor.close()
        return plato

    def insert(self,db,nombre,temperatura,ingredientes):
        cursor = db.cursor()
        sql = ("INSERT INTO Comidas (nombre,temperatura,ingredientes) values (%s,%s,%s) ")
        data = (nombre,temperatura,ingredientes)
        cursor.execute(sql,data)
        db.commit()

    def delete(self,db,plato):
        cursor = db.cursor()
        sql = ("delete from Comidas where plato = %s ")
        data = [plato]
        cursor.execute(sql, data)
        db.commit()
        
    def update(self,db,plato,nombre,temperatura,ingredientes):
        cursor = db.cursor()
        sql = ("update Comidas set nombre = %s, temperatura = %s, ingredientes = %s where plato = %s ")
        data = [nombre,temperatura,ingredientes,plato]
        cursor.execute(sql, data)
        db.commit()   
           
    def updateNombre(self,db,plato,nombre):
        cursor = db.cursor()
        sql = ("update Comidas set nombre = %s where plato = %s ")
        data = [nombre,plato]
        cursor.execute(sql, data)
        db.commit()           