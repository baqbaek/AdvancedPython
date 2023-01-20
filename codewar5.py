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
