"""Base part of language set"""

import collections
import random

class NamingLibException(Exception):
    """Basic exception class for naming"""
    pass

class AutoMemberSetType(type):
    """This metaclass automatically set the arguments and change it into list"""
    def __call__(cls, *args, **kwargs):
        # Initialize
        elem = type.__call__(cls, *args, **kwargs)
        name_arg = elem.__init__.__func__.__code__.co_varnames[1:]
        defaults = elem.__init__.__func__.__defaults__

        # Write the default arguments and user-defined arguments with *args
        for (name, value) in zip(name_arg, args + defaults[len(args):]):
            setattr(elem, name, value)
        # Write the user-defined arguments with **kwargs
        for (name, value) in kwargs.items():
            setattr(elem, name, value)
        return elem

class AutoMemberListSetType(AutoMemberSetType):
    """This metaclass automatically set the arguments and change it into list"""
    def __call__(cls, *args, **kwargs):
        # Initialize
        elem = type.__call__(cls, *args, **kwargs)
        name_arg = elem.__init__.__func__.__code__.co_varnames[1:]
        defaults = elem.__init__.__func__.__defaults__

        # Write the default arguments and user-defined arguments with *args
        buf_dict = collections.OrderedDict()
        if defaults is None:
            defaults = tuple()
        for (name, value) in zip(name_arg, args + defaults[len(args):]):
            buf_dict[name] = cls.__list(value)
        # Write the user-defined arguments with **kwargs
        for (name, value) in kwargs.items():
            buf_dict[name] = cls.__list(value)
        setattr(elem, 'element', list(buf_dict.values()))
        return elem
    #@staticmethod
    def __list(cls, elem):
        if isinstance(elem, tuple) or isinstance(elem, list):
            return list(elem)
        elif isinstance(elem, str) or isinstance(elem, int):
            return [elem]
        elif elem is None:
            return list()
        else:
            raise NamingLibException('Wrong type for __list')

class SimplifiedElementBase(metaclass=AutoMemberSetType):
    """Base element class"""
    element = None
    def __init__(self, element=None):
        pass
    def __repr__(self):
        return '<{}: {}>'.format('SElement', self.element)

class ListBase(SimplifiedElementBase, metaclass=AutoMemberListSetType):
    """Base class of customed list class"""
    element = list()
    def digitize(self, list_compare):
        """Digitize the list"""
        # pylint: disable=unused-variable
        for (idx, elem) in enumerate(self.element[0]):
            if elem in list_compare:
                self.element[0][idx] = list_compare.index(elem)
        return True
    def characterize(self, list_compare):
        # pylint: disable=unused-variable
        """Characterize the list"""
        for (idx, elem) in enumerate(self.element[0]):
            if elem in range(len(list_compare)):
                self.element[0][idx] = list_compare[idx]
        return True
    def check_element_index(self, list_compare):
        """Check whether number in list is out of range"""
        for elem in (self.element)[0]:
            if not elem in range(len(list_compare)):
                raise NamingLibException('Character index - out of range')
        return True
    def choice(self, list_input):
        """Basic method of choose"""
        pass

class IncludeList(ListBase):
    """Use this class to include"""
    def choice(self, list_input=None):
        """Choose one from list. You don't have to use list_input argument"""
        return random.choice(self.element[0])

class ExcludeList(ListBase):
    """Use this class to exclude"""
    def choice(self, list_input):
        """Choose one and exclude elements from list_compare"""
        if self.element[0] == list(range(len(list_input))):
            raise NamingLibException('All letters are excluded')

        while True:
            elem = random.randrange(len(list_input))
            if elem in self.element[0]:
                continue
            else:
                break
        return elem

class ComposerElementBase(metaclass=AutoMemberSetType):
    """Base class of element composer"""
    # Please revise with metaclass
    character = None
    argument = tuple()
    result = None
    #@abc.abstractmethod
    def compose(self):
        """Compose the name"""
        pass
