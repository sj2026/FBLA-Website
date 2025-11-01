import json
import requests

from db.JobDataAccess import JobDataAccess

dataAccess = JobDataAccess()

class NewChatbot():

    def createDocuments(self):
        """
        Retrieves all the Jobs 

        Returns: Array of Jobs in JSON format
        """

        documents = []
        df = dataAccess.getJobs("Approved")

        for index, row in df.iterrows():    
            jsonROW = row.to_json()
            documents.append({'content': jsonROW})
        
        return documents

    #Send request to chatbot and return the response
    def sendRequest(self, inputJson, command):
        """
        Calls the chatbot REST API to get the response

        Args:
            inputJson: input to query the chatbot.
            command: REST resource/command to call.

        Returns:
            response from chatbot.
        """
        url = "http://localhost:9555/" + command  # Example public API
        
        HEADERS = {
        "Content-Type": "application/json"
        }

        try:
            response = requests.post(url, headers=HEADERS, json=inputJson)
            response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)

            return response.json()

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

