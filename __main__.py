"""Main"""

import argparse

import basepart
import ko

def main():
    """Main procedure of application"""
    # Parse arguments
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument( \
        'language', \
        help='set the valid language' \
        )
    arg_parser.add_argument( \
        'length', \
        type=int, \
        nargs='?', \
        help='set the length of name' \
        )
    arg_parser.add_argument( \
        'repeat', \
        type=int, \
        nargs='?', \
        default=1, \
        help='set the number of repetition' \
        )
    arg_parser.add_argument( \
        '-s', '--store', \
        default=basepart.DEFAULT_STORAGE, \
        help='set the storage of result' \
        )
    arg = arg_parser.parse_args()

    # Language-specified modification
    if arg.language == 'ko':
        if arg.length is None:
            arg.length = 2
    else:
        raise basepart.NamingLibException('Unsupported language', arg.language)

    # General modification
    if arg.length <= 0:
        raise basepart.NamingLibException('Wrong name length', arg.length)
    if arg.repeat <= 0:
        raise basepart.NamingLibException('Wrong repeat number', arg.repeat)

    # Generate name
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

        print(''.join(result))

if __name__ == '__main__':
    main()
