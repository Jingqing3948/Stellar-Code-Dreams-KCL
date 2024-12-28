## Preface

只有一套例题，没答案，我根据gpt边学边做的。如有疑问请dd~

**1. The following network is a Hidden Markov Model:**

![Figure 1](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412262121422.png)

**If we have evidence about Y1 and Y2, and we establish the probability of X1, what kind of inference is this?**

A. Prediction

B. Filtering

**C. Smoothing** 

D. Flattening

E. None of the above

> 课程中没有学过隐式马尔科夫链，但是学过推理的几种类型，这道题相当于举了一个推理例子让我们猜它是什么类型的推理。
>
> 我认为答案是 Smoothing。根据教材（570页）：
>
> ![ ](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412262043428.png)
>
> ![ ](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412262043293.png)
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

![Figure 3](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412262121954.png)

**What is P(¬p∧ ¬r)?**

A. 0.113 

**B. 0.217** 

C. 0.51 

D. 0.636 

E. None of the above

> 很简单，把所有 ¬p∧ ¬r 的情况概率相加。

---

**4. Consider the joint probability table for the three binary variables P, Q and R:**

![Figure 4](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412262127495.png)

 **What is P((p ∧ q) ∨ ¬r)?** 

A. 0.212 

B. 0.493 

**C. 0.438** 

D. 0.514 

E. None of the above

> 很简单，把图中黄色部分求和。

---

**5.  Consider the joint probability table for the three binary variables P, Q and R:**

![Figure 5](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412262130129.png)

**What is P( ¬q|p, r)?**

A. a number in (0, 0.1] 

B. a number in (0.1, 0.2] 

C. a number in (0.2, 0.3] 

**D. a number in (0.4, 0.5]** 

E. None of the above

> 简单条件概率计算，黄色部分/蓝色部分。

---

**6. Consider the following normal form game:**

![Figure 6](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412262136808.png)

**Identify any Pareto optimal outcomes:** 

**A. (U, L)** 

**B. (U, R)** 

**C. (D, L)** 

**D. (D, R)** 

E. There are none

> 我觉得全都是帕累托最优。想提升一方的收益的时候，必须牺牲另一方的收益才能满足（横向纵向或斜向切换都没有完全的更优解）。

---

**7. Consider the following normal form game:**

![Figure 7](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412262138511.png)

**Identify the outcomes that minimize social welfare:** 

**A. (U, L)** 

B. (U, R) 

C. (D, L) 

**D. (D, R)** 

E. There are none

> 社会福利就是两方收益求和。4+4=8是最小值。

---

**8. Consider the following normal form game:**

![Figure 8](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412262144255.png)

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

**9. Given the Bayesian network:**

![Figure 9](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412262147145.png)

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

![Figure 10](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412262151491.png)

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

**13.  In the context of Markov decision processes, a policy:**

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

---

**14. Use prior sampling to create an estimate of P(a b cd) based on three sampled events from the following network and its associated probabilities.**

![Figure 14](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412262216197.png)

**A. The first samples returns the event a ¬b c d.** 

**B. The second sample returns the event a ¬b c d.** 

C. The third sample returns the event a ¬b c d. [4 marks] 

D. There exists no sequence of random numbers such that the sample re turns the event a ¬b c d. 

E. None of he above.

> 记住是先验抽样抽到的概率小于对应概率值时该事件才会发生。
>
> 第一波：a ¬b c d
>
> 第二波：a ¬b c d
>
> 第三波：a b ¬c ¬d

---

**15. Use rejection sampling to create an estimate of P(a|b, ¬d) based on five sampled events from the following network and its associated probabilities.**

![Figure 15](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412262300163.png)

**Then, rejection sample yields the following estimate**

![ ](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412262320311.png)

> P 上方有一个 hat 代表是根据采样数据统计得到的概率，并非真实概率。只需要根据5个采样数据估计概率即可。

---

**16. Consider n binary random variables X1, X2... Xn. Which of the following  statements are correct.**

A. Assume n is even and you and you are promised that all Xi for i<=n/2 are independent and identically distributed random variables. Then the joint probability distribution P(X1, X2... Xn) can always be stored using O(n) space. 

B. There always exists i j such that Xi and Xj have the same distribution. 

**C. There are distributions such that it is required to store at least 2^n-2^-1 different values.** 

D. There are cases where the joint distribution can be stored in o(sqrt(n)) space. 

E. None of the above

