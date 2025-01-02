# Problems

这里记录一些历年题，课后习题等，用于应试。

## January 2022 File

### 1-5题

课程的第一个常见题型：判断一个系统的稳定性，因果性，线性时不变性等。

![January 2022 q1-5](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412110632768.png)

1) 稳定性：假设 x[n]<=Bx，是否能找到 By 使得 y[n]<=By 有界？如果是则稳定，否则如果 y[n] 能延伸到正无穷则不稳定。

​	那个指数部分的模长=1，所以 $$y[n]\le1*B_x+\alpha$$，假设右边这个式子为 By 即可，说明该系统是稳定的。

2. 因果性：y[n] 只依赖于 x[n] 当前的值和 x[n-n0] 过去某一个时刻的值，不可能未卜先知需要知道 x[n+n0] 的值才能得到 y[n]，系统就是因果性的。

​	很明显 y[n] 式子的两个部分一个依赖于 x[n] 当前的状态，一个是常数，所以满足因果性。

3. 线性：证明 $$S\{ax1[n]+bx2[n]\}=aS\{x1[n]\}+bS\{x2[n]\}.$$ 

   等式左右区别是，先计算 ax1[n]+bx2[n] 的值再代入 y[n]，还是 x1[n] x2[n] 分别代入 y[n] 后再倍数求和。一个是把 y[n] 式子中 x[n] 的部分替换为 ax1[n]+bx2[n]，一个是把 y[n] 式子中 x[n] 的部分替换为 x1[n] 和 x2[n] 后，两者结果乘常数再求和，判断是否相等。

$$
a\cdot(e^{j\omega_0 n}\cdot x_1[n]+\alpha)+b\cdot(e^{j\omega_0 n}\cdot x_2[n]+\alpha)\ne e^{j\omega_0 n}(a\cdot x_1[n]+b\cdot x_2[n])+\alpha
$$

​	结果明显不相等，有 α 常数项。所以不是线性系统。

4. 时不变性：把 x[n]=x[n-k] 代入系统得到 y1[n] 和直接代入 n=n-k 得到 y2[n]，判断两者是否相等。明显不等（*我懒得敲公式了，如下图*）。

<img src="https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412110644858.png" alt="gpt解答" style="zoom:67%;" /> 

5. 求传递函数，也就是我们常见的 H(e) 形式。解法是对 y[n] 进行傅里叶变换，再除以 X(e)。

<img src="https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412110709522.png" alt="gpt解答" style="zoom:67%;" />

### 6-8题

是连续信号采样得到离散信号的题型。

![January 2022 q6-8](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412110720709.png)

6. 怎样采样不发生混叠。经典奈奎斯特采样问题：采样频率要达到原信号频率2倍以上，所以角速度应当达到 2000π rad/s，周期=2π/2000π=1ms。
7. 第7题的采样频率正好是原来信号的频率。采取特定采样频率后的频域图像如下（这也有助于理解奈奎斯特采样定律）：

![ ](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202501021705118.png)

x(e^jw^) 截取 ±π 之间的部分，就是全1的矩形函数吧。

8. 首先系统处理得到：$$Y(e^{j\omega})=500e^{-j\omega}$$，范围是 -pi/2 到 pi/2.

   然后还原到连续信号：$$Y(j\Omega)=e^{-j\Omega}$$，范围是 -250pi 到 250pi。

   最后用公式求反傅里叶变换：
   $$
   \begin{align}
   y(t)&=\frac{1}{2\pi}\int^{\infty}_{-\infty}Y(j\Omega)e^{j\Omega t}d\Omega\\
   &=\frac{1}{2\pi}\int^{250\pi}_{-250\pi}e^{-j\Omega}\cdot e^{j\Omega t}d\Omega\\
   &=\frac{1}{2\pi}\int^{250\pi}_{-250\pi}e^{j\Omega (t-1)}d\Omega\\
   &=\frac{1}{2j\pi\cdot (t-1)}\cdot e^{j\Omega (t-1)}\vert^{250\pi}_{\Omega=-250\pi}\\
   &=\frac{1}{2j\pi\cdot (t-1)}\cdot (e^{j\cdot 250\pi \cdot(t-1)}-e^{-j\cdot 250\pi \cdot(t-1)})\\
   &=\frac{1}{2j\pi\cdot (t-1)}\cdot [2j\cdot 250\pi \cdot sin((t-1))]\\
   &=\frac{sin(250\pi(t-1))}{\pi(t-1)}
   \end{align}
   $$
   

其中用到了一个公式：$$e^{j\omega}-e^{-j\omega}=2jsin\theta$$

*有点难，希望不是我做错了*

