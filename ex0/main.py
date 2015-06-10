# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# 1. Получить лист целых чисел, которые без остатка делятся на 3, в диапазоне от 0 до n
n = 10000000

# 2. Написать функцию, которая принимает в качетве параметров число n, а возвращает лист
# с последовательностью Фибоначчи в диапазоне от 0 до n.

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

    # !!!
    # вставь свой код сюда

    return count if string is not None and sub_string is not None else None


print(sub_str_entry_counter(input_str, 'Master'))

# 4. Написать функцию, которая принимает строку (например "MDMA"), а возвращает строку с символами в побратном
# порядке (например "AMDM").

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
