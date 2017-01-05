"""Language set"""

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
            return None
        else:
            raise NamingLibException('Wrong type for __list')

class SimplifiedElementBase(metaclass=AutoMemberSetType):
    """Base element class"""
    element = None
    def __init__(self, element=None):
        pass
    def __repr__(self):
        return str(self.element)

class ListBase(SimplifiedElementBase, metaclass=AutoMemberListSetType):
    """Base class of customed list class"""
    pass

class IncludeList(ListBase):
    """Use this class to include"""
    pass

class ExcludeList(ListBase):
    """Use this class to exclude"""
    pass

class ComposerElementBase(metaclass=AutoMemberSetType):
    """Base class of element composer"""
    # Please revise with metaclass
    characters = None
    argument = tuple()
    result = None
    #@abc.abstractmethod
    def compose(self):
        """Compose the name"""
        pass
    def __digitize(self, list_control, list_compare):
        for elem in list_control:
            if elem in list_compare:
                elem = list_compare.index(elem)
    def __characterize(self, list_control, list_compare):
        for elem in list_control:
            if elem in range(len(list_compare)):
                elem = list_compare[elem]

class ComposerElement_ko(ComposerElementBase):
    """Korean name composer - inspired by 이강성, 『파이썬 3 바이블』"""
    characters = ( \
    ('ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', \
    'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'), \
    ('ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', \
    'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ'), \
    ('', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', \
    'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ') \
    )
    def __init__(self, initial=None, medial=None, final=None):
        pass # See the metaclass
    def compose(self):
        """Compose the Korean name"""
        characters = self.characters
        argument = list(self.argument)
        ingredient = [None, None, None]

        # Change str to index
        for (elem, compare) in zip(argument, (characters[0], characters[1], characters[2])):
            self.__digitize(elem, compare)

        # Check
        # under dev

        #result_int = 0xac00 + ((ingredient[0] * 21) + ingredient[1]) * 28 + ingredient[2]
        #result_char = chr(result_int)

        #self.result = result_char
        #return result_char
