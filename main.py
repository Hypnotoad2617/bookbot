def main():
    from stats import get_num_words, get_character_count, dict_sorter
    import sys
   
    if len(sys.argv) <2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path=sys.argv[1]


    def print_report(path_to_file):
        sorted_list=dict_sorter(get_character_count(path_to_file))
        #do the printing
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path_to_file}...")
        print("----------- Word Count ----------")
        print(f"Found {get_num_words(path_to_file)} total words")
        print("--------- Character Count -------")

        for i in sorted_list:
            print(f"{i["char"]}: {i["num"]}")
        
        print("============= END ===============")
        return None


    print_report(book_path)


    return None

main()