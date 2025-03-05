# Sensors and Actuators

# Introduction

传感器：接受信号转换为电信号（比如图像通过摄像头转化为电信号）进行处理。

执行器：执行动作，如驱动电机。

estimation：传感器接收到的可能并不是我们想要的数值，需要模型转换；或者传感器精度不高存在误差，所以 estimation 估计十分重要。

两个 error：model error（来自所选模型，类似 AI 中的 bias 概念吧）和 measurement error（来自测量误差）。

常用术语：

- plant / process：要控制的系统。
- inputs outputs
- controller：产生控制信号的设备
- control law：控制信号产生的方案
- control system：至少包含 controller 和 plant
- feedback control：有反馈控制
- open-loop control：无反馈控制

## 衡量系统性能的参数

- speed of performance
- stability
- accuracy

两个参数分类：

- static：静态参数，工程实践中常用，比如精准度，测量范围等。
- dynamic：动态参数，根据工程理论定义，通常描述设备在变化条件下的行为，比如阻尼比、自然频率、响应时间等。

对于动态类参数，一般会用时域微分方程动态模型 differential-equation 和频域传递函数动态模型 transfer-function。其中常用两种模型：一阶导模型和二阶导模型（简单震荡器模型 simple oscillator）（我猜这两个模型就是考试重点）。

时域的动态参数比如上升时间 rise time，峰值时间 peak time，下降时间 settling time，百分比过冲 percent overshot 等。

频域动态参数比如带宽 bandwidth，静态增益 static gain，谐振频率 resonant frequency，共振幅度 magnitude at resonance，阻抗 impedances，增益裕度 gain margin，相位裕度 phase margin 等。

## 动态模型

一阶导模型：
$$
\tau \dot y +y=ku
$$
τ：时间常数

k：dc 增益

y：输出

u：输入

拉普拉斯变换后的传递函数：
$$
\frac{Y(s)}{U(s)}=H(s)=\frac{k}{\tau s+1}
$$
二阶导模型：
$$
\ddot y+2\zeta ω_n\dot y+ω_n^2y=ω_n^2u(t)
$$
ζ：阻尼比 damping ratio，描述系统振荡受到扰动 disturbance 后如何衰减的无量纲测量。

*阻尼是减少系统震荡冲击的机制，通过吸收能量来保证系统的稳定性和安全性。*

传递函数：
$$
\frac{Y(s)}{U(s)}=H(s)=[\frac{w^2_n}{s^2+2\zeta \omega_n s+\omega^2_n}]
$$
图像如下。还有一些需要了解的概念：

rise time：系统初次达到稳定状态值 steady-state value 所用时间，图中稳定状态值为1.0，用时 T_r.

Modified rise time：系统初次达到 90% 稳态值的时间，T_rd.

Delay time：达到 50% 稳态值的用时。T_d.

Peak Time：达到第一个峰值的用时。T_p.

Settling Time：系统稳定在稳态值的一定百分比范围内（通常是2%）所用时间。T_s，这个时候我们可以说系统达到稳定 stability 了。

Percentage Overshoot：超调，即系统的状态超过稳定值。图中震荡状态离稳态距离最远的一次震荡占稳态的百分比。

Steady-State Error：期望稳态值和实际稳态值之间的偏差。

![image-20250116194303741](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202501161943815.png)

![image-20250116201529216](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202501162015263.png)

传感器频率应当比信号频率快4倍（最好10倍）以上才可以精准测量。

例题1：运用了传感器频率应当高10倍以及计算时间常数的公式。

![image-20250116201349696](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202501162013749.png)

例题2：这道题用到了车辆四分之一模型，二阶导模型原式，还有 PO 和 ζ 的转换公式（红框上面那个）。

![image-20250116201840671](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202501162018745.png)

![image-20250116201856403](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202501162018480.png)

## Frequency-Domain Specifications

用频域的一些方法评估传感器性能。

Gain 增益：输出信号振幅和原信号之间的比率。

Phase angle 相位角：输出信号相对原信号滞后或提前。

