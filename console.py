#!/usr/bin/python3
"""This module contains the code for the console implementation."""
import cmd
import shlex
import json
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
            print([str(obj) for obj in all_objs.values()
                   if args[0] in obj.__class__.__name__])

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the
        JSON file)."""
        args = arg.split()
        if args[2][0] == '{' and args[-1][-1] == '}':
            dict_str = " ".join(args[2:])
            args[2] = dict_str
            args = args[:3]
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
                    if args[2].startswith('{') and args[2].endswith('}'):
                        attr_dict = json.loads(args[2])
                        for k, v in attr_dict.items():
                            setattr(all_objs[key], k, v)
                        storage.save()
                    else:
                        print("** value missing **")
                else:
                    setattr(all_objs[key], args[2], args[3])
                    storage.save()
            else:
                print("** no instance found **")

    def default(self, arg):
        """Method called on an input line when the command prefix is not
        recognized. It parses arg as a command name and a string containing a
        list of arguments. It then looks for a method named 'do_' + command,
        dispatching to that method if it exists. If it doesn't, it raises an
        error."""
        args = arg.split(".")
        if len(args) == 2:
            if args[1] == "all()":
                self.do_all(args[0])
            elif args[1] == "count()":
                all_objs = storage.all()
                count = 0
                for key in all_objs:
                    if key.split(".")[0] == args[0]:
                        count += 1
                print(count)
            elif args[1][:5] == "show(" and args[1][-1] == ")":
                self.do_show(args[0] + " " + args[1][5:-1])
            elif args[1][:8] == "destroy(" and args[1][-1] == ")":
                self.do_destroy(args[0] + " " + args[1][8:-1])
            elif args[1][:7] == "update(" and args[1][-1] == ")":
                args1 = args[1][7:-1].split(", ")
                if len(args1) == 0:
                    self.do_update(args[0])
                elif len(args1) == 1:
                    self.do_update(args[0] + " " + args1[0])
                elif len(args1) == 2:
                    self.do_update(args[0] + " " + args1[0] + " " + args1[1])
                elif len(args1) == 3:
                    self.do_update(args[0] + " " + args1[0] + " " +
                                   args1[1] + " " + args1[2])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
