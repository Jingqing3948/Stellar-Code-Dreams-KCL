## 前言

结合：离散信号处理第三版（奥本海姆）、KCL DSP 课件以及：

 【《数字信号处理》考研基础强化课(讲义齐全)【13h】适配通信考研离散时间信号处理考研期末速成】 https://www.bilibili.com/video/BV1Uw411U7un/?p=6&share_source=copy_web&vd_source=dcdc734e318da0cd82bcccb180b12b40

**离散时间信号处理是什么东西**？

我们自然界大多数信息，信号都是连续的，比如温度，光照，电压（**连续时间信号**，**模拟信号**）。但是这些连续数据无法交给计算机直接处理，我们知道计算机只能处理01二进制数据（**离散时间信号**，**数字信号**）。两者主要区别是时间域是否连续。

ADC将信号采样转为离散的数字信号供计算机处理，这门课程的主要内容就是对离散的数字信号的处理方法。

在FFT出现之前，直到20世纪60年代，离散时间信号处理的主要方法都是利用数字信号去逼近或者仿真模拟信号。FFT则引发了一系列新的离散时间信号处理的概念与方法。

## 离散时间信号与系统

### 模拟信号转为数字信号的方法

如图，曲线为连续时间信号，蓝色和红色的是数字信号，我们设定一定的采样周期对原信号进行采样。采样周期越小，也就是采样频率越高，数字信号越能模拟出模拟信号（红色信号明显比蓝色信号更接近原曲线的形状）。

![连续与离散信号图示](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202409142251075.png)

模拟信号转换为数字信号的方式：
$$
x[n]={x_a[nT]},	-\infty<n<+\infty
$$
简单来说就是以一定的周期进行采样嘛。周期是T，我们对原模拟函数x_a在 [0, T, 2T, 3T...]处取样得到y轴的数值，生成数字信号。

x[n]的函数形式表示这个函数是一个离散时间信号，x(n)的函数是连续时间信号。

![离散信号图解](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202409142257453.png)

### 几个重要的单位样本序列

以下的一些函数比较重要，可能会多次在离散时间信号处理中用到。所以作者在这里集中列了一下。

**单位样本序列**，又叫（离散时间）脉冲，冲激：
$$
\delta[n]=
\begin{cases}
0 & \text{if } n \neq 0 \\
1 & \text{if } n = 0
\end{cases}
$$
这个序列很简单。图示如下：

![delta函数图示](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202409142302318.png)

这个序列的一个重要作用是用于取样：
$$
x[n]=\sum^{\infty}_{k=-\infty}x[k]\delta[n-k]
$$
对于任何序列，这个公式都适用。也就是说在每个采样点，我用δ[n]的1与这个采样点的x值相乘，得到的序列和原序列一样。也就相当于 $$x[n]=x[n]*1$$ 嘛！

后面再讲其具体作用。

**单位阶跃序列**：
$$
u[n]=\begin{cases}
1& \text{if } n \geq 0\\
0& \text{if } n \lt 0
\end{cases}
$$
也就是说正半轴是u=1的直线，负半轴全是0.

![单位阶跃序列图像](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202409142307365.png)

单位阶跃序列和单位样本序列的关系：单位样本序列从-\infty到当前采样点的累加，就等于当前采样点单位阶跃序列的值。
$$
u[n]=\sum^{n}_{k=-\infty}\delta[k]
$$
单位样本序列是单位阶跃序列的一阶后向差分。
$$
\delta[n]=u[n]-u[n-1]
$$
**指数序列：**形如 $$x[n]=Aα^n$$。下图是 $$0<α<1$$ 的形状：

![指数序列图像](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202409142315667.png)

如果α>1，则逐渐上升。

如果-1<α<0，则序列正负交替，但摆动幅度逐渐减小，趋近于0.

如果α是复数？

