import pandas as pd
from beans.User import User
from db import ConnectionUtil

class UserDataAccess:
    def getUsers(self, status):
        connection_obj = ConnectionUtil.getConnection()
        userList = []
         
        try:
            cursor_obj = connection_obj.cursor()

            # Base SQL query
            statement = '''SELECT * FROM User'''
            
            # Add WHERE clause if necessary
            if status != "All":
                statement += " WHERE status = ?"
                cursor_obj.execute(statement, (status,))
            else:
                cursor_obj.execute(statement)

            # Fetch results
            output = cursor_obj.fetchall()

            # Convert rows to User objects
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
                
            # Convert to DataFrame
            df = pd.DataFrame.from_records([d.to_dict() for d in userList])
            return df

        except Exception as e:
            print(f"Error in getUsers: {e}")
            return pd.DataFrame()  # Return an empty DataFrame in case of error

        finally:
            connection_obj.close()
          
    def doesUserExist(self, password, username):
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

            # Use parameterized query for updates
            #sql = '''UPDATE User 
            #         SET status = ?, isAdmin = ? 
            #         WHERE id = ?'''
                     
            sql = "UPDATE USER SET status = '" + user.status + "', isAdmin = '" + user.isAdmin +  "' WHERE id = " + str(user.id)
   
            #print(user.status)
            #print(user.isAdmin)
            #print(user.id)
            #cursor_obj.execute(sql, (user.status, str(user.isAdmin), user.id))
            cursor_obj.execute(sql) 
            
            connection_obj.commit()

        except Exception as e:
            print(f"Error in updateUser: {e}")
            connection_obj.rollback()

        finally:
            connection_obj.close()
                
                
    def getUserStatus(self, userID):
        connection_obj = ConnectionUtil.getConnection()
         
        try:
            cursor_obj = connection_obj.cursor()

            # Base SQL query
            statement = '''SELECT * FROM User WHERE Id = ''' + str(userID)
            
            cursor_obj.execute(statement)
            
            # Fetch results
            output = cursor_obj.fetchall()

            # Convert rows to User objects
            for row in output:
                return row[6]

        except Exception as e:
            print(f"Error in getUsers: {e}")
            return pd.DataFrame()  # Return an empty DataFrame in case of error

        finally:
            connection_obj.close()
        
    def createUser(self, user):
        connection_obj = ConnectionUtil.getConnection()
        
        try:
            cursor_obj = connection_obj.cursor()

            # Use parameterized query for inserts
            sql = '''INSERT INTO User 
                     (firstName, lastName, email, phoneNumber, isAdmin, status, password, username) 
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
            cursor_obj.execute(sql, (user.firstName, user.lastName, user.email, user.phoneNumber, 
                                     user.isAdmin, user.status, user.password, user.username))
            connection_obj.commit()

        except Exception as e:
            print(f"Error in createUser: {e}")
            connection_obj.rollback()

        finally:
            connection_obj.close()