def chop(a_list):
    a = a_list.pop(0) and a_list.pop(-1)
    return None


def sum_multiples(a_list):
    i = 0
    x = []
    for i in a_list:
        if i % 5 == 0:
            x.append(i)
        elif i % 3 == 0:
            x.append(i)
    return sum(x)


def rotate(numbers, k):
    rot_right = numbers[-k:] + numbers[:-k]
    return rot_right


def on_all(func, a_list):
    mod_list = []
    for number in a_list:
          mod_list.append(func(number))
    return mod_list


def matrix_times_vector(mat, vec):
    prod_mat = []
    
    for ind_mat in mat:
        total = 0
        i = 0
        for ind_list in ind_mat:
            total += ind_list * vec[i]
            i += 1
        prod_mat.append(total)

    return prod_mat


def coder(text, to_morse=True):
    morse = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----'}

    morse_flipped = dict((v,k) for k,v in morse.items())
    
    if len(text) == 0:
        print('')
    else:   
        if to_morse == True:
            text_clean = text.upper()
            out_morse = ""
            for text_clean in text_clean:
                out_morse += morse.get(text_clean, text_clean) + " "
            return out_morse.strip()

        else:
            out_eng = ""
            cleaned = text.replace('   ', ' / ')
            clean = cleaned.split()
            for clean in clean:
                out_eng += morse_flipped.get(clean, clean)
            return out_eng.replace('/', ' ')


def sort_by_key(items_with_keys, ascending=True):
    if ascending == True:
        sorted_list = sorted(items_with_keys, key = lambda x:x[1])
        return sorted_list
    else:
        reverse_list = sorted(items_with_keys,
                              key = lambda x:x[1], reverse=True)
        return reverse_list


def count_words(text):
    txt_low = text.lower()
    txt_list = txt_low.split()
    txt_list.sort()
    dict_text = {}
    for x in txt_list:
        dict_text[x] = txt_list.count(x)
    return dict_text


def display_tree(dictionary, indent=''):
    cleaned = sorted(dictionary.items()) 
    
    tree = '' 
    for key, value in cleaned:
        tree += indent + str(key) + ':' 
        if type(value) is not dict:
            tree += ' ' + str(value) + '\n'
        elif type(value) is dict:
            tree += '\n' + display_tree(value, indent + '  ')
        else:
            print('The input is invalid')
            break
    return tree


def get_nested_key_value(nested_dict, key):
    listed_key = key.split('.')
    
    if type(nested_dict) is not dict:
        return None
    else:
        for key_index in range(len(listed_key)):
            if ((type(nested_dict) == dict) and listed_key[key_index]
                in list(nested_dict.keys())):
                nested_dict = nested_dict[listed_key[key_index]]
            else:
                return None
        return nested_dict

