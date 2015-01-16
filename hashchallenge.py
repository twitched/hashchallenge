#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Create hash cracking challenges
"""

import sys, argparse, shlex

def main(argv):
    args = parse_args(argv)
    
    
def parse_args(argv):
    parser = argparse.ArgumentParser(description='Create hash cracking challenges',epilog=file_description(),formatter_class=argparse.RawDescriptionHelpFormatter)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-l', '--namelist', type=file, help="file containing challenge names, one per line")
    group.add_argument('-n', '--number', default=2, type=int, help="number of challenges to create")
    parser.add_argument('-c', '--challenge-file', type=file, required=True, help="File containing a list of challenges to add")

    return parser.parse_args(argv)
    
def file_description():
    return """
    The challenge file will have one challenge per line in the following format
        
        type points (hashcat_mask|num_words) algorithm description [url] [max_word]
    
    type is either h or w.  h is a hashcat mask, w is words from a file
    points - the number of points the challenge is worth
    hashcat_mask - a mask in hashcat format if the type is h. hashcat masks use built-in charsets (adds '9' for alphanumeric and removes ?b)
    num_words - the number of words from the given file if the type is w
    algorithm - one of md5, sha1, or sha256
    description - a description of the challenge
    url - URL of the file from which the words will be obtained with one word per line  This argument is required if the type is 'w'
    max_word - the size of the file given or the highest line to be read in the file.  This argument is required if a file is given
    """

def create_challenge_files(args):
    challenges = generate_challenges(args)
    if args.namelist:
        for name in args.namelist.open()

def generate_challenges(challenge_file):
    challenges = []
    for challenge in challenge_file:
        challenge = challenge.strip()
        if challenge.startswith("#") or challenge == '':
            pass
        else:
            generate_challenge_from_line()
                    
    return challenges

def generate_challenge_from_line(line):
    line_parts = shlex.split(line)

if __name__ == '__main__':
    sys.exit(main(sys.argv))