> A. 如果所有变量都是独立变量，那么存储空间是 O(n)，分别存储每个变量的概率。如果只有一半是独立变量，存储空间是n/2+2^n/2^
>
> B. 不一定
>
> C. 从 n 到 2^n^-1 的存储空间都有可能。
>
> 如果所有变量都彼此独立：n
>
> 如果所有变量都不独立且对结果有影响：2^n^-1，-1是因为最后一种情况可以用1-其他情况获得，这叫归一化约束。
>
> 如果Xn-1和Xn依赖于其他变量，其他变量不彼此独立：2^n-2^-1.
>
> D. 最小就是O(n)了，不能再小了。

---

**17. A diagnostic test has a probability 0.95 of giving a positive result when ap plied to a person suffering from a certain disease, and a probability 0.10 of giving a (false) positive when applied to a non-sufferer. It is estimated that 0.5% of the population are sufferers. Suppose that the test is now administered to a person about whom we have no relevant information relating to the disease (apart from the fact that he/she comes from this population). Which of the following statements is correct:**

 A. The probability that the test result will be positive is 0.20425; 

B. The probability that, given a positive result, the person is a sufferer is 0.0495; 

**C. The probability that, given a negative result, the person is a non-sufferer is 0.9997;** 

D. The probability that the person will be misclassified (i.e., they get an incorrect diagnose) is 0.09975. 

E. None of the above

> 也是一个条件概率计算题。
>
> A. 诊断为阳性的概率：0.95\*0.005+0.10\*0.995=0.10425
>
> B. 阳性结果中诊断正确的概率：0.95\*0.005/A=0.0455
>
> C. 阴性结果中诊断正确的概率：(0.90\*0.995)/(0.05\*0.005+0.90\*0.995)=0.9997
>
> D. 诊断错误的概率：1-B+1-C=0.9548

---

**18.**

![Figure 18](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412271346518.png)

A. E[X] = 12 

B. E[X] < 10 

C. Pr(X > 1000) > 0 

D. Pr(X = 5) =1 / 32 

E. None of the above

> 应该是等比数列求和计算问题。但是我懒得算，反正 C 肯定是对的，如果 X 一直原地打转超过1000步才到达终点，这种情况是存在的，那么概率就>0.

---

**19. Which of the following statements are correct. **

**A. A Pareto optimal solution can minimise social welfare, but it doesn’t have to.** 

**B. A Nash equilibrium can minimise social welfare, but it doesn’t have to.** 

**C. A Nash equilibrium can be a Pareto optimal solution, but it doesn’t have to be.** 

**D. Consider the case with two players. A pair of strategies (i j) can be such that it a) is not Pareto optimal, b) it is not a Nash equilibrium and c) it does not optimise social welfare.** 

E. None of the above

> 好像是全对。帕累托最优和纳什均衡都有可能是最小的社会福利；帕累托最优有可能是纳什均衡；一个组合可能既不是帕累托最优，也不是纳什均衡，也不是最小社会福利。这些没有什么特殊的关系。

---

**20. Consider a game with payoff matrices A (to i) and B (to j). Let (x\*, y\*) be a mixed strategy that is a Nash equilibrium. Which of the following statements are correct:**

![Figure 20](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412271354113.png)

> 题目的意思是：A B 分别是玩家 i j 的收益。xAy\* 的意思是固定 y\* 策略的情况下，x 最大化 A 的收益，即玩家 i 无力改变策略。
>
> A：正确，首先等式右边，如果固定 y=y\*，那么想让 A 收益最大化，x 就只能选择 x\*。然后我们确实可以找到一个组合 x'Ay'>x\*Ay\*，因为纳什均衡并不一定是某个维度上的最大值，只是固定另一维度时，这个维度的最大值策略。
>
> B：正确，见下图，YY 是一个纳什均衡，但是 XX 带来的两个维度的收益都更高。
>
> <img src="https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412271408845.png" alt="Figure 20.1" style="zoom:50%;" />
>
> C：可能画等号
>
> D：不符合纳什均衡的定义，如果确定 y 选 y\*，x 最优解一定是 x\*
>

---

**21. Consider the argumentation framework shown below.**

![image-20241227151333727](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412271513861.png)

**Identify all complete extensions from the options below:** 

A.  {}

B. a3a5 

**C. a2a3** 

D. a2a3a5 

E. a2

> *21开始的三道题我都存疑，没找到这部分知识点。*
>
> complete extension 的要求：
>
> 1. 集合内部没有论点互相攻击。所以 D 不行。
> 2. 集合对所有外界攻击都反击回去了。所以 B 不行，a2 攻击 a5 没有被反击。
> 3. 集合尽可能大，包含所有不矛盾的点。所以 E 不行，因为 E 可以再加一个 a3.

---

**22. （还是上图） Identify all of the false statements from the options below. **

A. The empty set does not defend any arguments. 

