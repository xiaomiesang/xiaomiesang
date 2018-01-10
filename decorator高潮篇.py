import time

user,passwd = 'xsx','xsxwan'
def auth(auth_type):
    def outer_wapper(func):
        def wapper(*args,**kwargs):
            if auth_type == 'local':
                username = input('Username:').strip()
                password = input('Password:').strip()
                if user == username and passwd == password:
                    print('\033[32;1mUser has passed authentication\033[0m')
                    func(*args,**kwargs)
                else:
                    exit('\033[31;1mInvalid username or password\033[0m')
            elif auth_type == 'ldap':
                print('不会')
        return wapper
    return outer_wapper

def index():
    print('welcome to index page')
@auth(auth_type='local')
def home():
    print('welcome to home home page')
@auth(auth_type='ldap')
def bbs():
    print('welcome to bbs page')

index()
home()
bbs()