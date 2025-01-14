import pandas as pd
from beans.User import User
from db import ConnectionUtil

class UserDataAccess:
    def getUsers(self, status):
        connection_obj = ConnectionUtil.getConnection()
        userList = []
         
        try:
            cursor_obj = connection_obj.cursor()

            statement = '''SELECT * FROM User '''
            
   
            if (status != "All"):
                statement = statement + "where Status = '" + status + "'"
            
            

            cursor_obj.execute(statement)

            output = cursor_obj.fetchall()

            for row in output:
                user = User()
                user.id = row[0]
                user.firstName = row[1]
                user.lastName = row[2]
                user.email = row[3]
                user.phoneNumber = row[4]
                user.isAdmin = row[5]
                user.status = row[6]
                user.password = row[7]
                user.username = row[8]
                userList.append(user)
                
            df = pd.DataFrame.from_records([d.to_dict() for d in userList])
            connection_obj.commit()
            return df

        except Exception as e:
            print(e)
            connection_obj.rollback()
            
        finally:
            #cursor_obj.close()
            connection_obj.close()
          
    def doesUserExist(self, username, password):
        connection_obj = ConnectionUtil.getConnection()
        userList = []
         
        try:
            cursor_obj = connection_obj.cursor()

            statement = '''SELECT * FROM User where Username = ''' +  "'" + username + "'"
            

            cursor_obj.execute(statement)

            output = cursor_obj.fetchall()

            for row in output:
                user = User()
                user.id = row[0]
                user.password = row[7]
                
                if (user.password == password):
                    return user.id
            
            return 0
                

        except Exception as e:
            print(e)
            connection_obj.rollback()
            
        finally:
            #cursor_obj.close()
            connection_obj.close()
        
          
    def updateUser(self, user):
        connection_obj = ConnectionUtil.getConnection()
        
        try:
            cursor_obj = connection_obj.cursor()
            sql = "UPDATE USER SET status = '" + user.status + "', isAdmin = '" + user.isAdmin +  "' WHERE id = " + str(user.id)
            cursor_obj.execute(sql) 
            connection_obj.commit()
                                       
        
        except Exception as e:
            print(e)
            connection_obj.rollback()
            
        finally:
            #cursor_obj.close()
            connection_obj.close()
                

    def createUser(self, user):
        connection_obj = ConnectionUtil.getConnection()
        
        try:
            cursor_obj = connection_obj.cursor()

            cursor_obj.execute('INSERT INTO USER (firstName, lastName, email, phoneNumber, isAdmin, status, password, username) VALUES (?,?,?,?,?,?,?,?)', (user.firstName, user.lastName, user.email, user.phoneNumber, user.isAdmin, user.status, user.password, user.username))
            connection_obj.commit()
        
        except Exception as e:
            print(e)
            connection_obj.rollback()
            
        finally:
            #cursor_obj.close()
            connection_obj.close()