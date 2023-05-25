import sqlite3

# Método que conecta nuestra app con la base de datos
def conectar():
    conexion = sqlite3.connect("miBD.db") #realiza la conexión
    cursor = conexion.cursor() 
    return conexion, cursor

def crearTabla():
    conexion, cursor = conectar()
    sql = """
        CREATE TABLE IF NOT EXISTS agenda(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nombre VARCHAR(20) NOT NULL,
            telefono VARCHAR (14) NOT NULL
        )
    """

    if (cursor.execute(sql)):
        print("Tabla creada")
    else: 
        print("No se pudo crear la tabla")
    conexion.close()

def insertar(datos):
    conexion, cursor = conectar()
    sql = """
            INSERT INTO agenda(nombre, telefono) VALUES (?, ?)
        """
    if(cursor.execute(sql, datos)):
        print('Datos guardados')
    else:
        print('No se pudieron guardar los datos')
    conexion.commit()
    conexion.close()

def consultar():
    conexion, cursor = conectar()
    cursor.execute("SELECT id,nombre,telefono FROM agenda")
    for fila in cursor:
        print("ID = ", fila[0])
        print("NOMBRE = ", fila[1])
        print("TELEFONO = ", fila[2])
    conexion.close()

def modificar(id, telefono):
    conexion, cursor = conectar()
    sql = "UPDATE agenda SET TELEFONO="+telefono+" WHERE ID="+id
    cursor.execute(sql)
    cursor.close()
    conexion.commit()
    conexion.close()
    
def borrar(id):
    conexion, cursor = conectar()
    sql = "DELETE FROM agenda WHERE ID="+id
    cursor.execute(sql)
    cursor.close()
    conexion.commit()
    conexion.close()


crearTabla()
datos = ("Alex", "653478933")
insertar(datos)
datos = ("Cristian", "646455647")
insertar(datos)
datos = ("M Mar", "345457567")
insertar(datos)
datos = ("Cristian", "123456798")
insertar(datos)
consultar()
modificar("4", "022345776")
consultar()
borrar("1")
borrar("2")
borrar("3")
borrar("4")
borrar("5")
borrar("6")
