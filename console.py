#!/usr/bin/python3
"""This is the console module, it defines the HBNBCommand"""

import cmd
import json
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import re


class HBNBCommand(cmd.Cmd):
    """This class contains the entry point of the command interpreter."""
    prompt = '(hbnb) '
    data = {}
    classes = ['BaseModel', 'User', 'State',
               'City', 'Amenity', 'Place', 'Review']

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF commant to exit the program"""
        print()
        return True

    def emptyline(self):
        """an empty line + ENTER: shouldn’t execute anything"""
        pass

    def do_create(self, line):
        """Creates a new instance of a class.
        Usage: create <className>"""
        # split the line into a list of arguments
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = globals()[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance
based on the class name and id.
        Usage: show <className> <id>"""
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            if key in models.storage.all():
                print(models.storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id.
        Usage: destroy <className> <id>"""
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            if key in models.storage.all():
                del models.storage.all()[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances
based or not on the class name.
        Usage: all [<className>]"""
        args = line.split()

        if len(args) > 0 and args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            for instance in models.storage.all().values():
                if len(args) > 0 and instance.__class__.__name__ != args[0]:
                    continue
                print(instance)

    def do_update(self, line):
        """Updates an instance based on the class name and id
by adding or updating attribute.
        Usage: update <className> <id> <attributeName> "<attributeValue>" """
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] + '.' + args[1] not in models.storage.all():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = args[0] + '.' + args[1]
            instance = models.storage.all()[key]
            try:
                attr_type = type(getattr(instance, args[2]))
                args[3] = attr_type(args[3])
            except AttributeError:
                pass
            setattr(instance, args[2], args[3])
            instance.save()

    def count(self, cls):
        """Retrieves all instances of a class"""
        if cls not in self.classes:
            print("** class doesn't exist **")
        else:
            counter = 0
            for instance in models.storage.all().values():
                if type(instance).__name__ == cls:
                    counter += 1
            print(counter)

    def parameters(self, args):
        """Gets the parameters as a string"""
        string = [args[0]]  # className
        pattern = re.compile(r'\((.*)\)')
        arguments = pattern.findall(args[1])
        string.extend(arguments[0].split(','))
        return " ".join(string)

    def default(self, line):
        """Handles unrecognized commands"""
        args = line.split('.')
        if len(args) == 2:
            if args[1] == "all()":
                self.do_all(args[0])
            elif args[1] == "count()":
                self.count(args[0])
            elif args[1].startswith("show("):
                self.do_show(self.parameters(args))
            elif args[1].startswith("destroy("):
                self.do_destroy(self.parameters(args))
            elif args[1].startswith("update("):
                self.do_update(self.parameters(args))
            else:
                super().default(line)
        else:
            super().default(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
