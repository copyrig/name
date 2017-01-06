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
            return [[]]
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
    def digitize(self, list_control, list_compare):
        """Digitize the list"""
        # pylint: disable=unused-variable
        for (idx, elem) in enumerate(list_control):
            if list_control[idx] in list_compare:
                list_control[idx] = list_compare.index(list_control[idx])
    def characterize(self, list_control, list_compare):
        # pylint: disable=unused-variable
        """Characterize the list"""
        for (idx, elem) in enumerate(list_control):
            if list_control[idx] in range(len(list_compare)):
                list_control[idx] = list_compare.index(list_control[idx])

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
    initial = ListBase()
    medial = ListBase()
    final = ListBase()
    def __init__(self, initial=None, medial=None, final=None):
        pass # See the metaclass
    def compose(self):
        """Compose the Korean name"""
        characters = self.characters
        list_original = [self.initial, self.medial, self.final]
        list_process = list(list_original)
        ingredient = [None, None, None]

        # Check type and switch
        for (idx, elem) in enumerate(list_process):
            if isinstance(elem, ListBase):
                list_process[idx] = (list_process[idx].element)[0]
            elif elem is None:
                list_process[idx] = list()
            else:
                raise NamingLibException("Check composer's input type")

        # Change str to index
        for (elem, compare) in zip(list_process, (characters[0], characters[1], characters[2])):
            self.digitize(elem, compare)

        # Check whether index is out of range
        for elem in list_process:
            pass

        result_int = 0xac00 + ((ingredient[0] * 21) + ingredient[1]) * 28 + ingredient[2]
        result_char = chr(result_int)

        self.result = result_char
        return result_char

x = ComposerElement_ko(IncludeList('ㄱ'), IncludeList('ㅏ'))
print(x.compose())
