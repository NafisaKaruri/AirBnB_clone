# Airbnb Console Project

This is a team project, part of Alx Software Engineering program. That aims to help us deploy on our server a simple copy of the AirBnB website.

This project, implemented over a period of 4 months, is a console-based application for managing Airbnb listings. It includes a command interpreter (like in a shell) for manipulating data without a visual interface, a front-end website for displaying the final product, a database for storing data, and an API for communication between the front-end and the data.

## Technologies Used
- Python
- MySQL
- HTML/CSS
- JavaScript (JQuery)

## Installation and Setup
1. Clone the repository: `git clone https://github.com/NafisaKaruri/AirBnB_clone`
2. Navigate to the project directory: `cd AirBnB_clone`

## Usage
To use the command interpreter, run `./console.py`, and to quit it. You can then enter `help` command to show you the available commands and `help <command>` to show you how to use them.

It can be used in both interactive and non-interactive modes:

### Interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

### Non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

| Command | Description |
|---------|-------------|
| `./console.py` | Start the command interpreter |
| `quit` or `EOF` | Exit the command interpreter |
| `help` | Show available commands |
| `help <command>` | Show how to use a command |
| `create <class name>` | Creates a new instance of `<class name>`, saves it to the JSON file, and prints the id. |
| `show <class name> <id>` | Prints the string representation of an instance based on the class name and id. |
| `destroy <class name> <id>` | Deletes an instance based on the class name and id (save the change into the JSON file). |
| `all <class name>` or `all` | Prints all string representation of all instances based or not on the class name. |
| `update <class name> <id> <attribute name> "<attribute value>"` | Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Only one attribute can be updated at a time. |

## Testing
Unittests can be found in the tests folder. To run them execute the following command:
```python3 -m unittest discover tests```

## Steps to Build the Project

### 1. The Console
The console is the heart of our application. It allows us to:
- Create our data model.
- Manage (create, update, destroy, etc.) objects via a console/command interpreter.
- Store and persist objects to a file (JSON file).

### 2. Web static
In this step, we:
- Create the HTML of the application.
- Create a template for each object.

### 3. MySQL storage
Here, we:
- Replace the file storage with a Database storage.
- Map models to a table in the database using an O.R.M.

### 4. Web framework - templating
In this phase, we:
- Create the web server in Python.
- Make the static HTML file dynamic by using objects stored in a file or database.

### 5. RESTful API
In this step, we:
- Expose all the objects stored via a JSON web interface.
- Manipulate the objects via RESTful API.

### 6. Web dynamic
Finally, we make the web dynamic by:
- Using JQuery.
- Loading objects from the client side by using our own RESTful API.
