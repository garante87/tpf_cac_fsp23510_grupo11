
# importo librerías
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import mysql.connector
import os
import time

#--------------------------------------------------------------------
app = Flask(__name__)
CORS(app)

#--------------------------------------------------------------------
class BaseDeDatos:
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
                self.cursor.execute(f"CREATE DATABASE {database}") # crea la base de datos si no existe
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

#--------------------------------------------------------------------
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

# inicio servicio flask
if __name__ == "__main__":
    app.run(debug=True)