### 9-11题

![January 2022 q9-11](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202501021743100.png)

先求出 H(z)
$$
Y(z)=X(z)-z^{-1}X(z)+\frac{5}{6}z^{-1}Y(z)-\frac{1}{6}z^{-2}Y(z)\\
H(z)=\frac{Y(z)}{X(z)}=\frac{1-z^{-1}}{1-\frac{5}{6}z^{-1}+\frac{1}{6}z^{-2}}=\frac{1-z^{-1}}{(1-\frac{1}{2}z^{-1})(1-\frac{1}{3}z^{-1})}
$$
系统是因果的所以推断出 ROC 延伸到正无穷，ROC 是 |z|>1/2

9. 逆系统：$$\frac{(1-\frac{1}{2}z^{-1})(1-\frac{1}{3}z^{-1})}{1-z^{-1}}$$，极点在单位圆上所以不稳定。

10. ROC |z|>1 即可。
    $$
    H(z)=\frac{(1-\frac{1}{2}z^{-1})(1-\frac{1}{3}z^{-1})}{1-z^{-1}}\\
    =-\frac{1}{6}z^{-1}+\frac{2}{3}+\frac{\frac{1}{3}}{1-z^{-1}},\ ROC:\ |z|>1\\
    h[n]=-\frac{1}{6}\delta[n-1]+\frac{2}{3}\delta[n]+\frac{1}{3}u[n]
    $$
    

11. 不唯一。因为其逆系统只要和原系统有交集就行，|z|<1 和 |z|>1 都和 |z|>1/2 有交集。
    $$
    h_1[n]=-\frac{1}{6}\delta[n-1]+\frac{2}{3}\delta[n]+\frac{1}{3}(-1)^nu[-n-1]
    $$

### 12-14题

![January 2022 q12-14](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202501021759380.png)

12. 想不发生混叠的话，最小长度应该是 L1+L2-1，也就是3+3-1=5.

13. 线性卷积的范围是 $$n∈[n_{1min}+n_{2min},n_{1max}+n_{2max}]=[2+0,4+2]=[2,6].$$

14. 对于 c 中所给数据部分：可以用卷积公式直接计算：
    $$
    x[n]=\sum^{+\infty}_{k=-\infty}x_1[k]x_2[n-k]
    $$
    代入计算即可。x[2]到x[6]的值分别是{4, 8, 7, 4, 1}。

    $$\tilde{x}[0]\ \tilde{x}[1]$$ 是周期性循环的 x[5] 和 x[6] 的值，所以 $$\tilde{x}[n]$$ 从 0 到 4 的值分别是 {4, 1, 4, 8, 7}.

*这道题其实我不完全理解，不过看着gpt做的挺对的。*

## January 2023 File

### 第3题

![January 2023 3](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412301701649.png)

也是第五章常出现的问题。判断 stable 我不太确定，因为我做题的时候不怎么遇到极点在1上的情况，我不知道极点在1上的话算不算 stable。

![ ](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412301701925.jpg)

## January 2024 File

### 第1题

![January 2024 q1](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412301213344.png)

![January 2024 q1](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412301214980.png)

如果我到现在为止没理解错的话：

- $$X(j\Omega)$$ 表示的是连续信号 x(t) 的傅里叶变换；$$X(e^{j\omega})$$ 表示的是离散信号 x[n] 的傅里叶变换。
- 采样后傅里叶变换的图像变化：$$\omega=\Omega T$$，幅度值变为原幅度值/T. 考虑混叠情况后最终只保留 ±π 范围内的图像。
- 恢复采样过程相反。

a) 和 January 2022 6-8 有点相似。首先我们计算不会发生混叠的奈奎斯特采样周期：$$\frac{2\pi}{2\Omega_N}=1ms$$，正好=T1，也就是说采样后的频域图像正好不发生混叠，一个个三角形紧挨着。

c) 和 January 2022 7又一样。

b) d) 先与 $$H(e^{j\omega})$$ 相乘后还原信号。

![](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202501021600046.jpg)

### 第2题

![January 2024 q2](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412302119995.png)

a) 逆系统就是求倒数。

b) ROC 根据因果性，以及正逆系统 ROC 有交集判断，求 h[n]。

c) 求出逆系统的 ROC 范围并确定是否包含单位圆。

d) ROC 包含单位圆和正无穷的逆系统。

这道题我不太确定

![ ](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412310428528.jpg)

### 第3题

![January 2024 q3](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412301659953.png)

第五章经常出现的题型。

![ ](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412301659281.jpg)

### 第4题

![January 2024 q4](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412301700982.png)

求 DFT 的知识点。

![](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412301700421.jpg)
