Todo list application
This is a simple application built using Python and Flask.

Requirements-
Python 3.11.2


See requirements.txt for a list of required Python packages


Installation-

Clone the repository to your local machine
Install required packages using pip: pip install -r requirements.txt


Run the application: python server.py

Navigate to http://localhost:5000 in your web browser to access the API Usage
The following endpoints are available:

GET /tasks - Retrieve a list of all tasks
GET /tasks/<int:id> - Retrieve a specific task by ID
POST /tasks - Create a new task
PUT /tasks/<int:id> - Update an existing task by ID
DELETE /tasks/<int:id> - Delete a specific task by ID

To make requests to the API, you can use an HTTP client such as Postman or cURL.

In this case i have used postman