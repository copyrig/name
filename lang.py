"""Language set"""

import random
import collections

class NamingLibException(Exception):
    """Basic exception class for naming"""
    pass

class AutoMemberTupleSetType(type):
    """This metaclass automatically set the arguments and change it into tuple"""
    def __call__(cls, *args, **kwargs):
        # Initialize
        elem = type.__call__(cls, *args, **kwargs)
        name_arg = elem.__init__.__func__.__code__.co_varnames[1:]
        defaults = elem.__init__.__func__.__defaults__

        # Write the default arguments
        buf_dict = collections.OrderedDict()

        for (name, value) in zip(name_arg, args + defaults):
            buf_dict[name] = value
        # Write the user-defined arguments
        for (name, value) in kwargs.items():
            if isinstance(value, tuple) or isinstance(value, list):
                buf_dict[name] = tuple(value)
            elif isinstance(value, str) or isinstance(value, int):
                buf_dict[name] = (value,)
            elif value is None:
                buf_dict[name] = (None,)
            else:
                raise NamingLibException('Wrong character')
        setattr(elem, 'argument', tuple(buf_dict.values()))
        return elem

class ComposerElementBase(metaclass=AutoMemberTupleSetType):
    """Base class of element composer"""
    # Please revise with metaclass
    characters = None
    argument = tuple()
    result = None
    def compose(self):
        """Compose the name"""
        pass

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
    def __init__(self, initial=None, initial_exclude=None, medial=None, \
                        medial_exclude=None, final=None, final_exclude=None):
        pass # See the metaclass
    def compose(self):
        """Compose the Korean name"""
        jamo = self.characters
        argument = self.argument
        ingredient = [None, None, None]

        # Change str to index
        for elem_base in argument:
            for (idx_target, elem_target) in enumerate(elem_base):
                pass

        for idx in range(3):
            pass # Under dev

        result_int = 0xac00 + ((ingredient[0] * 21) + ingredient[1]) * 28 + ingredient[2]
        result_char = chr(result_int)

        self.result = result_char
        return result_char

x = ComposerElement_ko(initial='ㄱ', final=11)
