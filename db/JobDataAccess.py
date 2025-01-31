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

            # Base SQL statement
            statement = '''SELECT * FROM JobPosting'''
            
            # Add condition for status
            if status != "All":
                statement += " WHERE status = '" + status + "'" 
                #cursor_obj.execute(statement, (status))
            #else:
            
            cursor_obj.execute(statement)

            # Fetch results
            output = cursor_obj.fetchall()

            # Convert results to Job objects
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
                
            # Convert to DataFrame
            df = pd.DataFrame.from_records([d.to_dict() for d in jobList])
            return df

        except Exception as e:
            print(f"Error in getJobs: {e}")
            return pd.DataFrame()  # Return an empty DataFrame in case of error

        finally:
            connection_obj.close()

    def getEmployerJobs(self, employerID):
        connection_obj = ConnectionUtil.getConnection()
        jobList = []
        
        try:
            cursor_obj = connection_obj.cursor()

            # Base SQL statement
            statement = '''SELECT * FROM JobPosting Where EmployerID = ''' + str(employerID)
            
            # Add condition for status
            cursor_obj.execute(statement)

            # Fetch results
            output = cursor_obj.fetchall()

            # Convert results to Job objects
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
                job.employerID = row[11]
                job.link_student = '[' + row[1] + '](/job/view/' +  str(job.id) + ")"
                job.link_applications = '[Applications](/viewallapplications/' + str(job.id) + ")"
                jobList.append(job)
                
            # Convert to DataFrame
            df = pd.DataFrame.from_records([d.to_dict() for d in jobList])
            return df

        except Exception as e:
            print(f"Error in getEmployerJobs: {e}")
            return pd.DataFrame()  # Return an empty DataFrame in case of error

        finally:
            connection_obj.close()
    
    def updateJob(self, job):
        connection_obj = ConnectionUtil.getConnection()
        
        try:
            cursor_obj = connection_obj.cursor()
            sql = "UPDATE JobPosting SET status = '" + str(job.status) + "' WHERE id = " + str(job.id)
            #cursor_obj.execute(sql, (job.status, job.id))
            #print(sql)
            cursor_obj.execute(sql)
            connection_obj.commit()

        except Exception as e:
            print(f"Error in updateJob: {e}")
            connection_obj.rollback()

        finally:
            connection_obj.close()

    def createJob(self, job):
        connection_obj = ConnectionUtil.getConnection()
        
        try:
            cursor_obj = connection_obj.cursor()
            sql = '''INSERT INTO JobPosting 
                     (title, company, location, workHours, wageAmount, description, qualifications, benefits, keywords, status, employerID) 
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            cursor_obj.execute(sql, (job.title, job.company, job.location, job.workHours, job.wageAmount, 
                                     job.description, job.qualifications, job.benefits, job.keywords, job.status, job.employerID))
            connection_obj.commit()

        except Exception as e:
            print(f"Error in createJob: {e}")
            connection_obj.rollback()

        finally:
            connection_obj.close()