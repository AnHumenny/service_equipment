import pymysql
import os
from dotenv import load_dotenv
load_dotenv()


class SqlEquipment:
    def __init__(self, host, port, user, password, dtb):
        self.connection = pymysql.connect(
            host=os.getenv('host'),
            port=3306,
            user=os.getenv('user'),
            password=os.getenv('password'),
            database=os.getenv('database'),
            cursorclass=pymysql.cursors.DictCursor
        )

    def check_admin(self, login, password):
        query_authent = "SELECT id, login, password, access FROM `user` WHERE login = %s AND password = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query_authent, (login, password))
                result = cursor.fetchone()
                if result is not None:
                    return True
                else:
                    return False
        except Exception as e:
            print("error: ", e)

    def check_superadmin(self, login, password):
        query_authent = "SELECT id, login, password, access FROM `user` WHERE login = %s AND password = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query_authent, (login, password))
                result = cursor.fetchone()
                answer = result.get('access')
                if answer == 'superadmin':
                    return True
                else:
                    return False
        except Exception as e:
            print("error: ", e)
        finally:
            cursor.close()

    def select_all_users(self):
        query_all = "SELECT name, login, access FROM `user` ORDER BY id"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query_all)
                result = cursor.fetchall()
                return result
        except Exception as e:
            print("error: ", e)
        finally:
            cursor.close()

    def insert_new_user(self, name, login, password, status):
        query_new_user = "INSERT INTO `user` (name, login, password, access) VALUES ( %s, %s, %s, %s )"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query_new_user, (name, login, password, status))
                cursor.connection.commit()
                cursor.close()
            return True
        except pymysql.err.OperationalError:
            print('Некорректные данные')
        finally:
            cursor.close()

    def delete_user(self, login):
        query_dlt_user = "DELETE FROM `user` WHERE login = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query_dlt_user, (login, ))
                cursor.connection.commit()
                return
        except Exception as e:
            print("error: ", e)
        finally:
            cursor.close()

    def check_login(self, login):      #проверка существующего пользователя
        query_check_login = "SELECT login FROM `user` WHERE login = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query_check_login, (login, ))
                result = cursor.fetchall()
                if len(result) > 0:
                    return False
                else:
                    return True
        except Exception as e:
            print("error: ", e)
        finally:
            cursor.close()

    def select_equipment_result(self, equip):
        query_equip = "SELECT * FROM `replacement` WHERE equipment LIKE '%" + equip + "%'"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query_equip)
                result_equip = cursor.fetchall()
                return result_equip
        except Exception as e:
            print("error: ", e)
        finally:
            cursor.close()

    def select_equipment_name(self, name):
        query_name_equip = "SELECT * FROM `replacement` WHERE responsible LIKE '%" + name + "%'"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query_name_equip)
                result_query = cursor.fetchall()
                return result_query
        except Exception as e:
            print("error: ", e)
        finally:
            cursor.close()

    def select_adresses_equipment(self, address):
        query_address = "SELECT * FROM `replacement` WHERE address LIKE '%" + address + "%'"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query_address)
                res_address = cursor.fetchall()
                return res_address
        except Exception as e:
            print("error: ", e)
        finally:
            cursor.close()

    def select_ascue_all(self):
        query_ascue = "SELECT id, sity, street, namber, askue FROM `baza` "
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query_ascue)
                res_ascue = cursor.fetchall()
                return res_ascue
        except Exception as e:
            print("error: ", e)
        finally:
            cursor.close()

    def insert_equip(self, equipment, address, date, problem, responsible):
        query_insert = "INSERT INTO `replacement` (equipment, address, date, problem, responsible) VALUES (%s, %s, %s, %s, %s)"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query_insert, (equipment, address, date, problem, responsible))
                self.connection.commit()
                return
        except Exception as e:
            print("error: ", e)
        finally:
            cursor.close()


    def res_add(self):
        query_insert_add = "SELECT equipment, address, date, problem, responsible FROM `replacement` WHERE id=LAST_INSERT_ID()"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query_insert_add)
                result = cursor.fetchone()
                return result
        except Exception as e:
            print("error: ", e)
        finally:
            cursor.close()

    def csv_export(self):
        query_support = "SELECT * FROM `replacement` ORDER BY id"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query_support)
                result = cursor.fetchall()
                return result
        except Exception as e:
            print("error: ", e)
        finally:
            cursor.close()

    def searth_ascue_street(self, street):
        query_ascue = "SELECT id, sity, street, namber, askue FROM `baza` WHERE street LIKE '%" + street + "%'"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query_ascue)
                searth_street = cursor.fetchall()
                return searth_street
        except Exception as e:
            print("error: ", e)
        finally:
            cursor.close()

    def street_with_namber(self, street, home):
        query_ascue_address = "SELECT * FROM `baza` WHERE street = %s AND namber = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query_ascue_address, (street, home))
                searth_street = cursor.fetchone()
                return searth_street
        except Exception as e:
            print("error: ", e)
        finally:
            cursor.close()

    def search_ascue_ip(self, ip):
        query_ip = "SELECT * FROM `baza` WHERE askue = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query_ip, (ip, ))
                search_ip = cursor.fetchone()
                return search_ip
        except Exception as e:
            print("error: ", e)
        finally:
            cursor.close()

    def select_ascue_del(self):
        del_ascue = "SELECT id, sity, street, namber, askue FROM `baza` WHERE askue LIKE '%снят%' OR askue LIKE '%демонтирован%'"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(del_ascue)
                res_del = cursor.fetchall()
                return res_del
        except Exception as e:
            print("error: ", e)
        finally:
            cursor.close()
