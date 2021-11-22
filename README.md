# python-flask-docker

Basic Python Flask app, build by a Docker file.
This app prints "Hello World" inside the content of the page.
The project using GitHub Action Workflow for CI pipeline with tests.
For trigger this workflow, just push something to the master(ask me for an admin permission or create pull request).

The workflow contains two jobs - Build & Test.

## Build job:
Included building and running the container and installation of all dependancies that reqired for flask to run.
We share the IP address of the build job container with the test job for testing our enviroment.

## Test job:
Included unit test which done by using Pytest module.
We are testing the content of the page(should be "Hello World!"), and IP address of the build container.

![image](https://user-images.githubusercontent.com/55482825/142743557-5747e7df-7204-47ee-942a-d70b61217ffb.png)
![image](https://user-images.githubusercontent.com/55482825/142743567-574f5a14-822d-4b12-8aa6-e8a7b2550cf4.png)
![image](https://user-images.githubusercontent.com/55482825/142743569-609d6319-c593-4971-aacb-be46479cb240.png)

