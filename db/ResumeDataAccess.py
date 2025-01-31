import pandas as pd
from beans.Resume import Resume
from db import ConnectionUtil

class ResumeDataAccess:
    def getResume(self, ResumeID):
        connection_obj = ConnectionUtil.getConnection()
        
        try:
            cursor_obj = connection_obj.cursor()

            statement = '''SELECT * FROM Resume where ID = ''' + ResumeID + ''''''


            cursor_obj.execute(statement)

            output = cursor_obj.fetchall()

            for row in output:
                resume = Resume()
                resume.id = row[0]
                resume.resumeName = row[1]
                resume.studentID = row[2]
                resume.pastExperience = row[3]
                resume.skillset = row[4]
                resume.summary = row[5]
            
                return resume
    
    

        except Exception as e:
            print(e)
            connection_obj.rollback()
            
        finally:
            #cursor_obj.close()
            connection_obj.close()
    
    
    def getResumes(self, StudentID, format):
        connection_obj = ConnectionUtil.getConnection()
        resumeList = []
        
        try:
            cursor_obj = connection_obj.cursor()

            statement = '''SELECT * FROM Resume where StudentID = ''' + str(StudentID) + ''''''

            
            cursor_obj.execute(statement)

            output = cursor_obj.fetchall()
            
            for row in output:
                resume = Resume()
                resume.id = row[0]
                resume.resumeName = row[1]
                resume.studentID = row[2]
                resume.pastExperience = row[3]
                resume.skillset = row[4]
                resume.summary = row[5]
                resume.link_edit = '[' + str(resume.id) + '](/resume/edit/' +  str(resume.id) + ")"
                resumeList.append(resume)
            
            if (format != "List"):
                df = pd.DataFrame.from_records([d.to_dict() for d in resumeList])
                connection_obj.commit()
                return df

            else:
                return resumeList

        except Exception as e:
            print(e)
            connection_obj.rollback()
            
        finally:
            #cursor_obj.close()
            connection_obj.close()
            
            
    def updateResume(self, resume):
        connection_obj = ConnectionUtil.getConnection()

        try:
            cursor_obj = connection_obj.cursor()
            sql = "UPDATE Resume SET ResumeName = ? WHERE id = ?" #, () + str(resume.id)
            print(sql)
            cursor_obj.execute(sql,(str(resume.resumeName), str(resume.id))) 
        
            connection_obj.commit()

                                       
        
        except Exception as e:
            print(e)
            connection_obj.rollback()
            
        finally:
            #cursor_obj.close()
            connection_obj.close()
                
                

    def createResume(self, resume):
        connection_obj = ConnectionUtil.getConnection()      
        
        try:
            cursor_obj = connection_obj.cursor()

            cursor_obj.execute('INSERT INTO Resume (resumeName, studentID, pastExperience, skillset, summary) VALUES (?,?,?,?,?)', (resume.resumeName, resume.studentID, resume.pastExperience, resume.skillset, resume.summary))
            connection_obj.commit()
            
        except Exception as e:
            print(e)
            connection_obj.rollback()
            
        finally:
            #cursor_obj.close()
            connection_obj.close()