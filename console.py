#!/usr/bin/python3
"""This module contains the code for the console implementation."""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """This class contains the code for the console implementation."""
    prompt = '(hbnb) '
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id."""
        if arg == "":
            print("** class name missing **")
        elif arg not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        else:
            new = HBNBCommand.classes[arg]()
            new.save()
            print(new.id)

    def do_show(self, arg):
        """Prints the string representation based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            key = args[0] + "." + args[1]
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file)."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            key = args[0] + "." + args[1]
            if key in all_objs:
                del all_objs[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all the string representation of
        all instances based or not on the class name."""
        args = arg.split()
        all_objs = storage.all()
        if len(args) == 0:
            print([str(obj) for obj in all_objs.values()])
        elif args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        else:
            print([str(obj) for obj in all_objs.values()])

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the
        JSON file)."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            key = args[0] + "." + args[1]
            if key in all_objs:
                if len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    setattr(all_objs[key], args[2], args[3])
                    storage.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
