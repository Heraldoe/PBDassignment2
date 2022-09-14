# Assignment 2

Hyperlink : https://catalogueeee.herokuapp.com/katalog/

## Number 5 questions

## Create a diagram containing client request to the Django web application and its response. Also explain the flow of the diagram and how the urls.py, views.py, models.py and HTML files connected each other.

urls.py --> views.py --> Response to User
             |     |
             |     |
             |     |
     Models.py     HTML files    

When the user makes a request, urls will then continues that request to the views.py and if the request requires some data from models.py, then views.py will make a query to models. After obtaining the data from models.py, views.py will then pass on the request to the HTML files where all of the template of the output will be handled. After getting the output from the HTML files, the output will then be displayed to the user.

## Explain why do we use virtual environments? Let's say, if we do not use the virtual environments, can we still create a Django web application?

A virtual environment is an environment which is used to execute an application that is being worked on. When working on multiple web applications we may need third party packages for one and no third party packages for the others. If we were to work on a web application without virtual environments, some errors might occur due to the difference in packages. In theory, we can still create a Django web application without using any virtual environments however, it is much safer with one.

## Explain how did you implement the steps on point 1 to point 4 above.

First, the render function will take the request as its argument and the template name as its second argument and a dictionary as its third. From then on, the render function can handle the rest as it will map out the data from the templates and the data data in the json file. After this, the Procfile will handle the deployment to Heroku with the help of the dpl.yml file. After all of this process the deployment will be using the API key and app name from Heroku.