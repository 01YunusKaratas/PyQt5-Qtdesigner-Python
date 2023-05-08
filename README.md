# PyQt5-Qtdesigner-Python
With Qt Designer and Python, we have created a beautiful product insertion interface.
This code creates an application that uses PyQt5 to implement a user login screen and transition between a login screen and a main screen. 
When the application is launched, an object of the Login class is created and it displays the user login screen.
In the user login screen, the user enters a username and password, and clicks the "Login" button.
If the entered username and password are correct, the main screen (class AnaEkran) is displayed. 
If the login credentials are incorrect, the user is given a few attempts to try again. 
If the correct information is not entered, the application exits.
The main screen provides an interface for adding a product. 
After entering the product name, quantity, and description, clicking the "Save" button stores the entered values in a list and displays a list of the added products.
In this code example,
three separate Python files are used:
anaekran_python.py: Defines the interface of the main screen.
eklenenler_python.py: Defines a class that holds the list of added products and the necessary functions to update the list.
giriş_python.py: Defines the interface of the user login screen and the class that performs the login operations.
The application is launched in the main file (main.py). An object of the Login class is created and shown. The application is terminated at the line sys.exit(app.exec_()).
This code demonstrates how to create a simple user login screen and main screen using PyQt5.
