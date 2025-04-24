def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents=f.read()
        return file_contents

def get_num_words(path_to_file):
    fulltext= get_book_text(path_to_file).split()
    return len(fulltext)

def get_character_count(path_to_file):
    #return print(get_book_text("books/frankenstein.txt").lower().split(None,1))
    char_dict={}
    for c in list(get_book_text(path_to_file).lower()):
        if c in char_dict:
            char_dict[c]+=1
        else:
            char_dict[c]=1
    return char_dict

def sort_on(dict):
    return dict["num"]

def dict_sorter(dictionary):
    char_list=[]
    for key, value in dictionary.items():
        if key.isalpha():
            char_list.append({"char": key, "num": value})
            #print(f"key: {key} , value: {value}")
    char_list.sort(reverse=True, key=sort_on)
    return char_list
   

