# Assignment 3

Hyperlink : https://catalogueeee.herokuapp.com/mywatchlist/html,<br>
            https://catalogueeee.herokuapp.com/mywatchlist/xml,<br>
            https://catalogueeee.herokuapp.com/mywatchlist/json<br>

## Essay questions

## Explain the difference between JSON, XML, and HTML!

A JSON file, or JavaScript Oject Notation is a file format which uses strings to store and send data which contains an attribute-value pairs. It is used to keep data in such a way that it is human-readable. XML stands for Extensible Markup Language and is a markup language which defines a rule on how to encode data that is both human and machine readable. Lastly HTML stands for Hypertext Markup Language. It is the standard markup language when creating a web page. <br>
One of the differences between JSON and XML is that just like its name, JSON is based on the JavaScript language while XML is derived from SGML which stands for the Standard Generalized Markup Language. XML is made to improve the readability as it adds extra information to plain text and also to store and show data. Unlike XML, JSON is said to be more readable as it looks more like a list instead of a nested outline like XML. It is also said that JSON is more lightweight than XML. <br>
Finally, HTML is the most different when comparing the three. If JSON and XML is used to storing and sending data, HTML is used to define how to represent the existing data. HTML will represent the structure of a web page. Instead of storing any data, it just shows how a web page would look like and how it will be rendered on a browser, this would mean that a web page would need all three JSON, XML and HTML so that it can both store and represent data.

## Explain why we need the data delivery when implementing on a platform!

The reason we need data delivery is because most application today will have a database which stores their data which may be large. Only when the users requests for the data, then the application will fetch the data requested and not all of the data. With this, data delivery becomes a must-have for any application. In addition to that, by using the data delivery system, the application won't have to store data in itself which in general reduces the burden on the application if the data is too large to store.

 ## Explain how do you complete the tasks in this assignment!

First, I initiated a new app called mywatchlist with "python manage.py startapp mywatchlist" and added "mywatchlist" in the INSTALLED_APPS. Next, I added the urlpattern for the application mywatchlist to the urls.py in the folder project_django. After that, I added the models for the data in the models.py file in the mywatchlist application folder so that the data will be represented properly. This is then followed by adding 10 data entries by creating a new folder called fixtures and creating a JSON file in the folder to hold the 10 data entries. The next step after this is to add new urlpatterns in the url.py file in the application folder so that the user can open the data in HTML, JSON or XML format. Since this repository is the same as the repository from the previous assignment, I didn't need to add my API key from Heroku to the repository to deploy it. However, if this was a new repository that have not been deployed to Heroku, then I would need to copy my application API key from Heroku to the repository. With that, the application should be up and running for everyone.

## Postman screenshots
![html ss](https://user-images.githubusercontent.com/111977201/191517061-2acc4acd-9a29-4d5a-8f09-71f8e6b1ef64.png)<br>
![json ss](https://user-images.githubusercontent.com/111977201/191517136-327b04fe-8a85-49ce-9d39-e35dd1b69698.png)<br>
![xml ss](https://user-images.githubusercontent.com/111977201/191517236-543a09e9-0fbb-45de-9551-78e75c0f16de.png)
