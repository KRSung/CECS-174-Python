# user_input1 = input('Enter the first word: ')
# user_input2 = input('Enter the second word: ')


def testForAnagram(user_input1, user_input2):
    a = sorted(user_input1)
    b = sorted(user_input2)
    if a == b:
        return 'Anagram'
    else:
        return 'Different Words'


if __name__ == '__main__':
    print(testForAnagram(input('Enter the first word: '), input('Enter the second word: ')))
