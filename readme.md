# ToDoList Web Application
### Description
**The ToDoList web application adds your tasks to a list.**

### Technologies used and Architectural Decisions:
* **HTML**
* **CSS**
* **Bootstrap**
* **FastAPI**: FastAPI is a type of REST API and offers several benefits compared to other Python Web API frameworks like Django and Flask. These advantages include rapid development, high performance, and type checks.
* **SQLAlchemy**: It is a library that provides ORM in Python.
* **Alembic**:It is a database migration tool based on SQLAlchemy.
* **Jinja2Templates**:
* **psycopg2**: psycopg2 is a library used for interacting with PostgreSQL DBMS in the Python. PostgreSQL provides high compatibility with SQL standards and supports many advanced SQL features. It is used for large and complex database projects.
* **Requests**
* **Starlette** 
* **Python-multipart**
* **httpx**
* **Pytest**
* **Uvicorn**

### Building of an Application
In order to build this application, we need to follow steps that are described in below.
Firstly, as a best practices, we are going to create a virtual environment. The virtual enviironment provides us preventing crossing library versions each other from the other projects. We are going to create a venv file.After that, we will work in that file like installing libraries, building application etc.

Virtual environment creating steps:

<pre><code>Python -m venv venv</code></pre>
This script allows us to create Virtual Environment with "venv" as file name.
<pre><code>venv/Scripts/activate</code></pre> 
After the creation of virtual environment, we need to going into the venv file. 
<pre><code>pip install -r requirements.txt</code></pre>
This script provides to install all libraries that are in the file of "requirements.txt".

### Database Configurations

1. After the all required libraries are installed, we need to configure our database environment. Related to your database informations, you can fill the "dbconfig.py" file. When you filled that file, it will be adding to the "database.py" file automatically and sqlalchemy can connect with your database link for postgresql.
2. Additionaly, to use a alembic library we need to configure "sqlalchemy.url" in the alembic.ini file. In order to this, we need to fill the link manually.
3. After the database configurations, we need to create our tables in the database environment. Tables that are created in "model.py" file need to be synchronized in the configured database environment. In order to do that, we need to use "Alembic migration" library. It can be followed the steps in below:
<pre><code>alembic revision --autogenerate -m "first commit"</code></pre> 
This script provides us to autogenerate all tables that are created in models.py as a revision file.   
<pre><code>alembic upgrade head</code></pre> 
This script allows to us sychronize all tables that are autogenerated from revision file to the our database enviroment.

After all these steps are done. We can use our database's tables to crud process.

### Run the Application in a Uvicorn Server

We need to use the script in below:

<pre><code>python -m uvicorn main:app --reload</code></pre> In this script, main is describing to our "main.py filename", app is describing to our "FastAPI variable that we used in our main.py file", --reload means that, server is reloaded in every changement automatically. With this whole code we can run the our application in a localhost. Also we can use the link (https://localhost/docs) to check our API's easily from the Swagger UI. 





### Display of Functions
![Jpeg-1](https://github.com/UmitEkmekci/TodoListApplication/blob/main/adding.PNG)
<br/>
After entering the item in the input area, the "add" button is clicked.

![Jpeg-1](https://github.com/UmitEkmekci/TodoListApplication/blob/main/listing.PNG)
<br/>
As seen in this image, the item has been added to the list.

