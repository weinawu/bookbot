def get_word_count(text):
    return len(text.split())

def get_letter_count(text):
    letter_counts = {}
    for char in text.lower():
        if char in letter_counts:     
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1
    return letter_counts


def get_sorted(dict): 
    list_dict = []
    temp = {}
    def sort_on(dict):
        return dict["num"]
    for key, value in dict.items():
        temp = {"char": key, "num" : value}
        list_dict.append(temp)
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict