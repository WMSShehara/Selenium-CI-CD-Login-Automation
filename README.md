# Jenkins CI/CD Pipeline with GitHub Webhooks

This simple, self studying project demonstrates a simple CI/CD pipeline using Jenkins and GitHub webhooks. 
The pipeline is triggered automatically whenever a change is pushed to the GitHub repository,
 allowing for continuous integration and deployment (to be continued...).

## Prerequisites

- Jenkins server
- GitHub account and repository.
- Git client on local machine.


## Simple Login Application
The application used in this project is a simple login system built to demonstrate basic authentication functionality.
 It consists of a user interface where users can input their credentials (username and password).

 ## Features
 - Login Validation: The app checks for valid user inputs and returns appropriate success or error messages based on login success or failure.
 - Input Error Handling: The app provides feedback for invalid inputs, such as empty fields or incorrect credentials.
 - User Authentication: Simulates a basic user authentication flow where valid users are granted access and invalid users are prompted to retry

 ## Techniques 

- Jenkins: Jenkins is an open-source automation server that orchestrates the CI/CD pipeline. 
   It runs automated builds and tests every time new code is pushed to the repository.
- GitHub Webhooks: Webhooks are used to trigger Jenkins builds automatically when changes are made to the GitHub repository. 
    This ensures that the CI/CD process is initiated as soon as a developer commits code.
- Pipeline Script: The project uses a Jenkinsfile that defines the stages of the pipeline, 
    such as pulling the latest code, running tests, and preparing the application for deployment.
- Automated Testing: The pipeline includes test stages to ensure that the new code does not break the build. 
    These tests can be automated using testing frameworks like Selenium for UI tests or unit test frameworks for backend validation.
- Continuous Deployment: While this stage is yet to be implemented, 
    the pipeline will eventually deploy the tested code to a staging or production environment, streamlining the release process.