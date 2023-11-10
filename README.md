# Project Description
* The focus of this project is to build a Command interface or console
for single use to create, update, retrieve, and destroy the objects or instances we have stored.
# Command Interface Description:
## How to Start the Program:
* Start the command interpreter by executing the console.py program.
Example:

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
* it can also be used in non-interactive mode this way:
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

### How to use the program:
* The program has certain commands which can be used to manage our objects.
To see the commands you can use "help" or ? to see the commands and their details.
Example:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) quit
```

