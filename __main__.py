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
        num_total_characters = ko.ComposerElementKorean.num_character_recommend ** 2
    else:
        raise basepart.NamingLibException('Unsupported language', arg.language)

    # General modification
    if arg.length <= 0:
        raise basepart.NamingLibException('Wrong name length', arg.length)
    if arg.repeat <= 0:
        raise basepart.NamingLibException('Wrong repeat number', arg.repeat)

    # Open file
    file_stream = open(arg.storage, 'a+')
    file_stream.seek(0)
    list_name_original = file_stream.readlines()
    list_name_added = list()

    # Generate and store
    idx_generated = 0
    while idx_generated < arg.repeat:
        result = list()

        if arg.language == 'ko':
            for _ in range(arg.length):
                result.append(ko.ComposerElementKorean( \
                    initial=basepart.IncludeList(ko.ComposerElementKorean.character_recommend[0]), \
                    medial=basepart.IncludeList(ko.ComposerElementKorean.character_recommend[1]), \
                    final=basepart.IncludeList(ko.ComposerElementKorean.character_recommend[2]) \
                    ).compose() \
                )
        result = ''.join(result)

        if arg.fresh and (result + '\n') in list_name_original + list_name_added:
            if len(list_name_original + list_name_added) >= \
                num_total_characters:
                raise basepart.NamingLibException('generated all of the eligible names')
        else:
            list_name_added.append(result + '\n')
            if arg.print:
                print(result)
            idx_generated += 1

    # Write to file and close file
    file_stream.writelines(list_name_added)
    file_stream.close()

if __name__ == '__main__':
    main()
