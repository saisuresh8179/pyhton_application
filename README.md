--------------------------How to run this application in linux sever----------------------------
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
