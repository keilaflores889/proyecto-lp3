from flask import current_app as app
from app.conexion.Conexion import Conexion

class CiudadDao:

    def getCiudades(self):
        ciudadSQL = """
        SELECT id_ciudades, descripcion
        FROM ciudades
        """
        
        # Crear conexión y cursor
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(ciudadSQL)
            ciudades = cur.fetchall()

            # Transformar los datos en una lista de diccionarios
            return [{'id': ciudad[0], 'descripcion': ciudad[1]} for ciudad in ciudades]

        except Exception as e:
            app.logger.error(f"Error al obtener todas las ciudades: {str(e)}")
            return []

        finally:
            # Cerrar cursor y conexión
            cur.close()
            con.close()

    def getCiudadById(self, id):
        ciudadSQL = """
        SELECT id_ciudades, descripcion
        FROM ciudades WHERE id_ciudades=%s
        """
        
        # Crear conexión y cursor
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(ciudadSQL, (id,))
            ciudadEncontrada = cur.fetchone()
            if ciudadEncontrada:
                return {
                    "id": ciudadEncontrada[0],
                    "descripcion": ciudadEncontrada[1]
                }
            else:
                return None  # Retornar None si no se encuentra la ciudad

        except Exception as e:
            app.logger.error(f"Error al obtener ciudad por ID: {str(e)}")
            return None

        finally:
            # Cerrar cursor y conexión
            cur.close()
            con.close()

    def guardarCiudad(self, descripcion):
        insertCiudadSQL = """
        INSERT INTO ciudades(descripcion) VALUES(%s) RETURNING id_ciudades
        """
        
        # Crear conexión y cursor
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(insertCiudadSQL, (descripcion,))
            ciudad_id = cur.fetchone()[0]
            con.commit()  # Confirmar la inserción
            return ciudad_id

        except Exception as e:
            app.logger.error(f"Error al insertar ciudad: {str(e)}")
            con.rollback()  # Revertir en caso de error
            return False

        finally:
            # Cerrar cursor y conexión
            cur.close()
            con.close()

    def updateCiudad(self, id, descripcion):
        updateCiudadSQL = """
        UPDATE ciudades
        SET descripcion=%s
        WHERE id_ciudades=%s
        """
        
        # Crear conexión y cursor
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateCiudadSQL, (descripcion, id))
            filas_afectadas = cur.rowcount
            con.commit()

            return filas_afectadas > 0  # Retornar True si se actualizó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al actualizar ciudad: {str(e)}")
            con.rollback()
            return False

        finally:
            # Cerrar cursor y conexión
            cur.close()
            con.close()

    def deleteCiudad(self, id):
        deleteCiudadSQL = """
        DELETE FROM ciudades
        WHERE id_ciudades=%s
        """
        
        # Crear conexión y cursor
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(deleteCiudadSQL, (id,))
            rows_affected = cur.rowcount
            con.commit()

            return rows_affected > 0  # Retornar True si se eliminó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al eliminar ciudad: {str(e)}")
            con.rollback()
            return False

        finally:
            # Cerrar cursor y conexión
            cur.close()
            con.close()
