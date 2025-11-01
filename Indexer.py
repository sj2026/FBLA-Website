from whoosh.index import create_in
from whoosh.fields import *
from db.JobDataAccess import JobDataAccess

"""
Creates an index to perform text based search.
Gets all the approved jobs and adds it to the index.

"""
schema = Schema(id = ID(stored=True), title=TEXT(stored=True), company=TEXT(stored=True), location=TEXT(stored=True), workHours=TEXT(stored=True), wageAmount=TEXT(stored=True), description=TEXT(stored=True), qualifications=TEXT(stored=True), benefits=TEXT(stored=True), keywords=TEXT)

ix = create_in("indexdir", schema)
writer = ix.writer()
dataAccess = JobDataAccess()

df = dataAccess.getJobs("Approved")

for index, row in df.iterrows():
    writer.add_document(id = str(row['id']), title=row["title"], company=row["company"], location=row["location"], workHours=row["workHours"], wageAmount=row["wageAmount"], description=row["description"], qualifications=row["qualifications"], benefits=row["benefits"], keywords=row["keywords"])

writer.commit()