首先我们需要了解一下复数极坐标的概念，如何表示复数：[复数与相位(旋转)_相位旋转-CSDN博客](https://blog.csdn.net/zoujiachi666/article/details/72568450)

那么，我们就可以假设A=|A|e^{jΦ}^，α=|α|e^{jω}^（实数和复数都可以这样表示，实数只不过是相位角=π的倍数罢了）：
$$
x[n]=A\alpha ^n
=|A\alpha ^n|e^{j(\Phi +n\omega )}=|A\alpha^n|[cos(n\omega+\phi)+jsin(n\omega+\phi)]
$$
包络，也就是振幅，也就是|Aα|这一块，如果α>1，则和n成正比。如果0<α<1，则成反比。

ω被称作频率，Φ被称作相位。

*顺带一提，nω+Φ 的单位应该是弧度 rad，但是n是一个无量纲整数（就是没有单位的意思吧）。所以ω的单位是弧度（而非rad/s之类的）。*

由于正余弦的周期性，ω一般范围是(-π, π]或者[0, 2π)。

对于连续时间信号来说，这个函数一定是周期函数。对于离散时间信号来说，判断是否为周期函数的依据是：
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

只有当上式满足的时候，该正弦离散时间序列才是周期序列。也就是说ω需要是π的一定倍数。$$T=\frac{2\pi}{\omega}$$

### 离散时间系统

就是一个离散时间序列处理后得到另一个呗。
$$
y[n]=T{x[n]}
$$
![image-20240915000257914](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202409150002990.png)

T 代表一些处理方式。需要注意的是n点处的y并不一定只和x[n]有关系，可能和x[n]序列的全部和部分内容有关。比如前面提到的，单位冲激序列从-∞到当前采样点的累加，等于当前采样点单位阶跃序列的值。

### 几个重要的系统

下面是一些简单系统。其中，做题常考的是：线性系统证明，时不变系统证明，因果系统证明，稳定系统证明。

**理想延迟系统**：每个采样点的信号的延迟都一样，整个信号完美右移。
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

很明显前两个系统都不是无记忆系统（参考了过去或未来某一采样点的 x[n]）。

**线性系统**：满足如下公式就是线性系统。
$$
T\{a\cdot x_1[n]+b\cdot x_2[n]\}=a\cdot T\{x_1[n]\}+b\cdot T\{x_2[n]\}=a\cdot y_1[n]+b\cdot y_2[n]
$$
也就是说满足累加性和齐次性，累加性是T{x1[n]+x2[n]}=y1[n]+y2[n]，齐次性是T{ax1[n]}=ay1[n].

证明方式如上，先代入 x1[n] 和 x2[n] 得到 y1[n] y2[n]，然后分别乘a，b相加；再直接令 x[n]=ax1[n]+ax2[n] 代入，得到 y[n]，比较两式是否相等。

**累加器系统**：系统在某个时刻的输出等于这个该时刻之前所有输入之和。
$$
y[n]=\sum^{n}_{k=-\infty}x[k]
$$
累加器系统是一个线性系统。（本来就是数据求和嘛，乘函数以及两个累加器相加得到的结果也是原数据的倍数累加而已）

**时不变系统** time-invariant：输入延时一定值，输出也延时同样的值，则为时不变系统。判别公式为：
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

**因果性系统** casual：某个采样点的输出值取决于这个采样点左边的所有输入，y[n_0]只和n<=n_0的输入序列有关系。那么我们只要知道一个节点的输入值和这个节点之后的所有输入值，就可以判断这个节点的输出了。如果出现形如 y[n]=x[n+1] 的式子，就不是因果性的了。

比如很典型的累加器是因果的；滑动平均系统是不是因果的取决于M1，M1<=0则是因果的（只取到后边一段数据的平均）。

**前向差分系统**：y[n]=x[n+1]-x[n]，不是因果的。

**后向差分系统**：y[n]=x[n]-x[n-1]，是因果的。

**稳定系统** stable：对于有界的输入，必定会产生有界的输出。
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
![时不变卷积性质](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202409160052171.png)

### 线性时不变系统的性质

1. x h可以交换，如果感觉卷积运算不好算可以调换。
2. 满足交换律，x[n]\*h1[n]+x[n]\*h2[n]=x[n]\*(h1[n]+h2[n])
3. 满足结合律，x[n]\*h1[n]\*h2[n]=x[n]\*(h1[n]\*h2[n])
4. 稳定性：y[n]<=BxBh。而且，当且仅当h函数的**绝对值**从负无穷到正无穷累加结果不是无穷大时（summable），y[n]有界。所以判断系统是否稳定的时候，算一下sum |h[n]|。
5. 因果性，所以冲激序列的响应h[n]在n<0时=0。在负半轴=0的序列也叫因果序列。
6. x[n]和理想延迟的单位冲击响应卷积，得到的结果相当于平移x[n]。如x[n]\*δ[n-1]=x[n-1]，x[n]\*δ[n]=x[n]
7. 一个单位冲激序列，经过系统得到的单位冲激响应h[n]，与这个单位冲击序列经过逆系统得到的单位冲激响应hi[n]，两者卷积会得到δ[n]. 有一些场景逆系统是很有用的。

### 线性常系数差分方程

可以表示为如下形式的系统被称作线性常系数差分方程：
$$
\sum^{N}_{k=0}a_ky[n-k]=\sum^{M}_{m=0}b_mx[n-m]
$$
注意线性常系数差分方程并不一定是线性系统。

比如累加器系统，y[n]=x[n]从-∞到n的求和，那么y[n]-y[n-1]=x[n]，这是一个线性常系数差分方程。

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

H(e^jω^) 被称为频率响应，是 h[n] 的傅里叶变换。它是一个复数函数，以2π为周期。所以绘制图像一般只绘制 -pi到 pi 的范围。
$$
H(e^{j\omega})=|H(e^{j\omega})|e^{j\angle H(e^{j\omega})}
$$


上式的第一部分是幅度响应，第二部分是相位响应。

而频域到时域的转换则相反：
$$
x[n]=\frac{1}{2\pi}\int_{-\pi}^{\pi}X[e^{j\omega}]e^{j\omega n}d\omega
$$
注意两种域的序列的表示方式，x[n]和X(e^jω^)

1. 有无限长度的离散序列才能求傅里叶变换。因为傅里叶变换本质是用一些sin和cos函数的拉伸加减变换来模拟出原信号，变换后我们值记录这些函数的周期相位幅度等信息。但是这些函数都是延伸到正无穷和负无穷的，所以没法表示出有界的离散信号。

2. 如果x[n]从负无穷到正无穷的全部绝对值求和不是无穷（也就是说，可加的 summable）那么X(e^jω^) 就是收敛 Convergence 的。

   下面是一种特殊的 convergence：uniform convergence
   $$
   \forall \epsilon \gt 0, \exists N_0=N_0(\epsilon)\,s.t,\,\forall N\ge N_0\\
   |X(e^{j\omega})-\sum^{N}_{n=-N}x[n]e^{-j\omega n}|\le \epsilon \,for\,all\,\omega\in (-\pi, \pi)
   $$

3. x[n]的平方求和可加 square-summable，那么其傅里叶变换也收敛。也就是说其总能量有限。相比之下，x[n] 可积只是傅里叶变换收敛的一个强条件。

4. $$
   if~functions~X_1(e^{j\omega})~and~X_2(e^{j\omega})~satisfy:\\
   \int^\pi_{-\pi}|X_1(e^{j\omega})-X_2(e^{j\omega})|^2d\omega=0,~\Rightarrow x_1[n]=x_2[n],~\forall n \in Z\\
   x_i[n]=\frac{1}{2\pi}\int ^{\pi}_{-\pi}X_i(e^{j\omega})e^{j\omega n }d\omega,~i=1,2
   $$

5. 如果 x[n] 是一个实序列，那么：
   $$
   X_R(e^{-j\omega})=X_R(e^{j\omega}), X_I(e^{-j\omega})=-X_I(e^{j\omega})
   $$

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

- ROC在图上表现为一个圆环或者圆。**当单位圆（z=e^{-jw}^）包含在内时，X(z) 是稳定的，**x[n]的傅里叶变换存在（因为 $$z=e^{-jw}$$ 时就是傅里叶变换的公式，说明收敛）

- **当z=+∞被包含在 ROC 内时，X(z) 是因果的**。也就是说 ROC 的公式类似：$$|z|>\alpha$$ 的形态，而不能是 $$\alpha < |z| < \beta$$ 形态。

-  当x[n]由有限个非零值组成时，z[n]的取值就非常随意了，基本除了0和无穷都可以取（z可以取到无穷的）。

- X(z)=0的z解叫zeros, X(z)=infinite 的解叫poles. 如果 X(z)可以表示为P(z)/Q(z) 的分式，**P(z)的根是zeros，Q(z)的根是poles.** 比如 $$X(z)=\frac{z-3}{z-2}$$，z=3 是 zero point, z=2 是 pole point.

### z逆变换

$$
x[n]=\frac{1}{j2\pi}\oint_Cz^{n-1}X(z)dz=\frac{1}{2\pi}\int_{-\pi}^{\pi}X(e^{j\omega n})d\omega,\,z=e^{j\omega}
$$

1/ j被de^{jw}出来的 j 约掉了。中间的式子相当于绕原点转一圈，求 ROC 圆环面积。

如果X(z)不好变换，可以拆成几个好求 x[n] 的 Xi(z) 的和，分别求解。

如果X(z)可以被化简为下面的形式，那么就可以直接求出x[n].

<img src="https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410151152213.png" alt="image-20241015115229852" style="zoom:67%;" />

如果遇到两个多项式做除法的形式，先因式分离成可以直接逆变换的形式，再处理（常用z变换对在下面）。

### z变换的性质

1. 线性，两个x[n]相加，z变换是分别的X(z)相加。ROC 是两者交集。
2. 时移： x[n-n0] ←→ z^-n0^X(z)，ROC 不变。
3. z^n0^x[n] ←→ X(z/z0)，ROC=|z0|R。
4. x[-n] ←→ X(z^-1^)，ROC=1/R。
5. nx[n] ←→ -z (dX(z)/dz)，ROC 不变。
6. x[n]=lim{z→∞}X(z)，ROC 不变。
7. x[n]*h[n] ←→ H(z)X(z)，ROC 是两者交集。

### 常用z变换对

![image-20241017232423031](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410172324191.png)

## 连续时间信号取样

这节课是叫离散信号处理没错，我们避免处理连续信号，可以把连续信号取样为离散信号处理。

![image-20241027184733652](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410271847897.png)

变量解释：

T：采样周期

$$\Omega_s$$：采样角频率，比如 cos(400πn) 就是400π

$$\Omega_N$$：原连续信号频率

$$\omega$$：离散信号角频率，$$\Omega=\frac{\omega}{T}$$

采样效果上相当于原连续信号乘了多个 δ 函数求和。
$$
x_s(t)=x_c(t)s(t),s(t)=\sum^\infty_{n=-\infty}\delta(t-nT)
$$
采样的频域表示：
$$
X_s(j\Omega)=X_C(j\Omega)*S(j\Omega)=\frac{1}{T}\sum^{\infty}_{k=-\infty}X_c(j(\Omega-k\Omega_s))
$$

从公式来看，采样后的频域函数其实就是原来的频域函数进行一定频移后求和。

如果采样频率过低，可能会导致对原信号的推测不准确，比如下图，原信号是红色部分，采样出的结果是蓝色部分：

![[什么是混叠? - 知乎](https://zhuanlan.zhihu.com/p/23923059)](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410292020213.jpeg)

这种现象叫做混叠 aliasing，主要就是采样频率不够大造成的，频域图像发生一定程度的重叠导致无法正确推测回原信号。如下图（信号的最大频率用 Ω\_N 表示，采样频率用 Ω\_s 表示）：

![image-20241213033100982](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412130331196.png)

或者可能会出现下面这种情况：信号只有采样范围外的高频部分而没有采样部分内的低频部分时，高频部分会落在其他区间里被视作低频部分：

<img src="https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412130510700.png" alt="image-20241213051006408" style="zoom:67%;" />

### 奈奎斯特采样定律

如何确保不发生混叠？从上图我们可以看出，当 $$\Omega_s-0>2\Omega_N$$ 的时候信号不发生混叠。这就是奈奎斯特采样定律。

如果频域满足如下两个条件：

- 对于 $$|\Omega|>\Omega_N$$ ，$$X_c(j\Omega)=0$$ （也就是说 x_c(t) 是 bandlimited 的）
- T 小到 $$\Omega_s>2\Omega_N$$ , 取样频率是原频率的2倍以上

那么 $$X_c(j(\Omega-k\Omega))$$ 就不发生混叠，并且我们可以用一个 filter h_r(t) 和 x_s(t) 卷积重构的 x_c(t) （采样频率够高，可以从采样后的信号恢复原信号）. 滤波器就是形如矩形的 H(e^jw^)，相当于只提取出 X(e^jw^) 中的特定频域范围的信号进行处理。

原理如下图，首先采样频率够大，可以确保频域图像不发生混叠；然后我们用滤波器只提取出 ±Ω_N 范围内的部分，就是原信号，这样得到的采样后的离散信号的频域图和连续信号的频域图完全一致，可以还原。

![image-20241213033452373](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412130334536.png)

过滤公式和过滤器的傅里叶变换如下（简单说就是时域卷积频域乘积）：
$$
\begin{aligned}
x_r(t)=\int^{\infty}_{-\infty}x_s(\xi)h_r(t-\xi)d\xi=\sum^{\infty}_{n=-\infty}x_c(nT)h_r(t-nT)\\
H_r(j\Omega)=\begin{cases}
T &  |\Omega|<\Omega_c \\
0 & |\Omega|>\Omega_c
\end{cases}
\end{aligned}
$$
其中 Ω_c 是低通滤波器 H 的频率， $$\Omega_N<\Omega_c<\Omega_s-\Omega_N$$ （确保只采样到原始频域信号）

没有混叠发生时，有如下公式：
$$
X(e^{j\omega})=\frac{1}{T}\sum^{\infty}_{k=-\infty}X_c(j(\frac{\omega}{T}-\frac{2\pi k}{T}))
$$
这就是奈奎斯特采样定律，其中 $$\Omega_s=2\Omega_N$$ 的采样频率就是奈奎斯特采样率（Ωc=Ωs/2=π/T）。从图像上看的效果就是刚好每次采样的频域信号是相接的。

### 带限信号的重建

奈奎斯特定律只能保证采样的频率正确，但也不能保证可以无损恢复为原信号。如下图的恢复：

![[《信号与系统》解读 第4章 连续信号的离散化：采样与采样定理、奈奎斯特准则、脉冲编码调制PCM_采样定理和奈奎斯特定理-CSDN博客](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410292026474.png)](https://i-blog.csdnimg.cn/blog_migrate/10232bcdec0367bca77a0c42fcb56804.png)

如果设置合适的 h 函数，即理想低通滤波器就可以无损恢复原信号。

截止频率设置为：$$\Omega_C=\Omega_s/2$$

则有：
$$
\begin{aligned}
h_r(t)&=\frac{sin(\pi t/T)}{\pi t/T}\\
x_r(t)&=\sum^{\infty}_{n=-\infty}x[n]\frac{sin(\pi (t-nT)/T)}{\pi (t-nT)/T}
\end{aligned}
$$
![[没有幻灯片标题](https://realtimetech.ustc.edu.cn/_upload/article/files/5f/71/77450bde46de832d7f14ae714039/e16a2953-6949-4393-997d-8dede2a612d7.pdf)](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410301417957.png)

### 连续信号处理

对于输入的连续信号，首先我们进行采样转换为离散信号，然后通过系统处理，最终再重建为连续信号。

![image-20241030142506011](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410301425372.png)



那么整个过程的公式就可以写作：
$$
Y_r(j\Omega)=H_r(j\Omega)H(e^{j\Omega T})X(e^{j\Omega T})
$$
第一个 H 是重建连续信号用的，上面我们已经讲过其公式就是在 $$\pm \frac{\Omega_s}{2}$$ 范围内都=T，超过这个范围都=0.

第二个 H 是离散时间系统的频率响应。

根据离散和连续信号的频域关系，可以进一步化简;
$$
\begin{align}
Y_r(j\Omega)=H_r(j\Omega)H(e^{j\Omega T})\frac{1}{T}\sum^{\infty}_{k=-\infty}X_c[j(\Omega-\frac{2\pi k}{T})]\\

=\begin{cases}
&H(e^{j\Omega T})X_c(j\Omega), &|\Omega|\lt\pi/T \\
&0, &|\Omega|\ge\pi/T
\end{cases}
\end{align}
$$


Hr(jΩ) 和 1/T 系数约掉了。

那么整个连续系统的频率响应可以写作：
$$
H_{eff}(j\Omega)=\begin{cases} &H(e^{j\Omega T}),&|\Omega|<\frac{\pi}{T}\\
&0,&|\Omega|>\frac{\pi}{T}
\end{cases}
$$
离散信号的连续时间处理：令：
$$
h[n]=Th_c(nT)
$$

### 降采样 downsampling

奈奎斯特采样率的描述是：必须高于这个采样率，频域信号才不会发生混叠。

但是实际上，并不是“发生混叠就会损失信息”。对于有些情况来说即使采样率不够大，信号会发生混叠，但我们仍然可以还原出原来的信号。比如我们用滤波器把三角形频域信号混叠的部分削减一下：

![[对信号做降采样处理时，需要先滤波，后抽取（降采样）；升采样操作与之相反-CSDN博客](https://blog.csdn.net/qq_42233059/article/details/128693344)](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412132229264.png)

也就是说如果降低采样率变为 MT（T 是原采样率，不是原信号周期），**要么原采样率是奈奎斯特率的 M 倍，降低 M 倍也不会混叠；要么先用低通滤波器削减信号防止混叠，再降采样**；这两点满足一点，也不会发生混叠。

Sampling Rate Reduction 减小采样率，实现起来很简单，周期变成 MT，$$x[n]=x[nM]$$

如果 x[n] 带宽（2$$\omega$$）小于 $$\frac{\pi}{M}$$，那么不会发生 information loss.

如果 x[n] 带宽= $$\frac{\pi}{M}$$，那么会发生 aliasing.

如果 x[n] 带宽大于 $$\frac{\pi}{M}$$，那么会发生 information loss. 可以应用低通滤波器降低频率到带宽为 $$\frac{\pi}{M}$$ 来降低损失。

如下图所示的系统叫做抽取器 decimator，先用低通滤波器压缩后再减采样的过程叫做抽取 decimaton.

![image-20241105095556692](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411050955949.png)

### 升采样 upsampling

把采样周期变为 T/L，$$x[n]=x[\frac{n}{L}]$$。一般周期用 $$\frac{MT}{L}$$ 表示，M 是降低采样率的系数，L 是提高采样率的系数。

降采样的过程类似 C/D 转换，升采样的过程就类似离散信号还原 D/C 转换。

但是升采样怎么从一个比自己频率低的离散信号中用更高频率采集出更多信息？原离散信号本身就携带这么多信息啊。所以我们只能给其中插入零值，这个过程叫做内插 interpolation。

![在这里插入图片描述](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412210844348.png)

但是这样会导致周期变大，所以要用低通滤波器滤波，去除采样信号之外的信号。

![image-20241221085028280](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412210850466.png)

如下图所示，该系统左边的部分被称为扩展器 expander. 右边的低通滤波器效果相当于离散信号重建中的理想 DC 转换器，作用是重建该序列。整体被叫做内插器 interpolator。

![image-20241105095431610](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411050954849.png)

整体如图，为了降低信息损失所以先增加频率再减少：

![image-20241105100633959](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411051006110.png)

## LTI 变换分析

### 线性时不变系统的性质

- 根据 h[n] 是否是有穷的持续时间，可分为 FIR (Finite Impulse Response) 和 IIR 系统。由此可以推出，FIR 是稳定系统；系统是因果的当且仅当 h[n] 在 n<0 处全部=0.
- H(z) 被称为系统函数 / 传递函数 System / transfer function. H(e) 是频率响应 frequency response.

### 群延时

Group Delay：
$$
\tau _g(\omega)=-\frac{d \angle H(e^{j\omega})}{d\omega}
$$
在足够小的 omega_0 范围内可以这样表示：

![image-20241114141619133](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411141416373.png)

### 理想滤波器

理想低通滤波器：

![image-20241114141805654](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411141418840.png)

理想高通滤波器：

![image-20241114141825225](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411141418446.png)

理想带通滤波器：

![image-20241114141843223](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411141418418.png)

### LCCD Equations

形如下图的公式：

![image-20241114142230823](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411141422416.png)

性质：

![image-20241114142327244](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411141423432.png)

![image-20241114142344819](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411141423022.png)

![image-20241114142357479](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411141423091.png)

![image-20241114142412666](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411141424457.png)

### 逆系统

经过一次系统 T，再经过一次其逆系统Ti，还等于原函数。

![image-20241114184919817](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411141849534.png)

![image-20241114191529766](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411141915291.png)

LTI 系统并不一定有逆；有逆的系统逆不一定唯一；Hi(z) 是唯一的但是不同的 ROC 可能产生不同的逆。

根据 $$H(z)H_i(z)=1$$ 的引理，可得知：两者 ROC 必须是非空交集，否则这个系统没有逆冲激响应。

例题：判断 Hi(z) 可能的逆系统冲击响应。

![逆系统例题](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411142224133.png)

首先，i) 不是一个有效集合，排除。

iii) 也排除，因为 iii) 的 ROC 是小于 1/6，和 H(z) 的 ROC 没有交集，这个逆系统不存在。

剩下的两个选项是可能得逆系统，用逆 z 变换求出其原式。ii) 的 ROC 是 |z|>2，casual but not stable；iv) 的 ROC 是 1/6<|z|<2，stable but not casual.

### 全通系统

形如：
$$
H_{ap}(z)=\frac{z^{-1}-a^*}{1-az^{-1}}
$$
并且其幅度值=1.

如果 z=e^w^ 是一个零点，那么z=1/e^w^\* 是其一个极点（分子分母）。**全通系统的零点和极点关于单位圆对称分布。**

![image-20241117220653701](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411172206883.png)

### 最小相位系统

Minimum Phase Systems：稳定且因果，有逆系统，也是稳定且因果的。当且仅当**其所有零点和极点都在单位圆内才会发生**。

### 频率响应补偿

DSP 处理时有时我们需要找到一个稳定因果无逆系统的逆系统，怎么办？退而求其次，不找完全的逆系统，只要其幅值乘积=1满足即可。

<img src="https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411172214485.png" alt="image-20241117221411220" style="zoom: 50%;" />

过程：

![image-20241117221546283](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411172215541.png)

![image-20241117221555656](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411172215999.png)

### 最小相位和全通分解

如果稳定因果系统 H(z) 在单位圆上没零点，它就可以拆成一个 ap 系统和一个 mp 系统的乘积。

根据之前最小相位和全通分解系统的图像特点，要把一个系统拆分为最小相位系统和全通系统，最小相位系统部分要求零极点必须全部在单位圆内；全通系统部分要求必须共轭，所有零极点关于单位圆对称。所以对于单位圆内的零极点，分配给最小相位系统；单位圆外的零极点可以复制一份单位圆内的零极点形成全通系统（例如：$$1-2z^{-1}=\frac{1-2z^{-1}}{z^{-1}-2}\cdot (z^{-1}-2)=\frac{z^{-1}-1/2}{1-\frac{1}{2}z^{-1}}\cdot (z^{-1}-2)$$），前一项是全通系统（注意幅值要化为1），后一项是最小相位系统。

![image-20241117221844867](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411172218421.png)

如果所有输入信号都会被 H(e^jw^) 延迟固定的线性相位值：

![image-20241126175720754](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411261757922.png)

那么输入信号的对称性和 transition points 都会被很好地传递给输出信号。

### Generalised Linear Phase 广义线性相位滤波器

1. 是否对称。

2. 是否可以化简为如下形式：

   ![image-20241228215223777](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412282152092.png)

   如果可以说明 General Linear.

3. A(e^jw^) 这一项是否恒>0，如果是的话 Linear Phase. 23 两条合并方能得出结论：Generalized Linear Phase Filter.

例题：textbook 5.15，判断如下系统哪些是 Generalized Linear Phase Filter。

![image-20241228215425524](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412282154739.png)

b 不对称，所以肯定不是（奇对称偶对称都可以）。

![image-20241228215552253](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412282155554.png)

Generalized Linear Phase 分为四种类型（Type I to IV）：

1. 偶对称（symmetric）且长度为奇数，形如上面例题 c。
2. 偶对称且长度为偶数，形如上题 d。
3. 奇对称（anti-symmetric）且长度为奇数，形如上题 e。
4. 奇对称且长度为偶数，形如上题 e 去掉中间点。

## 滤波器设计

之前的章节我们简单学习了一下滤波器的类型：低通，高通，带通、带阻。这章介绍更多的滤波器类型，以及他们的应用。

### 非理想滤波器

之前介绍滤波器的时候一直有一个词：ideal。什么是理想的滤波器？就是形状上真的是严丝合缝的矩形，过了 w_c 范围后频域信号幅度骤降为0.

但是现实生活中我们很难实现这种滤波器，只能说容忍一定误差范围内的滤波器图像如下：

![image-20241228220629699](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412282206918.png)

<img src="https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412282207244.png" alt="image-20241228220748916" style="zoom:67%;" />

滤波器分为两种：无限长度的 IIR 和有限长度的 FIR.

IIR 滤波器设计方式是先设计连续信号滤波器，再用 Impulse Invariance 方法或者 Bilinear Transformation 方法采样。因为连续信号处理相较于离散信号处理成熟很多，所以很多时候我们都是采用连续信号的处理方式处理。

FIR 滤波器的设计方法是用窗函数（类似于一个滤波器的滤波器）将其截断。

以及，本章还涉及 FIR 滤波器的优化。

### IIR By Impulse Invariance 脉冲响应不变设计

和之前连续信号到离散信号的采样内容一样：

![image-20241228222154265](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412282221575.png)

由于 IIR 长度无限，混叠不可避免。因此我们只能尽可能在满足滤波器设计需求的前提下，让混叠产生的影响减小。

对于最终得到的离散信号滤波器 $$H(e^{j\omega})$$，我们的需求是：

![image-20241228222345684](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412282223903.png)

*见本章开头*

因此延伸得到连续信号滤波器要满足的需求有：

![image-20241228222511232](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412282225458.png)

满足此需求后，通过 $$h_d[n]=T_d h_c(nT_d)$$ 采样获得离散滤波器的时域信号。

z 平面上的变换公式为：

![image-20241228222721738](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412282227943.png)

性质：如果原连续滤波器是稳定的，那么得到的离散滤波器也是稳定的。不稳定的连续滤波器得到的离散滤波器也是不稳定的。

**Impulse Invariance 设计法适用于低通和带通 LP & BP，不适用于高通和带阻 HP & BS 滤波器！** 因为我们知道这种处理方式对混叠处理的不好，而高通和带阻在 ±π 处都有值，一发生混叠影响特别大。所以不适用。

### IIR By Bilinear Transformation 双线变换滤波器设计

通过改变自变量 s=f(s)，z=f(z) 进行设计。

通过将 s 平面整个虚轴映射到 z 平面单位圆上避免发生混叠。我暂时不太理解。

![image-20241228224222691](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412282242001.png)

<img src="https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412282242487.png" alt="image-20241228224254149" style="zoom:50%;" />

设计流程：

![image-20241228224600650](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412282246984.png)

### FIR By Windowing 窗设计

矩形窗函数：很简单：

![image-20241228225021999](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412282250280.png)

但是这样的硬生生的截断窗设计会导致误差增加，更加得不到理想的频率响应。

矩形窗函数的频域表示：



![image-20241229003329409](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412290033669.png)

一些其他的常见窗函数：

![image-20241229004321961](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412290043188.png)

Keiser window：用于求出窗函数合适的长度和形状。

![image-20241229004517968](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412290045275.png)

广义线性相位滤波器：在 w[n] 基础上稍作改动。假设 w[n] 关于 M/2 对称，则：

![image-20241229004653872](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412290046087.png)

## 离散傅里叶变换

如果 x[n] 的持续时间为 n，我们应该可以用 n 个其傅里叶变换的形式来表示它，即：$$X(e^{j\omega_k}), k=0,1,...,N-1, \omega_k=\frac{2\pi}{N}k$$

也就是说我们可以用如图所示的近似值表示标准离散信号的傅里叶变换：

![image-20241229130910579](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412291309803.png)

这里我们给出的 x[n] 定义是只有在 0~N-1 范围内有值，或者以 N 为周期，我们只拿出 0~N-1 部分表示。

### 离散傅里叶变换性质

线性，时移性，可以看出和之前章节学的傅里叶变换性质很像。

![image-20241229131220952](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412291312188.png)

卷积性质：图中出现的卷积符号是循环卷积，大概意思是超过 0 和 N-1 的范围要 mod N 进行卷积运算。

![image-20241229131327687](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412291313016.png)

![image-20241229131503013](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412291315321.png)

帕斯维尔定理：面积相等。

![image-20241229131609755](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412291316963.png)

共轭对称性：

![image-20241229131651281](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412291316503.png)

### Overlap-Add

分段卷积：当 x[n] 的长度比 h[n] 长很多时，收集所有 x[n] 的内容与 h[n] 卷积并不现实（从计算机的角度来说，我们可能要将所有 x[n] 的内容拿到内存中与 h[n] 进行运算）。所以将 x[n] 分成 L 长度的分段，分别与 h[n] 进行卷积后求和求得 y[n] 更方便。

如果 h[n] 的长度是 P，那么每次分段卷积需要计算的长度就是 L+P-1.

![image-20241229133723791](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412291337036.png)

## DFT 相关计算

直接计算：

![image-20241229134252136](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412291342421.png)

快速傅里叶变换：利用对称性快速计算。

简单来说，比如普通傅里叶变换计算，在卷积过程中我们要用每个 X 的元素和每个 H 的元素过一遍，时间复杂度是 O(N^2^)。但是这其中出现了很多重复计算值。

快速傅里叶变换

首先我们将原傅里叶变换公式划分为奇偶两部分：

![image-20241229135638121](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412291356344.png)

即：

![image-20241229135721308](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412291357550.png)

二分后还可以进一步四分，八分……从下图中可以看出有很多计算结果不需要重复计算，可以一次计算后直接加到对应的 X[k] 处。

![image-20241229150219526](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412291502792.png)
