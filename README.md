FBLA Website Coding and Development 2024-2025: Job Search Website

This project contains code for the Job Search Website. The website covers the following user personas: 

* Employer - Submit job postings, review the applications & schedule interviews.
* Administrator - Approve & decline users and job postings
* Students - Search & apply for jobs, create & manage resumes.

The website also implements the following advanced functions:

* AI chatbot using Retrieval-Augmented Generation (RAG)
* Accessibility features like text to speech, and changeable text size/color.
* Integration with Zoom for interviews.
* Graph displaying application statuses for employers.

The project contains the following files and folders:

* app.py: Contains code to run the dash application.
* FBLA Website 2024.db - Sqllite database for the website.
* Indexer.py - Contains code for indexing the job postings for text based search.
* NewChatbot.py - The file contains code to call AI Assistant REST API to get the response.
* requirements.txt: Run this file to setup the required python libraries using command
    pip install requirements.txt


Folders:

* assets - Contains required assets like logos
* beans - Contains generic/data objects (e.g. Application.py, Job.py, User.py)
* db  - Contains files related to database access. Also contains CreateEmail (email sent to applicant), CreateZoom (interview link generation), Searcher (job search), and TextToSpeech (accessibility feature).
* pages - Contains code for website pages.
 
