from sqlalchemy import Column, Integer, String, text
from sqlalchemy.orm import declarative_base

from Util.sql_config_sqlalchemy import get_mydb

Base = declarative_base()
error ="error"

class user(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, comment='id')
    username = Column(String(255))
    password = Column(String(255))
    name = Column(String(255))
    def __init__(self,username,password,name):
        self.name=name
        self.username=username
        self.password=password


sesson = get_mydb()

# 查询所有的用户
def user_get_all():
    try:
        result = sesson.query(user).all()
    except:
        result=error
    return result

# 根据条件查询用户
def user_get_by(para):
    try:
        result = sesson.query(user).filter(para)
    except:
        result=error
    return result


# 添加用户
def user_add(one):
    try:
        result = sesson.add(one)
        sesson.commit()
    except:
        result = "error"

    return result


# 根据名字磨模糊查询用户
def user_get_byname(name):
    try:
        result = sesson.execute(text("SELECT * FROM USER WHERE NAME like :X "),[{"X":'%'+name+'%'}])
    except:
        result=error
    return result

# 修改用户
# 传入用户的id与要修改的参数
# 成功返回1失败返回0
def user_change(id,para):
    try:
        result = sesson.query(user).filter(user.id == id).update(para)
        sesson.commit()
    except:
        result=error
    return result

# 删除用户
# 传入用户的id
# 成功返回1失败返回0
def user_delete(id):
    try:
        result = sesson.query(user).filter(user.id == id).delete()
        sesson.commit()
    except:
        result=error
    return result


if __name__ =="__main__":
   a=user_get_by(user.username == "123" and user.password == "123")
   print(len(a))
