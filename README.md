--------------------------How to test and run this python code in linux sever----------------------------

-> install python3, python3-pip and install python3.10-venv
-> Then, create your own venv.
   cmd: python -m venv tutorial-env
-> change to created venv.
   cmd: source tutorial-env/bin/activate
-> Afterthat,install your requriments to run application.
   cmd: pip intsall -r requriments.txt
-> Then, change the hostname, username, passwd, port, database_name in app.py to connect your DB.
-> Afterthat, run the test cases in test_app.py
   cmd: pytest
-> If test cases execute sucessfully then, run the application.
   cmd: python3 app.py

-------------------------How to test this python code and run this python code in container-----------------------

-> install python3, python3-pip and install python3.10-venv
-> Then, create your own venv.
   cmd: python -m venv tutorial-env
-> change to created venv.
   cmd: source tutorial-env/bin/activate
-> Afterthat,install your requriments to run application.
   cmd: pip intsall -r requriments.txt
-> Then, change the hostname, username, passwd, port, database_name in app.py to connect your DB.
-> Afterthat, run the test cases in test_app.py
   cmd: pytest
-> If all 5 test cases run sucessfully create the image and conatiner. 
-> create the docker image 
   cmd: docker build -t <image_name:version> .
-> create the docker container
   cmd: docker run --name <container_name> -d -p <server_port>:<app_port> <image_name:v1>


