## 前言

项目 project: 简单来说就是一部分人，为了一个共同的目标，利用有限的时间和其他资源制定计划来达到目标。

It is a piece of planned work completed over a period of time or an activity that is and intended to achieve a particular purpose.

程序 Program：关联多个项目来达到大目标，可能涉及到不同领域的项目，比如造一个飞机，要审批，竞标，科研，生产等等。项目的结果可能更加注重成品，而程序的结果注重多个项目的效益（除了成品，还有花费的时间金钱等）。

Project Structure, work package, task, activity 是逐步细化的概念。比如 project structure 是“后端开发”，work package是“设计后端数据库”，task是“设计数据库接口”，activity是“编写单元测试代码”。

project和business operations的区别在于introduces business change.

## 项目模型

### Waterfall 瀑布模型

瀑布模型的特点在于专门化，每个阶段都只基于之前的阶段，考虑这个阶段的任务（因果性？）。

<img src="https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410032132696.png" alt="image-20241003213207578" style="zoom:67%;" />

### V 模型

也叫 Verification and Validation 验证确认模型，客户的最终反馈可以让我们反过来从头修改迭代计划。

![image-20241003213350532](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410032133598.png)

### Agile 敏捷开发模型

持续集成/持续交付（CI/CD）。rapid delivery

打个比方，瀑布模型可能是做一道菜，我先准备食材，下锅，加调料，炒完出锅再给客户品尝，客户才能反馈做得如何。敏捷开发可以拆成一些小任务持续地交付，比如煮一点，尝一口，看看咸淡，及时调整。不需要整个大项目组一起做几个月做出全部成果再等反馈。

![image-20241003213541417](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410032135489.png)

## 项目管理概述

### 基本概念

Project Management: Project Management (PM): is the Application of knowledge, skills,  tools and techniques to the project activities in order to meet stakeholders needs and expectations from the project. 利用所学知识管理项目来达到预期结果。

- Bid Manager 投标经理：主要协调客户和项目组，制定工作计划和提案达到客户预期。
- Project Manager 项目经理：主要管他负责的一块进度。

Project Management Context：为了完成项目需求的一系列活动，包括 initiating, planning, organizing, executing, monitoring  and controlling the project activities （启动，计划，组织，执行，监控）

Project Life Cycle (PLC)：项目生命周期。定义了项目运行过程中的不同阶段 distinct phases，这些阶段需要哪些人，花多长时间。

比如瀑布模型，大致分为：

1. 初始化阶段，分析客户需求，研究可行性。
2. 计划阶段，选择合适的人，制定计划。
3. 执行和交付阶段，下达指令，监控执行情况，提出新方案，发给客户。

### 技术对项目管理的促进

技术指的是科技产物，比如有形的工具（计算机），无形的软件，算法等。

### 成熟度

Readiness Level 是衡量项目的指标之一。

- Customer Readiness Level：比如低成熟度，用户需要自己百度才能用明白对方的产品。高成熟度，产品非常好懂，易于操作。
- Business Readiness Level：市场需求，是否可扩展到其他项目。
- Technology Readiness Level：从简单的技术概念，到可交付的系统。

随着项目发展，成熟度会越来越高，比如项目前期可能会提出一些新技术概念，项目后期新概念经过多次迭代后已经成熟许多。

### Bid & Proposal B&P 投标提案

向客户证明：我们有能力能完成你的目标，我们的初步计划，公司价值等。

在提案开始的过程中会进行两个操作（**PROSPECT PHASE**）：

- Horizon Scanning：对新兴技术和威胁的早期检测评估。Aims to spot changes in the world, so that we can plan on how to  exploit these changes
- Technology Watch：获取有用信息用于制定策略。Systematic process of capturing, analysing and exploiting useful  information for strategic decision making in the company

招标方会发布 Request For Proposal （RFP）由招标方发布，发布自己的需求，让感兴趣的投标方提供解决方案，报价等。

### Sources of Project Initiation 项目启动来源

- **客户请求 (Customer Requests)**: 基于客户的具体需求启动项目。
- **高层管理指令 (Top Management Directives)**: 由战略决策推动的新项目。
- **已有系统（Existing systems）：**进一步迭代。
- **外部因素 (External Factors)**: 市场趋势、新技术或监管变化促发项目创意。

###  Project Organization Structure 项目组织结构

项目组织是项目和上级组织之间的中间者 Project organisation is defined as the interface  between the project and its parent organisation.

