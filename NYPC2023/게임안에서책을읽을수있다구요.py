'''
프로그램이 안멈춰서 안되는 거였ㅈ다다다다다다ㅏ
'''
import math #math 모듈을 먼저 import해야 한다.
N, M = map(int, input().split())
cnt = 0
while cnt < N:
    letter = input()
    cnt += 1
    if letter[0]=='<':
        if letter=='<CENTER>':
            while True:
                letter = input().split()
                cnt += 1
                if letter[0]=='</CENTER>':
                    break
                printLetter = []
                for l in letter:
                    printLetter.append(l)
                    if len("-".join(printLetter)) > M:
                        print(("-"*((M-len("-".join(printLetter[:-1])))//2))+
                               "-".join(printLetter[:-1])+
                              ("-"*math.ceil(((M-len("-".join(printLetter[:-1])))/2.0))))
                        printLetter = [printLetter[-1]]
                if printLetter:
                    print(("-"*((M-len("-".join(printLetter)))//2))+
                           "-".join(printLetter)+
                          ("-"*math.ceil(((M-len("-".join(printLetter)))/2.0))))
        if letter=='<RIGHT>':
            while True:
                letter = input().split()
                cnt += 1
                if letter[0]=='</RIGHT>':
                    break
                printLetter = []
                for l in letter:
                    printLetter.append(l)
                    if len("-".join(printLetter)) > M:
                        print("-".join(printLetter[:-1]).rjust(M, '-'))
                        printLetter = [printLetter[-1]]
                if printLetter:
                    print("-".join(printLetter).rjust(M, '-'))
                pass
    else:
        letter = letter.split()
        printLetter = []
        for l in letter:
            printLetter.append(l)
            if len("-".join(printLetter)) > M:
                print("-".join(printLetter[:-1]).ljust(M, '-'))
                printLetter = [printLetter[-1]]
        if printLetter:
            print("-".join(printLetter).ljust(M, '-'))























