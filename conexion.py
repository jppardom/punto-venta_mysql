import pymysql
class conexion:
   
    @classmethod
    def ejecutarSQL (self, sql, parametros = ()):
        con = pymysql.connect(host="localhost", user="root", passwd= "", db="punto_venta")
        with con.cursor() as cursor:
            rest = cursor.execute(sql, parametros)
            con.commit()
        if sql.upper().startswith('SELECT',0):
            data = cursor.fetchall()
            cursor.close()
            return data
        else:
            return rest
        
     