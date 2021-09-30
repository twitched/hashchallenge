#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Create hash cracking challenges
"""

import os, sys, argparse, shlex, challenge, collections, csv

pwd = os.getcwd()

def main(argv):
    args = parse_args(argv)
    print(args)
    create_challenge_files(args)

def parse_args(argv):
    parser = argparse.ArgumentParser(description='Create hash cracking challenges',epilog=file_description(),formatter_class=argparse.RawDescriptionHelpFormatter)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--namelist', help="a csv file containing challenge 'user_id' and 'name'")
    group.add_argument('--number', default=2, type=int, help="number of challenges to create")
    parser.add_argument('--challenge-file', type=argparse.FileType('r', encoding='utf-8'), required=True, help="File containing a list of challenges to add")
    parser.add_argument('--output-dir', required=True, help="Directory where output files will go")
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
    if args.namelist:
        with open(args.namelist, 'r', newline='') as csvfile, open(os.path.splitext(args.namelist)[0] + '_out.csv', 'w', newline='') as outfile:
            reader = csv.DictReader(csvfile)
            writer = csv.writer(outfile)
            writer.writerow(['user_id', 'name', 'challenge_file', 'solution_file'])
            for row in reader:
                name = row['name']
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
                challenge_file = os.path.join(challengenamedir, name.strip()) + ".csv"
                solution_file = os.path.join(solutiondir, name.strip() + "_solution.csv")
                write_challenges_to_file(challenges, challenge_file, False)
                write_challenges_to_file(challenges, solution_file, True)
                writer.writerow([row['user_id'], name, challenge_file, solution_file])
                
                

def write_challenges_to_file(challenges, file, show_collision):
    """Writes the given challenges to the given file as a Markdown table"""
    challenge_table = []
    counter = 1
    with open(file, 'w', newline='') as f:
        fieldnames = ['Number','Points','Description','Hash','Alg','Collision','Method' ]
        writer = csv.writer(f)
        writer.writerow(fieldnames)
        for challenge in challenges:
            collision = ''
            if show_collision:
                collision = challenge.password
            writer.writerow([counter, challenge.points, challenge.desc, challenge.digest, challenge.alg, collision, ''])
            counter = counter + 1

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
    print(line)
    parts = shlex.split(line)
    if len(parts) > 4:
        return challenge.Mask_challenge(parts[0], parts[2], parts[3], parts[1], parts[4], int(parts[5]), int(parts[6]))
    else:
        return challenge.Mask_challenge(parts[0], parts[2], parts[3], parts[1])


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
