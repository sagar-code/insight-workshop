# 3. Write code that will print out the anagrams (words that use the same
# letters) from a paragraph of text.


def is_anagram(st1, st2):
    """
    checks whether given two words are anagram or not
    :param st1: String
    :param st2: String
    :return: Boolean
    """
    if len(st1) != len(st2):
        return False
    else:
        st1_list =[]
        for _ in st1:
            st1_list.append(_)

        for s in st2:
            if s in st1_list:
                st1_list.remove(s)
            else:
                return False
    return True


if __name__ == "__main__":
    arr = input('Enter a paragraph: ').split()
    anagram_words = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if is_anagram(arr[i], arr[j]):
                l = [arr[i], arr[j]]
                anagram_words.append(l)

    print('Pair of anagram words found: ',anagram_words)