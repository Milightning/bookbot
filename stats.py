def count_words(book):
    with open(book) as f:
        text = f.read()
        return len(text.split())
    
def get_char_number(book):
    with open(book) as f:
        text = f.read()
        lowercased_text = text.lower()
    char_count = {}
    for i in lowercased_text:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    return char_count

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    char_list = []
    for char, number in dict.items():
        char_list.append({"char": char, "num": number})
    char_list.sort(reverse=True, key=sort_on)
    return(char_list)