"""Naming set for Korean"""

import basepart

class ComposerElementKorean(basepart.ComposerElementBase):
    """Korean name composer - inspired by 이강성, 『파이썬 3 바이블』"""
    characters = ( \
    ('ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', \
    'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'), \
    ('ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', \
    'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ'), \
    ('', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', \
    'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ') \
    )
    initial = basepart.ListBase()
    medial = basepart.ListBase()
    final = basepart.ListBase()
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
            if isinstance(elem, basepart.ListBase):
                list_process[idx] = (list_process[idx].element)[0]
            elif elem is None:
                list_process[idx] = list()
            else:
                raise basepart.NamingLibException("Check composer's input type")

        # Change str to index
        for (elem, compare) in zip(list_process, (characters[0], characters[1], characters[2])):
            self.digitize(elem, compare)

        # Check whether index is out of range
        for elem in list_process:
            for idx in range(len(elem)):
                pass

        result_int = 0xac00 + ((ingredient[0] * 21) + ingredient[1]) * 28 + ingredient[2]
        result_char = chr(result_int)

        self.result = result_char
        return result_char
