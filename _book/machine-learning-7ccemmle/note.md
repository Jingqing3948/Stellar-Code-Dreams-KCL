<html>
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/gitalk@1/dist/gitalk.css">
	<script src="https://cdn.jsdelivr.net/npm/gitalk@1/dist/gitalk.min.js"></script>
	<div id="gitalk-container"></div>
	<script>
	var gitalk = new Gitalk({
		"clientID": "Ov23li1TkQEYXFu51qLu",
		"clientSecret": "0c4ca8b5adfcc2aedd741ba78ca96fcbf2c4f5b5",
		"repo": "Jingqing3948.github.io",
		"owner": "Jingqing3948",
		"admin": ["Jingqing3948"],
		"id": location.pathname,      
		"distractionFreeMode": false  
	});
	gitalk.render("gitalk-container");
	</script>
</html>


## Probability 概率论基础

### Random Variables 随机变量

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

- 连续随机变量通常用概率密度函数表示，x~p(*x*)，同样p(x)在域上求积分=1.

  比如经典的高斯变量，x~N(µ,σ^2^)，表示公式：
  $$
  p(x)= N(x|\mu,\sigma ^2) = \frac{1}{\sqrt{2\pi \sigma ^2}}exp(-\frac{(x-\mu)^2}{2\sigma ^2})
  $$
  ![image-20240930123225957](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202409301232062.png)

- 期望：最有可能的结果。离散随机变量的期望：
  $$
  E_{\mathbb{x}\sim p(x)}[\mathbb{x}]=\sum_{x\in\mathcal{X}}p(x)\bullet x
  $$
  一个离散变量的函数的期望：可以理解为首先x有多大的概率等于这个值，然后再用x的这个值代入f(x)得到的结果，我们要计算这个结果的期望值。
  $$
  xE_{\mathbb{x}\sim p(x)}[f(\mathbb{x})]=\sum_{x\in \mathcal{X}}p(x)\bullet f(x)
  $$

- 

​	![image-20240930124426965](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202409301244100.png)

- 连续函数类似，求积分而已。
  $$
  xE_{\mathbb{x}\sim p(x)}[f(\mathbb{x})]=\int_{-\infty }^{+\infty }p(x)f(x)dx
  $$

- 

- 高斯随机变量 N(µ, σ^2^) 的期望，对于f(x)=x函数来说=µ，对于f(x)=x^2^函数来说=µ^2^+σ^2^.
- 高斯随机变量的期望是线性的，aµ\_1+bµ\_2.

### Vector 向量

这部分知识也多次出现了就不多赘述了。向量的表示形式是列向量（L×1长度）。

**inner product 内积**：两个长度相同的列向量每个元素相乘，x^T^y。内积一般用来衡量相似度 similarity.

比如下面这两对xy，内积都=6，说明其相似度差不多。

![image-20240930131327706](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202409301313822.png)

**norm 范数**：就是向量的标量长度，可以通过x^T^x计算。

L1范数：x^T^x

L2范数：L1范数再开根。

$\widetilde{x}$：x的归一化，相当于一个和x方向相同但是长度=1的向量，用x/L2范数（||x||）就可以得到。

比如上面的笑脸图，除了右上角的y的范数=6，其他向量范数=8.

### matrix 矩阵

![image-20240930132654242](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202409301326346.png)

**diagonal matrix 对角矩阵**：只有对角线上的值非零（a_ii）

![image-20240930132133255](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202409301321401.png)

L×1列向量的对角矩阵相当于把列向量中的元素均匀分到L×L矩阵的对角线上。那么两个列向量的乘积=一方的对角矩阵与另一方的乘积=x⊙y（逐元素相乘）得到的列向量。

**Symmetric matrix 对称矩阵**：矩阵转置仍然等于其本身。[A]_{i,j}=[A]\_{j,i}

### Random Vector 随机向量

随机变量中所有元素按列向量排列。其中某个元素的概率：Pr[x=x_i]

**joint pmf p(x) 联合随机向量**：类似于：第一次硬币投出正面，第二次投出反面的概率。p(x)=Pr[x1 = x1 and x2=x2...and xL = xL]

Jointly Bernoulli random vector：只有两种情况，类似投硬币。

![image-20240930134410880](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202409301344092.png)

连续随机变量的联合表示就从二维的平面变为三维的空间了。比如下图是高斯随机变量的联合表示图：

![image-20240930134543755](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202409301345912.png)

**Marginal Distributions 边际分布**：只考虑多个变量中的部分变量的概率。比如下图，p(x1=0)=0.45+0.05=0.5，所以x1\~Bern(0.5)，而x2\~Bern(0.45)（非零部分的概率）

![image-20240930134828510](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202409301348690.png)

**Conditional Distributions 条件概率**：当其他变量为xx时，这个变量为xxx的概率是多少。比如上图，x2=0的话x1的概率分布：P(x1=0 | x2=0)=0.45/0.55,P(x1=1 | x2=0)=0.1/0.55, (x1|x2=0)~Bern(0.18)

GenAI 里面会用到这个概率，当GPT已经生成了之前的一千个词后，再生成下一个词为xxx的概率为多少。

**Independence 独立性**：两个变量没有什么关系。那么两者同时发生的概率就是两者分别发生的概率的乘积，p(x1, x2)=p(x1)p(x2).

p(x1,x2) = p(x1)p(x2|x1).

