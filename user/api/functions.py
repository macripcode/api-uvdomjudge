import os
import json
import MySQLdb

host = '127.0.0.1'
usuario_bd = 'macripco'
pass_usuario_db = 'macripco'
db='api_uvdomjudge'
port = 3306

def set_id_user(username,id_user):

    try:

        conn = MySQLdb.connect(host=host, port=port, user=usuario_bd, passwd=pass_usuario_db, db=db)
        cur = conn.cursor()
        cur.execute(
            "update auth_user set id="+str(id_user)+" where username='"+username+"'")
        cur.close()
        conn.commit()
        conn.close()

    except MySQLdb.Error as e:
        #return '500'
        return e

    return '200'

def create_token_user(id_user, token):
    try:

        conn = MySQLdb.connect(host=host, port=port, user=usuario_bd, passwd=pass_usuario_db, db=db)
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO authtoken_token  VALUES ('"+token+"', NOW(),"+str(id_user)+");")
        cur.close()
        conn.commit()
        conn.close()

    except MySQLdb.Error as e:
        # return '500'
        return e
    return '201'
