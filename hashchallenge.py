#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

"""
Create hash cracking challenges
"""

import os, sys, argparse, shlex, challenge, tabulate, collections

pwd = os.getcwd()

def main(argv):
    args = parse_args(argv)
    print args
    create_challenge_files(args)

def parse_args(argv):
    parser = argparse.ArgumentParser(description='Create hash cracking challenges',epilog=file_description(),formatter_class=argparse.RawDescriptionHelpFormatter)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--namelist', type=file, help="file containing challenge names, one per line")
    group.add_argument('--number', default=2, type=int, help="number of challenges to create")
    parser.add_argument('--challenge-file', type=file, required=True, help="File containing a list of challenges to add")
    parser.add_argument('--output-dir', required=True, help="Directory where output files will go")
    parser.add_argument('--header-file', type=file, help="File containing a header to go before the table of challenges")

    return parser.parse_args(argv)

def file_description():
    return """
    The challenge file will have one challenge per line in the following format

        points mask algorithm description [url] [min_word][max_word]

    type is either h or w.  h is a hashcat mask, w is words from a file
    points - the number of points the challenge is worth
    hashcat_mask - a mask in hashcat format if the type is h. hashcat masks use built-in charsets (adds '?9' for alphanumeric and removes ?b)
    num_words - the number of words from the given file if the type is w
    algorithm - one of md5, sha1, or sha256
    description - a description of the challenge
    url - URL of the file from which the words will be obtained with one word per line  This argument is required if the type is 'w'
    min_word - the first line in the range from which to choose the words
    max_word - the last line in the range from which to choose the words
    """

def create_challenge_files(args):
    header = args.header_file.read()
    args.header_file.close()
    if args.namelist:
        for name in args.namelist:
            challenges = generate_challenges(args.challenge_file)
            args.challenge_file.seek(0)
            challengedir = os.path.join(pwd, args.output_dir, "challenges")
            if not os.path.exists(challengedir):
                os.makedirs(challengedir)
            challengenamedir = os.path.join(challengedir, name.strip())
            if not os.path.exists(challengenamedir):
                os.makedirs(challengenamedir)
            solutiondir = os.path.join(pwd, args.output_dir, "solutions")
            if not os.path.exists(solutiondir):
                os.makedirs(solutiondir)
            write_challenges_to_file(challenges, open(os.path.join(challengenamedir, name.strip() + ".md"), 'w+'), header, False)
            write_challenges_to_file(challenges, open(os.path.join(solutiondir, name.strip() + "_solution.md"), 'w+'), header, True)
        args.challenge_file.close()


def write_challenges_to_file(challenges, file, header, show_collision):
    """Writes the given challenges to the given file as a Markdown table"""
    challenge_table = []
    counter = 1
    for challenge in challenges:
        collision = ''
        if show_collision:
            collision = challenge.password
        challenge_table.append(collections.OrderedDict((('Number', counter),
                                ('Points', challenge.points),
                                ('Description', challenge.desc),
                                ('Hash', challenge.digest),
                                ('Alg', challenge.alg),
                                ('Collision', collision),
                                ('Method', ''))))
        counter = counter + 1

    file.write(header)
    file.write(tabulate.tabulate(challenge_table, headers="keys", tablefmt="pipe"))
    file.close()

def generate_challenges(challenge_file):
    challenges = []
    for challenge in challenge_file:
        challenge = challenge.strip()
        if challenge.startswith("#") or challenge == '':
            pass
        else:
            challenges.append(generate_challenge_from_line(challenge))
    return challenges

def generate_challenge_from_line(line):
    print line
    parts = shlex.split(line)
    if len(parts) > 4:
        return challenge.Mask_challenge(parts[0], parts[2], parts[3], parts[1], parts[4], int(parts[5]), int(parts[6]))
    else:
        return challenge.Mask_challenge(parts[0], parts[2], parts[3], parts[1])


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
