atch size S 

## Probability 概率论基础

在正式开始机器学习方法之前，我们先学习一些概率论的知识以便后面进入算法正题。

### Random Variables 随机变量

#### Discrete 离散随机变量

随机变量x可能在集合X的范围内取值，比如投掷硬币的概率随机变量x，取值集合X={正面，反面}。随机变量实质是函数。

投硬币是一个离散的例子，X还可能是连续的集合。

注意区分随机变量x和它的取值 realization *x*的区别，x=*x* 意思是随机向量x取值为*x*（类似于投硬币事件x投出了*正面*结果吧。）rv x takes value *x*.

对于每个不同的*x*值，都有它在这个随机变量x里的概率，用函数表示就是：

**x~p(*x*)=Pr[x=*x*]**

p(x)的范围肯定是0到1的，概率不可能大于1.rv x中的所有概率求和=1.

- Binary/Bernoulli variable 二元随机变量：x中只有两个值，类似投硬币的正反。那么这两个值概率互补。比如投硬币正反概率各50%。

- categorical/multinoulli variable 分类随机变量：有多个结果。

<div align="center">


$$
\begin{aligned}
X&={0, 1, ... , C-1}\\
p(k)&=q_k\\
Random\; Variable\; q&=[q_0, q_1, ... ,q_{C-1}]
\end{aligned}
$$

</div>

且随机向量内所有元素求和=1.

机器学习中常用一种叫做 one-hot vector 独热编码的方式表示随机变量，就是q里面只有一个值=1，其他的都是0. 比如：

![image-20240930122901541](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202409301229711.png)

#### Continuous 连续随机变量

连续随机变量通常用概率密度函数表示，x~p(*x*)，同样p(x)在域上求积分=1.

比如经典的高斯变量，x~N(µ,σ^2^)，表示公式：
$$
p(x)= N(x|\mu,\sigma ^2) = \frac{1}{\sqrt{2\pi \sigma ^2}}exp(-\frac{(x-\mu)^2}{2\sigma ^2})
$$
![image-20240930123225957](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202409301232062.png)

### Expection 期望

也叫平均值，最有可能的结果。离散随机变量的期望：
$$
E_{\mathbb{x}\sim p(x)}[\mathbb{x}]=\sum_{x\in\mathcal{X}}p(x)\bullet x
$$
离散变量的**函数**的期望：给定 x 的，f(x) 的期望值是多少。可以理解为首先x有多大的概率等于这个值，然后再用x的这个值代入f(x)得到的结果，我们要计算这个结果的期望值。
$$
xE_{\mathbb{x}\sim p(x)}[f(\mathbb{x})]=\sum_{x\in \mathcal{X}}p(x)\bullet f(x)
$$
比如下题，cat 是分类分布，表示 x 有0.1的概率=1,0.2的概率=2,0.7的概率=3，求f(x)的期望值：
$$
\begin{aligned}
x\sim Cat([0.1,0.2,0.7])\,and\,f(x)=x^2\\
E_{x\sim Cat(q)}[x^2]=0.1 \cdot 0^2+0.2\cdot 1^2+0.3\cdot 3^2=3
\end{aligned}
$$
连续函数类似，求积分而已。
$$
xE_{\mathbb{x}\sim p(x)}[f(\mathbb{x})]=\int_{-\infty }^{+\infty }p(x)f(x)dx
$$
高斯随机变量 N(µ, σ^2^) 的期望，对于f(x)=x函数来说=µ，对于f(x)=x^2^函数来说=µ^2^+σ^2^.

- 高斯随机变量的期望是线性的.

### Vector 向量

这部分知识也多次出现了就不多赘述了。这里指的向量的表示形式是列向量（L×1长度）。

**inner product 内积**：两个长度相同的列向量每个元素相乘，x^T^y。内积一般用来衡量相似度 similarity.

比如下面这两对xy，内积都=6，说明其相似度差不多。

![image-20240930131327706](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202409301313822.png)

**norm 范数**：就是向量的标量长度，可以通过x^T^x计算。

L1范数：x^T^x

L2范数：L1范数再开根。

比如上面的笑脸图，除了右上角的y的L1范数=6，其他向量L2范数=8.

$\widetilde{x}$：x的归一化，相当于一个和x方向相同但是长度=1的向量，用x/L2范数（||x||）就可以得到。

### matrix 矩阵

**diagonal matrix 对角矩阵**：只有对角线上的值非零（a_ii）

![image-20240930132133255](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202409301321401.png)

L×1列向量的对角矩阵相当于把列向量中的元素均匀分到L×L矩阵的对角线上。两个列向量的乘积=一方的对角矩阵与另一方列向量的乘积。

**Symmetric matrix 对称矩阵**：矩阵转置仍然等于其本身。

### Random Vector 随机向量

随机变量中所有元素按列向量排列。其中某个元素的概率：Pr[x=x_i]

**joint pmf p(x) 联合随机向量**：类似于：第一次硬币投出正面，第二次投出反面的概率。p(x)=Pr[x1 = x1 and x2=x2...and xL = xL]

Bernoulli random vector 伯努利随机向量：只有两种情况，类似投硬币，一正一反。

Jointly Bernoulli random vector 联合伯努利随机向量：2个维度。

| x1/x2 | 0           | 1           |
| ----- | ----------- | ----------- |
| 0     | p(0,0)=0.45 | p(0,1)=0.05 |
| 1     | p(1,0)=0.1  | p(1,1)=0.4  |

连续随机变量的联合表示就从二维的平面变为三维的空间了。比如下图是高斯随机变量的联合表示图，x y 坐标决定z坐标值：

![image-20240930134543755](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202409301345912.png)

