#!/usr/bin/python3
"""Module for entry point of the command interpreter."""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone project."""

    prompt = "(hbnb)"

    def do_quit(self, args):
        """Exit the program."""
        return True

    def do_EOF(self, args):
        """Exit the prorm."""
        print()
        return True

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

    def default(self, line):
        """Called input line when command prefix not recognized."""
        class_name = line.split('.')[0]
        if class_name in storage.classes():
            method_name = line.split('(')[1].split(')')[0]
            if method_name == 'count':
                self.do_count(class_name)
        else:
            print("*** Unknown syntax: {}".format(line))

    def postcmd(self, stop, line):
        """Hook method executed just when command dispatch finished"""
        if "." in line:
            parts = line.split('.')
            if len(parts) == 2:
                class_name, method_name = parts
                if method_name == "all()":
                    self.do_all(class_name)
                    return False
                elif method_name == "count()":
                    self.do_count(class_name)
                    return False
        return stop

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return
        new_instance = storage.classes()[class_name]()
        storage.save()
        print(new_instance.id)

    def do_show(self, args):
        """Print the string representation of an instance."""
        if not args:
            print("** class name missing **")
            return

        args_list = args.split()
        class_name = args_list[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        instances = storage.all()
        obj_id = args_list[1]
        obj_key = "{}.{}".format(class_name, obj_id)
        if obj_key in instances:
            print(instances[obj_key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id.
                """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances"""
        if line != "":
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                nl = [str(obj) for key, obj in storage.all().items()
                      if type(obj).__name__ == words[0]]
                print(nl)
        else:
            new_list = [str(obj) for key, obj in storage.all().items()]
            print(new_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instances = storage.all()
        obj_id = args[1]
        obj_key = "{}.{}".format(class_name, obj_id)
        if obj_key not in instances:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_name = args[2]
        attribute_value = args[3]
        instance = instances[obj_key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()

    def do_count(self, class_name):
        """Count the number of instances of a class."""
        if class_name not in storage.classes():
            print("** class doesn't exist **")
        else:
            instances_count = len([obj for obj in storage.all().values()
                                   if type(obj).__name__ == class_name])
            print(instances_count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
