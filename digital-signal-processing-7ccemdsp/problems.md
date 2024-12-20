# Problems

这里记录一些历年题，课后习题等，用于应试。

## January 2022 File

1-5题：课程的第一个常见题型：判断一个系统的稳定性，因果性，线性时不变性等。

![image-20241211063225564](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412110632768.png)

1) 稳定性：假设 x[n]<=Bx，是否能找到 By 使得 y[n]<=By 有界？如果是则稳定，否则如果 y[n] 能延伸到正无穷则不稳定。

那个指数部分的模长=1，所以 $$y[n]\le1*B_x+\alpha$$，假设右边这个式子为 By 即可，说明该系统是稳定的。

2. 因果性：y[n] 只依赖于 x[n] 当前的值和 x[n-n0] 过去某一个时刻的值，不可能未卜先知需要知道 x[n+n0] 的值才能得到 y[n]，系统就是因果性的。

很明显 y[n] 式子的两个部分一个依赖于 x[n] 当前的状态，一个是常数，所以满足因果性。

3. 线性：证明 $$S\{ax1[n]+bx2[n]\}=aS\{x1[n]\}+bS\{x2[n]\}.$$ 等式左右区别是，先计算 ax1[n]+bx2[n] 的值再代入 y[n]，还是 x1[n] x2[n] 分别代入 y[n] 后再倍数求和。一个是把 y[n] 式子中 x[n] 的部分替换为 ax1[n]+bx2[n]，一个是把 y[n] 式子中 x[n] 的部分替换为 x1[n] 和 x2[n] 后，两者结果乘常数再求和，判断是否相等。

$$
a\cdot(e^{j\omega_0 n}\cdot x_1[n]+\alpha)+b\cdot(e^{j\omega_0 n}\cdot x_2[n]+\alpha)\ne e^{j\omega_0 n}(a\cdot x_1[n]+b\cdot x_2[n])+\alpha
$$

结果明显不相等，有 α 常数项。所以不是线性系统。

4. 时不变性：把 x[n]=x[n-k] 代入系统得到 y1[n] 和直接代入 n=n-k 得到 y2[n]，判断两者是否相等。明显不等（*我懒得敲公式了，如下图*）。

<img src="https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412110644858.png" alt="gpt解答" style="zoom:67%;" /> 

5. 求传递函数，也就是我们常见的 H(e) 形式。解法是对 y[n] 进行傅里叶变换，再除以 X(e)。

<img src="https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412110709522.png" alt="gpt解答" style="zoom:67%;" />

6-10题

是连续信号采样得到离散信号的部分。

![image-20241211072047573](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412110720709.png)

6. 怎样采样不发生混叠。经典奈奎斯特采样问题：采样频率要达到原信号频率2倍以上，所以角速度应当达到 2000π rad/s，周期=2π/2000π=1ms。
7. 第7题的采样频率正好是原来信号的频率。采取特定采样频率后的频域图像如下（这也有助于理解奈奎斯特采样定律）：

![image-20241211082316812](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412110823925.png)

x(e^jw^) 截取 ±π 之间的部分，就是全1的矩形函数吧。

8. 
