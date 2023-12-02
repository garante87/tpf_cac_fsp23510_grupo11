
# importo librerías
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import mysql.connector
import os
import time

#####################################################################
app = Flask(__name__)
CORS(app)

#####################################################################
class BaseDeDatos:
    
    # contructor ####################################################
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        self.cursor = self.conn.cursor()

        try:
            self.cursor.execute(f"USE {database}")
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f"CREATE DATABASE {database}") # crea la bd si no existe
                self.conn.database = database
            else:
                raise err
        self.cursor.execute(
            '''
                CREATE TABLE IF NOT EXISTS libros (
                    id INT,
                    titulo VARCHAR(255) NOT NULL,
                    autor VARCHAR(255),
                    editorial VARCHAR(255),
                    genero VARCHAR(255),
                    paginas INT,
                    imagen_url VARCHAR(255),
                    precio INT,
                    descripcion VARCHAR(255) NOT NULL
                )
            ''')
        
        self.conn.commit() # guarda los cambios
        
        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True)
        
    # alta ##########################################################
    def agregar_libro(self, id, titulo, autor, editorial, genero, paginas, imagen_url, precio, descripcion):
        self.cursor.execute(f"SELECT * FROM libros WHERE id = {id}")
        hay_libro = self.cursor.fetchone()
        if hay_libro: return False
        query = "INSERT INTO libros (id, titulo, autor, editorial, genero, paginas, imagen_url, precio, descripcion) " \
            + "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        print(query)
        datos = (id, titulo, autor, editorial, genero, paginas, imagen_url, precio, descripcion)
        self.cursor.execute(query, datos)        
        self.conn.commit()
        return True
    
    # modificacion ##################################################
    def modificar_libro(self, id, titulo2, autor2, editorial2, genero2, paginas2, imagen_url2, precio2, descripcion2):
        query = "UPDATE libros " \
            + "SET titulo = %s, autor = %s, editorial = %s, genero = %s, paginas = %s, imagen_url = %s, precio = %s, descripcion = %s " \
            + "WHERE id = %s"
        datos = (titulo2, autor2, editorial2, genero2, paginas2, imagen_url2, precio2, descripcion2, id)
        self.cursor.execute(query, datos)
        self.conn.commit()
        return self.cursor.rowcount > 0
    
    # consulta ######################################################
    def consultar_libro(self, id):
        self.cursor.execute(f"SELECT * FROM libros WHERE id = {id}")
        return self.cursor.fetchone()

    # listar ########################################################
    def listar_libros(self):
        self.cursor.execute("SELECT * FROM libros")
        return self.cursor.fetchall()

    # eliminar ######################################################
    def eliminar_libro(self, id):
        self.cursor.execute(f"DELETE FROM libros WHERE id = {id}")
        self.conn.commit()
        return self.cursor.rowcount > 0

    # mostrar #######################################################
    def mostrar_libro(self, id):
        libro = self.consultar_libro(id)
        if libro:
            print("="*20)
            print(f"{libro['id']}")
            print(f"{libro['titulo']} de {libro['autor']}. Editorial {libro['editorial']}.")
            print(f"Descripción: {libro['descripcion']}")
            print(f"{libro['paginas']} páginas. Género: {libro['genero']}. ${libro['precio']}")
            print(f"URL de Imágen: {libro['imagen_url']}")
            print("")
        else:
            print("El libro no existe")

#####################################################################
#clrscr
print("\033[H\033[J")

# prueba directorio raiz
@app.route("/")
def prueba_inicio():
    return "<p>Prueba</p>"

db =  BaseDeDatos(
                host="localhost",
                user="root", 
                password="", 
                database="tienda_mangas"
            )

# prueba agregar
# db.agregar_libro( 413, "Dragon Ball 1", "Akira Toriyama", "Ivrea", "Shonen", 200, "null", 2200, "Las aventuras de Goku")
# db.agregar_libro( 414, "Saint Seiya 12", "Masami Kurumada", "Ivrea", "Shonen", 200, "null", 2500, "Las aventuras de Seiya")
# db.agregar_libro( 415, "Sailor Moon 4", "Naoko Takeuchi", "Ivrea", "Shojo", 200, "null", 2200, "Las aventuras de Usagi")

# prueba modificar
#db.modificar_libro( 412, "Dragon Ball 8", "Akira Pérez", "Larp", "Seinen", 212, "null", 2450, "Ninguna")

# prueba consulta
# print(db.consultar_libro( 412 ))

# prueba lista completa
# print(db.listar_libros())

# prueba eliminar
# db.eliminar_libro(412)

# prueba mostrar
db.mostrar_libro(413)
db.mostrar_libro(414)
db.mostrar_libro(415)

# inicio servicio flask
if __name__ == "__main__":
    app.run(debug=True)