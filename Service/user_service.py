import eel

from Dao.user_dao import user_get_by, user


def user_login(username,password):
    try:
        a = user_get_by(user.username == username and user.password == password)
        if (a[0].name):
            result = "ok"
        else:
            result ="no"
    except:
        result ="no"
    return result

def admin_login(username,password):
    if(username == 'admin' and password == '123'):
        return "ok"
    else:
        return "no"


if __name__ =="__main__":
    a=user_login("123d","1w23")
    print(a)