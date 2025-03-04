def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    data = {}
    for c in text:
        lower_c = c.lower()
        if lower_c not in data:
            # initialize the key
            data[lower_c] = 1
        else:
            # add to the count
            data[lower_c] += 1

    return data

def sort_on_count(dict):
    return dict["count"]

def report(char_dict):
    sorted_list = []
    for char in char_dict:
        sorted_list.append(
            {
                "char": char,
                "count": char_dict[char]
            }
        )
    sorted_list.sort(reverse=True, key=sort_on_count)
    for record in sorted_list:
        if record["char"].isalpha():
            print(f"{record['char']}: {record['count']}")
