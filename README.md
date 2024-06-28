## Custom API

### Introduction & Project Scope
This API gets data provided by the user, and creates an account for said user in a database. Furthermore, if a user wants to send a message, the data in the message, will also be stored in a database. With all of this information stored, the user can access their account information, update their details, and even delete their account. The same can be said for the messages section. This project was done as part of an onboarding for a research group with the purpose of getting familiar with certain technologies.

### How does it all work?
The MVC design pattern was used to develop the codebase for this custom API. Using Flask, a number of routes were created for the different actions the users can take with regards to their account or their messages. The corresponding model takes care of the user input, sends it to the model where the database is updated. The database used for storing all of the inputed data is a MySQL database. Furthermore, this custom API was launched in Microsoft Azure. 

### Usage
In order to make use of this custom API, you must make sure you have all of the libraries installed, as well as have a database configured. 

### Advisory on Usage
Make sure you have fully read the repository's license rule before taking any actions.

### Additional Notes
The API can be tested using Postman. Make sure to copy the correct route names to ensure it will work in the tests made. 
