"""Main"""

import argparse

import basepart
import ko

def main():
    ARG_PARSER = argparse.ArgumentParser()
    ARG_PARSER.add_argument('language', type=str)
    ARG_PARSER.add_argument('length', type=int)
    ARG_PARSER.add_argument('repeat', type=int)
    ARG = ARG_PARSER.parse_args()

    for idx in range(ARG.repeat):
        RESULT = list()

        if ARG.language == 'ko':
            for idx in range(ARG.length):
                RESULT.append(ko.ComposerElementKorean( \
                    initial=basepart.IncludeList(ko.ComposerElementKorean.recommend_initial), \
                    medial=basepart.IncludeList(ko.ComposerElementKorean.recommend_medial), \
                    final=basepart.IncludeList(ko.ComposerElementKorean.recommend_final) \
                    ).compose() \
                )
        else:
            raise basepart.NamingLibException('{} is unsupported language'.format(ARG.language))

        print(''.join(RESULT))

if __name__ == '__main__':
    main()
