import eel

from Service.commodity_service import com_get_all, com_get_byname
from Service.user_service import user_login, admin_login

if __name__ =="__main__":
    eel.init('Web')

    # eel注册函数
    eel.expose(user_login)
    eel.expose(admin_login)
    eel.expose(com_get_all)
    eel.expose( com_get_byname)

    eel.start('login.html')