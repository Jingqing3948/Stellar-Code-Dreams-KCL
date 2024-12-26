## 介绍

人工智能主要从两个方面描述：“复刻**人类行为**”和“**理性**”。而大家对”智能“的主题也有两种看法：”智能“是**内部思维推理**，还是**外在行为**的表现。这两个维度会诞生四种不同的人工智能发展方向。

1. 类人行为：比如典型的图灵测试就是测试这类人工智能的，为了“骗过人类”。这类人工智能需要具备以下能力：

   - 自然语言处理：能听和说人类的语言。
   - 知识表示：能存储它接受的知识。
   - 自动推理：回答问题得出结论。
   - 机器学习：适应新环境，推断模式。

   以及可选的计算机视觉和机器人学（不同的输入输出方式吧）。

2. 类人思考：认知科学致力于研究人工智能的计算机模型和心理学。我们可以通过内省（反思自己思考的过程），心理实验（观察受试者的行为）和大脑成像等方式了解人类思维，并让程序模拟这些理论。

3. 理性思考：主要是通过逻辑推理（根据已知的内容推出结论，如：苏格拉底是人，人都是凡人，则苏格拉底是凡人）和概率（弥补不确定的条件），建立理性思维模型。

4. 理性行为：为取得最佳的（确定的或者期望的）结果而采取行动。

理性行为看起来优于类人行为，因为人类的思维模式可能会有很多无法达到的最优解（也就是：**可计算性**和**易处理性**的平衡）。但是完美理性计算代价太高了，环境因素过于复杂。所以后面会讲到有限理性，适当地采取一些行动。

AI：可以进行“思考”，做出决策，给其他软硬件分配任务。

> 做决策并不是 if else 那么简单，并不能涵盖大多数情况。23年我参加ST峰会的时候第一次开始了解AI，当时工作人员介绍他们的工厂电机可以通过深度学习判断一些异常状况（比如设备未水平，或者有异物卡住电机等）来停止电机。我当时就问，我说这为啥要用深度学习呢，不用不也能解决，他和我说状态机并不总是能准确判断所有情况的，利用深度学习总结一些已有模式，决策才会更加准确快速。23年ST的峰会主题之一就是AI的边缘侧应用。

Simple Agent： 给每种 percept 认知指向一个 action。比如，0是周一，1是周二，2是周三……检测到地面脏就开启吸尘，否则拖地……

<img src="https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202409302259773.png" alt="image-20240930225951674" style="zoom:50%;" />

弊端非常明显，首先代码量很大，情况太多的话速度也会变慢，比如GTA5里有19.8亿次的if。而且我们并不能准确判断出所有情况（地面怎样算脏？90%的部分被遮挡就算脏吗？边缘的90%和中部的90%情况如何清扫？）

所以对于所有可能的情况都准确已知的情况下，simple agent才更好。但是我们的环境中变量，影响因素太多了，大多数时候没有这么简单的情况。

Utility-based agents：穷举出当前情况的所有actions，以及其效用，并递归推导下一步。比如一枚象棋，可以先往哪些方向走，到达这些方向后又可以继续往哪些方向走……我们会发现有的方向走不了因为被其他棋子挡住，有的方向不能走因为可能走到对方棋子攻击范围内了，这些步骤的效用都不好都可以舍弃。

我们还可以根据这些数据计算出期望效用值。

但是效用代理的缺点也很明显，一方面消耗大量资源时间（穷举），另一方面很难看得长远，比如国际象棋棋局，这种代理方式很可能只按照每一步的最佳走法走，长远目光不行。

## LLM

通过构建单词短语之间的关联而建立。根据上文猜测下文应该说的内容，GPT就是非常典型的例子。

缺点在于：

1. 数据全部来源于训练日期前的数据。
2. 训练底层不透明（可能意思是我们很难知道模型被训练成什么样了？）
3. 可能会幻想，自己编造数据。
4. 如果数据来源不准确，不全面，有偏见等，也会影响生成的结果。所以需要很多评估，比如是否有偏见，数据准确度，语调等。

## 概率

这一段基本和机器学习是一样的内容，概率，条件概率，独立，贝叶斯公式等。

马尔科夫链：每个节点都条件独立于其他结点。**一个结点的马尔科夫链是他的父节点，他的子节点，和他的子节点的其他父节点**。

