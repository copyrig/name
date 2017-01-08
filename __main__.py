"""Main"""

import argparse

import basepart
import ko

if __name__ == '__main__':
    ARG_PARSER = argparse.ArgumentParser()
    ARG_PARSER.add_argument('language', type=str)
    ARG_PARSER.add_argument('length', type=int)
    ARG_PARSER.add_argument('repeat', type=int)
    ARG = ARG_PARSER.parse_args()

    for idx in range(ARG.repeat):
        RESULT = list()

        if ARG.language == 'ko':
            for idx in range(ARG.length):
                RESULT.append( \
                                ko.ComposerElementKorean(basepart.ExcludeList( \
                                            ko.ComposerElementKorean.tenuis_consonant), \
                    final=basepart.ExcludeList(ko.ComposerElementKorean.multiple_final) \
                    ).compose() \
                )
        else:
            raise basepart.NamingLibException('{} is unsupported language'.format(ARG.language))

        print(''.join(RESULT))
