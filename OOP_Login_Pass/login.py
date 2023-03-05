class LoginPass:
    login = None
    password = 0
    
    def __init__(self, login, password):
        self.login = login
        self.password = password
        
    def check_password(self):
        if len(self.password) < 8:
            raise ValueError ("Пароль должен быть 8 символов или больше")
        
    def save_login_pass(self):
        with open(r"C:\Users\Chris\Desktop\my_solved_tasks\OOP_Login_Pass\logs.txt", "a") as file:
            file.write(f"{self.login, self.password}"+" \n")
            
    def check_login(self):
        with open(r"C:\Users\Chris\Desktop\my_solved_tasks\OOP_Login_Pass\logs.txt", "r") as file:
            for i in file:
                print(i)
                if (f"{self.login, self.password}"+" \n") == i:
                        
                    raise ValueError ("Логин уже существует")