对于简单振幅系统，增益最大时相应频率 $\omega_r=\sqrt{1-2\zeta^2}\omega_n,\ zeta \le\frac{1}{\sqrt{2}}$。当 $\omega = \omega_n$ 时，Gain=1/(2ζ)，phase lead=-π/2.

## Linear and Non-linear system

可以用线性微分方程建模的系统是线性系统，满足类似 T{ax1+bx2}=ay1+by2 的线性性质。

非线性系统通常有如下两个重要性质：

- **Saturation 饱和**：如下图上部分。
- **Dead zone 死区**：如下图下部分，系统对激励没有响应的部分。

![image-20250117054634026](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202501170546165.png)

**迟滞（Hysteresis）**：输入输出曲线随着输入方向变化而改变。

![image-20250117054852748](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202501170548822.png)

**Frequency Creation**：线性系统稳定状态下会产生和正弦激励同频的输出，而非线性系统可能会产生新的频率。

![image-20250117055238782](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202501170552873.png)

这道题比前两道简单一些。给定公式：
$$
\left(\frac{dy}{dt}\right)^{1/2} = u(t)
$$
证明该非线性系统输出产生了新的频率分量，即 **frequency creation**。公式还原后代入线性的输入信号求输出。

为了缓解非线性问题，可以采取如下预防措施：

- 避免在大范围的信号电平上操作设备（wide range of signal levels inputs）。
- 避免宽频带操作（wide frequency band）。
- 使用不会产生大机械运动的设备（large mechanical motions）。
- 尽量减少库伦摩擦和粘滞，比如使用润滑剂（coulomb friction and stiction, e.g., using proper lubrication）。
- 避免松动的接头和齿轮联轴器，即使用直接驱动结构（loose joints and gear coupling, i.e., using direct-drive mechanisms）。
- 尽量减少对不良影响的敏感性（sensitivity to undesirable influences）。
- 减少损耗（wear and tear）。

## 仪器性能参数

### 1. 灵敏度（Sensitivity）

仪器对输入信号变化的响应程度。具体来说，它是输出信号相对于输入信号变化的比率。

灵敏度通常通过改变输入并观察输出的变化来测量，可以用单位输出变化/单位输入来表达（例如，伏特/卢克斯，牛顿/米）。

下题中，设备整体的灵敏度 = 数字输出精度 / 光信号输入精度；单独对于 ADC 来说的敏感度 = 数字输出精度 / 电信号精度。

![image-20250117073924541](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202501170739747.png)

### 2. 信噪比（Signal-to-Noise Ratio, SNR）

测量信号强度与背景噪声强度的比例，通常以分贝（dB）表示。
$$
SNR (dB) = 20 \times \log_{10}(\frac{P_{signal}}{P_{noise}})
$$
，>=10 最佳。

![image-20250117075930787](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202501170759010.png)

### 3. 动态范围（Dynamic Range）

仪器可以测量的最小值和最大值之间的比率，表明了仪器能处理的最弱和最强信号的范围。
$$
Dynamic\ range = 20\log_{10}[\frac{Range\ of\ operation}{Resolution}] = \frac{\gamma_{max}-\gamma_{min}}{\delta \gamma}
$$

### 4. 分辨率（Resolution）

仪器能够区分的最小的输入信号变化，是衡量仪器精密度的重要指标。

![image-20250117075117866](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202501170751173.png)

### 5. 偏置（Offset, Bias）

仪器的零点偏移，需要校准来修正。

![image-20250117080624488](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202501170806728.png)

### 6. 静态校准曲线（Static Calibration Curve）

稳态条件下输出随着输入的变化。

![image-20250117080855613](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202501170808710.png)

### 7. 漂移（Drift）

- **零点漂移（Zero Drift）**：在没有输入信号时，仪器输出随时间发生的变化。
- **全量程漂移（Full-Scale Drift）**：在最大输入信号下，输出随时间的最大变化。

### 8. 频率特性

- **有用频率范围（Useful Frequency Range）**： 增益稳定，相位角接近 0 的有效工作范围，一般是信号主频率的一部分（如 1/2 或 1/5）。
- **带宽（Bandwidth）**：仪器可以有效响应的最大范围和响应速度，应当为信号主频率的兴趣点（interest）的几倍。