**Marginal Distributions 边际分布**：只考虑多个变量中的部分变量的概率。比如上面的表格，x1\~Bern(0.5)，x2\~Bern(0.45)（伯努利的写法是 Bern(非0部分的概率)）

**Conditional Distributions 条件概率**：当其他变量为xx的条件下，这个变量为xxx的概率是多少。比如上表格，x2=0的话x1的概率分布：P(x1=0 | x2=0)=0.45/0.55,P(x1=1 | x2=0)=0.1/0.55, (x1|x2=0)~Bern(0.18)

应用：比如生成式语言模型，已经生成了之前1k个词后下一个词为“xxx”的概率为多少。

**Independence 独立性**：两个变量没有什么关系。那么两者同时发生的概率就是两者分别发生的概率的乘积，p(x1, x2)=p(x1)p(x2).

p(x1,x2) = p(x1)p(x2|x1).

### 贝叶斯定理

*贝叶斯定理被称为：改变信念 brief 的定理，大概是从概率角度上让人更改自己的偏好。所以也常用在机器学习中。*
$$
p(x_2|x_1) = p(x_2) \frac{p(x_1|x_2)}{p(x_1)} 
$$


> 以吴军老师在中文分词领域举的一个例子来说，对于一个句子：南京市长江大桥，可以有两种划分：
>
> - 南京市 / 长江大桥
> - 南京市长 / 江大桥
>
> 到底哪一种更合理？我们可以计算条件概率：
>
> - P(长江大桥|南京市) = 出现“南京市”时，出现“长江大桥”的概率；
> - P(江大桥|南京市长) = 出现“南京市长”时，出现“江大桥”的概率。
>
> 提前准备好大量的中文语料，计算出两种分词的条件概率，我们就可以得出哪种分词更合理。
>
> [一文搞懂贝叶斯定理（应用篇） - Blogs - 廖雪峰的官方网站 (liaoxuefeng.com)](https://liaoxuefeng.com/blogs/all/2023-08-29-bayes-use/index.html)

生成式大模型，搜索引擎等常见其应用。

## Inference 推理

现在我们已经有一定概率论基础了。我们开始学习“推理”，即：已知概率的情况下，根据输入 x 猜测输出 t。

推理的中间过程是一个概率模型 probabilistic model （x和t的联合分布 p(x,t) ）来预测最可能的t。

模型的具体实现被称作预测器 predictor。

推理问题主要分为两类，离散的 detection （比如晴天或者雨天）和连续的 estimation（比如温度）。

而推理结果又分为两种：hard predictor 和 soft predictor，hard 就是有具体结果的（比如t是一个关于x的函数，代入x，t的值唯一确定）；soft 就是不确定的（当x=某个值时，t为0的概率有10%，为1的概率有90%）。

下面的公式示例中，第一行是 hard 的写法，代表：x=0时t的预测结果=1。

第二行是条件概率的 soft 的写法，代表：x=0时t=1的概率是0.2。
$$
\begin{aligned}
\hat t(0)=1\\
q(1|0)=0.2
\end{aligned}
$$

### Optimal Soft Prediction / Bayesian Inference 贝叶斯推理

比如我们求出，q(t|0)=Bern(t|0.8)，那么可以说：ˆ t(1) = 1 with associated probability of error of 0.2（误差=0.2的硬推理）。这样设置是最优的。

### Loss Function 代价函数

代价函数用于计算预测器和正确值之间的偏差，进而后续决定如何修改预测器让代价更小。

对于硬推理，我们用代价函数 loss function 记录预测的硬推理值与真实值之间的偏差来评估硬推理。
$$
\mathcal{l} (t,\hat t)=|t-\hat t|^k
$$
k一般=2，也就是平方损失 quadratic error loss。

一种损失函数：detection-error loss，也叫 0-1 loss。指实际值和预测值要么相等，要么差1.

$\mathbb{1}$ 是指示符函数，条件为真时=1，否则=0.
$$
\begin{aligned}
 \mathcal{l} (t, \hat t) = \mathbb{1}(t= \hat t)\\
 \mathbb{1}(a) = 
 \begin{cases}
      1 & \text{if a = true}\\
      
      0 & \text{if a = false}
    \end{cases}     
\end{aligned}
$$

什么情况下预测一定和真实值相等或者差1？比如只有0和1两种结果的伯努利随机向量情况（猜猜明天是晴天还是雨天。猜对了损失=0，猜错了=1）。

如何评估硬推理的整体性能？一般用损失函数的平均值 population loss 计算。
$$
L_p(\hat t(\cdot))=E_{(x,t)\sim p(x,t)}[l(t,\hat t(x))]
$$
比如下题，预测器是令t永远=1，求 population loss。只需要计算算错部分的概率即可。

<img src="https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410070004028.png" alt="image-20241007000444949" style="zoom: 50%;" />

### Optimal Hard Prediction 最优硬预测

最优硬预测器的预测思路就是让 population loss 最小的预测函数。比如上图，很明显^t(1)=0, ^t(0)=1 的代价最小，=0.15。

对于离散预测，我们只需要挑出概率最大的条件概率点作为预测值即可。

### Cross-Entropy Loss and Optimal Soft Prediction 最优软预测

预测函数q一定用后验概率p最好吗？

软预测的损失函数突然就上强度了，要算 log。cross-entropy loss：−log q(t|x)

这是因为，对数损失的惩罚更高，迫使预测器做出更高概率更准确额预测：

![image-20241007014247176](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410070142271.png)

population 对数损失的计算公式如下（按x求期望)：

![image-20241007014320347](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410142205452.png)

[对数损失（Log Loss）详解（code） - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/659617924)

最优软预测就是让 log loss 最小化的预测取值。

## Supervised Learning 监督学习

### 监督学习简介

推理和学习的主要区别在于 p(x, t) 是否已知。下面的天气例题说明了这一点。

