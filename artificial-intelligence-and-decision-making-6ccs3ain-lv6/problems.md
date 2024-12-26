## Preface

只有一套例题，没答案，我根据gpt边学边做的。如有疑问请dd~

**1. The following network is a Hidden Markov Model:**

![Figure 1](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412262121422.png)

**If we have evidence about Y1 and Y2, and we establish the probability of X1, what kind of inference is this?**

A. Prediction

**B. Filtering**

C. Smoothing 

D. Flattening

E. None of the above

> 课程中没有学过隐式马尔科夫链，但是学过推理的几种类型，这道题相当于举了一个推理例子让我们猜它是什么类型的推理。
>
> 我认为答案是 Filtering。根据教材（570页）：
>
> ![image-20241226204304357](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412262043428.png)
>
> ![image-20241226204323237](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412262043293.png)
>
> prediction 是根据已知证据预测未来的状态；smoothing 是根据过去到现在的证据推理过去的某一状态；filtering 是根据观测到的状态反推其 evidence；flatten 好像不是推理部分的内容。
>
> 这题仍有待商榷。

---

**2. The random variables Y and Z are non-interacting causes of X. Given the conditional probability values P(¬x|y) = 0.1 and P(x|z) = 0.3, what does the Noisy Or model give as the value of P(x|y, z)?**

A. 0.9

**B. 0.93**

C. 0.27

D. 0.6

E. 0.28

> Noisy or 局部概率模型的特点是除了所有 cause 对结果的影响，还可能存在 leak probability 泄露概率。比如：x 是老师给学生及格成绩；y 是学生平时成绩表现；z 是学生在老师心里的印象；但是除了 y 和 z 两个原因，可能还有一个 x_0 表示老师是否要捞这个学生，这个值就是泄露概率，哪怕 y 和 z 都不想让 x 成为1，x_0 一个变量也足以影响最终 x 的结果=1.
>
> 在这个泄露概率的影响下，我们就没法直接通过 P(x|y)·P(x|z) 来计算 P(x|y,z) 了。只能通过 $$1-P(¬x|y)P(¬x|z)$$ 获得（y，z题目中说了是互相独立影响 x 的 cause）。

---

**3. Consider the joint probability table for the three binary variables P, Q and R:**

![image-20241226212113871](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412262121954.png)

**What is P(¬p∧ ¬r)?**

A. 0.113 

**B. 0.217** 

C. 0.51 

D. 0.636 

E. None of the above

> 很简单，把所有 ¬p∧ ¬r 的情况概率相加。

---

**4. Consider the joint probability table for the three binary variables P, Q and R:**

![image-20241226212706451](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412262127495.png)

 **What is P((p ∧ q) ∨ ¬r)?** 

A. 0.212 

B. 0.493 

**C. 0.438** 

D. 0.514 

E. None of the above

> 很简单，把图中黄色部分求和。

---

**5.  Consider the joint probability table for the three binary variables P, Q and R:**

![image-20241226213052887](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412262130129.png)

**What is P( ¬q|p, r)?**

A. a number in (0, 0.1] 

B. a number in (0.1, 0.2] 

C. a number in (0.2, 0.3] 

**D. a number in (0.4, 0.5]** 

E. None of the above

> 简单条件概率计算，黄色部分/蓝色部分。

---

**6. Consider the following normal form game:**

![image-20241226213605749](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412262136808.png)

**Identify any Pareto optimal outcomes:** 

**A. (U, L)** 

**B. (U, R)** 

**C. (D, L)** 

**D. (D, R)** 

E. There are none

> 我觉得全都是帕累托最优。想提升一方的收益的时候，必须牺牲另一方的收益才能满足（横向纵向或斜向切换都没有完全的更优解）。

---

**7. Consider the following normal form game:**

![image-20241226213850460](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412262138511.png)

**Identify the outcomes that minimize social welfare:** 

**A. (U, L)** 

B. (U, R) 

C. (D, L) 

**D. (D, R)** 

E. There are none

> 社会福利就是两方收益求和。4+4=8是最小值。

---

**8. Consider the following normal form game:**

![image-20241226214422206](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412262144255.png)

**Identify any pure strategy Nash equilibria:**

A. (U, L) 

B. (U, R) 

C. (D, L) 

D. (D, R) 

**E. There are none**

> 纳什均衡是一个均衡组合，比如假设 LU 是纳什均衡，纵向选择 L 的时候横向也偏向选 U，横向选 U 的时候纵向也偏向选 L。
>
> LU：选择 U 后纵向更偏向选 R，6>3
>
> RU：选择 R 后横向更偏向选 D，3>2
>
> LD：选择 L 后横向更偏向选 U，3>2
>
> RD：选择 D 后纵向更偏向选 L，5>3
>
> 没有纳什均衡。

---

**9. Given the Bayesian network: **

![image-20241226214735105](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412262147145.png)

**Which variables are in the Markov blanket of Q?**

**A. P** 

**B. R** 

C. T 

D. S 

E. None of the above

> 找马尔科夫链：该节点的父亲，儿子，儿子的其他父亲（后爸？）
>
> 答案就是：Q的儿子R，R的父亲P。

---

**10. In the Bellman equation:**

![image-20241226215105444](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412262151491.png)

**which elements represent the sensor model?**

A. U(s) 

B. R(s) 

**C. P(s'|s, a)** 

D. U(s') 

E. None of the above

> U(s)：效用。U(s')：下一状态的效用。R(s)：即时奖励（比如吃豆人走一步-0.4，促使吃豆人尽快结束游戏）。P：传感器模型，动作a从s到s'的概率。

---

**11. Given the probability distribution P(U,V,W,X,Y), and the query P(¬w|¬x, y), which of the following are hidden variables:**

 **A. U **

**B. V** 

C. W 

D. X 

E. Y

> 隐藏变量：没有观测到但可能影响结果。XY 是观测到的变量，W 是结果。

---

**12.  A variable X has values x1, ... xn, and there is a probability distribution P(X) over X. P(X) is such that:**

A. There is at least one P(xi) with value 1. 

B. E[x1 +x2] = x1 +x2 

**C. The values of P(xi) add up to 1.** 

D. There exists i and j such that P(xi) and P(xj), P(xi) + P(xj) = 1. 

E. For all $$i \in \{1,2,...,n\}$$ , xi has to be an integer.

> 分清变量值和对应概率的区别。
>
> A. 最多有一个。
>
> B. 两个变量的概率期望，不是他俩变量值求和，是他俩概率值求平均。
>
> C. 正确。
>
> D. 不一定有。
>
> E. 变量值爱多少多少，没人说非得整数。

---

**13.  In the context of Markov decision processes, a policy: **

**A. Generates the maximum expected utility.** 

B. Tells an agent what to do. 

C. Ensures that the agents always ends up in a terminal state eventually. 

D. Is a mapping from actions to states. 

E. None of he above.

> B: 策略只计算不同动作带来的效用并找到最大效用，不直接告诉 agent 采取哪个动作。
>
> C：没法保证游戏结束状态。吃豆人可能活可能死。
>
> D：说反了，根据状态采取行动。
