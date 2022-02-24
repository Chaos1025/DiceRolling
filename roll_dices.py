import random   # 用于生成随机数的模块


# 输入重复实验的次数
while True:
    times = int(input("Times of the experiments:"))
    if times > 0:
        break
    else:
        print("Wrong times!")
# 输入单次实验中抛掷骰子的数量
while True:
    diceNum = int(input("Amount of dices:"))
    if diceNum > 0:
        break
    else:
        print("Wrong amount!")
# 输入单次实验中抛掷骰子的次数
while True:
    rollNum = int(input("Amount of rolling:"))
    if rollNum > 0:
        break
    else:
        print("Wrong amount!")

# 用于储存最终结果的列表
res = []
# 抛掷times次
for n in range(0, times):
    # 通过生成器生成模拟的结果
    exp_res = [[random.randint(1, 6) for ndice in range(0, diceNum)]for nroll in range(0, rollNum)]
    # 将每次实验的结果放入总结果中
    res.append(exp_res)
# 打印出结果
# print(res)

# 事件出现的可能性
bingo = float(0)
# 统计事件发生的可能性
for n in range(0, times):
    sixNum = 0
    for nroll in range(0, rollNum):
        # 如果单次抛掷满足条件（抛一个骰子出现一个6点或者抛两个骰子出现双6）
        if res[n][nroll] == [6 for ndice in range(0, diceNum)]:
            sixNum += 1
    # 如果单次实验满足条件
    if sixNum > 0:
        bingo += 1
print("The frequency is:", "%.2f" % ((bingo/times)*100), "%")


print("Experiment Ending~")
