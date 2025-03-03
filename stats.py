
def get_num_words(text):
    text_array = text.split()
    words_num = len(text_array)
    return words_num

def get_num_characters(text):
    character_dictionary = {}
    
    for character in text.lower():
        if character in character_dictionary:
            character_dictionary[character] += 1
        else:
            character_dictionary[character] = 1
    return character_dictionary

def sort_on(sortable_list):
    return sortable_list["count"]

def build_list_of_dictionaries(character_count):
    character_list_of_dictionaries = []

    for characters in character_count:
        dic = {}
        if characters.isalpha():
            dic["characters"] = characters
            dic["count"] = character_count[characters]
            character_list_of_dictionaries.append(dic)

    character_list_of_dictionaries.sort(reverse=True, key=sort_on)

    return character_list_of_dictionaries



