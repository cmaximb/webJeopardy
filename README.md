# Web Jeopardy

Project created for 24 hour programming contest. Uses restless API to access http://jservice.io/ and creates HTML website to play web version with randomised questions in traditional grid.

## How to install

Download the repository as a zip and then extract it. Open the folder in Visual studio code. Make sure you have the most recent version of python. Install flask by following the instructions on their [page](https://flask.palletsprojects.com/en/3.0.x/installation/#python-version). Also, install the necessary imports in python with the following commands (write in VS code powershell):

```
 pip install html2text
```

followed by


```
 pip install requests
```

Everything is now installed!

## How to run

To run, simply run the following command in the command line (with *--host=0.0.0.0* to make it public on your public network):


```
 flask --app .\webjeopardy\**init**.py run *--host=0.0.0.0*
```

Then, go to your favourite browser and go to the link http://127.0.0.1:5000/jeopardy/. Refreshing the page will update the grid with new, updated categories. Click on the boxes to answer questions.
