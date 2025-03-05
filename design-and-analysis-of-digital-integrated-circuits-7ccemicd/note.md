# Preface

今年学期都过半了，3月才开始记笔记。之前记了3周左右，但是电脑被偷了，我还没有及时上传到 gitbook 里，凉凉。

由于明天有实验，所以决定先从这门课开始补吧。

# 介绍

摩尔定律：芯片上的晶体管数量每18~24个月翻一番。但是增长速度现在已经逐渐放缓了，芯片的功耗是一个主要问题，晶体管太密了，power density is too high，导致芯片难以保持低温。

而且芯片上的晶体管数量增加，设计难度也在增加，可以通过抽象层次来提升设计效率。

![image-20250303224841029](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202503032248204.png)

# Digital design 的设计指标

芯片的设计指标有很多，诸如：成本，良率，性能等。

Yield: 芯片制作时，是用一块圆形晶圆切割得到的。晶圆上可能有瑕疵，所以芯片体积越小，不仅产量越高，良率也会越高，因为没有瑕疵的小芯片更多。

![image-20250303231126005](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202503032311037.png)

Cost: 随着摩尔定律的发展，晶体管体积逐渐减小，成本也大致随着体积减小而下降。不过晶体管体积小于28nm后成本下降速度减慢。

Reliability: 现实世界的真实信号是模拟的 analog，不像数字有准确的数值。比如对于下面这个反相器 CMOS，理想状态下我们希望输入电压一旦超过 VDD/2，输出就降为0. 但是真实情况下的输出电压做不到骤降的。

![image-20250303231735291](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202503032317380.png)

![image-20250303231746762](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202503032317804.png)

那么我们就要制定一系列的规范，到底什么值的电压输出视作“高电平”，什么值视作“低电平”？什么值范围内的输入电平有效，什么值范围内算作 noise? 

如下图。输出电压的 VOH VOL 是输出高/低电平，只有大于 VOH 或者小于 VOL 的输出电压才视作有效。

VIH VIL 则是电压曲线中变化斜率=-1的两个点，输入电压小于 VIL 视作“令输出电压为高电平”的输入值，大于 VIH 视作“令输出电压为低电平”的输入值。

Negative gain 点，或者说 VM 点，是图像与 Vout=Vin 直线的交点。

![image-20250303231907797](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202503032319926.png)

制定了这些标准后，就可以用一个指标来衡量此电路的可靠性：noise margin 噪声边界。
$$
NM_H=V_{OH}-V_{IH}\\
NM_L=V_{IL}-V_{OL}\\
$$
计算方法反正只要记住 noise margin high 和 noise margin low 都是 >0 的就行。

Regenerative Property 再生性：再生性质指的是信号通过每个级别的处理后，逐渐稳定并恢复到标准的逻辑电平的能力。

多个反相器串联，可以让输入信号切换更明显，高低电平界线更分明。

![image-20250303232933221](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202503032329274.png)

下图是再生和非再生电路的电压曲线对比，再生电路在中间的不确定区域下降速度更快，停留更短。

![image-20250303233029193](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202503032330244.png)

## Delay

输入信号到输出的延迟。注意下图中的命名，tpHL 指的是反相器输出电压 High to Low 的时延，而不是输入电压 High to Low.

![image-20250304163824314](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202503041638536.png)

下面是一个一阶导 RC 电路，输入电压阶跃升高给电容充电，tp 是电压达到一半的时间：

![image-20250304164426086](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202503041644148.png)

对于一阶 RC 电路，其 $$t_{pHL}=0.69RC.$$

## Power and Energy

电压计算公式简单说就是 VI 求积分：
$$
Pave=\frac{1}{T}\int^{t+\tau}_{t}p(t)dt
$$
$$E=P_{av}t$$，Energy 也叫 Power-Delay Product

Energy-Delay Product (EDP) 能量延迟积 =Et，是一个能同时衡量功耗和时延的指标。

一阶 RC 电路电压从0到最大值 Vdd 的过程中，整个电路消耗的能量和电容器消耗的能量计算方式如下：

![image-20250305111829667](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202503051118768.png)

# Layouts and Design rules 设计原则

以一个 CMOS 举例，设计原则中主要考虑俯视图的 xy 维度，也就是 CMOS 的宽度和长度。厚度不作为考虑因素：

![image-20250305112331112](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202503051123186.png)

图中可以看出，W 是源极，漏极，栅极共有的宽度值，L 则是三者的长度相加。一个反相器 CMOS 的图像大致如下，注意层级关系：

![image-20250305112511552](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202503051125601.png)

对于不同材质，可能设计原则的长度宽度范围，以及和其他材料之间的间距范围都不同。

晶体管 transistor：一个理想的，忽略 MOS 非理想二阶导的“开关”，一样是通过 Gate 控制源极和漏极的联通。

NMOS 晶体管 Gate 高电平（达到一定值）时导通；PMOS 晶体管 Gate 低电平时导通。合而为之可以制作出如下图所示的反相器，PMOS 相较 NMOS 多一个圆圈代表取反：

![image-20250305113059636](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202503051130675.png)

如果给定一个有 CL 的电容，在其前面串联多少个反相器可以最小化 delay？以及，每个 inverter 的 size 应该是多少？

![image-20250305114222053](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202503051142105.png)

对于 inverter，其延迟计算公式如下：
$$
t_{pHL}=(ln2)R_NC_L\\
t_{pLH}=(ln2)R_PC_L
$$
也很好理解，因为（反相器输出）高电平到低电平是 NMOS 导通的过程，低电平到高电平是 PMOS 导通的过程。

一般将 W_p 宽度设置为2倍的 W_n，使得上拉和下拉电流相同，R_N 近似=R_P，t_pHL 近似等于 t_pLH（rule of thumb）。

$$t_p=(ln2)\frac{R_{inv}}{W}C_L$$，其中 Rinv 指的是单位面积的 MOS 的电阻，因为电阻和宽度成反比，所以整个 MOS 的电阻=$$\frac{R_{inv}}{W}$$.

$$C_{in}=WC_{ginv}=W(3C_G)$$，反相器的等效电容。$$C_{ginv}$$ 是整个 CMOS 的单位面积电容，$$C_G$$ 是一个 MOS 的单位栅极电容，我们知道 PMOS 的宽度是 2W，NMOS 是 W，以此来计算。

整体延迟计算公式如下：
$$
\begin{aligned}
t_p&=kR_W(C_{int}+C_L)\\
&=kR_WC_{in}(\frac{C_{int}}{C_{in}}+\frac{C_{L}}{C_{in}})\\
&=t_{inv}(\gamma+f)
\end{aligned}
$$
其中，$$C_{in}$$ 指的是单位面积 MOS 的电容（输入电容），所以 $$t_{inv}$$ 和栅极的 size 无关。

γ 是内部电容相对于输入电容的比例，而对于一个 CMOS inverter 的电路来说，$$C_{int}=C_{in},\ \gamma=1$$。

f 是扇入扇出因子，负载电容相对于输入电容的比例。