模型不可靠或者太复杂的时候，如果知道输入数据和期望输出我们可以用监督学习。

监督学习的步骤简单来说分为五步：

1. Inductive bias selection 归纳偏置。首先我们假设一下**目标模型**是什么样的，比如：一次函数？二次函数？做了这个假设之后再代入训练（比如t=ax，代入训练数据后求出a）。当然，我们的假设可能会有偏差，毕竟不一定所有问题都能找到完全合适的问题解决，这个偏差就叫 bias。以及定义**损失函数**，损失函数用于计算预测值与训练数据之间的偏差以此调整模型；**正交函数**；**训练方法**（比如：让loss最小化）。
2. Training 训练。下面会讲到，我们把已知的数据分为训练集和测试集，训练集用于训练我们的模型，测试集用于检验模型效果不用于训练。
3. Validation 验证，利用训练集数据计算 loss 损失判断模型的合理性，比如二次函数用一次函数的模型，偏差就会很大。
4. Revise inductive bias 可能考虑是否修改归纳偏置模型。
5. test 测试集测试。

监督学习解决的问题主要分为：

- regression problem 回归问题，连续
- classification problem 分类问题，离散

*memoralizing 是记忆，记住训练数据中的x,t的键值对。learning是学习，找规律。*

no free lunch theorem 没有免费的午餐定理: **没有一种通用的学习算法可以在各种任务中都有很好的表现**。我们需要对数据进行先验假设 inductive bias ，在归纳过程中再做修改。最终得到一个预测器 predictor，连续问题是软预测器 soft，离散问题是硬预测器 hard。

比如下面这张图，我们觉得两条横线不同长度，就是因为我们大脑根据经验觉得在参考线的辅助下两条线不一样长。这个过程有点类似于计算机的归纳偏置。

<img src="https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410111628240.png" alt="image-20241011162802012" style="zoom: 25%;" />



#### 常见符号解释

训练集：D，内含N个数据。training set D with N training data points 
$$
D=\{(x_n,t_n)^N_{n=1}\}
$$
硬预测器：^t
$$
\hat t_D(x)
$$
软预测器：q
$$
q_D(t|x)
$$
硬预测模型类 model class：意为首先我们对预测器做一个大概的假设，这个预测器属于某一个模型类（比如一次函数的预测器类，二次函数的预测器类等）。θ 是模型的参数，属于一个特定范围，在训练过程中调整 θ 值。注意 θ 是一个向量代表一系列系数。
$$
H=\{\hat t(\cdot|\theta):\theta\in\Theta\}
$$
如果选择的模型类是多项式函数，一般用 degree M 表示其项数。
$$
\hat t(x|\theta)=\theta_0+\theta_1x+\theta_2x^2+...+\theta_Mx^M=\theta^Tu(x)
$$
其中的 u(x) 可不是阶跃函数，而是 feature vector 表示 $$[1, x, x^2, x^3...x^M]^T$$ 这个列向量。

这个模型类被称为线性预测器（不是因为 t 和 x 呈线性关系，很明显不是。而是因为 t 和 θ 呈线性关系）。

总体损失 population loss：特指推理中的损失，因为我们知道概率 p(x,t) 的具体值：
$$
L_p(\theta)=E_{(x,t)\sim p(x,t)}[l(t,\hat t(x|\theta))]
$$
但是学习和推理不同，我们不知道具体概率值因此这个损失无法得到。我们可以评估训练损失：
$$
L_D(\theta)=\frac{1}{N}\sum^{N}_{n=1}l(t_n,\hat t(x_n|\theta))=\sum_{x,t}p_D(x,t)l(t,\hat t(x|\theta))
$$
### Inductive Bias Selection 归纳偏差选择

选择模型类 / 预测器的过程也是确定归纳偏差的过程。

#### 三种预测器

Population-optimal unconstrainded predictor 总体最优无约束预测器：最小化总体损失且无视模型，所以叫做无约束预测器，因为不受模型类的限制。但是我们不知道标准概率分布所以很难实现。
$$
t^*(\cdot)=arg\,\mathop{min}\limits_{t(\cdot)}L_p(t(\cdot))
$$
Population-optimal within-class predictor 总体最优类内预测器：首先确定模型类，在这种模型类的前提下选择 θ 最小化损失。
$$
\theta ^*_M=arg \mathop{min}\limits_{\theta \in R^{M+1}}L_p(\theta)
$$
Trained ERM predictor 经验风险最小化训练预测器：确定模型类，且使用有限的训练数据集来计算损失。
$$
\theta_M^{ERM}==arg \mathop{min}\limits_{\theta \in R^{M+1}}L_D(\theta)
$$

#### ERM 经验风险最小化预测

针对这个损失函数，一种训练原则是 Empirical Risk Minimization 经验风险最小化（ERM），即找到使得 LD(θ) 最小的 θ 作为预测器参数。
$$
\theta_D^{ERM}=arg\,\mathop{min}\limits_{\theta \in \Theta}L_D(\theta)
$$

$$
L_D(\theta)=\frac{1}{N}||t_D-X_D\theta||^2
$$

*和之前提到的一样，连续问题（如 Regression）的损失函数是求次方偏差，离散问题（如 Classification）的损失函数是求0-1偏差。*

t_D：一个列向量，依次存储了所有目标值.

X_D：一个矩阵，每行存储了一个 u(x)，和 θ 向量相乘后就组成了每行一个预测器（第一行：输入x1得到的t1值；第二行：输入x2得到的t2值……）。

意思就是所有预测值和训练值之间的代价损失的平均值。

让这个代价函数最小的θ的解是：
$$
\theta^{ERM}_D=(X_D^TX_D)^{-1}X_D^Tt_D
$$
如果第一部分的矩阵乘积是不可逆的，舍去这一部分即可。

