## 前言

**离散时间信号处理是什么东西**？

我们自然界大多数信息，信号都是连续的，比如温度，光照，电压（**连续时间信号**，**模拟信号**）。但是这些连续数据无法交给计算机直接处理，我们知道计算机只能处理01二进制数据（**离散时间信号**，**数字信号**）。两者主要区别是时间域是否连续。

ADC将信号采样转为离散的数字信号供计算机处理，这门课程的主要内容就是对离散的数字信号的处理方法。

在FFT出现之前，直到20世纪60年代，离散时间信号处理的主要方法都是利用数字信号去逼近或者仿真模拟信号。FFT则引发了一系列新的离散时间信号处理的概念与方法。

## 离散时间信号与系统

### 模拟信号转为数字信号的方法

如图，曲线为连续时间信号，蓝色和红色的是数字信号，我们设定一定的采样周期对原信号进行采样。采样周期越小，也就是采样频率越高，数字信号越能模拟出模拟信号（红色信号明显比蓝色信号更接近原曲线的形状）。

![image-20240914225114843](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202409142251075.png)

模拟信号转换为数字信号的方式：
$$
x[n]={x_a[nT]},	-\infty<n<+\infty
$$
简单来说就是以一定的周期进行采样嘛。周期是T，我们对原模拟函数x_a在 [0, T, 2T, 3T...]处取样得到y轴的数值，生成数字信号。

x[n]的函数形式表示这个函数是一个离散时间信号，x(n)的函数是连续时间信号。

![image-20240914225712380](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202409142257453.png)

### 几个重要的单位样本序列

以下的一些函数比较重要，可能会多次在离散时间信号处理中用到。所以作者在这里集中列了一下。

**单位样本序列**，又叫（离散时间）脉冲：
$$
\delta[n]=
\begin{cases}
0 & \text{if } n \neq 0 \\
1 & \text{if } n = 0
\end{cases}
$$
这个序列很简单。图示如下：

![image-20240914230218255](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202409142302318.png)

这个序列的一个重要作用是：
$$
x[n]=\sum^{\infty}_{k=-\infty}x[k]\delta[n-k]
$$
对于任何序列，这个公式都适用。也就是说在每个采样点，我用δ[n]的1与这个采样点的x值相乘，得到的序列和原序列一样。也就相当于x[n]=x[n]*1嘛！

后面再讲其具体作用。

**单位阶跃序列**：
$$
u[n]=\begin{cases}
1& \text{if } n \geq 0\\
0& \text{if } n \lt 0
\end{cases}
$$
也就是说正半轴是u=1的直线，负半轴全是0.

![image-20240914230733299](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202409142307365.png)

单位阶跃序列和单位样本序列的关系：单位样本序列从-\infty到当前采样点的累加，就等于当前采样点单位阶跃序列的值。
$$
u[n]=\sum^{n}_{k=-\infty}\delta[k]
$$
单位样本序列是单位阶跃序列的一阶后向差分。
$$
\delta[n]=u[n]-u[n-1]
$$
**指数序列：**形如x[n]=Aα^n^。下图是0<α<1的形状：

![image-20240914231532621](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202409142315667.png)

如果α>1，则逐渐上升。

如果-1<α<0，则序列正负交替，但摆动幅度逐渐减小，趋近于0.

如果α是复数？

