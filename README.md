# hashchallenge
Create password cracking challenges.

I created this program to generate challenges for my security students to crack.  

    usage: hashchallenge.py [-h] [-l NAMELIST] [-n NUMBER] [-c CHALLENGE_FILE]
    
    Create hash cracking challenges
    
    optional arguments:
      -h, --help            show this help message and exit
      -l NAMELIST, --namelist NAMELIST
                            file containing challenge names, one per line
      -n NUMBER, --number NUMBER
                            number of challenges to create. Ignored if name list
                            given
      -c CHALLENGE_FILE, --challenge-file CHALLENGE_FILE
                            File containing a list of challenges to add
    
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
