记录往年题。

## January 2024 File

### 1

![January 2024 q1](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202501031831362.png)

a) 题中给了一个条件概率，想求联合概率很简单，给条件概率中每一项乘对应的 x 的概率即可。也就是全乘 0.5.

| x\\y | 0    | 1    | 2    |
| ---- | ---- | ---- | ---- |
| 0    | 0.05 | 0.45 | 0    |
| 1    | 0.05 | 0    | 0.45 |

b) 想再求 y 作为已知条件的条件概率，就用 1 中的联合概率除以对应 y 的概率。对应 y 的概率是每一列概率求和。

| x\\y | 0    | 1    | 2    |
| ---- | ---- | ---- | ---- |
| 0    | 0.5  | 1    | 0    |
| 1    | 0.5  | 0    | 1    |

c) 硬预测当 x=1 条件给出时，y 的预测值。从原表格中可以看出此时 y=2 的概率最大，那么就令 $$\hat y=arg\ \mathop{max}\limits_{y}\ P(y|x=1)=2$$

d) 最小误差概率：发生预测出错的概率情况。y 硬预测器很明显，当 x=0 时预测值=1，当 x=1 时预测值 =2. 而发生预测出错的两种情况是 x=0, y=0 的情况和  x=1, y=0 的情况，联合概率加起来 =0.1，这就是最小误差概率。

### 2

![January 2024 q2](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202501031841108.png)

a) Empirical Distribution 就是不知道标准概率，根据经验判断。这里根据取样值推算概率即可。

| x\\t | 0    | 1    |
| ---- | ---- | ---- |
| 0    | 0.5  | 0    |
| 1    | 0.25 | 0.25 |

b) q 是软预测器，我们可以写出完整预测表：

| x\\t | 0    | 1    |
| ---- | ---- | ---- |
| 0    | 0.8  | 0.2  |
| 1    | 0.6  | 0.4  |

再计算总损失：$$L_D(q(t|x))=-0.5\cdot log(0.8)-0.25\cdot log(0.6)-0.25\cdot log(0.4)=0.4684$$ ，注意 log 以 e 为底。

c) Population distribution 是标准的，正确的概率值，也就是说正确概率值我们现在不用 a) 里面的样本估计方法近似了：

| x\\t | 0    | 1    |
| ---- | ---- | ---- |
| 0    | 0.4  | 0.1  |
| 1    | 0.4  | 0.1  |

再计算总损失：$$L_D(q(t|x))=-0.4\cdot log(0.8)-0.1\cdot log(0.2)-0.4\cdot log(0.6)-0.1\cdot log(0.4)=0.5462$$ .

d) 想让总体损失最小，软预测器的值应该和总体分布概率值一样。根据 c) 算条件概率 q(t|x)：

| x\t  | 0    | 1    |
| ---- | ---- | ---- |
| 0    | 0.8  | 0.2  |
| 1    | 0.8  | 0.2  |

e) 损失由三部分组成，最优预测的损失；bias 模型选择的损失；estimation 数据集造成的损失。
$$
L_p(q(t|x))=\underbrace{L_p(q^*(t|x))}_\text{最优分布损失}+\underbrace{\underbrace{L_p(q(t|x))}_\text{当前模型的分布损失}-L_p(q^*(t|x))}_\text{最优分布和当前模型的分布损失之间的差值}\\
$$
没太看懂，先待定。

### 3

![January 2024 q3](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202501040015888.png)

a) stationary point 极值点：求导=0 的点。
$$
g'(\theta)=0.4(\theta-1)+1.6(\theta-4)=2\theta-6.8\\
\theta=3.4
$$
b) 梯度下降让损失函数进一步减小：根据导数下降最快的方向修改 θ 值。
$$
\theta_2=\theta_1-\gamma\cdot \frac{d g(\theta_1)}{d\theta}=0.68
$$
c) L-smooth：g(θ) 的二阶导永远小于等于 L. 从 a) 可推断出 g(θ) 的二阶导恒=2，L=2.

d) 根据公式，两者差值最小值= $$\frac{\gamma}{2}\nabla g^2(\theta^{(1)})$$ ，梯度下降的平方值。$$\gamma=1/L$$ ，代入 θ_1=0 后计算得到差值最小值=11.56

### 4

![January 2024 q4](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202501040101609.png)

a) 首先通过权重层，W 与输入列向量 x 相乘，得到 [1,1]^T^。

然后通过激活函数，ReLU 激活函数就是 max(0,a)，得到 [1,1]^T^。

再通过 classification vector，1\*1+1\*1=2.

最后计算 σ 函数，代入2：$$\frac{e^2}{1+e^2}=0.881$$

*我感觉他给的答案错了。*

b) 硬分类预测：因为 a) 中计算得出 P(t=1|x, θ) > 0.5，所以 $$\hat t(x)=arg\ max\ P(t|x, \theta)=1$$

c) 先前向传播，传播过程中对每个 x 求导；然后后向传播，最终结果和 W w^2^ 分别相乘获取梯度。如果是求梯度更新后的权重，就让原权重值 W 和梯度值求和。

![ ](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202501040342442.jpg)

*这道题因为前面和答案有分歧所以整个重做了，不确定对不对。*