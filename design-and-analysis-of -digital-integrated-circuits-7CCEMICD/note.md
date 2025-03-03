# Preface

今年学期都过半了，3月才开始记笔记。之前记了3周左右，但是电脑被偷了，我还没有及时上传到 gitbook 里，凉凉。

由于明天有实验，所以决定先从这门课开始补吧。

# 介绍

摩尔定律：芯片上的晶体管数量每18~24个月翻一番。但是增长速度现在已经逐渐放缓了，芯片的功耗是一个主要问题，晶体管太密了，power density is too high，导致芯片难以保持低温。

而且芯片上的晶体管数量增加，设计难度也在增加，可以通过抽象层次来提升设计效率。

![image-20250303224841029](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202503032248204.png)

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