**B. The only argument that is defended by the set a1 is a4.** 

C. The set a3 is admissible. 

D. The set a2a4 is conflict-free. 

**E. The set a1a2a3a4a5 is conflict free.**

> conflict-free 是指该集合内没有元素互相攻击。
>
> admissible 是指该集合满足 conflict-free 的前提下，还能防御外界所有攻击。
>
> A. 空集合没有防御任何攻击，对。
>
> B. a3 是唯一防御了 a1 攻击的元素。
>
> C. a3 不仅是 conflict-free 的，而且防御住了 a1 的攻击（打回去了），所以是 admissible 的。
>
> D. a2 a4 没有互相攻击，所以是冲突自由的。
>
> E. 其中有很多互相攻击的情况。错误。

---

**23.**

![Figure 23](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412272207474.png)

**Identify all of the true statements from the options below.** 

A. The set {} is a complete extension. 

B. The set a1a3 defends all of its elements. 

C. The set a1a3 is conflict-free. 

**D. The grounded extension is a1 .** 

E. The set a2 is a complete extension.

> A. 空集没法防御任何攻击，所以不是 complete extension.
>
> B. a3 自我攻击没有防御住，所以错误。
>
> C. a3 自我攻击了所以错误？存疑。
>
> D. grounded extension 是最小的且能防御住所有外界攻击的集合，a1 正确。
>
> E. a2 没有反击 a3 的攻击，不是 complete extension.

---

**24.**

![Figure 24](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412271536553.png)

![Figure 24.1](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412271536137.png)

**A. The maximum reward the agent may receive is 10.** 

**B. The environment is not deterministic.** 

C. The agent is guaranteed to reach the goal state at some point. 

**D. It is possible to determine the minimum reward that the agent may receive.** 

E. None of the above.

> 最大奖励10，最小奖励-10. 由于做出决策前不知道下一步状态，所以环境是非确定的。

---

**25. You are the lead AI software developer for a company which designs, builds and sells autonomous (self-driving) cars. One of the cars sold by your com pany is involved in a road accident, where the vehicle was faced with a sudden difficult choice. The owner of the self-driving car was in the passen ger seat of the car at the time, and she had the power to stop the car in an emergency. The choice faced by the self-driving car was either to keep driving straight ahead and face a head-on collision with an oncoming car driven by a human that was driving in the wrong lane OR to move onto the footpath where there was a risk of killing some pedestrians who were there. The self-driving vehicle stayed in its current lane and crashed into the oncoming vehicle, killing the family that was in the car. The insurance company that had insured the driver of the oncoming vehicle has now taken action in court to sue you and your employer for damages, saying that you were responsible for the actions of the self-driving car. Which one of the following arguments do you think a court would find the most acceptable?**

A. This is the responsibility of my employer, not me. I was just doing what I was told by my boss. 

B. The choice made by the self-driving car was a difficult ethical trade-off, with potential negative consequences no matter what choice was made. 

C. The owner of the self-driving car was a passenger in the car at the time, so she should have over-ruled the AI driving the car and stopped it. 

**D. Any driver, whether they be human or an AI program, has to make such a decision on the spur of the moment,and so neither myself nor my company can be held responsible for a decision made so quickly. The AI should be judged by the same standards as would apply if a human were driving the car.** 

E. As part of the software development for the car design, my team had run extensive game theory simulations. Based on these simulations, we expected the other driver to chicken out and swerve aside before the two vehicles crashed. It is not our fault that the human driver did not behave according to our simulations.

> 待定，B还是D呢。

---

**26.  The technology company you work for has tasked you with developing an AI application which searches social media, such as Facebook and Linked In, for information and photos of potential recruits and then matches this information against profiles of the company’s best-performing existing staff to identify the best potential recruits. The plan is that the Human Resources Department will contact the potential recruits to invite them for an interview. After developing the system but before putting it into production, you notice that almost all the recommended potential recruits are men. Your realize that this may be because most of the staff in the technology sector, including most of company’s existing staff and most potential recruits, are men. You also notice that the system seems to reject any potential recruits whose photos show them wearing a hat or other headgear. You do not know why the AI system does this, but it may just be some trivial quirk of a machine learning system. What do you do?**

A. Nothing. All AI systems have quirks, and it is best to leave them alone. 

B. This decision is the responsibility of my employer, so I will just follow orders. 

**C. Try to eliminate the bias against both women and hat-wearers.** 

D. Try to eliminate the bias against women but ignore the issue of the hat-wearers, as this is trivial. 

E. Try to eliminate the bias against hat-wearers but ignore the issue of gender bias, because this is a problem across the entire technology sector which one company cannot solve

> 消除所有偏见。
