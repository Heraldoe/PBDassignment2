# Assignment 4

Hyperlink : https://catalogueeee.herokuapp.com/todolist <br>

## Essay questions

## What does % csrf_token % do in the form element? What happens if there is no such "code snippet" in the form element?

CSRF stands for Cross-Site Request Forgery. These CSRF tokens prevents CSRF attacks by making it a requirement to have a "key" to send a request from the user. This CSRF token is then compared with the current session token. If the tokens do not match, then the request will not be accepted. If there is no CSRF token, CSRF attacks can easily happen when unauthorized users can forge a request and gain access from an authorized user's session. This can cause a lot of harm to the user data as these unauthorized users could forge a request a user's username or password which would then give the unauthorized users access to other users.

## Can we create the form element manually (without using a generator like {{ form.as_table }})? Explain generally how to create form manually.

It is possible to create a form element manually without using the generator. Instead of using the generator, we would have to use the form tag and make it wrap around an input while also containing the designated URL. After that, we can simply close the form tag. Unlike when using a generator, we would have to manually add the URL and the input of the form element on our own.

## Describe the data flow process from the submission made by the user through the HTML form, data storage in the database, until the appearance of the data that has been stored in the HTML template.

First, a request must be made from the user, for example when the user creates a new task with a new title and description, views.py will run the create_task function to create and store the new data in the database. After this, the process is then redirected back to the show_todolist function. At this moment, the new data that was recently created by the user should already be in the database and the render function would use the new data and gives a response containing the data in the html back to the user.

## Explain how you implement the checklist above.

To complete the assignment, first I made a new app named "todolist" using "python manage.py startapp todolist". After this, I added the todolist app to the INSTALLED_APPS in the settings.py file in the project_django folder. Next would be handling the urls.py file so that the app could be accessed locally. Continuing, I created a new class in the models.py file named Task as instructed. The class Task has fields user, date, title and decription with their own respective fields also as instructed. The next step was to add the registration, login and logout forms which I did by creating new functions register, login_user and logout_user in the views.py file. The register and the login_user function would then have a html file in the template folder which would handle for when the user is registering and/or logging in. Each of the newly added functions would also be added to the urls.py file to handle for when each of them are needed or called. The next step would be to restrict the access of the application to unauthorized users. I did this by first importing "login_required" from django.contrib.auth.decorators and then adding the code "@login_required(login_url='/wishlist/login/')" before the "show_todolist" function. Finally, the last step would be to add Cookies so that the users who are already logged in won't have to log in again if they refresh the page. I did this by using the imported HttpResponseRedirect function and adding it to the login_user function. <br>
After this was finished, I added a new button to add a new task into the database and also a new html file to handle this function which I also added to the file urls.py.