#### ERM 相关的两个定理

对于学习，有两个定理：

- 魏尔斯特拉斯近似定理 Weierstrass approximation theorem：任何连续函数，随着M的增加（M是多项式模型的最高项数），精准度都会逐渐增大。（当然预测器复杂度也增加了，所以并不能只一味增加了事，计算难度也会大幅增加的）
- 由于学习不知道准确概率只是根据训练数据估算的概率，所以这只能算是一种**估计**的损失。根据大数定理  law of large numbers，测试案例越多，估计损失越接近真正的 population loss.

例题：

![image-20241012181643970](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410121816117.png)

给出的预测器形式很简单，就是x=0时预测结果为θ\_0，x=1时预测结果为θ\_1。我们计算2个维度四种情况分别的 loss 选取损失最小的预测器。

![image-20241012181732276](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410121817373.png)

#### 最优预测器和经验风险最小化预测器的对比

例：

![image-20241014131224176](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410141312358.png)

当采用多项式函数模型，M=1时，两种预测器拟合出的预测结果分别如图：

![image-20241014131359896](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410141314110.png)

这种情况下，ERM **underfits** the data 欠拟合数据：

- 模型不够复杂，the model is not rich enough
- estimation error 很小，ERM 和 population-optimal 的预测结果很像
- 但是 bias 很大，因为用错公式了，一次方的函数怎么样也不可能和原函数很接近。
- training loss 和 population loss 都很大。

如果M=9：

![image-20241014131846579](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410141318744.png)

这种情况下，ERM **overfits** the data 过拟合数据：

- 模型太复杂了，为了匹配所有训练数据，训练数据外的数据不够精确。
- 这是因为训练模型重点在于记住训练的数据集，而不是总结出没见过的数据的规律。
- estimation error 很大，ERM 和 population -optimal 差距很大；
- bias 很小，population -optimal 预测器和真正的数据规律很像。如果bias很大那两个模型的损失应该都很大，但是既然人家行你不行说明问题出在  ERM 本身上而不是归纳偏置上。
- 当训练数据够多时，training 和 population -optimal 之间的差距会越来越小，training 会越来越准确。

M=3 时，模型预测如图，可以看出 ERM 在欠拟合和过拟合中间的M值会比较贴近正确预测结果：

![image-20241014132520199](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410141325430.png)

但是我们如何判断模型是否过拟合？我们不一定知道正确的模型公式。因为我们到目前为止只是用训练数据在测试，就算训练出了完全拟合训练数据的预测器（如上面第二个图，M=9 的例子）我怎么知道这是适用于所有数据的预测器呢？

#### Probabilistic Models 软预测器的概率模型

软预测器用已知 t 和 θ 的条件概率表示。第三章的时候用 q 符号表示，这章用 p 符号，反正意思到位了。
$$
\mathcal H=\left\{p(t|x,\theta):\theta \in \Theta \right\}
$$


概率模型的训练采用软预测，因为其中的概率不确定性。

事实上很多确定性模型也可以用概率模型的特例来看待，也同样可以应用其公式。

总体损失：
$$
L_p(\theta)=E_{(x,t)~p(x,t)}[-log\,p(t|x,\theta)]
$$
ERM训练损失：
$$
L_D(\theta)=\frac{1}{N}\sum^{N}_{n=1}(-log\,p(t_n|x_n,\theta))
$$
也叫 Maximum Likehood Learning (ML Learning) 最大似然学习。最小化 log 损失，最大化概率。

### Validation 验证

可以先拿出一部分已知数据作为验证集 validation 不参与训练。预测器用训练集训练，验证集再计算损失。计算损失的方法仍然是整体损失：
$$
\hat L_p(\theta)=L_{D^v}(\theta)=\frac{1}{N^v}\sum^{N^v}_{n=1}l(t^v_n,\hat t(x^v_n|\theta))
$$

- 损失函数应该会小于真实值，因为 ERM 是基于整个训练集训练的。

- 偏差问题：大数定理不再有效，因为大数定理是“训练集数量越多，整个训练集的损失越小”，而验证集的损失和训练集是分开的。所以验证集的损失是整体损失的有偏估计 biased estimate。

比如我们可以利用验证选择更合适的模型：

![image-20241014135027400](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410141350628.png)

如何选择验证集？

#### K-Fold Cross-Validation

首先将模型划分为K个类。每次迭代从每个类中选取一个值作为验证集，比如第3次就把3类作为验证集，把剩下的类作为训练集。

<img src="https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410141707768.png" alt="image-20241014170717690" style="zoom: 80%;" />

最后求所有迭代的损失平均值：
$$
\hat L_p = \frac{1}{K}\sum^{K}_{k=1}L_{D_k}(\theta^{ERM}_{\mathop{D}\limits^{\sim}_{-k}})
$$


例题：如下，尝试计算只选取两个元素作为验证集（不用 K-Fold 验证方式）的损失。

![image-20241014171317611](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410141713672.png)

如果是总体最优预测模型：很简单，把所有数据都记录下来，并且如果只涉及到这四个数据，损失=0.

<img src="https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410141717057.png" alt="image-20241014171717926" style="zoom:50%;" />

ERM 学习：现在假设我们先选择两个数据作为训练数据。假设我们选择了x=2 x=3. 那就完蛋了，用这两个数据我们训练得到的预测器是t(x)=2，t的值不受x的影响。
$$
\hat t(x|\theta) = \theta _0 + \theta _1x. \theta _0=2, \theta _1=0.
$$
总体损失就是(2^2^+1^2^+0+0)/4=5/4，过拟合。

#### Bias vs Estimation Error

