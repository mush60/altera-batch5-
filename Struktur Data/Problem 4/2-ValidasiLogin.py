import re

def checkEmail(email) :
    pattern = r'[\w]{1,}@[a-z]{1,}.*[com|id|co.id]{2,5}'
    hasil = str(re.findall(pattern, email)).replace("['", '').replace("']", '')

    if hasil == email :
        return True
    else :
        return False

def validasiLogin(email, password) :
    database = [
        {'email':'johndoe@gmail.com', 'password': '123456'},
        {'email':'johndoe@yahoo.co.id', 'password': '123456'},
        {'email':'john_doe@gmail.com', 'password': 'asdfasdfds'} ]
    
    if checkEmail(email) == True :
        
    else :
        res['pesan'] = 'email tidak valid'
        res['status'] = 'False'

    # for i in database :
    #     if i['email'] == email and i['password'] == password :
    #         return {'pesan' : [], 'status' : True}

    return database
        
# you can only write your code here! 
# Driver Code 
# print(validasiLogin('johndoe@gmail.com','123456')) 
print(checkEmail('johndoe@gmail.com')) 
# Cpesan': 0, 'status': True) 
# Cpesan': [password tidak valid], 'status': False 
print(validasiLogin('johndoe_gmail.com','123456')) 
# {'pesan': ['email tidak valid'], 'status': False) 
print(validasiLogin('johndoe@yahoo.co.id','12abcd')) 
# {'pesan': [password tidak valid], 'status': False) 
## {'pesan': 0, 'status': True)