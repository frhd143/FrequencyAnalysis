# Labration 3 
# Skriven av Farhad Asadi, 11 oktober 2021



# Frekvensanalys

def frequency(file_name):
    file = open(file_name, "r")
    data = file.read()
    # conver all the charecters in data to uppercase
    data_lowercase = data.lower()
    # convert the data to a list
    all_words_lowercase = data_lowercase.split()
    # make a copy of the original list
    all_words_copy = all_words_lowercase.copy()
    # remove all duplicates from the copied list
    new_all_words_copy = list(dict.fromkeys(all_words_copy))
    word_and_number = {}
    for i in range(len(new_all_words_copy)):
        occurences = all_words_lowercase.count(new_all_words_copy[i])
        word_and_number[new_all_words_copy[i]] = occurences
    return word_and_number



def most_frequent(freq_dict):
    if len(freq_dict) < 10:
        freq_dict_copy = freq_dict.copy()
        return freq_dict_copy
    else:
        new_dict = {}
        # Sort the dictionary by value, high to low
        sort_freq_dict = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
        new_list = sort_freq_dict[0:10]
        for i in new_list:
            new_dict[i[0]] = i[1]
        return new_dict


def word_count(freq_dict):
    # convert the dictionary to a list ex. [("the", 2), ("most"), 1]
    # list of tuples
    freq_dict_list = list(freq_dict.items())
    total_word = 0
    for i in freq_dict_list:
        total_word += i[1]
    return total_word



def unique_words(freq_dict):
    # list of tuples
    freq_dict_list = list(freq_dict.items())
    length_of_freq_dict = len(freq_dict_list)
    return length_of_freq_dict


def mean_frequency(freq_dict):
    freq_dict_list = list(freq_dict.items())
    frequencies = 0
    for i in freq_dict_list:
        frequencies += i[1]

    denominator = len(freq_dict_list)
    average = frequencies / denominator
    return average



def median_frequency(freq_dict):
    sort_freq_dict = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    list_num = []
    for i in sort_freq_dict:
        list_num.append(i[1])


    list_num.sort()
    #print(list_num)
    if len(list_num) % 2 == 1:
        return list_num[len(list_num)//2]
    else:
        return (list_num[len(list_num)//2-1] + list_num[len(list_num)//2]) / 2


def closest_word(freq_dict, rate):
    freq_dict_list = list(freq_dict.items())
    new_list = []
    for i in freq_dict_list:
        new_list.append(i[1])
    # Find the nearest or closest vallue in a list to a given number
    closest_value = min(new_list, key=lambda x:abs(x-rate))
    for i in freq_dict_list:
        if i[1] == closest_value:
            return i[0]



# The script to run all funktions!
if __name__ == "__main__":
    print("Welcome to 'Frekvensanalys'\n")

    input_file = input("Which file do you want to examine?\n")
    var_frequency = frequency(input_file)
    var_word_cout = word_count(var_frequency)
    var_unique_words = unique_words(var_frequency)
    var_most_frequent = most_frequent(var_frequency)
    var_mean_frequency = mean_frequency(var_most_frequent)
    var_median_frequency = median_frequency(var_most_frequent)
    var_closest_word = closest_word(var_frequency, var_mean_frequency)

    print("\n")
    print("The file contanins: ")
    print("Word count: ", var_word_cout)
    print("Unique word count: ", var_unique_words, "\n")
    print("Here are the 10 most common words in the file in descending order: \n")
    print("Word\tNumber of occurrences")
    print("----------------------------------------------------")
    print("\n".join("{}\t{}".format(k, v) for k, v in var_most_frequent.items()))
    print("\n")
    print("Of the words in the top list is... ")
    print("Frequency-average = ", var_mean_frequency)
    print("Frequency-median = ", var_median_frequency)
    print("\n")
    print("The word ", "'",var_closest_word,"'", "has the frequency that is closest to the Frequency-average")
