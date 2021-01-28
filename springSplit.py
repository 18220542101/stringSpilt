'''给定一个人字符串,字符串由若干个word组成，每个word由数字和字母组成，空格分割。要求该字符串中每个word的字母部分逆序'''
def stringSplit(string):
    lis = string.split()
    length = len(lis)
    for i in range(0,length):
        lis[i] = charReverse(lis[i])
    string1 = ' '.join(lis)
    return string1

# 实现将一个单词的字母逆序输出的功能
def charReverse(word):
    word1 = word[::-1]
    return word1

# 输入内容并输出转化后结果
inString = input('请输入:\n')
print(stringSplit(inString))

