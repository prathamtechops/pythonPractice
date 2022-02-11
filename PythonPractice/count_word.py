def countword(filename):
    """Count the words in the file 

    Args:
        filename (text file): [will count the words in the file by spilting the strings]
    """
    try:
        with open(filename) as f:
            content = f.read()
    except FileNotFoundError:
        print('File not found: %s' % filename)
    else:
        words = content.split()
        num_words = len(words)
        print('Number of words: %d' % num_words)
filename = [ ]
for files in filename:
    countword(files)