我们可以先用变量描述要解决的问题，然后将其转化为相互条件概率链接的马尔科夫链解决问题。

### Inference by enumeration 枚举推理法

列出所有条件概率。很明显这种方法能涵盖所有情况但是效率低。

<img src="https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410091446081.png" alt="image-20241009144650015" style="zoom:67%;" />

### Prior sampling 先验抽样

> 1）先验——根据若干年的统计（经验）或者气候（常识），某地方下雨的概率；
>
> 2）似然——下雨（果）的时候有乌云（因/证据/观察的数据）的概率，即已经有了果，对证据发生的可能性描述；
>
> 3）后验——根据天上有乌云（原因或者证据/观察数据），下雨（结果）的概率；
>
> 后验 ~ 先验*似然 ： 存在下雨的可能（先验），下雨之前会有乌云（似然）~ 通过现在有乌云推断下雨概率（后验）
>
> [机器学习中的先验、后验和似然_先验后验背景-CSDN博客](https://blog.csdn.net/qq_39905917/article/details/83035386)

我们随机抽样一些数字，通过其最终概率规律来预测最终结果，而不是精准地计算出所有条件概率。

因为现实世界中变量概率影响因素太多，这样计算负担过大。

先验采样适用于联合概率。

比如下面这个题：

![image-20241009154642824](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410091546895.png)

我们随机生成一个概率序列：0.4 0.2 0.71 0.2

0.4<P(C)，所以C发生。

0.2>=P(S|C)，所以S没发生。

0.71<P(R|C)，所以R发生。

S没发生，R发生的情况下，P(W|S,R)=0.9>0.2，所以W发生。

**记住：是我们随机生成的概率小于该概率，该情况才发生。**

那么这次采样结果就是：C, not S, R, W。

多采样几次总结出序列 P(c, not s, r, w) 的发生概率，采样越多越精确。

但是先验概率没法算条件概率。

### Rejection Sampling 接受-拒绝定理

比如计算P(X|e)，我们先用先验概率采样所有点，只选择其中落在e中的点进行统计。对于每个点i，让N[X=i]++统计总数，最后正交化数组N[X]统计所有在e范围内的X的概率分布情况。

简单来说就是落在e之外的不用嘛。不过会带来的问题在于，如果e特别小，那么就会浪费很多采样点没用。

### Likelihood weighting

已经观测到结果，条件发生的可能性。

采用最大最有可能发生的概率。

如题：

![image-20241009165638431](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410091656513.png)

也就是说，现在观测到下雨 Rain了，那么 Cloudy 和 WetGrass=true 的发生概率有多大？

还是按顺序推导。首先设权重w=1.

想满足C=true：让w=0.5

S没要求（not a evidence variable）所以=多少都行，不用改权重值。假设S=false。

R也是同理，不是条件，假设 R=true.

想让W=true，w=0.5*0.9=0.45.

所以权重为0.95的时候最可能发生有云且草地湿了后下雨了。

### Gibbs sampling

有点抽象，从一道例题来看吧。

条件概率图如下：

![image-20241009173512060](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410091735113.png)

我们想计算： P(Cloudy|Sprinker = true, WetGrass = true)

1. 随机初始化所有变量。evidence variables 的值要固定为题目要求，也就是 Sprinker = true, WetGrass = true。假设初始化得到的是 [Cloudy = true, Rain = false, Spinker = true, WetGrass = true]
2. 先采样 C，其他变量不变。获取 C 的马尔科夫链（S, R），从 P[C | S=true, R=false] 和 P[C=false | S=true, R=false] 中取样。采样完了根据概率分布决定C的值，假设是false。
3. 然后采样 R，其马尔科夫链是（C, S, WG），采样 P[R | C=false, S=true, W=true] 
4. 可能重复上述步骤多次。最后根据采样结果估算这些采样中 P(Cloudy|Sprinker = true, WetGrass = true) 的概率。

## Sequential decision making 顺序决策

比如走迷宫，每个结点依赖于之前的结点的选择。

decision making 的要点在于简化决策。主要有两种方法做决策：

1. 永远找最好的结果。
2. 永远规避最坏的结果。

### 乐观版：尽可能选择最好的结果

例题：投硬币，正面赔2元，反面赚3元，玩合适吗？

算数学期望，平均能得到0.5元，不玩0元。合适。

连玩10次的期望值就是5元。

*想起了齐先生的赌场老虎机*

当然并不是说玩了就能得到5毛钱，这只是“数学期望”，在数据量上来的情况下更可能偏向的结果。

制定决策其实就是转换为概率问题，我们在每个节点处选择概率可能性更大的结果，比如吃豆人往前走得分的期望是0.5，往左走是-1，往右走是-2，那么我们最终结果最好偏向于往前走。

吃豆人结束一整局后的分数期望就是利用 sequence 中每一步选择的期望效用（utility）计算最终效用。

### 悲观版：避开最坏的结果

比如下面这个图，乐观版追求最佳结果s6，选择a2方向。悲观版为了避开s4，选择a1方向。

![image-20241016232906205](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410162329292.png)

但这两种方式都有弊端：但是当前的最佳结果不一定是全局的最佳结果。下棋就是很明显的例子，每一步都想吃对方，可能会中陷阱。

### Transition Model：概率

用于描述多步概率，比如吃豆人走“上上下下左右左右”这条路径的概率。
$$
P(s'|s,a)
$$
从s出发，走了a的行动后（比如[上，上，下……]）到达s'的概率。

概率这东西有什么用？我只选择分数最高的决策不就可以了吗？并非如此，一些决策问题中充斥着不确定性，比如吃豆人在当前状态下，往左和往右走活命概率是0.1，往上走活命概率是0.8. 这种不确定性无法准确归纳到分数中，只有和分数效用结合才能取得更好的答案。（下面会给出计算公式）

Transition Model 是一阶马尔科夫链，只和当前以及下一步的状态有关，所以我们可以根据当前状态开始往后推出所有概率的概率表。

除了行动概率，我们还需要一个算分数的激励函数来鼓励小吃豆人更有效地寻路（比如，用时更短？吃掉的豆子更多？等等）。分数可能包含在地图的点位上（路径点上哪些地方有食物，到达此点吃豆人加分），以及吃豆人每一步行动会消耗分数来鼓励吃豆人尽快到达目的地。

这个问题也叫做：

### Markov decision process (MDP)：效用

已知：

- s：当前位置。
- A(s)：在s处能采取哪些行动。
- P(s'|s,a)：transition model。
- R(s)：奖励函数，s点行动后得到的奖励，可能是正数也可能是负数。

马尔科夫决策过程最终期望得到：policy $\pi (s)$，比如 $\pi (s1)=left$ 表示在 s1 处往左走的决策。

optimum policy：最佳决策 $\pi ^*(s)$。

utilities：最终效用。效用有很多种，比如：

- 有限还是无限？比如吃豆人，吃完所有豆豆就结束游戏了，如果每一步都扣分数，吃掉豆豆加分，那么 utilities 明显是有限的，有最大值。
- stationary 可统计的吗？比如同一套决策，两次应用，会得到相同的结果吗？第二局鬼魂的行动方式会不会发生改变？今天看到阴天，明天会不会不下雨？
- additive：每一步效用相加=最终效用。discount：  $R(s1)+\gamma R(s2)++\gamma ^2 R(s3)+...$ γ是折扣因子，0-1。

例题：+1 -1是两个出口，最终效用是所有效用相加。在四个场景中给定四个R(s)值，看看计算机会偏向于怎么走。

<img src="https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410162352374.png" alt="image-20241016235203319" style="zoom: 67%;" />

图1：每一步的损失太大了。吃豆人只想赶紧走到终点结束，哪怕是-1的终点，早些结束比绕路吃到+1的损失也小。

图2：损失小了一点，吃豆人尽可能避开-1的情况下朝着+1出口以最快速度前进。

图3：损失更小了，吃豆人显得没有那么在意每一步的损失了，不吃到-1的情况下，绕远路到+1都可以。损失不大。

图4：每一步都没有损失只有激励。吃豆人不想走到终点离开游戏，只想不停地在迷宫里徘徊，因为每一步都有加分。

图4的情况就可以用 discount 规避，如果想在迷宫里一直混分数，γR(s)得到的分数会越来越少。

如果在有限的决策步数内可以结束问题，那么每一步的平均奖励也可以作为评价结果的指标之一， expected utility。我们可以选择平均期望值更高的路径，这也是一种决策方法（感觉更有全局观一点）。
$$
\pi ^*=arg\; \mathop{max}\limits_{max}U^\pi (s)
$$
例题：图中给出了每个点位走到终点的期望效用。如果在左下角开始出发，走上路的期望效用要比走右路的大。

<img src="https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410171636764.png" alt="image-20241017163646639" style="zoom:67%;" />

最终我们得到的最佳效用公式：结合了不确定性和效用。
$$
\pi ^*(s)=arg\; \mathop{max}\limits_{a \in A(s)}\sum_{s'}P(s'|s,a) U^{\pi ^*} (s')
$$
其中最后一项就是单步期望效用，也就是说我们每一次决策都走期望效用最大的决策方向。

### Bellman equation

那么问题就转化为：如何得到单步期望效用？每个状态的即时奖励期望 + 下一个状态的价值期望，不同的决策可能导致不同的下一个状态的价值期望不同，我们尝试所有的决策，最后取得期望效用最大的结果。
$$
U(s)=R(s)+\gamma \mathop {max}_{a \in A(s)}\sum_{s'}P(s'|s,a)U(s')
$$
例：从(1,1)出发，格子中写了每个点位的期望效用。

如果我想往一个方向走，会有0.2的概率往这个方向的左右两侧走。

下面的公式是计算了4个方向的决策的效用。最终我们选择最大值。

![image-20241017184758222](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410171847327.png)

当然，每次移动的-0.04成本也可以用函数 c(s, a) 表示，可以赋值来表达移动偏好。

### Policy Iteration 策略迭代

Policy evaluation：给定一个 policy （比如当前的策略是向上走），求效用 U(s)

Policy improvement：根据效用找到当前状态的最好策略，更新效用。如果没有更好的策略，说明效用已经收敛了，当前策略已经是最佳策略了。

![[强化学习基础篇: 策略迭代 (Policy Iteration) - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/34006925)](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410171917677.webp)

如上例，首先所有点都采用“向下”的策略。然后计算期望效用，发现左右两列一直向下找不到宝藏需要更新策略，中间列还可以。

然后第一轮迭代，采用“横向移动”的策略，因为往中间列走可以带来更大的效用。而中间列不动。左右两列期望值变大了，那么左右两列最优策略更新.

但是这样计算量可能会很大（n个线性方程，每个有3种策略的话，计算量可能达到n^3^）所以我们取得近似值即可。

## Principle Component Analysis 主成分分析

之前我们已经学习了机器学习的决策方法。这部分主要讲述“怎么合理运用这些决策方法”。

PCA 是一种线性降维方法。

比如计算机视觉通过图片识别数字：

![image-20241101204707782](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411012047233.png)

每个图片都是128*128像素的，我们如果把这16384个像素点都作为特征/维度，计算量太大了。是否可以降低维度只选取部分对结果影响较大的特征？

比如是否可以降低维度为2维特征？我们选取两个适当的特征，找到的规律如下图：

![image-20241101205309695](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411012053930.png)

这时我们在输入一个测试图片，它在图中落到的位置如图：

![image-20241101205341680](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411012053761.png)

很明显可以推测它是0那一类的。

PCA 既方便数据存储，也降低了学习难度。

比如：判断学生公寓是“标准公寓”还是“豪华公寓”，“公寓大小”的影响维度可能有“公寓面积”和“几室几厅”等影响因素；“公寓位置”维度可能包括“离超市距离”，“离学校距离”，“离地铁距离”……等。

我们先选择“公寓面积”和“几室几厅”两个维度进行对比。绘制一张2维图并把所有数据点标注出来。

![image-20241101210624336](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411012106503.png)

这个图非常明显，我们应当舍弃 x 轴的特征因为数据集都是4室的房间。降维到1维只保留“公寓面积”即可。

当然一般情况都会更复杂：

![image-20241101211007184](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411012110254.png)

对于这个图我们找到一条线，让所有点到这条线的距离最之和（最小二乘距离）：

<img src="https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411012110391.png" alt="image-20241101211043265" style="zoom:67%;" />

这条线就是降维后的特征。

### 特征向量

如何实现降维？首先我们了解一些概念。比如原坐标轴写法如下：

<img src="https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411012235907.png" alt="image-20241101223535647" style="zoom:67%;" />

其变形可以写作（两个列向量）：

<img src="https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411012235173.png" alt="image-20241101223559089" style="zoom:67%;" />

这个就是从图1到图2的变形矩阵。对于原图1中的向量 (x,y) 乘以这个变形矩阵就是变形图中的向量。

<img src="https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411012238308.png" alt="image-20241101223833215" style="zoom:67%;" />

如果有一个向量乘这个矩阵后等于这个向量的一定倍数的向量，那么这个向量被称作 an eigenvector of the matrix M（M 矩阵的特征向量），倍数是 eigenvalue 特征值。
$$
M \cdot \bold{v}= \lambda \bold{v}
$$

### PCA 具体算法

1. 首先我们有包括所有数据所有维度的矩阵（每一行是一个数据，每一列是同一个维度。n×d矩阵）：

<img src="https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411012313454.png" alt="image-20241101231315350" style="zoom:67%;" />

2. 我们沿每个特征方向上求平均值，并且用原矩阵减去这个平均值把所有数据都调整到原点附近，这样更方便看出大致方向：

$$
B=\bold X - \bold{\overline{X}}
$$

大概效果如图：

![image-20241101231536083](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411012315159.png)

3. 再计算协方差矩阵，协方差矩阵主要作用是反应特征之间的相关性（获得一个d×d矩阵）。

$$
\bold C=\frac{1}{n}\bold{B}^T \bold B
$$

4. 选取前k大的特征向量 v_1到 v_k. 这部分好像比较难，本课程不涵盖，一般 python 直接解决。
5. 用特征向量组成一个 d×k 的矩阵。

![image-20241101233337882](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411012333956.png)

6. 用 W 和 x 数据点得到在新的维度上的 y 数据点：

$$
\bold y_i=\bold W^T \cdot \bold x_i
$$

y 是 1×d 的向量。

如何衡量特征向量的重要性？根据这k个新向量的方差比上原来的d个特征值（总方差）计算新的特征向量可以“解释”原来的特征向量的方差的占比。占比越大说明舍弃的部分占比方差越小，越没有意义，降维效果越好。
$$
\frac{\sum^r_{i=1}\lambda_i}{\sum^d_{i=1}\lambda_i}
$$

![image-20241101234233869](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411012342979.png)

## Consensus Mechanisms 共识机制

相比之前的算法，这种算法主要用于解决多个 Agent 的情况。

比如有一系列有颜色的 Agent 点，彼此之间能观测到其他点的颜色状态，我们每轮决策调整 Agent 颜色状态使得达到特定目标（如：全部同色；相邻的 Agent 异色；等等等等）。

### Voter Model 投票模型

比如下图的例子，每个节点的颜色就是当前的颜色状态，连线的结点表示彼此能互相观测到。

目标：reach consensus 达成共识，同一种颜色。

![image-20241110231520119](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411102315261.png)

投票模型：每一轮（round）每个节点随机抽取一个邻居节点，变成对方的颜色。

符号表示：

- t 时间表示第几轮。
- 无向图 $G=(V,E)$ 中存储了边和结点信息，比如一条边 $(v,u)$ 表示 v u 结点互相可见。v 结点的邻居集合用 $deg(v)$ 表示。
- $X=\{b,r\}$  存储了所有可选的颜色信息。
- 一次颜色转变的过程表示：$V\rightarrow X$。
- 某一时刻某个节点的颜色信息：$S_t(v)=b$

对于一幅给定的无向图，什么对尽快完成游戏，结点全部达到目标颜色来说是优势？这里有一个常见的误区是**误以为已经出现的目标颜色结点越多越快能结束游戏**。实际上这个说法并不准确，真正的衡量标准是**所有结点的目标颜色邻居的度之和越大，越快结束游戏（在没有死锁的前提下）。**
$$
Pr(S_{end}=blue|S_0=s)=\sum_{v \in V, s(v)=b}\frac{deg(v)}{2|E|}
$$
这个公式用于计算结束游戏的概览。分母上还用了总边数的平均，所以更准确了一些。

当然这是比较简单的问题，“结束游戏的概率有多大”。更复杂的问题可能是“第x轮结束游戏的概率”，“有权有向图（不是随机选取邻居进行变色，而是带有权重地选择）结束游戏的概率”，“对颜色的偏见（更倾向于变为某种颜色）情况下结束游戏的概率……）

### 应用：区块链技术

比特币，区块链，就是共识机制的典型应用。

比特币是一种电子货币。如果采用中心化的发放方式，一个中心服务器生产发放电子比特币，带来的问题在于中心服务器会成为黑客集中攻击对象。而且两个人转账必须通过中心服务器，中心服务器负载应该不小。

区块链是一种去中心化机制 decentralized consensus。每个结点都运行同一份程序，维护、存储、验证同一份账本（记录了转账信息），达成共识，也就是说只要去中心化的计算机网络中有一个结点的账本与其他结点不同，那么该节点的账本就不被视作有效。

节点发起交易就需要把转账信息打包成区块 block，并链接在一起 blockchain，其他所有节点核实账本的修改没有异常才认可此次交易。

上传正确区块的节点会得到一些激励（如比特币）。但是比特币网站是匿名的，如果只有激励没有惩罚那就可能受到恶意攻击。所以上传服务的节点需要完成一个计算题：工作证明 Proof of Work POW，这个题用于证明其工作有效性，上传节点算起来会很难，但是其他节点核实其正确性很简单（这就是比特币“挖矿”过程吧。计算过程也是一种哈希算法）。

区块链去中心化共识的四个部分：

1. 每个节点都独立验证交易有效性 transaction。
2. 通过挖矿节点 mining nodes 把交易打包成块，同时计算 POW。
3. 所有节点再验证块的有效性并打包成链。
4. 如果出现冲突（和其他节点的链不同），每个节点独立选取最大计算量的链（Longest-Chain-Rule）。
5. 如果出现两个计算量相同的冲突（可能由于网络延迟问题），那就等待明确答案出现再接收。

所以就算有节点恶意插入假块，过一段时间也会被取代。这个节点如果想一直维持假块，就需要一直在自己的假块链基础上计算新的块并链接发送给其他节点，但是由于 POW 问题，计算负担对于该节点来说非常大。

每个块10分钟左右就能产生（期望下），但是随之产生的比特币是逐渐减少的，2009年挖一个块有50个比特币，2020年左右630000个块才会产生6个比特币。而计算 POW 的过程其实很看运气，总体而言算力越大越可能更快地计算出结果。

## Game Theory 游戏理论

涉及多个 Agents 之间的交互，使得效用最大化。比如吃豆人游戏涉及到吃豆人和鬼两种 Agent，我们需要猜测鬼的行为并制定 solution strategy

例：choose a side 游戏，两辆车各从两个方向中选一个方向走，下图是收益矩阵 payoff matrix：

![image-20241126054816186](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411260548354.png)

可以看出 i 车走 up，j 车走 left 的时候或者正好相反的时候两者都有1的收益。

(up, left) 代表 i 往上，j 往左的结果。

对于某一个 Agent 的 payoff matrix 矩阵写法如下：

![image-20241126055000279](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411260550514.png)

$$a_{i'},_{j'}$$ 代表 i 采取 i' action，j 采取 j' action 的收益。

### Strategies

下面介绍几种效用策略。

#### Dominant Strategies 主导策略

如果采取某一个 action，取得的所有结果都优于另一个结果，可以说这个结果是占主导地位的，下图中明显对两个 Agents C 比 D 取得的结果都好：

![image-20241126055250801](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411260552062.png)

如果 s1 策略的所有效用都 > s2, 可以说 s1 strongly dominates s2.

如果 s1 策略的所有效用都 >= s2, 可以说 s1 weakly dominates s2.

我们可以先把效用一定最低的策略删掉再考虑其他情况。当然这种情况不太多见。

记住，每次只考虑某一侧的效用，比如下图，列策略就只考虑蓝色部分，可以删掉 R：

![image-20241126055803806](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411260558030.png)

#### Nash equilibrium 纳什均衡

指：在当前策略组合下，任何一方试图改变策略，都不会取得更好的结果。

下图中，当有一方选择 Y 后，另一方最优策略都是 Y。

![image-20241126060051945](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411260600188.png)

而 (X, Y) 就不是 NE 策略了，i 选 X 的时候 j 确实选 Y 合适，但 j 选 Y 的时候 X 选 Y 更合适。

一个游戏中可能有多个纳什均衡，也可能一个也没有。

#### Pareto Optimality 帕累托最优

如果某种结果下，想提升一个 Agents 的回报，就必须要牺牲另一个 Agents 的回报才能实现的话，那么这个结果就叫帕累托最优。

下图中 (C,D) (D,C) 是两个帕累托最优。**注意不光是横向和纵向对比，斜着也要满足，比如 j 从 D 到 C 提升后，i 保留原值 C 或者变成 D 都不会有更好的结果。**

![image-20241126060837133](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411260608278.png)

#### Social Welfare 社会福利

所有人福利求和，总体福利最大化才是最优结果。

### Normal form games 正规博弈

一个正规博弈 (N, A, u)：N 表示玩家 / Agents 个数，A 是存储了每个玩家可能的 actions 的集合，u 是每个玩家的效用真实值，比如 pay off 就是一种效用表示方式。

如果所有 player 的效用都是一样的（比如 payoff 表是对称的），那么可以称之为 common payoff game。

如果采取什么策略，总效益之和都一样，可以称之为 constant sum game. 如果=0，则为 zero sum game. （石头剪刀布）

### Mixed strategy 混合策略

就像 MDP 有0.2的概率不沿着目标方向前进，混合策略用概率来决定最终行为。我们需要计算 P 的最优值使得期望效益最大。

例题：

![image-20241126082944428](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411260829660.png)

求最佳 P(a1)。我们画两张图呈现随着 P(a1) 变化，j 选择 a3 或者 a4 的前提下效用变化：

![image-20241126083047287](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411260830723.png)

![image-20241126083054455](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411260830645.png)

两线交点处是 rational choice of mixed strategy。也就是 P(a1)=0.2，那么 P(a2)=0.8

## Software Agent 软件代理

### Agent Communications Languages (ACL)

我们希望代理可以独立、自动化地完成任务。

主要分为两种：

- Knowledge Query and Manipulation Language (KQML) 

- IEEE Foundation for Intelligent Physical Agents ACL  (FIPA ACL)

这些 ACLS 都包括两层交流信息：

1. 话题 topics
2. 其涉及到的 utterances 话语（比如：下雨了吗？下雨了）

#### FIPA ACL

语句类型包括：询问查询，通知，赞同，否认，请求等（下雨了吗？下雨了。没下雨吧……）knowledge-sharing and automated contract negotiations

这类语句比较简单，但是缺少论证、验证过程，自我转换过程 self-transformation。

#### ACL 的语义 Semantics

- Axiomatic 公理语义：阐述真理前提/结论。比如 A 告诉 B 下雨了，说明 A 相信下雨了且希望 B 相信下雨了，B 也知道 A 相信下雨了且希望自己相信下雨了（当然 B 不一定相信）. 或者计算机请求密码, A 相信 S 有密码且会给自己. 但是这并不一定发生。
- Operational 操作语义：状态的变化，比如“未登录状态”输入密码后变成“登录状态”。
- Game-theoretic 博弈语义：一些 players 之间相互对战，比如 AB 对战，语义为真当且仅当 A 总有获胜策略的情况下。
- Denotational 指称语义：比如 possible world Semantics，所有可能的状态散落在大世界中，一些状态可以推导出其他状态。

![image-20241126171733845](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411261717009.png)

#### Dialogue Game Protocols 对话博弈协议

FIPA ACL 的缺点是不够结构化。比如发起 query 不一定能受到响应。所以对话博弈协议用于规范化这一过程，比如假设会收到的答复，验证会收到的答复的准确性等（有点像 HTTPS）。

如下图：

![image-20241126172336773](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411261723891.png)

A 发起问话，B 可能给予 A 请求的内容或者给予不是A请求的内容，或者U代表没法回复。

随后 A 收到消息要质疑其有效性 Challenge 或者 accept 接受。如果接受了，对话就终止了。

如果质疑，B 就要拿出相应的 S 解释自己为什么这样回复。

然后回到 3 重复。

## Clustering 集群

比如分类问题。

### K-means

在机器学习课程中有了解：

https://stellaris.graysea.cn/kcl/machine-learning-7ccemmle/note#unsupervised-learning-wu-jian-du-xue-xi

将数据集分为 k 类。分类情况要求每个类的质心离该类中所有点欧几里得距离之和最小。

算法：随机选k个聚类点，将所有x分类到离其最近的聚类点的类中，计算每个类中所有 x 点的质心，所有质心更新为新的聚类点重复如上操作，直到质心不变为止。

但是可能会存在一些情况，尽管质心不变，但仍然不是最优解。比如如下的两张图聚类点都是该类的质心，但是距离总和不同。

![image-20241201053758545](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412010537704.png)

![image-20241201053807351](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412010538468.png)

### k-Means++

用于解决如上问题。

选择一些输入点x作为初始聚类点。

### K-median

不是求均值，而是中位数。

![image-20241201054018749](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412010540874.png)

### DBSCAN

一种基于密度的聚类算法。

两个参数：m 和 ε，m 是核心聚类点范围内的最少点数，ε 是核心聚类的半径。

- 首先统计所有的点周围 ε 半径的其他点。
- 统计完所有点的邻居信息后，如果这个点的邻居数大于 m，那么其就是一个核心聚类点。
- 核心聚类点保留，非核心聚类点内的点如果属于周围某些核心聚类点的 ε 半径内的点，就把这个点分配到那个聚类邻居中。否则，视作噪声点，舍弃。

### 确定合适的 k 值

如何确定 k 的数量多少合适？我们先画出不同 k 数量下 k-means 求得的欧几里得距离总和图：

![image-20241201055141855](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412010551020.png)

根据肘部定理，我们选择“肘部”的这个第一个下降得不再变快的点。因为这个点的 score 已经很低了，而且再增加 k 数量，score 不会下降多少。

### Flat Clustering 平坦聚类法

不是按距离来分的了。

比如我们将N篇文档分为k类（如科幻小说，历史小说……）分类结果满足特定的要求。最终挑选出最优的分类结果。比如四本书分3类，”计算机 物理 体育 体育“的分法不错，”科学 科学 网球 足球“的分法不好，因为感觉阶级乱了。

### Hierarchical Clustering 层级聚类

按一定层级进行分类。

例：

![image-20241201060019569](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412010600681.png)

那么层级聚类如何划分？通过两种方法。

#### Agglomerative 层次聚类（自下向上）

首先我们建立一个树形图来说明点与点之间的相似性。

对于相似度高的节点应该属于同一集群。也就是距离比较相近的一些组合点为同一集群。

两个集群之间距离的几种判别方式：

![image-20241201060922988](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412010609097.png)

Single 就是找距离最近的，最相似的一对点。

Average 是彼此之间相连的所有点的距离平均值。

Complete 是找距离最远最不像的两个点。

例：下例是通过 Single 建立集群的方式：

![image-20241201061154364](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412010611559.png)

![image-20241201061202473](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412010612576.png)

![image-20241201061225952](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412010612053.png)

这个过程可以建立一个层级树形图 dendogram：

![image-20241201061311377](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412010613539.png)



#### Divisive Heuristics 自顶向下聚类

接下来，对于 k 个聚类的划分，我们自顶向下依次划分。

比如首先可以分为 acebd 和 fghi 两个大类。以此类推。

切割的稀疏性 sparsity 用如下公式计算：

![image-20241201061750960](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412010617044.png)

分子是 S 和 S- 两个集合之间的连线的相似度之和。分母是他们两个内部的最小相似度。我们最终的聚类结果要让稀疏性最小。

## AI and Ethics AI 伦理问题

需要关注的问题：

- fairness 公平：不能带有偏见。
- transparency 透明度：输入数据，判断逻辑应当公开。
- explainability 可解释性：系统应该可以解释为什么这么做。
- rectification 可反转
- human involvement 是否可以由人类干预决策。
- governance of ai systems 政策。

责任分配：

- 开发人员编写的程序
- 开发人员的道德准则
- 开发人员的道德培训

### identify bias 识别偏见问题

比如以前银行贷款曾经试用过 AI 判断客户是否值得贷款，导致有一些客户穿着打扮长相可能会影响机器的判断。

在第一节课中介绍过，AI 有两种，数据驱动型（比如深度学习）和模型驱动型。数据驱动型没法解释为什么这样做，而模型驱动型可以，所以数据驱动型识别偏见很困难，所以可以专注于识别数据流和代码的正确性。

### 透明度问题

一般可能都需要我们建立一个仿照源模型逻辑的模型来呈现其内部透明逻辑。

模型驱动 AI 一般很好解释，就像 if else 结构（if 患者失去嗅觉 and 喉咙疼，then 可能是新冠……）

但是数据驱动型还是很难解释，因为它对于一些要处理的数据可能完全没有概念。而且当下机器学习深度学习方法仍然不成熟，需要大量数据。

### Humans in the loop 人类参与问题

什么情况下的应用需要人类参与，什么情况下不需要？参与的人类是什么职位结构呢？等等一系列问题。

