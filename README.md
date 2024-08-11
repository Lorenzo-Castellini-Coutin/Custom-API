## Custom API

### Introduction & Project Scope
This API is centered around account creation and messaging. A user, by giving certain data, can create an account, authenticate their account, update their user account, and delete their user account. Furthermore, a user can send and receive messages to other, exisiting users. These messages can be viewed and deleted as well. Note, this project was done as part of an onboarding for a research group with the purpose of getting familiar with certain libraries and technologies. This being said, this API was developed in such way to compily with the requirements of the project, and only features a back-end since it is a back-end position.

### How does it all work?
For this API, the MVC design pattern was used to develop and organize the codebase. Using Python's Flask library, a number of routes were created for the different actions the users can take with regards to their account or their messages. The corresponding controller takes care of the user input, which is taken from the view, and sends it to the model where the database is updated. The database, used for storing all of the inputed data in this API, is a MySQL database, which is running in a Docker container. Finally, this API was deployed as a web app using Microsoft Azure. In this process, the MySQL db was also migrated to Microsoft Azure, in which the Docker container was no longer used for the API. In essence, the Docker container was only used in the development phase or testing phase of the project. 

### Advisory on Usage
Make sure you have fully read the repository's license rule before taking any actions.

### Additional Notes
The API was fully tested in Postman, both when the API only ran locally on the machine and also when the API was fully deployed to Microsoft Azure.  