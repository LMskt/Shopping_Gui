from sqlalchemy import Column, Integer, String, text
from sqlalchemy.orm import declarative_base

from Util.sql_config_sqlalchemy import get_mydb

Base = declarative_base()
error ="error"

class commodity(Base):
    __tablename__ = 'commodity'
    id = Column(Integer, primary_key=True, comment='id')
    name = Column(String(255))
    price =  Column(Integer)
    number = Column(Integer)
    img = Column(String(255))
    introduce = Column(String(255))
    def __init__(self,name,price,number,img,introduce):
        self.name=name
        self.img=img
        self.number=number
        self.price=price
        self.introduce=introduce

sesson = get_mydb()

# 查询所有的商品
def commodity_get_all():
    try:
        result = sesson.query(commodity).all()
    except:
        result=error
    return result


# 根据条件查询商品
def commodity_get_by(para):
    try:
        result = sesson.query(commodity).filter(para)
    except:
        result=error
    return result

# 根据名字磨模糊查询商品
def commodity_get_byname(name):
    try:
        result = sesson.execute(text("SELECT * FROM COMMODITY WHERE NAME like :X "),[{"X":'%'+name+'%'}]).fetchall()
    except:
        result=error

    return result



# 添加商品
def commodity_add(one):
    try:
        result = sesson.add(one)
        sesson.commit()
    except:
        result = "error"

    return result



# 修改商品
# 传入用户的id与要修改的参数
# 成功返回1失败返回0
def commodity_change(id,para):
    try:
        result = sesson.query(commodity).filter(commodity.id == id).update(para)
        sesson.commit()
    except:
        result=error
    return result

# 删除商品
# 传入用户的id
# 成功返回1失败返回0
def commodity_delete(id):
    try:
        result = sesson.query(commodity).filter(commodity.id == id).delete()
        sesson.commit()
    except:
        result=error
    return result


if __name__ =="__main__":
    a = commodity_get_byname('龙')
    # a=commodity_get_all()
    print(a[0].name)

