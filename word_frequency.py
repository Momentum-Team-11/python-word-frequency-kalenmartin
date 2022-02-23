STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

# PUNCTUATION = !()-[]{};:'"\,<>./?@#$%^&*_~

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file) as file:
        d = dict()
        text_string = file.read()
        # print(text_string[0:100])
        print(f"{len(text_string)}")
        text_string = text_string.replace(".", "")
        text_string = text_string.replace(",", "")
        text_string = text_string.replace("'", "")
        text_string = text_string.replace("?", "")
        text_string = text_string.replace("!", "")
        text_string = text_string.replace("\\n", "")
        text_string = text_string.replace(":", "")
        text_string = text_string.replace("[", "")
        text_string = text_string.replace("]", "")
        text_string = text_string.replace("\"", "")
        text_string = text_string.replace("’", "")
        text_string = text_string.replace("-", "")
        text_string = text_string.replace("—", "")
        text_string = text_string.replace('"', "")
        text_string = text_string.lower().split()
        # print(text_string[0:100])
        # return text_string[0:100]
    
        text = text_string
        stop_word_set = set(STOP_WORDS)
        text_string = [item for item in text if item not in stop_word_set]
        print(text_string[0:100])
        # return text_string [0:100]

        for word in text_string:
            # print(word)
            if word in d:
                d[word] = d[word] + 1
            else:
                d[word] = 1
                
        for key in list(d.keys()):
            print(key, ":", d[key])
        
        # lines = file.readlines() 
        # print(type(lines))

        # text_string = file.read()
        # print(text_string)
        # print(f"{len(text_string)}")
    # word_list = text_string
    # word_list.lower


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