首先我们需要了解一下复数极坐标的概念，如何表示复数：[复数与相位(旋转)_相位旋转-CSDN博客](https://blog.csdn.net/zoujiachi666/article/details/72568450)

那么，我们就可以假设A=|A|e^{jΦ}^，α=|α|e^{jω}^（实数和复数都可以这样表示，实数只不过是相位角=π的倍数罢了）：
$$
x[n]=A\alpha ^n
=|A\alpha ^n|e^{j(\Phi +n\omega )}=|A\alpha^n|[cos(n\omega+\phi)+jsin(n\omega+\phi)]
$$
包络，也就是振幅，也就是|Aα|这一块，如果α>1，则和α成正比。如果0<α<1，则成反比。

ω被称作频率，Φ被称作相位。

顺带一提，nω+Φ的单位应该是弧度 rad，但是n是一个无量纲整数（就是没有单位的意思吧）。所以ω的单位是弧度（而非rad/s之类的）。

由于正余弦的周期性，ω一般范围是(-π, π]或者[0, 2π)。

对于连续时间信号来说，这个函数一定是周期函数。但是对于离散时间信号来说，判断是否为周期函数的依据是：
$$
x[n]=x[n+N], N\;is\;integer\;period
$$
我们把这个判别公式代入函数，挑简单的，只挑一个正弦函数，可以得到：
$$
\begin{aligned}
Acos(\omega n+\Phi )&=Acos(\omega n+N\omega +\Phi )\\
N\omega &=2\pi k,\,Nk\;are\;integers
\end{aligned}
$$

只有当上式满足的时候，该正弦离散时间序列才是周期序列。也就是说ω需要时π的一定倍数。

### 离散时间系统

就是一个离散时间序列处理后得到另一个呗。
$$
y[n]=T{x[n]}
$$
![image-20240915000257914](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202409150002990.png)

T就是一些处理方式。需要注意的是n点处的y并不一定只和x[n]有关系，可能和x[n]序列的全部和部分内容有关。比如前面提到的，单位样本序列从-∞到当前采样点的累加，等于当前采样点单位阶跃序列的值。

### 几个重要的系统

下面是一些简单系统：

**理想延迟系统**：每个采样点的信号的延迟都一样。
$$
y[n]=x[n-n_d]
$$
**滑动平均系统**：第n个样本是由其前后的一定数量样本的平均值得到。假设这个范围是n往左M1个，往右M2个的范围，则公式为：
$$
\begin{aligned}
y[n]&=\frac{1}{M_1+M_2+1}\sum^{M_2}_{k=-M_1}x[n-k]\\
&=\frac{1}{M_1+M_2+1}\{x[n+M_1]+x[n+M_1-1]+...+x[n]\\
\\
&+x[n-1]+...+x[n-M_2]\}
\end{aligned}
$$
**无记忆系统**：y[n]只和n采样点的x有关，y[n]只和x[n]有关。

很明显前两个系统都不是无记忆系统。

**线性系统**：满足如下公式就是线性系统。
$$
T\{a\cdot x_1[n]+b\cdot x_2[n]\}=a\cdot T\{x_1[n]\}+b\cdot T\{x_2[n]\}=a\cdot y_1[n]+b\cdot y_2[n]
$$
也就是说满足累加性和齐次性，累加性是T{x1[n]+x2[n]}=y1[n]+y2[n]，齐次性是T{ax1[n]}=ay1[n].

**累加器系统**：系统在某个时刻的输出等于这个该时刻之前所有输入之和。
$$
y[n]=\sum^{n}_{k=-\infty}x[k]
$$
累加器系统是一个线性系统。（本来就是数据求和嘛，乘函数以及两个累加器相加得到的结果也是原数据的倍数累加而已）

**时不变系统**：输入延时一定值，输出也延时同样的值，则为时不变系统。判别公式为：
$$
\begin{aligned}
if\;x_1[n]&=x[n-n_0]\\
y_1[n]=y[n-n_0]&=T\{x_1[n]\}=T\{x[n-n_0]\}
\end{aligned}
$$
**压缩器系统**：从样本中跳过M-1个数据选一个作为输出。
$$
y[n]=x[Mn]
$$
这个系统不是是不变的。我们代入公式试一下：
$$
\begin{aligned}
&y_1[n]=x_1[Mn]=x[Mn-n_0]\\
&T\{x[n-n_0]\}=x[Mn-Mn_0]
\end{aligned}
$$
等式不成立。

**因果性系统**：某个采样点的输出值取决于这个采样点左边的所有输入，y[n_0]只和n<=n_0的输入序列有关系。那么我们只要知道一个节点的输入值和这个节点之后的所有输入值，就可以判断这个节点的输出了。

比如很典型的累加器是因果的；滑动平均系统是不是因果的取决于M1，M1<=0则是因果的（只取到后边一段数据的平均）。

**前向差分系统**：y[n]=x[n+1]-x[n]，不是因果的。

**后向差分系统**：y[n]=x[n]-x[n-1]，是因果的。

**稳定系统：**对于有界的输入，必定会产生有界的输出。
$$
\begin{aligned}
|x[n]|\leq B_x\lt \infty\\
|y[n]|\leq B_y\lt \infty
\end{aligned}
$$
比如y[n]=x[n]^2^，如果我们设定|x[n]|<=Bx，那么y[n]一定<=By=Bx^2^可知这个系统稳定。

再比如，单位阶跃系统的累加器系统（也就是说在y轴往左，输出一直是0；在y轴往右，输出为n+1的一阶函数）|x[n]|也就是单位阶跃函数是一直<=1的。但是y[n]是无限增长的，y[n]会增长到正无穷。那么有界的x[n]没有得到有界的y[n]，这个系统不稳定。

**线性时不变系统**：线性+时不变。

那么根据线性时不变系统我们可以引出这个系统的卷积和公式，利用单位冲激信号表示。

首先单位冲激信号是δ[n]，我们知道这个信号是只在n=0的时候=1.

单位冲激信号的系统输出我们设定为h[n]。
$$

\begin{aligned}
x[n] &= \sum^{+\infty}_{k=-\infty} x[k] \delta[n-k] \\
y[n] &= T\left(x[n]\right) = T\left(\sum^{+\infty}_{k=-\infty} x[k] \delta[n-k]\right) \\
     &= \sum^{+\infty}_{k=-\infty} x[k] T\left(\delta[n-k]\right) \\
     &= \sum^{+\infty}_{k=-\infty} x[k] h[n-k]
\end{aligned}

$$
第二行到第三行的转变是线性系统的特性。

这个公式就是有名的卷积和公式。我们只需要对单位冲激函数进行系统处理，然后拿着处理后的系统输出像一个小放大镜滑块一样在x[n]上滑动相乘，就可以得到最终系统处理后的x[n]的输出。深度学习常用此方法来提取图片特征等。

另一种书写方式为：
$$
y[n]=x[n]*h[n]
$$
注意这个符号不是乘号，而是卷积运算符号，代表的效果就是上面的公式。

对于时不变性质，可以得出：
$$
y[n-n_0]=\sum^{+\infty}_{k=-\infty}x[k]h[n-n_0-k]
$$
简化写法：
$$
y[n-n_0]=x[n]*h[n-n_0]
$$
![image-20240916005211819](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202409160052171.png)

### 线性时不变系统的性质

1. x h可以交换，如果感觉卷积运算不好算可以调换。
2. 满足交换律，x[n]\*h1[n]+x[n]\*h2[n]=x[n]\*(h1[n]+h2[n])
3. 满足结合律，x[n]\*h1[n]\*h2[n]=x[n]\*(h1[n]\*h2[n])
4. 稳定性：y[n]<=BxBh。而且，当且仅当h函数的**绝对值**从负无穷到正无穷累加结果不是无穷大时（稳定，summable），y[n]有界。所以判断系统是否稳定的时候，算一下sum |h[n]|。
5. 因果性，所以冲激序列的响应h[n]在n<0时=0。在负半轴=0的序列也叫因果序列。
6. x[n]和理想延迟的单位冲击响应卷积，得到的结果相当于平移x[n]。如x[n]\*δ[n-1]=x[n-1]，x[n]\*δ[n]=x[n]
7. 一个单位冲激序列，经过系统得到的单位冲激响应h[n]，与这个单位冲击序列经过逆系统得到的单位冲激响应hi[n]，两者卷积会得到δ[n]. 有一些场景逆系统是很有用的。

### 线性常系数差分方程

可以表示为如下形式的系统：
$$
\sum^{N}_{k=0}a_ky[n-k]=\sum^{M}_{m=0}b_mx[n-m]
$$
注意线性常系数差分方程并不一定是线性系统。

比如累加器系统，y[n]=x[n]从-∞到n的求和嘛，那么y[n]-y[n-1]=x[n]，这是一个线性常系数差分方程。

*后面课程中会出现很多用差分方程表示的输入输出关系。*

满足线性常系数差分方程的系统可以写作如下：
$$
y[n]=y_p[n]+y_h[n]
$$
y_p[n]满足上面的差分方程，而y_h[n]又叫齐次差分方程，满足：
$$
\sum^{N}_{k=0}a_ky[n-k]=0
$$

### 频域，傅里叶变换

离散信号的时域到频域转换公式（傅里叶变换公式）：
$$
X(e^{j\omega})=\sum^{\infty}_{n=-\infty}x(n)e^{-j\omega n}
$$

$$
y(n)=H(e^{j\omega})e^{j\omega n}, H(e^{j\omega})=\sum^{\infty}_{n=-\infty}h(n)e^{-j\omega n}
$$

H(e^jω^) 被称为频率响应。它是一个复数函数，以2π为周期。

![image-20241001111652227](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410011116480.png)

而频域到时域的转换则相反：
$$
x[n]=\frac{1}{2\pi}\int_{-\pi}^{\pi}X[e^{j\omega}]e^{j\omega n}d\omega
$$
注意两种域的序列的表示方式，x[n]和X(e^jω^)

1. 有无限长度的离散序列才能求傅里叶变换。因为傅里叶变换本质是用一些sin和cos函数的拉伸加减变换来模拟出原信号，变换后我们值记录这些函数的周期相位幅度等信息。但是这些函数都是延伸到正无穷和负无穷的，所以没法表示出有界的离散信号。

2. 如果x[n]从负无穷到正无穷的全部绝对值求和不是无穷（也就是说，可加的 summable）那么X(e^jω^) 就是收敛 Convergence 的。

   ![image-20241001113738011](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410011137328.png)

3. x[n]的平方求和也可加，那么其傅里叶变换也收敛。也就是说其总能量有限。相比之下，x[n]可积只是傅里叶变换收敛的一个强条件。

   引理：

   ![image-20241001114027735](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410011140011.png)

4. ![image-20241001114819652](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410011148953.png)

5. 如果 x[n] 是一个实序列，那么：

   ![image-20241001122300639](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410011223958.png)

6. 如果x[n]是实序列且对称 real and symmetric, 那么其傅里叶变换也有着同样的性质。

### 一些常见的傅里叶变换对

注意条件，有些序列的格式或者域不对是求不了傅里叶变换的。

![image-20241015110753953](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410151107262.png)

## z变换


$$
\sum_{-\infty}^{+\infty}x[k]e^{-j\omega k}=\sum_{-\infty}^{+\infty}x[k]z^{-k},\,z=e^{-j\omega}
$$
如果x的傅里叶变换不收敛，z还可以加参数：e^{-jw}/r，让x[n]下降速度更快，从而收敛。

让x收敛的z取值被称为ROC Region of Convergence of X(z)
$$
X(z)=\sum_{-\infty}^{+\infty}x[k]z^{-k}=\sum_{-\infty}^{-1}x[k]z^{-k}+\sum_{0}^{+\infty}x[k]z^{-k}
$$
想让结果收敛，就必须让两个部分都收敛。假设第一部分收敛的z值是|z|<r-, 第二部分是|z|>r+, 那么 r+<|z|<r- 就是X(z)的ROC. 当然，r+ r-可能等于无穷，也可能没有交集。

X(z)和ROC共同确定x[n]. 两个不同的x[n]可能X(z)一样，ROC不同。根据上面的公式代入计算域即可。

![image-20241015112614881](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410151126207.png)

- ROC在图上表现为一个圆环或者圆。当单位圆（z=e^{-jw}^）包含在内时，x[n]的傅里叶变换存在（因为z=e^{-jw}^时就是傅里叶变换的公式，说明收敛）

- 当x[n]由有限个非零值组成时，z[n]的取值就非常随意了，基本除了0和无穷都可以取（z可以取到无穷的）。

- X(z)=0的z解叫zeros, X(z)=infinite 的解叫poles

### z逆变换

$$
x[n]=\frac{1}{j2\pi}\oint_Cz^{n-1}X(z)dz=\frac{1}{2\pi}\int_{-\pi}^{\pi}X(e^{j\omega n})d\omega,\,z=e^{j\omega}
$$

1/j被de^{jw}出来的j约掉了。中间的式子相当于绕原点转一圈，求圆环面积。

如果X(z)不好变换，可以拆成几个好求x[n]的Xi(z)的和，分别求解。

如果X(z)可以被化简为下面的形式，那么就可以直接求出x[n].

<img src="https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410151152213.png" alt="image-20241015115229852" style="zoom:67%;" />

如果遇到两个多项式做除法的形式，解法如下（有点逆天。这会考吗？）

![image-20241015211351195](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410152113373.png)

### z变换的性质

1. 线性，两个x[n]相加，z变换是分别的X(z)相加。ROC 是两者交集。
2. 时移： x[n-n0] ←→ z^-n0^X(z)，ROC 不变。
3. z^n0^x[n] ←→ X(z/z0)，ROC=|z0|R。
4. x[-n] ←→ X(z^-1^)，ROC=1/R。
5. nx[n] ←→ -z (dX(z)/dz)，ROC 不变。
6. x[n]=lim{z→∞}X(z)，ROC 不变。
7. x[n]*h[n] ←→ H(z)X(z)，ROC 是两者交集。
