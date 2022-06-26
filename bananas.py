def bananas(s, word='banana'):
    result = set()

    if word == '':
        result.add(''.rjust(len(s), '-'))
        return result

    for i in range(len(s)):
        if word[0] == s[i]:
            left_s = ''.rjust(i, '-') + s[i]
            if s[i + 1:] == '' and word[1:] == '':
                result.add(left_s)
            else:
                right_s_list = bananas(s[i + 1:], word[1:])
                for right_s in right_s_list:
                    result.add(left_s + right_s)
    return result


print(bananas('bbananana'))
print(bananas('banann'))
print(bananas('banana'))
print(bananas('bananaaa'))
print(bananas('bananana'))
