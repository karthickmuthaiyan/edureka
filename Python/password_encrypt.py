import maskpass
import bcrypt

def create_newuser(usr,pwd):
    print("Registering new user")
    pwd=pwd.encode('utf-8')
    pwd=bcrypt.hashpw(pwd,bcrypt.gensalt())
    with open("cred.txt","a") as fp:
        #usr=usr.encode('utf-8')
        line=usr+','+pwd.decode()+"\n"
        fp.write(line)
        

def verify_auth(usr,pwd):
    ctr=0
    with open("cred.txt","r") as fp:
        lines=fp.readlines()
        for line in lines:
            #print(line)
            if usr in line:
                print ('Existing user account, doing password validation '+line)
                v_usr,v_pwd=line.split(",")
                pwd=pwd.encode('utf-8')
                v_pwd=v_pwd.replace("\n",'')
                v_pwd=v_pwd.encode('utf-8')
                #print(pwd,',',v_pwd)
                if bcrypt.checkpw(pwd,v_pwd):
                    print ('User:{} login successful'.format(v_usr))
                else:
                    print ('Login Failure')
                ctr+=1
                break
        if not lines or ctr==0: 
            print("User not exist, creating user")
            create_newuser(usr,pwd)

username=input("Enter username")
password=maskpass.askpass()
verify_auth(username,password)

