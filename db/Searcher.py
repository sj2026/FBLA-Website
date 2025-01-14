from whoosh.query import *
from whoosh.qparser import QueryParser
from whoosh.index import open_dir
import pandas as pd

from beans.Job import Job


class Searcher:
    def search(self,searchTerm):
        ix = open_dir("indexdir")
        jobList = []
        with ix.searcher() as searcher:
            query = QueryParser("keywords", ix.schema).parse(searchTerm)
            results = searcher.search(query)
            for row in results:
                job = Job()
                job.id = row['id']
                job.title = row['title']
                job.company = row['company']
                job.location = row['location']
                job.workHours = row['workHours']
                job.wageAmount = row['wageAmount']
                job.description = row['description']
                job.qualifications = row['qualifications']
                job.benefits = row['benefits']
                #job.keywords = row['keywords']
                job.status = 'Approved'
                jobList.append(job)
        
        df = pd.DataFrame.from_records([d.to_dict() for d in jobList])
        
        return df