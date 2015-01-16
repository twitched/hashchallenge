#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Create hash cracking challenges
"""

import sys, argparse

def main(argv):
    args = parse_args(argv)
    if args.help:
        print file_description()
    
def parse_args(argv):
    parser = argparse.ArgumentParser(description='Create hash cracking challenges',epilog=file_description(),formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-l', '--namelist', type=file, help="file containing challenge names, one per line")
    parser.add_argument('-n', '--number', default=2, type=int, help="number of challenges to create.  Ignored if name list given")
    parser.add_argument('-c', '--challenge-file', type=file, help="File containing a list of challenges to add")

    return parser.parse_args(argv)
    
def file_description():
    return """
    The challenge file will have one challenge per line in the following format
        
        type points (hashcat_mask|num_words) algorithm description [url] [max_word]
    
    type is either h or w.  h is a hashcat mask, w is words from a file
    points - the number of points the challenge is worth
    hashcat_mask - a mask in hashcat format if the type is h.
    num_words - the number of words from the given file if the type is w
    algorithm - one of md5, sha1, sha256, bcrypt, or scrypt
    description - a description of the challenge
    url - URL of the file from which the words will be obtained with one word per line  This argument is required if the type is 'w'
    max_word - the size of the file given or the highest line to be read in the file.  This argument is required if a file is given
    """

if __name__ == '__main__':
    sys.exit(main(sys.argv))