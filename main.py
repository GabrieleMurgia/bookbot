
def sort_on(dict):
    return dict["num"]

def main():
    with open('./books/frankenstein.txt') as f:
        file_contents = f.read()
        d_count_letters = {}
        list_of_dictionaries = []
        file_name = f.name



        for letter in file_contents:
            lower_letter = letter.lower()
            if lower_letter.isalpha():
                if lower_letter not in d_count_letters:
                 d_count_letters[lower_letter] = 1
                else:
                 d_count_letters[lower_letter] += 1
        
        for d in d_count_letters:
           list_of_dictionaries.append({
              "letter":d,
              "num":d_count_letters[d]
           })

        
        list_of_dictionaries.sort(reverse=True,key=sort_on)

        print(f"--- Begin report of books/{file_name}---")
        print(f"{len(file_contents.split())} words found in the document")
        print("  ")
        print("  ")
    
        for dictionary in list_of_dictionaries:
         print(f"The '{dictionary["letter"]}' character was found {dictionary["num"]} times")

        print('--- End report ---')

main()


