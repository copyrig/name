"""Main"""

import argparse

import basepart
import ko

def main():
    """Main procedure of application"""
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('language', type=str)
    arg_parser.add_argument('length', type=int)
    arg_parser.add_argument('repeat', type=int)
    arg = arg_parser.parse_args()

    for _ in range(arg.repeat):
        result = list()

        if arg.language == 'ko':
            for _ in range(arg.length):
                result.append(ko.ComposerElementKorean( \
                    initial=basepart.IncludeList(ko.ComposerElementKorean.recommend_initial), \
                    medial=basepart.IncludeList(ko.ComposerElementKorean.recommend_medial), \
                    final=basepart.IncludeList(ko.ComposerElementKorean.recommend_final) \
                    ).compose() \
                )
        else:
            raise basepart.NamingLibException('{} is unsupported language'.format(arg.language))

        print(''.join(result))

if __name__ == '__main__':
    main()
