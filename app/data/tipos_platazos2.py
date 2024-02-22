from app.data.modelo.tipos_platos import Plato
from app.data.modelo.tipos_platos2 import Union_plato


class Union_platazos:

    def select_all(self,db) -> list[Union_plato]:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM Union_platos')
        unionplatos_en_db = cursor.fetchall()
        unionplatos : list[Union_plato]= list()
        for union_plato_en_db in unionplatos_en_db:
           unionplatos.append(Union_plato(union_plato_en_db[0], union_plato_en_db[1], union_plato_en_db[2], union_plato_en_db[3]))

        cursor.close()
        return unionplatos
    

    def select_uno(self,db,nombre) -> Plato:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM Comidas where nombre = %s',[nombre])
        platos_en_db = cursor.fetchall()
        if (platos_en_db == []):
            return None
        plato_en_db = platos_en_db[0]        
        equipo = Plato(plato_en_db[0], plato_en_db[1], plato_en_db[2], plato_en_db[3])
        cursor.close()
        return equipo
