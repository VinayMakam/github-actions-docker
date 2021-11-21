# python-flask-docker
Basic Python Flask app in a Docker Container which prints "Hello World" inside the content of the page.
This project using GitHub Action Workflow for CI process with tests.
For trigger this workflow, just push something to the master.
The workflow contains two jobs - Build & Test.

## Build job:
Included building and running the container and installation of all dependancies that reqired for flask to run.

## Test job:
Included unit tests which done by using Pytest module.

![image](https://user-images.githubusercontent.com/55482825/142743557-5747e7df-7204-47ee-942a-d70b61217ffb.png)
![image](https://user-images.githubusercontent.com/55482825/142743567-574f5a14-822d-4b12-8aa6-e8a7b2550cf4.png)
![image](https://user-images.githubusercontent.com/55482825/142743569-609d6319-c593-4971-aacb-be46479cb240.png)