如果多个变量彼此独立，那么以此类推，所有变量概率相乘是发生某一种排列的可能性。

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
> 提前准备好大量的中文语料，计算出任意两个词的条件概率，我们就可以得出哪种分词更合理。
>
> [一文搞懂贝叶斯定理（应用篇） - Blogs - 廖雪峰的官方网站 (liaoxuefeng.com)](https://liaoxuefeng.com/blogs/all/2023-08-29-bayes-use/index.html)

以及搜索引擎，GPT根据用户上一个单词输入猜测下一个单词也是采用条件概率的算法。

## Inference 推理

输入：x

输出：t

中间是一个概率模型 probabilistic model （x和t的联合分布 p(x,t) ）来预测最可能的t。

推理问题主要分为两类，离散的 detection （比如晴天或者雨天）和连续的 estimation（比如温度）。

而预测器又分为两种：hard predictor 和 soft predictor，hard 就是有具体结果的（比如t是一个关于x的函数，代入x，t的值唯一确定）；soft 就是不确定的（当x=某个值时，t为0的概率有10%，为1的概率有90%）。

下面第一行是 hard 的写法，代表：x=0时t的预测结果=1。

第二行是条件概率的 soft 的写法。
$$
\begin{aligned}
\hat t(0)=1\\
q(1|0)=0.2
\end{aligned}
$$

### Optimal Soft Prediction / Bayesian Inference 贝叶斯推理

比如我们求出，q(t|0)=Bern(t|0.8)，那么可以说：ˆ t(1) = 1 with associated probability of error of 0.2（误差=0.2的硬推理）。这样设置是最优的。

### Loss Function and Optimal Hard Prediction 最优硬预测

对于硬推理，我们用损失函数记录预测的硬推理值与真实值之间的偏差来评估硬推理。
$$
\mathcal{l} (t,\hat t)=|t-\hat t|^k
$$
k一般=2，也就是平方损失 quadratic error loss。

一种损失函数：detection-error loss，也叫 0-1 loss。指实际值和预测值要么相等，要么差1.

$$
\begin{aligned}
 \mathcal{l} (t, \hat t) = 1(t= \hat t)\\
 1(a) = 
 \begin{cases}
      1 & \text{if a = true}\\
      
      0 & \text{if a = false}
    \end{cases}     
\end{aligned}
$$

什么情况下预测一定和真实值相等或者差1呢？只有0和1两种结果的伯努利随机向量情况就是。比如天气预测问题：

![image-20241006235908950](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410062359101.png)

如何评估硬推理的整体性能呢？一般用损失函数的平均值 population loss 计算。

![image-20241007000224593](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410070002656.png)

比如下题，预测器是令t永远=1，求 population loss。只需要计算算错部分的概率即可。

![image-20241007000444949](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410070004028.png)

那么最优预测器就是让 population loss 最小的预测函数。比如上图，很明显^t(1)=0, ^t(0)=1 的损失最小，=0.15。

对于离散预测，我们只需要挑出概率最大的条件概率点作为预测值即可。对于连续估计，我们需要计算所有点的概率平均值作为预测的期望值。

### Cross-Entropy Loss and Optimal Soft Prediction 最优软预测

预测函数q一定用后验概率p最好吗？

软预测的损失函数突然就上强度了，要算 log。cross-entropy loss：−log q(t|x)

对数损失的惩罚更高：

![image-20241007014247176](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410070142271.png)

而 population 对数损失的计算公式如下（按x求期望）：

![image-20241007014320347](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410070143416.png)

[对数损失（Log Loss）详解（code） - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/659617924)

最优软预测的公式就是让 log loss 最小化的预测取值。

*不过这一章我没有看到关于这个东西的计算，基本都是考离散的。不错，希望后面也不会有。*

## Supervised Learning 监督学习

模型不可靠或者太复杂的时候，如果知道输入数据和期望输出我们可以用监督学习。

监督学习解决的问题主要分为：

- regression problem 回归问题，连续
- classification problem 分类问题，离散

*memoralizing 是记忆，记住x,t的键值对。learning是学习，找规律。*

no free lunch theorem: 没有一种通用的学习算法可以在各种任务中都有很好的表现。我们需要对数据进行先验假设。这个假设叫做 inductive bias 归纳偏见，因为我们会在归纳过程中再做修改。

比如下面这张图，我们觉得两条横线不同长度，就是因为 inductive bias：

<img src="https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410111628240.png" alt="image-20241011162802012" style="zoom: 25%;" />

![image-20241011163108736](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410111631927.png)

inference 和 learning 的区别在于 p(x, t) 是否已知。

### Population-optimal within-class 预测模型

比如下题，下雨=0，晴天=1，x：今天天气，t：明天天气

![image-20241011163518385](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410111635618.png)

如果我们不知道概率，但是有1000次今天和明天天气的训练数据，我们可以输入系统并进行训练（把这1k次数据作为概率）。

### ERM 模型

先设立好 inductive bias 后，我们需要选一个预测器进行训练直到一定数量的结果预测正确。比如多项式预测器：

![image-20241011164938550](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410111649776.png)

根据魏尔斯特拉斯近似定理 Weierstrass approximation theorem：任何连续函数，随着M的增加，精准度都会逐渐增大。（当然预测器复杂度也增加了）

同样使用loss记录偏差：

![image-20241012140021710](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410121400861.png)

整体性能仍然是用求平均值的 population loss 计算（也叫 generalization or out-of-sample loss.）。

区别在于我们不知道准确的概率，我们是根据训练数据集的案例作为真正的概率值的估计的，所以这只能算是一种估计的损失。

根据大数定理  law of large numbers，测试案例越多，估计损失越接近真正的 population loss.

而 ERM 模型偏向真实的方法就是让损失尽可能小，这样训练结果也更偏向准确。

<img src="https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410121435595.png" alt="image-20241012143514514" style="zoom:50%;" />

例题：

![image-20241012181643970](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410121816117.png)

向量中两个元素的意思代表：[x=0时t预测为多少，x=1时t预测为多少]，loss就是x值不变，t值预测错的概率。

![image-20241012181732276](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410121817373.png)

![image-20241013234152760](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410132341005.png)