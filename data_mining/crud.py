'''
C => Create (INSERT INTO)
R => Read (SELECT)
U => Update (UPDATE) 
D => Delete (DELETE)

UPDATE AND DELETE NEED A WHERE CLAUSE.
'''


from database import conn, cur
import bcrypt
import os



status_menu = True
global status_op

def hash_password(passwd):
    return bcrypt.hashpw(passwd.encode(), bcrypt.gensalt())

def create_user(op):
    #Create a new user in the database
    os.system('clear')
    
    print("::: Singup form :::")
    fname = input("Enter your firstname: ")
    lname = input("Enter your lastname: ")
    ident = input("Enter your ident_number: ")
    email = input("Enter your email: ")
    passwd = input("Enter your password: ")
    paswd_hashed = hash_password(passwd)
    
    new_user = f'''
        INSERT INTO 
        users (firstname, lastname, ident_number, email, password) 
        VALUES('{fname}', '{lname}',"{ident}", '{email}', "{paswd_hashed}");    
    '''
    conn.execute(new_user)
    conn.commit()

    print("::: New user has been created successfully! :::")
    os.system('pause')
    menu()
        
def list_user(op):
    #Read al the data from table users
    os.system('clear')
    cur.execute("SELECT * FROM users")
    print(cur.fetchall())
    
    os.system('pause')
    menu()  
        
def search_user(op):
    #Search a user in the database
    os.system('clear')
    print(":::: SEARCH USER BY IDENTIFICATION NUMBER :::::")
    ident_num = input("Enter your identification number: ")
    
    cur.execute(f"SELECT firstname, email FROM users WHERE ident_number = '{ident_num}'")
    print(cur.fetchall())  
        
    os.system('pause')
    menu()  

def update_user(op):
    #Update a user in the database
    os.system('clear')
    print(":::: UPDATE USER FORM :::::")
    iden = input("Enter user identification number: ")
    
    cur.execute(f"SELECT firstname FROM users WHERE ident_number = '{iden}'")
    print(f"Current name: {cur.fetchall()}")
    
    user_name = input("Enter user new name: ")
    
    conf = input("Do you want to update the user-neme? (y/n): ")
    if conf == 'y' or conf == 'Y':
        cur.execute(f"UPDATE users SET firstname='{user_name}' WHERE ident_number = '{iden}'")
        conn.commit()
        print("::: User-name has been updated successfully! :::")
        
    cur.execute(f"SELECT firstname FROM users WHERE ident_number = '{iden}'")
    print(f"Current name: {cur.fetchall()}")
    
    os.system('pause')
    menu()
    
def delete_user(op):
    #Delete a user in the database
    os.system('clear')
    print(":::: DELETE USER FORM :::::")
    iden = input("Enter user identification number: ")
    
    cur.execute("SELECT firstname, lastname FROM users WHERE ident_number = ?", [iden])
    print(f"User to delete is: {cur.fetchall()}")
    
    conf = input("Do you want to delete the user? (y/n): ")
    if conf == 'y' or conf == 'Y':
        cur.execute(f"DELETE FROM users WHERE ident_number = '{iden}'")
        conn.commit()
        print("::: User has been deleted successfully! :::")
        
    cur.execute(f"SELECT firstname, lastname FROM users WHERE ident_number = ?", [iden])
    print(f"Current name: {cur.fetchall()}")
    
    os.system('pause')
    menu()
def menu():
    global opt
    status_opt = True 
    while status_menu:
        os.system('clear')
        print(":::::::::::::::::::::::::::")
        print(":::::: MAIN MENU ::::::::::::")
        print(":::::::::::::::::::::::::::")
        print("[1] - Create a new user")
        print("[2] - List users")
        print("[3] - search a user")
        print("[4] - Update a user")
        print("[5] - Delete a user")
        print("[6] - Exit")
        
        while status_opt:
            opt = input("Press an option: ")
            if opt < '1' or opt > '6':
                print("Invalid option!, try again!")
            else:
                status_opt = False
                
        if opt == '1':
            create_user(opt)
        elif opt == '2':
            list_user(opt)
        elif opt == '3':
            search_user(opt)
        elif opt == '4':
            update_user(opt)
        elif opt == '5':
            delete_user(opt)
        
        else:
            print("::: See you soon :::")
            exit()

#Call main menu    
menu()
    
#Close connection
conn.close()