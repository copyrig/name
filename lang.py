"""Language set"""

import random

class NamingException(Exception):
    """Basic exception class for naming"""
    pass

class ComposerElementBase:
    """Base class of element composer"""
    characters = None
    element = None
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
    ('ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', \
    'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ') \
    )
    def __init__(self, initial=None, medial=None, final=None):
        self.element = (initial, medial, final)
    def compose(self):
        """Compose the Korean name"""
        jamo = self.characters
        elem = self.element
        ingredient = [None, None, None]

        for idx in range(3):
            if elem[idx]:
                if isinstance(elem[idx], str):
                    ingredient[idx] = jamo[idx].index(elem)
                elif isinstance(elem[idx], int):
                    ingredient[idx] = elem[idx]
            else:
                ingredient[idx] = random.randrange(len(jamo[idx]))

        result_int = 0xac00 + ((ingredient[0] * 21) + ingredient[1]) * 28 + ingredient[2]
        result_char = chr(result_int)

        self.result = result_char
        return result_char