| 组织类型                                         | 描述                                                         | 优点                               | 缺点                                                     |
| ------------------------------------------------ | ------------------------------------------------------------ | ---------------------------------- | -------------------------------------------------------- |
| Functional Organisation 职能组织                 | 管理特定职能，如研发，市场，HR等。项目经理通常是其中的成员，由职能部门经理控制该职能。 | 资源利用率高；同专业人员沟通方便   | 跨部门沟通困难；过度关注自身目标可能偏离项目目标         |
| Pure Project Organisation 纯项目组织             | 每个项目有独立的组织实体；项目经理控制整个项目；团队成员不受其他组织影响 | 减少层级审批，效率高；大家目标一致 | 可能导致资源浪费（每个项目都是独立团队，行政管理成本大） |
| Matrix Organisation 矩阵组织                     | 结合两者，在不同项目间共享人力物资等资源                     | 有效利用资源，平衡目标             | 可能权责不清，沟通不便；决策效率降低                     |
| Collaborative Projects Organisation 合作项目组织 | 项目成员分布在不同地点甚至国家                               | 融会贯通，促进学习创新，扩展视野   | 沟通交流可能存在问题；知识产权界限                       |

## Stakeholders 股东

股东可以影响项目 having potential influence on the project

但是只有内部股东需要担责 Only Internal stakeholders are responsible/accountable  towards the project.

### 两种重要的股东

- 赞助者 sponsors / customers: 拥有项目，能管理项目，能提供资源给项目（比如资金，技术）。**top level management**

- 使用者 users

![image-20241011132016636](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410111320043.png)

在项目过程中，首先我们需要 identify stakeholders，因为这些人会制定一些需求，项目最终目标就是满足他们的这些需求。同时项目过程中缺什么资源也可以和他们要。

![image-20241011132322857](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410111323177.png)

methodology（制定需求）-> capture requirements（实现需求）-> consolodate requirements（评估结果）

### capture requirements

Validation: Checks the proposed concept/solution  stakeholders’ requirements  **against the  and needs** 确保股东需求能实现

Verification：Check the implemented solution (prototype/service) **meet  design specifications** 验证股东的需求如何实现

Performance:  **meet certain  performance (KPI) characteristics** 评估结果

### Categorisation of Stakeholders and Engagement

然后需要对**股东**进行优先级排序，判断谁说的话更有分量。

Stakeholder Power-Interest Matrix: 根据功能和股东兴趣两个维度制定优先级。

![image-20241011140933227](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410111409382.png)

Salience Model:  power, legitimacy, urgency 三个维度。（权力，比如我能给更多的钱，更能影响项目；权威，比如项目发起人，或者某些价值观的代表者；紧急性，比如我对这个项目的需求很急）

![image-20241011141649633](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410111416805.png)

Dormant stakeholders 休眠股东: no need for major communication，给钱就完事了，少交流。

Discretionary stakeholders 可自由支配的股东：regular project updates . 也不需要过多交流，给他们项目更新进度就行。

Demanding stakeholders 需求股东：Only keep them informed，他们比较急。

Dominant stakeholders主要股东：consider their communication and their involvement **needs at all times** 

Dangerous stakeholders 危险股东：有钱有权，Must meet their needs.

Dependent stakeholders 相关股东：Keep them informed when I need their resources

Definitive stakeholders 明确股东：Always keep them informed, satisfied and involved。

### Monitoring

股东部分我们就先不讲怎么实现项目了，直接讲到如何监控评估股东：

![image-20241011144022366](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410111440485.png)

**Communicate with key stakeholders to  discover and manage their expectations upfront and during the project.**

## PROJECT TEAMS 项目团队

![image-20241011144423888](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410111444012.png)

核心执行团队： conducting the works on a continuous basis, and are required for decision making 持续工作，以及做决定。

项目团队：贡献自己的部分，比如技术，人力。

项目支持团队：支持核心团队。

Characteristics of good team members:

- Credible and possess a high level of technical skill 技术能力强
- Resilient to pressures 抗压能力强
- Have an interest and ability in solving problems 解决问题兴趣高
- Should be robust 够强壮？？
- Should have a strong result/goal orientation 目标性强

##  BID / PROJECT MANAGER

Bid Manger：做计划，拉人组建团队， 筹备资源，在项目执行中确保足够的细节等等。

Project Manager：执行，监控，控制（可能还会改团队人员或者计划），报告（和 top management, 各个功能部门，other stakeholders）等等。
