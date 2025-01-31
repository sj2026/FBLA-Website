import pandas as pd
from beans.Application import Application
from db import ConnectionUtil

class ApplicationDataAccess:
    def getApplication(self, ApplicationID):
        connection_obj = ConnectionUtil.getConnection()
        
        try:
            cursor_obj = connection_obj.cursor()

            statement = '''SELECT * FROM JobApplication where ID = ''' + ApplicationID + ''''''


            cursor_obj.execute(statement)

            output = cursor_obj.fetchall()

            for row in output:
                application = Application()
                application.id = row[0]
                application.jobID = row[1]
                application.studentID = row[2]
                application.resumeID = row[3]
                application.status = row[4]
                application.additionalDetails = row[5]
            
                return application
    
    

        except Exception as e:
            print(e)
            connection_obj.rollback()
            
        finally:
            #cursor_obj.close()
            connection_obj.close()
    
    
    def getStudentApplications(self, StudentID):
        connection_obj = ConnectionUtil.getConnection()
        applicationList = []
        
        try:
            cursor_obj = connection_obj.cursor()

            statement = '''SELECT * FROM JobApplication where StudentID = ''' + StudentID + ''''''


            cursor_obj.execute(statement)

            output = cursor_obj.fetchall()

            for row in output:
                application = Application()
                application.id = row[0]
                application.jobID = row[1]
                application.studentID = row[2]
                application.resumeID = row[3]
                application.status = row[4]
                application.additionalDetails = row[5]
                applicationList.append(application)
            
            df = pd.DataFrame.from_records([d.to_dict() for d in applicationList])
            connection_obj.commit()
            return df

        except Exception as e:
            print(e)
            connection_obj.rollback()
            
        finally:
            #cursor_obj.close()
            connection_obj.close()
            
     
    def getJobApplications(self, JobID):
        connection_obj = ConnectionUtil.getConnection()
        applicationList = []
        
        try:
            cursor_obj = connection_obj.cursor()

            statement = '''SELECT job.id, job.JobID, job.StudentID, job.ResumeID, job.Status, job.AdditionalDetails, user.Firstname, user.LastName FROM JobApplication job, User user where job.JobID = ''' + str(JobID) + ''''''
            statement = statement + " and job.StudentId = user.Id"
            print(statement)

            cursor_obj.execute(statement)

            output = cursor_obj.fetchall()
            for row in output:
                application = Application()
                application.id = row[0]
                application.jobID = row[1]
                application.studentID = row[2]
                application.resumeID = row[3]
                application.status = row[4]
                application.additionalDetails = row[5]
                application.link_application = '[' + str(row[0]) + '](/jobapplication/view/' + str(application.jobID) +'/'+ str(application.id) +")"
                application.studentName = str(row[6]) + " " + str(row[7])
                applicationList.append(application)
            
            df = pd.DataFrame.from_records([d.to_dict() for d in applicationList])
            connection_obj.commit()
            return df

        except Exception as e:
            print(e)
            connection_obj.rollback()
            
        finally:
            #cursor_obj.close()
            connection_obj.close()
             
            
    def updateApplication(self, application):
        connection_obj = ConnectionUtil.getConnection()

        try:
            cursor_obj = connection_obj.cursor()
            sql = "UPDATE JobApplication SET JobID = '" + application.jobID + "', StudentID = '" + application.studentID + "', ResumeID = '" + application.resumeID + "', AdditionalDetails = '" + application.additionalDetails + "', Status = '" + application.status + "' WHERE id = " + str(application.id)
            cursor_obj.execute(sql) 
        
            connection_obj.commit()

                                       
        
        except Exception as e:
            print(e)
            connection_obj.rollback()
            
        finally:
            #cursor_obj.close()
            connection_obj.close()
                
                

    def createApplication(self, application):
        connection_obj = ConnectionUtil.getConnection()      
        
        try:
            cursor_obj = connection_obj.cursor()

            cursor_obj.execute('INSERT INTO JobApplication (jobID, studentID, resumeID, additionalDetails, status) VALUES (?,?,?,?,?)', (application.jobID, application.studentID, application.resumeID, application.additionalDetails, application.status))
            connection_obj.commit()
            
        except Exception as e:
            print(e)
            connection_obj.rollback()
            
        finally:
            #cursor_obj.close()
            connection_obj.close()