如何权衡偏差和估计错误？
$$
L_p(\theta _D) = L_p(\hat t^*(\cdot))^{\text{minimum unconstrained population loss}} + \left(L_p(\theta^*_H) - L_p(\hat t^*(\cdot))\right)^{\text{bias}} + \left(L_p(\theta_D) - L_p(\theta^*_H)\right)^{\text{estimation error}}
$$
第一部分：最优预测的损失。当然最优预测很难找到因为不知道概率。

第二部分：bias。跟模型选择有关。

第三部分：估计错误。跟训练数据集大小有关。

在之前的例子中，我们知道：

M增加，也就是模型 class 复杂度增加，bias 会下降，但 estimation error 可能会增加，过度拟合。

N 增加，也就是训练数据集增加，bias 不变，estimation error 会减少。

<img src="https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410142027925.png" alt="image-20241014202757817" style="zoom:67%;" />

再细化一点，对于每个输入x，损失函数的表达方式是：
$$
L_p(\theta _D |x)=\underbrace{L_p(\hat t^*(x) |x)}_\text{aleatoric\,uncertainty}+\underbrace{(L_p(\theta^*_H|x)-L_p(\hat t^*(x)|x))}_\text{bias}+\underbrace{(L_p(\theta_D|x)-L_p(\theta^*_H|x))}_\text{epistemic\,uncertainty}\\
$$


*其实这里对模型容量，数据量的介绍有些过于简化其作用了，训练效果和要解决的问题，模型选择，训练算法等等都有影响。比如深度神经网络一般是大容量模型，并不一定适用“模型容量越大，越容易过拟合”的定理。当模型容量增加的时候，测试误差会首先增加（过拟合）然后下降，直到一个插值点 interpolation point。这个特性被称为“双降 double descent”，意思是 training loss 随着模型容量增加而下降的同时，population loss 也没有如过拟合预期的那样增加。*

#### Regularization 正交化

一种让 ERM 模型变得更加泛化的方法。

θ的参数过多会导致 overfitting，而正交化期望：降低θ的权重使得过拟合问题不那么明显。
$$
\theta^{R-ERM}_D = arg\,\mathop{min}\limits_{\theta \in \Theta}\left\{L_D(\theta)+\frac{\lambda}{N}R(\theta) \right\}
$$


括号内的部分是正交训练损失，Regularized training loss.

λ：一个可以设定的参数，尽可能的在减小训练损失和准确度之间权衡。

R：正交化θ。比如一维范式就是所有 θ 的值求和 ||θ||，二维范式是其平方求和 $$||θ||^2$$。*一维范式被称作 LASSO Least Absolute Shrinkage and Selection Operator 最小绝对收缩和选择算子回归。*

θ 数量越多，第二项也会使得整体的值增加，作用相当于 loss 增加。

### Test 测试

验证集多次迭代的过程是有偏估计，所以损失一般小于总体损失。

建议提前拿出一组数据作为测试集，不参与训练和验证，用测试集评估总体损失且训练者不应该知道测试集的内容。



### Optimization 优化

我们之前已经得出损失公式，以及训练的目标就是让损失最小化：
$$
min_{\theta}\{g(\theta)=\frac{1}{N}\sum^N_{n=1}f(x_n,t_n|\theta)+\frac{\lambda}{N}R(\theta)\}
$$
但是并不能一定取到最小值，比如类似e^n的函数，最小值无限接近0永远取不到。

最小值点被称为 global optimal point g(θ\*)，对于所有 g(θ) 都有 g(θ)>=g(θ\*)，但大多数时候找不到。

极小值点 local optimal point，对于θ\* 附近的 θ 值有 g(θ)>=g(θ\*)

找极小值点的方法当然是求导，如果 d(g(θ)/θ)=0 那就说明0处是一个极值点 stationary point（但可能是极大值点或者暂时停止上升）。

二阶导=0：在该点处局部线性。>0：说明是“U”形状。<0：说明是“倒U”形状。

如果二阶导一直>=0，那么 g(θ) 的增长率（一阶导）就是一直增加或不变的（比如二次函数），那么我们可以称原函数 g 为凸函数 convex，并且 stationary point 一定是最小值点。

![image-20241023063138746](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410230631921.png)

θ向量是从1到D维的所有θ系数，而 ∇g(θ) 是所有θ的导数的向量。

首先如果一个点是极值点 stationary point，这个点的一阶导一定=0，这是充分条件：一阶优化条件 first-order optimality condition。

多元函数的曲率由下公式定义 Hessian：

![image-20241023182828095](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410231828240.png)

这个矩阵是对称的，比如：

![image-20241023183135607](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410231831727.png)

其中的值全部=0说明是凸函数。

#### Gradient Descent 梯度下降优化

是一种局部优化方法 Local optimization。

简单来说，每次迭代的时候沿损失梯度下降最快的方向走一定的步长，让下次迭代的θ序列损失更小。

<img src="https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410270009617.png" alt="[神经网络基础理论与简单实践 | korilin's blog](https://korilin.com/posts/basic-theory-and-simple-practice-of-neural-network/image_21.png)" style="zoom:67%;" />

公式如下，注意这里的θ不是指多项式中的每一个参数θ，而是每次迭代产生的一组θ。初始化第一组 θ 后，后面的每组 θ 都迭代计算。γ是学习率，步长，决定每次迭代要迈多大的步子。
$$
\theta^{(i+1)}=\theta^{(i)}-\gamma\nabla g(\theta^{(i)})
$$


如果 γ 设置的太大了，就容易迈过，再回头往反方向走。

