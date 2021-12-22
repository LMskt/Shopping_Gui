import eel
from Service.user_service import user_login, admin_login

if __name__ =="__main__":
    eel.init('Web')

    eel.expose(user_login)
    eel.expose(admin_login)

    eel.start('login.html')