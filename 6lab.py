import random


def task1_1():
    print(f"Task 1.1")
    data = open("data/text1.txt")
    for i, line in enumerate(data):
        print(line, end='')
    data.close()


def task1_2():
    print(f"\n\nTask 1.2")
    data = open("data/text1.txt")
    lines = data.readlines()
    print(lines[random.randint(0, len(lines))])


def task1_3():
    print(f"\n\nTask 1.3")
    data = open("data/text1.txt").read()
    uppercase_count = 0
    for i in range(0, len(data)):
        if data[i].isupper():
            uppercase_count += 1
    print(uppercase_count)


def task2_4():
    print(f"\n\nTask 2.4")
    data = open("data/text1.txt")
    lines = data.readlines()
    cnt = 0
    for line in range(0, len(lines)):
        if lines[line][0].upper() != 'D':
            cnt += 1
    print(cnt)


def task2_5():
    print(f"\n\nTask 2.5")
    data = open("data/text1.txt")
    lines = data.readlines()
    cnt = 0
    for i in range(0, len(lines)):
        line = lines[i]
        if line[len(line) - 1] == '\n':
            if line[len(line) - 2].upper() == 'F':
                cnt += 1
        else:
            if line[len(line) - 1].upper() == 'F':
                cnt += 1
    print(cnt)


def task2_6():
    print(f"\n\nTask 2.6")
    data = open("data/text1.txt")
    lines = data.readlines()
    cnt = 0
    for i in range(0, len(lines)):
        line = " " + lines[i].lower() + " "
        cnt += line.count(" all ") + line.count(" none ") + line.count(" all\n") + line.count(" none\n")
    print(cnt)


def task2_7():
    print(f"\n\nTask 2.7")
    data = open("data/text1.txt")
    punctuation = ".?!,;:-_'\" "
    lines = data.readlines()
    words = [i.lower().split() for i in lines]
    for i in range(len(words)):
        for j in range(len(words[i])):
            if words[i][j][len(words[i][j]) - 1] in punctuation:
                words[i][j] = words[i][j][:-1]
    words_dic = {}
    for i in words:
        for j in i:
            if j in words_dic:
                words_dic[j] += 1
            else:
                words_dic[j] = 1
    print(words_dic)


def task2_8():
    print(f"\n\nTask 2.8")
    data = open("data/text1.txt")
    lines = data.readlines()
    words = [i.lower().split() for i in lines]
    punctuation = ".?!,;:-_'\" "
    for i in range(len(words)):
        for j in range(len(words[i])):
            if words[i][j][len(words[i][j]) - 1] in punctuation:
                words[i][j] = words[i][j][:-1]
    longest_word = words[0][0]
    for i in words:
        for j in i:
            if len(j) > len(longest_word):
                longest_word = j
    print(longest_word)


def task3_9():
    print(f"\n\nTask 3.9")
    data = open("data/text1.txt").read()
    data = data.replace('B', 'J')
    data = data.replace('b', 'j')
    print(data)


def task3_10():
    print(f"\n\nTask 3.10")
    data = open("data/text1.txt")
    lines = data.readlines()
    cnt_a = 0
    cnt_b = 0
    for i in range(0, len(lines)):
        line = " " + lines[i].lower() + " "
        cnt_a += line.count('a')
        cnt_b += line.count('b')
    print(f"a={cnt_a}, b={cnt_b}")


def main():
    task1_1()
    task1_2()
    task1_3()
    task2_4()
    task2_5()
    task2_6()
    task2_7()
    task2_8()
    task3_9()
    task3_10()


main()