![[深度学习优化算法入门：一、梯度下降 - 知乎](https://zhuanlan.zhihu.com/p/45365719)](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410270016642.webp)

#### 梯度下降的性质

- 如果 g(θ) 的二阶导全部<=L，可以说 g(θ) 是 L-smooth 的函数。

$$
\frac{d^2g(\theta)}{d\theta^2}\le L
$$

就是 g(θ) 一阶导的增长率不会过快，一定在 L 的范围内。

![image-20241027002233224](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410270022541.png)

- 当学习率 γ<=1/L 时，有如下性质：
  -  guaranteed reduction of the loss function: 

$$
g(\theta^{(i+1)})\le g(\theta^{(i)})-\frac{\gamma}{2}\|\nabla g(\theta^{(i)})\|^2
$$

​		也就是说下一次迭代的 θ 一定能让损失下降这么多。

- - convergence to a stationary point：g(θ) 收敛，$$\nabla g(\theta^{(i)})\rightarrow0$$

不过问题在于 L 不一定知道。我们可以通过验证，以及其他方法获取（后续章节介绍）。

#### Stochastic Gradient Descent 随机梯度下降

计算整个数据集的梯度，对于大模型来说计算成本还是太高了。

每次迭代我们不挑出所有的训练集样本点计算 g(θ) ，只随机选取部分。
$$
\theta^{(i+1)}\leftarrow \theta^{(i)}-\frac{\gamma^{(i)}}{S^{(i)}}\sum_{n \in S^{(i)}}\nabla g_n(\theta^{(i)})
$$
SGD 相比 GD 可能需要多走几步因为一开始的每一步不一定精准朝着 g(θ) 下降方向。但是计算成本还是下降了，因为 GD 每一步迈之前都要先考虑清楚所有可能的方向，再决定出让损失最小化的下一次迈步；如果数据量太大，这个功夫都够 SGD 走好多步了。

所以选择合适的学习率也可以适当减少迭代次数。根据 Munro-Robbins conditions，SGD 的学习率设置：
$$
\sum^{\infty}_{i=1}\gamma^{(i)}=\infty\;and\;\sum^{\infty}_{i=1}(\gamma^{(i)})^2\lt\infty
$$
第一部分保证了学习率不会太小以至于原地踏步，永远无法到达 stationary point；第二部分确保学习率不会太大，SGD 的方差是逐渐减小直到消失的，保证逐渐逼近 stationary point 而不会在极点附近来回徘徊。

比如 $$\gamma^{(i)}=1/i^{\alpha},\alpha \in (0.5, 1]$$ 这个学习率满足这一条件。

多项式学习率常常用 $$ \gamma ^{(i)} = \gamma ^{(0)}/(1 + \beta i)^\alpha, \beta>0,\gamma^{(0)}>0,\alpha \in (0.5,1]$$

除了对学习率范围设限，另一种避免到达不了极点的方法是 S 样本量每次迭代都会增加。这两种方式可以结合使用。

#### 计算梯度的方式

Symbolic Differentiation：直接求导。

![image-20241027153846442](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410271538688.png)

Numerical Differentiation：利用导数定义近似求解。把 g(θ) 看作一个黑盒，不关心其内部结构，只考虑输入输出。

![image-20241027154010115](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410271540283.png)

![image-20241027154230734](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410271542004.png)

Automatic Differentiation：使用求导方法，但是只求出某个点的梯度值而不是先求出整体公式。

三种方式的对比：

![image-20241027161151946](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410271611213.png)

#### Computational Graph 计算图

便于计算梯度的图。

比如：
$$
g(\theta)=\theta^2_1+\theta^2_2+\theta^2_3
$$
计算图表示为：

![image-20241027162607416](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410271626631.png)

当然也可能出现θ1θ2这样的形式：

![image-20241027162639522](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410271626706.png)

已知 θ 序列求 g(θ) 非常简单，把参数带进去就可以。forward pass

backward pass 是反向传播，假设 g(θ)=1，反推回来。所有 f() 的部分要对相应的 θ 求导。

例题： $$g(\theta)=\theta^2_1+2\theta^2_2-\theta^2_3$$ ，求 [1,-1,1] 点处的梯度。

首先进行 forward pass，代入三点数值到计算图中求 g(θ) 在[1,-1,1] 处的数值，这一步的主要作用是确定计算图：

![image-20241027164947168](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410271649432.png)

接着假设 g(θ)=1，倒推回来：

![image-20241027165203236](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410271652421.png)

[2, -2, 2] 部分是对 forward pass 中三个函数求导再代入 [1,-1,1] 的值得到的。

最终得到的 $$\nabla g(\theta)=[2,-4,-2]^T$$

例题2：如下图，f1-f3都是 $$(x_1+2x_2)^2$$，f4=logx。

求[1, -2, 1] 点处的梯度下降值。

![image-20241027183553508](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410271835911.png)

首先 forward pass 求出 g(θ)，并且在此过程中把每个函数对于 x1 x2 的求导也算出来（并带入输入 x1 x2 值）：

![image-20241027183825574](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410271838872.png)

然后假设 g(θ)=1，反推回去得到 θ 的值。

![image-20241027184236357](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410271842537.png)

$$\nabla \theta=[-4/3, -8/3,0]^T$$

## Binary Classification 上述方法在二元分类中的应用

如下图，给了一个新点判断这个点可能是圈还是叉。

![image-20241112021653157](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411120216352.png)

目标t值：0或者1.
$$
t^{\pm}=2t-1=\left\{
\begin{aligned}
1,\,if\;t=1\\
-1,\,if\;t=0
\end{aligned}
\right.
$$


整体流程还是和之前讲的差不多：

- inductive bias selection
- training
- validation
- revise inductive bias
- test

模型主要分为线性模型和神经网络模型。

### Linear Models 线性模型

#### 预测器

还是经典公式：
$$
\theta^T u(x)= \sum^{D'}_{d=1}\theta_du_d(x)
$$
特征向量 u(x) 也不一定只是x的多次幂列向量，比如可能是“一个句子中不同词的出现次数”。

硬预测器的计算结果：如果公式值>0则t预测=1，如果<0则预测=0. 公式值=0的情况不考虑也很难发生。
$$
\hat t(x|\theta)=step(\theta^Tu(x))
$$
<img src="https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411120228255.png" alt="image-20241112022804087" style="zoom:67%;" />

软预测用指数函数处理：
$$
\begin{aligned}
p(t=1|x,\theta)&=\sigma (\theta^T u(x))\\
p(t=0|x,\theta)=1&-p(t=1|x,\theta)\\
\sigma (x)=(&1+e^{(-x)})^{-1}
\end{aligned}
$$
<img src="https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411120232281.png" alt="image-20241112023239039" style="zoom: 67%;" />

多项式计算结果区间位于0到5时，概率>0.5，说明更有可能发生。所以软预测器选择>0.5的那一项结果作为预测值。

<img src="https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411120233740.png" alt="image-20241112023354565" style="zoom:67%;" />

#### 损失函数

考虑下面这个式子，就是 classification margin：
$$
y=t^\pm \cdot \theta^T u(x)
$$
这个式子为正值时预测结果为正确，为负值时预测结果为错误。

所以硬预测的 Detection-Error Loss Function 损失函数（还是指示符函数，预测正确=0，预测错误=1）可以写作：
$$
\begin{aligned}
l(t,\hat t(x|\theta))&=\mathbb{1} (t\neq \hat t(x|\theta))\\
&=step(-y)
\end{aligned}
$$
但是这个函数没法应用 GD 降维（损失函数图像类似矩阵函数，只有0和1，没法降维）。所以我们可以应用其他的损失函数：

<img src="https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411120632479.png" alt="image-20241112063219179" style="zoom:67%;" />

Exponential loss 指数损失：$$l(y)=e^{-y}$$

hinge loss 铰链损失：$$l(y)=max(0,1-y)$$

hinge-at-zero loss 零损失铰链函数：$$l(y)=max(0,-y)$$

logistic loss 对数损失：$$l(y)=log(1+e^{-y})$$

这些函数都可以用，相比 detection-error loss 都可以应用 GD 降维。

软预测损失：$$l(t,\hat t(x|\theta))=log(1+e^{-y})$$

#### Perceptron Algorithm 感知器算法

应用了 ERM，hinge-at-zero loss，SGD 的算法。

损失函数：$$l(y)=max(0,-y)$$

梯度函数：
$$
\nabla l(t^\pm \cdot (\theta^T u(x)))=\left\{
\begin{aligned}
0\;\;\;if\;prediction\;is\;correct\\
-t^\pm \cdot u(x)\;\;if\;prediction\;is\;wrong
\end{aligned}
\right .
$$


例题：

![image-20241112074401735](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411120744954.png)

首先假设选取 (2.1, 1) 点计算梯度下降。
$$
\begin{aligned}
\theta_2&=\theta_1-\gamma g(\theta_1)\\
g(\theta_1)&=-1 \cdot 1 \cdot 2.1\,(prediction\;is\;wrong,\,-2.1 \neq 1)\\
\theta_2&=-1+0.1\cdot 2.1=-0.79
\end{aligned}
$$
然后选取 (-1.5, 0) 点计算梯度下降。
$$
\begin{aligned}
\theta_2&=\theta_1-\gamma g(\theta_1)\\
g(\theta_1)&=-1 \cdot -1 \cdot -1.5\,(prediction\;is\;wrong\,-1.5\cdot -0.79=1.185\neq 0)\\
\theta_2&=-0.79+0.1\cdot 1.5=-0.64
\end{aligned}
$$
计算每个步骤中的 classification margin 会发现值是逐渐接近于0的。

对于 log loss 软预测器的梯度下降函数：
$$
\nabla l(t^\pm \cdot (\theta^T(u(x)))=(\sigma(\theta^T u(x))-t)\cdot u(x)
$$
$$\sigma$$ 函数之前有介绍，=(1+exp\^(-x))\^-1.
$$\sigma(\theta^T u(x))-t$$ 部分又用 $$\delta(x,t) $$ 表示，表示 mean error，=0 的时候说明预测完全准确。

当 mean error = 0 时，如果 t=1，则 $$\theta^T(u(x))\rightarrow \infty$$ ；如果 t=0，则 $$\theta^T(u(x))\rightarrow -\infty$$ 

软预测器梯度下降公式：
$$
\theta^{i+1}\leftarrow \theta^{(i)}-\gamma^{(i)}\frac{1}{S^{(i)}}\sum_{n\in S^{(i)}}(\sigma((\theta^{(i)})^Tu(x_n))-t^n)\cdot u(x_n)
$$
例题：还是形如上一道题的数据，初始预测器 $$\theta_1=-1, \lambda=0, \gamma=0.1$$, minimum batch size S=1

![image-20241112222114793](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411122221190.png)

### Neural Network Model 神经网络模型

主要用于处理非线性情况。

u(x) 并不像线性模型一样一开始是确定的，可能在模型训练过程中还有改动。对于难以建立先验的情况来说比较适用。

之前线性模型中我们常用 u(x) 来描述特征向量 feature vector，而神经网络模型中用 x 表示输入的特征向量，u(x) 是其一种表示形式。

另外，神经网络模型专注于概率计算问题。

![image-20241112223032270](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411122230604.png)

中间的每一层都叫做 feature extraction layers 特征提取层。

第一层输入 x 输出 D^1^ 维度的 h^1^ 向量。后面的每一层都用前一层的向量输入，输出一个 D^l-1^ 维度的 h^l-1^ 向量。最后一层叫做 classification layer 分类层，把 h 作为 u(x) 输入到预测器里计算概率。

每一层的处理公式如下：
$$
\begin{aligned}
a^l=W^lh^{l-1}\\

\end{aligned}
$$
W：权重向量，分配不同项之间的权重。

a：本层的 pre-activations 预激活向量。

h：列向量，用本层的 a 向量通过一个激活函数激活后得到。

<img src="https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411122312272.png" alt="image-20241112231053215" style="zoom:67%;" />

典型的几种激活函数：

- sigmoid：$$\sigma (a)$$
- hyperbolic tangent: $$tanh(a)$$
- Rectified Linear Unit: $$max(0,a)$$
- Leaky ReLU: $$max(\alpha a,a),\,\alpha\in[0,1]$$

下面是这四者的图像：

![image-20241113182349898](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411131823276.png)

梯度消失问题：见 Sigmoid 函数，其的导数特征在于：在±5范围之外，导数全部=0；在中间导数先增长为1再下降。这就导致a必须落在[-5,5]的区间内，梯度值才会有效；在某些层传播中，梯度值很容易消失变为0.

梯度爆炸：tanh 中间的梯度值都快到∞了，梯度范围浮动非常大，不稳定。

所以 ReLU 在这两点上优于 tanh 和 Sigmoid 函数，有效避免梯度下降和梯度消失问题。

最后一层获取 u(x|θ) 的公式：

![image-20241126033703135](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411260337845.png)

每一层的作用都是提取一些信息化表示的特征，为最终通过x分类t做准备。

其中，W 是权重矩阵向量。W^l^ 是一个 D^l^ \* D^l-1^ 形状的向量，作用是和前一层传入的 D^l-1^ 长度的行向量相乘后输出 D^l^ \* 1 长度的符合下一层形状的向量。**注意矩阵乘法的时候，W在前，D在后。**

一个比较通俗易懂的图解如下：

![img](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411260348069.png)

![img](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411260348830.png)

> 来源：[神经网络——最易懂最清晰的一篇文章-CSDN博客](https://blog.csdn.net/illikang/article/details/82019945)

而 θ 则这样表示：

![image-20241126034944517](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411260349886.png)

*如果 h 是线性函数，那么整个预测器就是一个线性预测器。*

![image-20241126035141459](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411260351906.png)

例题：

![image-20241126035428151](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411260354580.png)

![image-20241126035756581](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411260357979.png)

给定题目后，我们大概可知神经网络图像如下，两层（注意神经网络算出来的默认结果是预测值=1 的概率）：

![image-20241126035824630](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411260358132.png)

用输入向量逐层与权重相乘后激活计算得到：

![image-20241126040527762](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411260405256.png)

p(0|x,θ) 就1-0.12=0.88 即可。

#### SGD

又到了最喜欢的梯度下降优化环节。

首先还是要找一个计算损失的方法：

![image-20241126040841418](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411260408835.png)

最后一层：

![image-20241126041133897](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411260411210.png)

梯度：只说结论的话：
$$
\delta^l=\sigma(a^L)-t
$$


![image-20241126041317020](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411260413415.png)

比如：还是之前那道题，计算 t=0 时的梯度。首先是前向传播：

![image-20241126043115009](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411260431343.png)

输入损失函数后，t^±^=-1（那个公式=2t-1，预测值 t =0，t^±^=-1），a^2^ 是该层（第二层所以有个2的上标，不是平方）的输出=-2，两者相乘=2，代入公式计算得到0.13 为损失值。

然后假设结尾=1，开始后向传播：

![image-20241126043929691](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411260439190.png)

首先根据 t 和 a^2^ 计算出 δ=0.12，用1\*0.12再\*第二层权重回推。

第一层的梯度公式是h对a^1^求导，h是一个 ReLU 函数，所以当a>0时求导结果=1，a<0 时求导结果=0. （参考 ReLU 公式）所以得到这一层的向量是 [1,0]，回推出反向传播误差。

![image-20241126044627761](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411260446136.png)



最终，我们给输入值*反向传播误差计算权重梯度，用原权重-权重梯度\*学习率更新权重。这里貌似学习率视作1了吧？

![image-20241126044923671](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411260449094.png)

下图是不同层数，随着迭代次数增加训练损失下降情况图。可以看出3层反而是最有效进行二元分类的训练方法。

![image-20241126045100763](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411260451091.png)

## Transformer

一种常常用于自然语言处理的深度学习架构。

输入可以被划分为 subset 子集或者 token：

![image-20241126045944516](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411260459045.png)

![image-20241126045956864](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411260459330.png)

对于输入数据，创建N个Tokens，每一个都有D*1的维度：

![image-20241126050158513](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411260501909.png)

transformer 的一个重要机制在于 self-attention。

![image-20241126051531266](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411260515316.png)

softmax 是形如下图的公式，这只是一种计算方法：

![image-20241126052420915](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411260524551.png)

在自注意力公式中，我们发现初始词嵌入出现了3次。前两次是作为句中词向量与其他词（包括它自己）点积得到权重；第三次再与权重相乘得到最终带上下文的词嵌入。这三个地方出现的词嵌入我们给他们三个术语：查询(Query), 键(Key), 值(Value)。

![在这里插入图片描述](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411260529285.png)

> [【万字长文】深度解析 Transformer 和注意力机制（含完整代码实现）_transformer架构注意力机制-CSDN博客](https://blog.csdn.net/jarodyv/article/details/130867562)

Query 和 Key 不是对称的，一方对另一方的词注意力可能与反过来不同。比如“伦敦国王学院”和“大学”关联度很高，但”大学“和”伦敦国王学院“关联度不高，大学有那么多所呢。

#### MultiHead Attention 多头注意力

除了一个句子中不同词之间的关联，可能还有其他因素（如一词多义，语序问题等）。
