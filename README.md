# hashchallenge
Create password cracking challenges.

I created this program to generate challenges for my security students to crack.

[Example output](https://github.com/twitched/hashchallenge/blob/master/test/test_output/bob.md)

    	usage: hashchallenge.py [-h] (--namelist NAMELIST | --number NUMBER)
	                        --challenge-file CHALLENGE_FILE --output-dir
	                        OUTPUT_DIR [--header-file HEADER_FILE]

	Create hash cracking challenges

	optional arguments:
	  -h, --help            show this help message and exit
	  --namelist NAMELIST   file containing challenge names, one per line
	  --number NUMBER       number of challenges to create
	  --challenge-file CHALLENGE_FILE
	                        File containing a list of challenges to add
	  --output-dir OUTPUT_DIR
	                        Directory where output files will go
	  --header-file HEADER_FILE
	                        File containing a header to go before the table of
	                        challenges

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
