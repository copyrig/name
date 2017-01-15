"""Main"""

import argparse
import os

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
        'repeat', \
        type=int, \
        nargs='?', \
        default=1, \
        help='set the number of repetition' \
        )
    arg_parser.add_argument( \
        'length', \
        type=int, \
        nargs='?', \
        help='set the length of name' \
        )
    arg_parser.add_argument( \
        '-f', '--fresh', \
        action='store_true', \
        help='make the application return fresh result' \
        )
    arg_parser.add_argument( \
        '-p', '--print', \
        action='store_true', \
        help='print the result' \
        )
    arg_parser.add_argument( \
        '-s', '--storage', \
        default=basepart.DEFAULT_STORAGE, \
        help='set the path of result file' \
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

    # Generate and store
    file_stream = open(arg.storage, 'a+')

    idx_generated = 0
    idx_looped = 0
    while idx_generated < arg.repeat:
        result = list()
        file_stream.seek(os.SEEK_SET)
        filed_name = file_stream.readlines()

        idx_looped += 1

        if arg.language == 'ko':
            for _ in range(arg.length):
                result.append(ko.ComposerElementKorean( \
                    initial=basepart.IncludeList(ko.ComposerElementKorean.recommend_initial), \
                    medial=basepart.IncludeList(ko.ComposerElementKorean.recommend_medial), \
                    final=basepart.IncludeList(ko.ComposerElementKorean.recommend_final) \
                    ).compose() \
                )
        result = ''.join(result)

        if arg.fresh and (result + '\n') in filed_name:
            if idx_looped >= ( \
            (len(ko.ComposerElementKorean.recommend_initial) - 1) * \
            (len(ko.ComposerElementKorean.recommend_medial) - 1) * \
            (len(ko.ComposerElementKorean.recommend_final) - 1) \
            ):
                raise basepart.NamingLibException('generated all of the eligible names', idx_looped)
        else:
            file_stream.write(result + '\n')
            if arg.print:
                print(result)
            idx_generated += 1

    file_stream.close()

if __name__ == '__main__':
    main()
