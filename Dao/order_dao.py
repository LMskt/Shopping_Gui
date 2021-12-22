import datetime

from sqlalchemy import Column, Integer, String, TIMESTAMP, text, null
from sqlalchemy.orm import declarative_base

from Util.sql_config_sqlalchemy import get_mydb

Base = declarative_base()
error ="error"

class orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, comment='id')
    userid = Column(Integer)
    commodityid = Column(Integer)
    number = Column(Integer)
    time = Column(TIMESTAMP)
    def __init__(self,userid,commodityid,number):
        self.userid=userid
        self.number=number
        self.commodityid=commodityid

        now = datetime.datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M:%S")
        self.time=now



sesson = get_mydb()

# 根据用户查询订单
# 返回username,commodityname,price
def orders_get_byuserid(userid):
    try:
        result = sesson.execute(text("SELECT user.name AS username,commodity.name AS commodityname, commodity.price*orders.number AS price,orders.time AS TIME FROM orders LEFT JOIN USER ON orders.userid=user.id LEFT JOIN commodity ON commodity.id=orders.commodityid WHERE orders.userid=:x"),{"x":userid})
    except:
        result=error
    return result


# 根据商品查询订单
# 返回username,commodityname,price
def orders_get_bycommodityid(commodityid):
    try:
        result = sesson.execute(text("SELECT user.name AS username,commodity.name AS commodityname, commodity.price*orders.number AS price,orders.time AS TIME FROM orders LEFT JOIN USER ON orders.userid=user.id LEFT JOIN commodity ON commodity.id=orders.commodityid WHERE orders.commodityid=:x"),{"x":commodityid})
    except:
        result=error
    return result


# 添加订单
def orders_add(one):
    try:
        result = sesson.add(one)
        sesson.commit()
    except:
        result = "error"
    return result

# 删除订单
# 传入订单的id
# 成功返回1失败返回0
def orders_delete(id):
    try:
        result = sesson.query(orders).filter(orders.id == id).delete()
        sesson.commit()
    except:
        result=error
    return result


if __name__ =="__main__":
    a=orders_get_bycommodityid(1)
    for i in a:
        print(i.time)
