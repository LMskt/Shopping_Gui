import pymysql

serve = '127.0.0.1'
user = 'root'
password = 'liumiao271937'
database = 'shopping_serve'
charest = 'utf8'

def get_con():
    con = pymysql.connect(host=serve,user=user,password=password,database=database,charset=charest)
    cursor = con.cursor()
    sql = "SELECT * FROM user"
    res = cursor.execute(sql)
    # return cursor
    print(res)

if __name__ =='__main__':
    get_con()