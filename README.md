Prior to starting flask and testing it, create a virtual environment and install the packages from the requirements file by running these commands inside the terminal in order.

$ python -m venv venv (you may need to use python3 instead)
$ source venv/bin/activate (or .\venv\Scripts\activate on Windows)
$ pip install -r requirements.txt
$ flask --app app --debug run

Usage:

1) Once flask starts, the application should run (by default unless specified otherwise) locally at http://127.0.0.1:8080.

2) Navigation through the different routes can be done by altering the URL directly;

		- Home - http://127.0.0.1:8080
		- About Page - http://127.0.0.1:8080/about/
		- List Property Page: http://127.0.0.1:8080/properties/create
		- View Properties Page: http://127.0.0.1:8080/properties
		- View Specific Property - http://127.0.0.1:8080/properties/2

	OR

   by navigating the page normally by use of the links provided in the webpage header. Under the Properties section, specific properties can be viewed by clicking 'View Property'

3) Prior to adding a new property, ensure that the image representing said property is present in the app/static/uploads folder. Ensure that the format of the image you desire to use is 'png, jpeg or jpg'
