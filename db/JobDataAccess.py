import pandas as pd
from beans.Job import Job
from db import ConnectionUtil

class JobDataAccess:
    def getJob(self, jobID):
        connection_obj = ConnectionUtil.getConnection()
        
        try:
            cursor_obj = connection_obj.cursor()

            statement = '''SELECT * FROM jobPosting where ID = ''' + jobID + ''''''


            cursor_obj.execute(statement)

            output = cursor_obj.fetchall()

            for row in output:
                job = Job()
                job.id = row[0]
                job.title = row[1]
                job.company = row[2]
                job.location = row[3]
                job.workHours = row[4]
                job.wageAmount = row[5]
                job.description = row[6]
                job.qualifications = row[7]
                job.benefits = row[8]
                job.keywords = row[9]
                job.status = row[10]

                return job
    
    

        except Exception as e:
            print(e)
            connection_obj.rollback()
            
        finally:
            #cursor_obj.close()
            connection_obj.close()
    
    def getJobs(self, status):
        connection_obj = ConnectionUtil.getConnection()
        jobList = []
        
        try:
            cursor_obj = connection_obj.cursor()

            statement = '''SELECT * FROM JobPosting '''
            
   
            if (status != "All"):
                statement = statement + "where Status = '" + status + "'"
            
            

            cursor_obj.execute(statement)

            output = cursor_obj.fetchall()

            for row in output:
                job = Job()
                job.id = row[0]
                job.title = row[1]
                job.company = row[2]
                job.location = row[3]
                job.workHours = row[4]
                job.wageAmount = row[5]
                job.description = row[6]
                job.qualifications = row[7]
                job.benefits = row[8]
                job.keywords = row[9]
                job.status = row[10]
                jobList.append(job)
                
            df = pd.DataFrame.from_records([d.to_dict() for d in jobList])
            connection_obj.commit()
            return df

        except Exception as e:
            print(e)
            connection_obj.rollback()
            
        finally:
            #cursor_obj.close()
            connection_obj.close()
            
    def updateJob(self, job):
        connection_obj = ConnectionUtil.getConnection()
        
        try:
            cursor_obj = connection_obj.cursor()
            sql = "UPDATE jobPosting SET status = '" + job.status + "' WHERE id = " + str(job.id)
            cursor_obj.execute(sql) 
            connection_obj.commit()
                                       
        
        except Exception as e:
            print(e)
            connection_obj.rollback()
            
        finally:
            #cursor_obj.close()
            connection_obj.close()
                
                

    def createJob(self, job):
        connection_obj = ConnectionUtil.getConnection()
        
        try:
            cursor_obj = connection_obj.cursor()

            cursor_obj.execute('INSERT INTO jobPosting (title, company, location, workHours, wageAmount, description, qualifications, benefits, keywords, status) VALUES (?,?,?,?,?,?,?,?,?,?)', (job.title, job.company, job.location, job.workHours, job.wageAmount, job.description, job.qualifications, job.benefits, job.keywords, job.status))
            connection_obj.commit()
        
        except Exception as e:
            print(e)
            connection_obj.rollback()
            
        finally:
            #cursor_obj.close()
            connection_obj.close()