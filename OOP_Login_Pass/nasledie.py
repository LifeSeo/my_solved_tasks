from login import LoginPass

class Naslednic(LoginPass):
    pass


log = Naslednic("vasya4", "123456700")
log.check_password()
log.check_login()
log.save_login_pass()