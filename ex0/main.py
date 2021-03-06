# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# 1. Получить лист целых чисел, которые без остатка делятся на 3, в диапазоне от 0 до n
n = 10000000
div = []
for i in range(n):
    if not i % 3:
        div.append(i)
print(div)

print([j for j in range(0, n, 3)])


# 2. Написать функцию, которая принимает в качетве параметров число n, а возвращает лист
# с последовательностью Фибоначчи в диапазоне от 0 до n.
def fibonacci1(n):
    fib = [0,]
    a = 1
    b = 1
    while a <= n:
        fib.append(a)
        a, b = b, a + b
    return fib


def fibonacci2(n):
    def fibonacci_rec(m):
        if m == 0:
            return 0
        elif m == 1:
            return 1
        else:
            return fibonacci_rec(m - 2) + fibonacci_rec(m - 1)
    fib = []
    i = 0
    elem = fibonacci_rec(i)
    while elem <= n:
        fib.append(elem)
        i += 1
        elem = fibonacci_rec(i)
    return fib


# 3. Написать функцию считающую количество вхождений подстроки в строку
input_str = """
End of passion play, crumbling away
I'm your source of self-destruction
Veins that pump with fear, sucking darkest clear
Leading on your deaths' construction

Taste me you will see
More is all you need
Dedicated to
How I'm killing you

Come crawling faster
Obey your master
Your life burns faster
Obey your master
Master

Master of puppets I'm pulling your strings
Twisting your mind and smashing your dreams
Blinded by me, you can't see a thing
Just call my name, 'cause I'll hear you scream
Master
Master
Just call my name, 'cause I'll hear you scream
Master
Master

Needlework the way, never you betray
Life of death becoming clearer
Pain monopoly, ritual misery
Chop your breakfast on a mirror

Taste me you will see
More is all you need
You're dedicated to
How I'm killing you

Come crawling faster
Obey your master
Your life burns faster
Obey your master
Master

Master of puppets I'm pulling your strings
Twisting your mind and smashing your dreams
Blinded by me, you can't see a thing
Just call my name, 'cause I'll hear you scream
Master
Master
Just call my name, 'cause I'll hear you scream
Master
Master

Master, master, where's the dreams that I've been after?
Master, master, you promised only lies
Laughter, laughter, all I hear or see is laughter
Laughter, laughter, laughing at my cries
Fix Me

Hell is worth all that, natural habitat
Just a rhyme without a reason
Never ending maze, drift on numbered days
Now your life is out of season

I will occupy
I will help you die
I will run through you
Now I rule you too

Come crawling faster
Obey your master
Your life burns faster
Obey your master
Master

Master of puppets I'm pulling your strings
Twisting your mind and smashing your dreams
Blinded by me, you can't see a thing
Just call my name, 'cause I'll hear you scream
Master
Master
Just call my name, 'cause I'll hear you scream
Master
Master"""


def sub_str_entry_counter(string=None, sub_string=None):
    count = 0
    count = string.count(sub_string)
    return count if string is not None and sub_string is not None else None


print(sub_str_entry_counter(input_str, 'Master'))

# 4. Написать функцию, которая принимает строку (например "MDMA"), а возвращает строку с символами в побратном
# порядке (например "AMDM").


def reverse_string1(string):
    temp = list(str(string))
    temp.reverse()
    return ''.join(temp)


def reverse_string2(string):
    temp = list(str(string))
    for i in range(0, len(temp) // 2):
        temp[i], temp[-1 * (i + 1)] = temp[-1 * (i + 1)], temp[i]
    return ''.join(temp)

# 5. Нарисуй превдографикой бабочку, чего нить вроде такой:
#
# Z          Z
# ZZZ      ZZZ
# ZZZZZ  ZZZZZ
# ZZZZZZZZZZZZ
# ZZZZZ  ZZZZZ
# ZZZ      ZZZ
# Z          Z
#


def butterfly_init(m=7, n=13, sym="Z"):
    butterfly = [[sym,] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            if i < m // 2 and 2 * i + 1 <= j <= (n - 2) - 2 * i or \
               i >= m // 2 and (m - i) * 2 - 1 <= j <= n - 2 * (m - i):
                butterfly[i][j] = " "
    return butterfly


def butterfly_draw(butterfly):
    for i in range(len(butterfly)):
        print("".join(butterfly[i]))


but = butterfly_init(9, 15)
butterfly_draw(but)
