import math
import time
from random import randint
from random import shuffle


def check(c, d):
    return maze[y + d] // 3 ** (x + c) % 3 == 0


def extend(c, d):
    if new and showing:
        maze[y - d // 2] += 3 ** (x - c // 2)
        for l in maze[1: -1]:
            while l > 0:
                if l % 3 == 1:
                    print(road, end='')
                else:
                    print(wall, end='')
                l //= 3
            print()
        print()
        time.sleep(0.1)
        maze[y] += 3 ** x
        for l in maze[1: -1]:
            while l > 0:
                if l % 3 == 1:
                    print(road, end='')
                else:
                    print(wall, end='')
                l //= 3
            print()
        print()
        time.sleep(0.1)
    else:
        maze[y - d // 2] += 3 ** (x - c // 2)
        maze[y] += 3 ** x
    z.append([x, y])


flag = 1
show, showing = False, False
setting = True
x, y = 0, 0
a, b = 11, 11
i = 0
difficulty = 5
wall, road, key = '000', '   ', ' 1 '
_12 = [1, 1, 2]
outlooking = [0, ['000', '   ', ' 1 '], ['OOO', '   ', ' X '], ['   ', '000', '111'], ['[]', '  ', '.’'],
              ['W', ' ', '|'],
              ['888', '000', 'OOO']]
massage = {4: ['当前版本3.5',
               '0.5（另一种设计）：生成不能填满外框，可能无解或多解的迷宫，无出入口，已经可以设置长宽。',
               '1   ：生成能填满外框，有且只有一解的迷宫，有固定出入口，应用程序化，‘生成同尺寸迷宫’快捷键，更改了外观。',
               '2   ：可以生成答案。',
               '3.0 ：可以生成十字路口（本来只有丁字路口）',
               '3.1 ：优化生成十字路口，可以设置难度（对于一个出入口未确定的迷宫，计算 随机生成的多组出入口 的答案 的难度值（统计路线长度和路口数），再通过玩家设置的难度确定相应难度值的出入口）',
               '3.2 ：增加大量彩蛋 包括制作组，设置迷宫尺寸上限下限',
               '3.3 ：可以在程序中更改外观，可以查询版本信息',
               '3.4 ：增加主题外观，优化交互流程，优化彩蛋生成（用字典检索）',
               '3.5 ：增加难度值显示，优化交互流程，修复若干bug'],
           666: ['made by Petri_chor (佩奇)   start from April   still updating', 'thank Rocket for help'],
           985: ['祝你考上985！'], 211: ['祝你考上211！'], 123456789: ['你真闲得慌']
           }

print('（默认 长11宽11）')

while flag != 0:
    if outlooking[0] == 0:
        print('0=结束')
        print('1=生成新迷宫')
        print('2=生成同尺寸迷宫')
        print('3=设置')
        flag = int(input('> '))
        print()

    outlooking[0] = 0
    if flag == 1 or flag == 2:
        while flag != 2:
            a = int(input('长：'))
            b = int(input('宽：'))
            if a < 2 or b < 2:
                print('长或宽太小！')
            elif a * b > 10000:
                print('长宽太大！')
            else:
                break
        if show:
            if a * b >= 100 or b > 11:
                showing = False
                print('若要显示迷宫的生成过程，应满足长*宽<100且宽<10!')
            else:
                showing = True
        maze = [3 ** (2 * a + 3) - 1]
        for i in range(2 * b + 1):
            maze.append(3 ** (2 * a + 2) + 1)
        maze.append(3 ** (2 * a + 3) - 1)
        z = [[2 * randint(1, a), 2 * randint(1, b)]]
        maze[z[0][1]] += 3 ** z[0][0]
        t = 2 * int(math.sqrt(a * b))
        _4 = [1, 2, 3, 4]
        while len(z) != 0:
            x1 = z[0][0]
            y1 = z[0][1]
            for i in range(_12[randint(0, 2)]):
                x = x1
                y = y1
                for j in range(randint(t // 2, t)):
                    shuffle(_4)
                    new = False
                    for face in _4:
                        if face == 1 and check(0, 2):
                            y += 2
                            new = True
                            extend(0, 2)
                            break
                        elif face == 2 and check(-2, 0):
                            x -= 2
                            new = True
                            extend(-2, 0)
                            break
                        elif face == 3 and check(0, -2):
                            y -= 2
                            new = True
                            extend(0, -2)
                            break
                        elif face == 4 and check(2, 0):
                            x += 2
                            new = True
                            extend(2, 0)
                            break
            z.pop(0)
            if len(z) > 4:
                i = randint(1, len(z) - 1)
                z[0], z[i] = z[i], z[0]
        _4 = [1, 2, 3, 4]
        t = 2 * a
        rank = []
        for enter in range(1, a + 1):
            exit_ = randint(1, a) * 2
            enter *= 2
            maze[-2] += 3 ** enter
            maze[1] += 3 ** exit_
            x = enter
            y = 2 * b
            face = 1
            count = 0
            z = [[[], [], [x, y]]]
            while x != exit_ or y != 2:  # 1=up 2=left 3=down 4=right
                face2 = []
                if face != 3 and not check(0, -1):
                    face2.append(1)
                if face != 4 and not check(-1, 0):
                    face2.append(2)
                if face != 1 and not check(0, 1):
                    face2.append(3)
                if face != 2 and not check(1, 0):
                    face2.append(4)
                if len(face2) == 0:
                    face = z[-1][0][0]
                    z[-1][0].pop(0)
                    x = z[-1][2][0]
                    y = z[-1][2][1]
                    if len(z[-1][0]) == 0:
                        z[-2][1].append(z[-1][1][0])
                        z.pop(-1)
                    else:
                        z.append([z[-1][0], [z[-1][1][0]], [x, y]])
                        z.pop(-2)
                elif len(face2) == 1:
                    face = face2[0]
                else:
                    face = face2[0]
                    face2.pop(0)
                    if len(face2) == 1:
                        z.append([face2, [1], [x, y]])
                    else:
                        z.append([face2, [2], [x, y]])
                if face == 1:
                    y -= 2
                    z[-1].append([x, y + 1])
                    z[-1].append([x, y])
                elif face == 2:
                    x -= 2
                    z[-1].append([x + 1, y])
                    z[-1].append([x, y])
                elif face == 3:
                    y += 2
                    z[-1].append([x, y - 1])
                    z[-1].append([x, y])
                else:
                    x += 2
                    z[-1].append([x - 1, y])
                    z[-1].append([x, y])
            for j in z:
                j.pop(0)
                j.pop(1)
                for k in j[0]:
                    count += k * 7
                j.pop(0)
                for k in j:
                    count += 1
            range_ = 0
            for j in rank:
                if j[2] < count:
                    range_ += 1
                else:
                    j[3] += 1
            rank.append([enter, exit_, count, range_])
            maze[-2] -= 3 ** enter
            maze[1] -= 3 ** exit_
        z = []
        j = ((a - 1) * (difficulty - 1)) // 4
        for i in rank:
            if i[3] == j:
                break
        enter = i[0]
        exit_ = i[1]
        maze[-2] += 3 ** enter
        maze[1] += 3 ** exit_
        print()
        print()
        print(road * (2 * a + 3))
        for j in maze[1: -1]:
            while j > 0:
                if j % 3 == 1:
                    print(road, end='')
                else:
                    print(wall, end='')
                j //= 3
            print()
        print(road * (2 * a + 3))
        if setting:
            print('此迷宫的难度值为', i[2])
        print()
        print('0=结束')
        print('1=继续生成新迷宫')
        print('2=生成同尺寸迷宫')
        print('3=设置')
        print('4=显示答案')
        flag = int(input('> '))
        print()
        outlooking[0] = 1

        if flag == 4:
            x = enter
            y = 2 * b
            face = 1
            count = 0
            z = [[[], [x, y]]]
            while x != exit_ or y != 2:  # 1=up 2=left 3=down 4=right
                face2 = []
                if face != 3 and not check(0, -1):
                    face2.append(1)
                if face != 4 and not check(-1, 0):
                    face2.append(2)
                if face != 1 and not check(0, 1):
                    face2.append(3)
                if face != 2 and not check(1, 0):
                    face2.append(4)
                if len(face2) == 0:
                    face = z[-1][0][0]
                    z[-1][0].pop(0)
                    x = z[-1][1][0]
                    y = z[-1][1][1]
                    if len(z[-1][0]) == 0:
                        z.pop(-1)
                    else:
                        z.append([z[-1][0], [x, y]])
                        z.pop(-2)
                elif len(face2) == 1:
                    face = face2[0]
                else:
                    face = face2[0]
                    face2.pop(0)
                    z.append([face2, [x, y]])
                if face == 1:
                    y -= 2
                    z[-1].append([x, y + 1])
                    z[-1].append([x, y])
                elif face == 2:
                    x -= 2
                    z[-1].append([x + 1, y])
                    z[-1].append([x, y])
                elif face == 3:
                    y += 2
                    z[-1].append([x, y - 1])
                    z[-1].append([x, y])
                else:
                    x += 2
                    z[-1].append([x - 1, y])
                    z[-1].append([x, y])
            for i in z:
                i.pop(0)
                i.pop(0)
                for j in i:
                    maze[j[1]] += 3 ** j[0]
            maze[2 * b] += 3 ** enter
            maze[2 * b + 1] += 3 ** enter
            maze[1] += 3 ** exit_
            print(road * (2 * a + 3))
            for i in maze[1: -1]:
                while i > 0:
                    if i % 3 == 1:
                        print(road, end='')
                    elif i % 3 == 2:
                        print(key, end='')
                    else:
                        print(wall, end='')
                    i //= 3
                print()
            print(road * (2 * a + 3))
            print()
            print('0=结束')
            print('1=继续生成新迷宫')
            print('2=生成同尺寸迷宫')
            print('3=设置')
            flag = input('> ')
            print()
            if flag == ' ':
                print('......')
                print()
                flag = 1
            elif flag == '***':
                print('language!!!')
                print()
                flag = 1
            elif flag == '彩蛋':
                print('这是一个迷宫程序！')
                print()
                flag = 1
            flag = int(flag)

    elif flag == 3:
        while flag != 0:
            print('0=返回（回车也行）')
            print('1=调整难度（当前难度', difficulty, '）')
            print('2=难度值显示（目前', setting, '）')
            print('3=设置外观')
            print('4=显示版本信息')
            print('5=显示迷宫生成过程（目前', show, '）')
            flag = input('> ')
            if len(flag) == 0:
                print()
                break
            else:
                flag = int(flag)
            if flag == 1:
                while flag == 1:
                    print('选择1到5的难度。')
                    difficulty = int(input('难度值：'))
                    if 0 < difficulty < 6:
                        outlooking[0] = 0
                        break
                    else:
                        print('请重新输入！')
            elif flag == 2:
                print('1=在生成迷宫时显示难度值')
                print('2=在生成迷宫时隐藏难度值')
                flag = int(input('> '))
                if flag == 1:
                    setting = True
                else:
                    setting = False
            elif flag == 3:
                print('0=自定义     1=经典       2=简约       3=反转     4=方块   5=紧凑    6=瞎眼')
                print('          000   000   OOO   OOO      000      []  []    W W    888000888')
                print('          000   000   OOO   OOO      000      []  []    W W    888000888')
                print('           1  1 000    X  X OOO   111111      .’.‘[]    ||W    OOOOOO888')
                print('          000000000   OOOOOOOOO               [][][]    WWW    888888888')
                flag = int(input('选择主题：'))
                if flag == 0:
                    wall = ''
                    while not (len(wall) == len(road) == len(key)):
                        print('请输入长度相同的字符以设置外观')
                        wall = input('墙壁：')
                        road = input('道路：')
                        key = input('答案：')
                else:
                    wall, road, key = outlooking[flag][0], outlooking[flag][1], outlooking[flag][2]
            elif flag == 5:
                print('1=显示生成过程')
                print('2=隐藏生成过程')
                flag = int(input('> '))
                if flag == 1:
                    show = True
                else:
                    show = False
                    showing = False
            if flag in [4, 666, 985, 211, 123456789]:
                for i in massage[flag]:
                    print(i)
            else:
                print('设置成功！')
            outlooking[0] = 0
            print()
        print()
        flag = 1
