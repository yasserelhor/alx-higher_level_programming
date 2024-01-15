#!/usr/bin/python3
""" Module containing the Square class,
which inherits from the Rectangle class."""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class representing a square, inheriting from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes Square instances.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Special method for string representation.
        """
        str_square = "[Square] "
        str_id = "({}) ".format(self.id)
        str_position = "{}/{} - ".format(self.x, self.y)
        str_size = "{}".format(self.width)

        return str_square + str_id + str_position + str_size

    @property
    def size(self):
        """ Getter for the size.
        """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for the size.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Update method for modifying attributes.
        """
        if args is not None and len(args) != 0:
            list_attr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_attr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_attr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returns a dictionary with attributes.
        """
        list_attr = ['id', 'size', 'x', 'y']
        dict_result = {}

        for key in list_attr:
            if key == 'size':
                dict_result[key] = getattr(self, 'width')
            else:
                dict_result[key] = getattr(self, key)

        return dict_result
