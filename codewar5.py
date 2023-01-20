def spin_words(sentence):
    x = sentence.split()
    for i in range(len(x)):
        if len(x[i]) >= 5:
            x[i] = x[i][::-1]
    return ' '.join(x)


# Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
def dig_pow(n, p):
    digits = str(n)
    result = 0
    for i in range(len(digits)):
        result += int(digits[i]) ** (p + i)
    if result % n == 0:
        return result / n
    else:
        return -1


def rot13(message):
    char = ''
    for i in message:
        if i.isalpha():
            ascii_code = ord(i)
            if i.isupper():
                char += chr((ascii_code - 65 + 13) % 26 + 65)
            else:
                char += chr((ascii_code - 97 + 13) % 26 + 97)
        else:
            char += i
    return char
