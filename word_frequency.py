from ast import keyword
from cgitb import text
from hashlib import new


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

# PUNCTUATION = !()-[]{};:'"\,<>./?@#$%^&*_~

def print_word_freq(file):
    d = dict()
    
    # """Read in `file` and print out the frequency of words in that file."""
    with open(file) as file:
        # sd = sorted_dict()
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
        text_string = text_string.lower()
        newword_list = text_string.split()
        # print(text_string[0:100])
        # return text_string[0:100]

        newword_list_filtered = {}
        for word in newword_list:
            if word not in STOP_WORDS:
                if word in newword_list_filtered:
                    newword_list_filtered[word] += 1
                else:
                    newword_list_filtered[word] = 1
    
        newword_list_sorted = []
        newword_list_sorted = dict(sorted(newword_list_filtered.items(), key=lambda seq: seq[1], reverse=True))
        for key,value in newword_list_sorted.items():
            print(f"{key:>20} | {(value * '*'):<20}")
        
        return newword_list_sorted
        # word_dict = {}
        # for word in newword_list_sorted:
        #     word_dict[word] = newword_list_sorted.count(word)
        # for word in word_dict:
        #     print(f"{word} | {word_dict.get(word)} {'*' * int(word_dict.get(word))}")
        
        
        
        # text = text_string
        # stop_word_str = str(STOP_WORDS)
        # text_string = [item for item in text if item not in stop_word_str]
        # print(text_string[0:25])
        # return text_string [0:100]

        # for word in text_string:
        #     # print(word)
        #     if word in d:
        #         d[f"{word}"] += 1
        #     else:
        #         d[f"{word}"] = 1
                
                
                
        # d = sorted(d.items(), key=lambda x: x[1], reverse=True)
        
        
        # for key in list(d.keys()):
        #     print(key, ":", d[key])
                
        
                

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
