"""Naming set for Korean"""

import copy

import basepart

class ComposerElementKorean(basepart.ComposerElementBase):
    """Korean name composer - inspired by 이강성, 『파이썬 3 바이블』"""
    character = ( \
        tuple('ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ'), \
        tuple('ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ'), \
        tuple(' ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ') \
    )
    recommend_initial = list('ㄱㄴㄷㅁㅂㅅㅇㅈㅎ')
    recommend_medial = list('ㅏㅓㅗㅜㅡㅣ')
    recommend_final = list(' ㄴㅇ')
    initial = basepart.ListBase()
    medial = basepart.ListBase()
    final = basepart.ListBase()

    def __init__(self, initial=None, medial=None, final=None):
        pass # See the metaclass
    def compose(self):
        """Compose the Korean name"""
        character = self.character
        list_original = [self.initial, self.medial, self.final]
        list_process = [basepart.ListBase(), basepart.ListBase(), basepart.ListBase()]
        ingredient = [basepart.ListBase(), basepart.ListBase(), basepart.ListBase()]

        # Check type and init list_process
        for (idx, elem) in enumerate(list_original):
            if isinstance(elem, basepart.ListBase):
                list_process[idx] = copy.deepcopy(elem)
            elif elem is None:
                list_process[idx] = basepart.IncludeList(character[idx])
            else:
                raise basepart.NamingLibException('Check composer input type')

        for (elem, characterset) in zip(list_process, (character[0], character[1], character[2])):
            # Change str to index
            elem.digitize(characterset)
            # Check index whether that is out of range
            elem.check_element_index(characterset)

        # Fill the ingredient
        for (idx, elem) in enumerate(list_process):
            ingredient[idx] = elem.choice(character[idx])

        result_int = 0xac00 + ((ingredient[0] * 21) + ingredient[1]) * 28 + ingredient[2]
        result_char = chr(result_int)

        self.result = result_char
        return result_char
