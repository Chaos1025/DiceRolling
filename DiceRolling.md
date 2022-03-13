## 1 故事背景

&emsp;&emsp;1657年荷兰数学家Huygens根据发生数学家Pascal与Fermat之间关于掷骰子中的可能性问题做出的讨论，并结合自己的研究写成了《论掷骰子游戏中的计算》。这本书被认为是概率论中最早的论著。

&emsp;&emsp;这本书中记录了两位数学家关于法国贵族De Mere发现的一个“矛盾”的书信讨论。

&emsp;&emsp;De Mere认为掷一个骰子四次至少出现一次6点和掷一对骰子24次至少出现一次双6的可能性是相等的，他的推断过程如下：

&emsp;&emsp;一个骰子抛掷一次出现6点的可能性是$1/6$，所以抛掷四次就应该有$4\times 1/6=2/3$的可能性至少出现一次6点；而抛掷一对骰子一次出现双6的可能性是$1/36$，那么抛掷24次就一定有$24\times 1/36=2/3$的机会得到至少一次双6。于是这两个事情应该是等可能的。但是经验表明第一个事件的可能性应该会更大，“矛盾”便在于此。

&emsp;&emsp;而在Pascal与Fermat的通信中，他们讨论了这个问题，并得出了合理并且正确的结果。他们的计算依据主要有三点：输赢是对立事件，即它们的可能性之和为1；掷骰子的每一次之间都是相互独立的；乘法原理。据此正确的计算过程应该是：掷一个骰子四次至少出现一次6点的可能性为$1-\frac{5}{6}\times\frac{5}{6}\times\frac{5}{6}\times\frac{5}{6}\approx51.77\%$，而掷一对骰子24次至少出现一次双6的可能性则为$1-(\frac{35}{36})^{24}\approx49.14\%$。由此便可以发现这两个事件发生的可能性虽然很接近，但二者并不相等。

&emsp;&emsp;而De Mere原来的说法也有一个很大的漏洞，如果按照他的算法进行计算，当投掷一个骰子6次之后，出现每个面的可能性应该都是1，即每个面都出现一次，而这显然与常识矛盾，也很容易通过实验证明。

## 2 程序模拟

### 2.1 程序主体

&emsp;&emsp;据此，本人利用python提供的random模块对上述事件发生的可能性进行模拟，具体代码描述如下：（注：random模块产生的所谓随机数并非真正的随机数，但在此基本可以认为是对掷骰子事件的模拟）

```python
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
print(res)

# 事件出现的次数
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
# 计算并打印事件出现的频率
print("The frequency is:", "%.4f" % ((bingo/times)*100), "%")

print("Experiment Ending~")
```

### 2.2 模拟结果

&emsp;&emsp;最终模拟结果如下（为便于展示，这里不显示投掷结果列表）

&emsp;&emsp;掷一个骰子四次至少出现一次6点的情况如下：

```
Times of the experiments:999999
Amount of dices:1
Amount of rolling:4
The frequency is: 51.7340 %
Experiment Ending~
```
```
Times of the experiments:99999
Amount of dices:2
Amount of rolling:24
The frequency is: 49.1195 %
Experiment Ending~
```
### 2.3 结论

&emsp;&emsp;以上模拟结果与前文中根据三个论点而得到的计算结果基本一致，仅存在很小的误差。

