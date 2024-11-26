## 前言

项目 project: 简单来说就是一部分人，为了一个共同的目标，利用有限的时间和其他资源制定计划来达到目标。

It is a piece of planned work completed over a period of time or an activity that is and intended to achieve a particular purpose.

程序 Program：关联多个项目来达到大目标，可能涉及到不同领域的项目，比如造一个飞机，要审批，竞标，科研，生产等等。项目的结果可能更加注重成品，而程序的结果注重多个项目的效益（除了成品，还有花费的时间金钱等）。

Project Structure, work package, task, activity 是逐步细化的概念。比如 project structure 是“后端开发”，work package 是“设计后端数据库”，task 是“设计数据库接口”，activity是“编写单元测试代码”。

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
- Technology Readiness Level TRL：从简单的技术概念，到可交付的系统。

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

## 项目人员组成

### Stakeholders 股东

股东可以影响项目 having potential influence on the project

但是只有内部股东需要担责 Only Internal stakeholders are responsible/accountable  towards the project.

**两种重要的股东**：

- 赞助者 sponsors / customers: 拥有项目，能管理项目，能提供资源给项目（比如资金，技术）。**top level management**

- 使用者 users

![image-20241011132016636](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410111320043.png)

在项目过程中，首先我们需要 identify stakeholders，因为这些人会制定一些需求，项目最终目标就是满足他们的这些需求。同时项目过程中缺什么资源也可以和他们要。

![image-20241011132322857](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410111323177.png)

methodology（制定需求）-> capture requirements（实现需求）-> consolodate requirements（评估结果）

#### capture requirements 实现股东需求

Validation: Checks the proposed concept/solution  stakeholders’ requirements  **against the  and needs** 确保股东需求能实现

Verification：Check the implemented solution (prototype/service) **meet  design specifications** 验证股东的需求如何实现

Performance:  **meet certain  performance (KPI) characteristics** 评估结果

#### Categorisation of Stakeholders and Engagement 股东分类

然后需要对**股东**进行优先级排序，判断谁说的话更有分量。主要有两种分类方式：

Stakeholder Power-Interest Matrix: 根据功能和股东兴趣两个维度制定优先级。

![image-20241011140933227](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410111409382.png)

Salience Model:  power, legitimacy, urgency 三个维度。（权力，比如我能给更多的钱，更能影响项目；权威，比如项目发起人，或者某些价值观的代表者；紧急性，比如我对这个项目的需求很急）

![image-20241011141649633](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410111416805.png)

- Dormant stakeholders 休眠股东: no need for major communication，给钱就完事了，少交流。
- Discretionary stakeholders 可自由支配的股东：regular project updates . 也不需要过多交流，给他们项目更新进度就行。
- Demanding stakeholders 需求股东：Only keep them informed，他们比较急。
- Dominant stakeholders主要股东：consider their communication and their involvement **needs at all times** 
- Dangerous stakeholders 危险股东：有钱有权，Must meet their needs.
- Dependent stakeholders 相关股东：Keep them informed when I need their resources
- Definitive stakeholders 明确股东：Always keep them informed, satisfied and involved。

#### Monitoring 评估股东

股东部分我们就先不讲怎么实现项目了，直接讲到如何监控评估股东：

![image-20241011144022366](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410111440485.png)

**Communicate with key stakeholders to  discover and manage their expectations upfront and during the project.**

### Project Teams 项目团队

![image-20241011144423888](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410111444012.png)

核心执行团队： conducting the works on a continuous basis, and are required for decision making 负责持续工作，以及下决定。

项目团队：负责贡献自己的部分，比如技术，人力。

项目支持团队：负责支持核心团队。

Characteristics of good team members:

- Credible and possess a high level of technical skill 技术能力强
- Resilient to pressures 抗压能力强
- Have an interest and ability in solving problems 解决问题兴趣高
- Should be robust 够强壮？？
- Should have a strong result/goal orientation 目标性强

###  Bid / Project Manager 投标经理 / 项目经理

Bid Manger：做计划，拉人组建团队， 筹备资源，在项目执行中确保足够的细节等等。

Project Manager：执行，监控，控制（可能还会改团队人员或者计划），报告（和 top management, 各个功能部门，other stakeholders）等等。

## Managing Bid & Proposal 标书管理

主要目的是创建优的投标提案，满足公司和客户需求。

标书管理阶段和项目管理阶段关联紧密，比如对项目的组织规划，风险管理，各个阶段的评审等。

整体结构图如下：

![image-20241103131320088](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411031313153.png)

### Prospect Phase 前景阶段

调研现有市场数据进行分析（如竞品分析），评估**是否值得为某个项目准备投标**。

![image-20241018132641835](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410181326926.png)

### Project Evaluation & Selection 项目评估选择

可能有很多值得公司做的项目，但不同项目之间要竞争资源，所以不可能所有项目都做，要选择项目进行投标。

如何评估哪些项目适合选？

- 是否符合公司的目标
- 是否值得做，利益大于投入
- 是否是现有项目中最好的最值得做的

**Capital Budgeting** 资本预算法：estimating the financial viability of a capital investment over the life of  the investment. 评估投资周期内金融可行性。

其他方法：

数字计算类方法：

- **Payback Period Method 回收期法**: Length of time (years) required for a project to repay its initial fixed investment 项目偿还投资金需要花多久。
- **Accounting Rate of Return 会计收益率法**: Uses accounting profits rather than cash flows expected from a project as a percentage of the capital invested 利润占投资的百分比
- **Discounted Cash Flow (DCF) techniques 折现回收期法**: Calculates value of returns that occur over a long period rather than immediately after completion 计算折现后的现金流量收回投资金所需时间，考虑时间成本。

非数字类方法，根据对项目的兴趣以及项目的难度评估：

- **The Sacred Cow 神圣的奶牛？**: Project suggested by a senior and influential person 老板说选啥项目我就选啥
- **The Operating/Competitive Necessity Model 运营/竞争必要性模型**: Project is necessary for continued operation of the company or for maintaining a competitive  position. 项目对公司的持续运营或者确保公司的竞争力的重要性
- **The Comparative Benefit Model 比较效益模型**: A selection committee arranges projects in a ranked order and the projects will be selected 比较项目优先级。

#### Project Selection Review GR1

接下来，要进行 Review 环节。有外部客户的 Review 如下：

- B/P 负责人先建立一个 B&P Data Repository 投标数据库。
- 考虑项目可行性和收益 feasible & benefits
- 根据外部客户需求（如果涉及到外部客户的话）制定解决方案
- 再重新考虑一下是否要投标

这就引入了评估项目的优劣势、机会与威胁的重要方法：SWOT

![image-20241018135743001](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410181357066.png)

以及分析政治、经济、社会、技术、环境、法律等外部因素评估对项目的影响：PESTEL。

Political, Economic, Social, Technological,  Environmental and Legal

![image-20241018140127589](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410181401687.png)

### Prepare B&P 准备提案

评估完成后就开始准备提案了。首先需要根据客户需求创建 project 并制定项目计划。

#### Define project charter 定义项目章程

主要作用是让大家尽早达成一致，别做着做着发现大家目标不同。

- 项目定义 Project identification
- 项目背景
- 利益相关者 stakeholders
- 项目描述
- goals, objectives, constraints
- 等等……

##### Requirements & Requirements baseline 需求和需求基线

**注意下面的部分会提到一些概念，ppt 中强调务必不能搞混。Requirements, Goals, Objectives, Deliverables**

A requirement is a specific need or want defined in  unambiguous, abstract, clear, unique, consistent, atomic and verifiable terms and  identifies what is needed for stakeholder acceptance.

需求有几大特点：

- abstract：不包括具体的技术实现方法，就只是需求。
- unambiguous：必须没有歧义，清晰描述需求。
- Traceable：需求描述 requirement description，system requirement，solution 这三者之间有关联性。
- Testable：必须有方法可以测试需求是否满足。

需求基线：建立一个需求表格，对其中的需求分析是否保留，要采取什么样的措施解决这些需求。

![image-20241103122003256](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411031220378.png)

##### Goals and Objectives 目标和具体目标

Goal is  an overarching long-term clear aim. 项目的总体方向和预期成果，是一个长期、清晰、覆盖整个项目的目标。*比如：开发一个可用于自动驾驶车辆认证的模拟器。*

Objectives are concrete measurable achievements to be made following a certain  number of steps. 为了实现目标而设立的具体行动步骤，需要在一定时间预算质量要求内完成。相比 Goals 是可以衡量的，所以采用**SMART标准**，即**具体（Specific）、可衡量（Measurable）、可实现（Achievable）、相关性（Relevant）和时间限制（Time-bound）**。*比如：构建一个可扩展的架构，实现自动化单域的服务级协议（SLA）谈判。*

需求是项目必须满足的特定条件，用于判断项目是否成功。具体目标是为了实现项目总体目标制定的短期步骤，有助于项目逐步达成预期成果。比如需求规定系统响应时间必须小于1秒，那么具体目标可能会是“优化代码和数据库查询，在6个月内将系统响应时间减少到1秒以内”。*主要区别可能是具体目标有特定的步骤，时间金钱等限制？*

##### Deliverable 可交付物

 the outcome/result of a project’s task/activity. 在 execution phase 产生，交给股东衡量是否和 proposal phase 阶段的 objectives 相符。

#### Define Project Structures 定义项目结构

#####  Organisational Breakdown Structure 组织分解结构

to Organize the people who will be working on the project 所有要给这个项目打工的人。下图是一个 OBS 的示例，细化到每个层次的人，以及他们要向谁汇报。

![image-20241103125335269](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411031253335.png)

#####  Work Breakdown Structure 工作分解结构

把整体大工作分解为许多小工作（并且包含交付 deliverables 部分）。

![image-20241103125915339](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411031259405.png)

并且每个 WP（Work package，第一章的概念）都需要细致的描述：

- SMART 目标
- scope, requirements, descriptions, dependencies, inputs 前置条件
- schedule 时间表
- deliverables, milestones 产出
- resources estimates 资源评估

##### Responsibility Assignment Matrix (RAM)

这部分有点像之前的股东分类。列出每个 WP 有谁参与，这些人的参与度。

![image-20241103131021874](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411031310967.png)

#### Create Management Plans (PMP) 准备管理计划

 defines how the project is executed,  monitored, and controlled.

![image-20241103133651829](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411031336900.png)

#### Estimates - Develop Costs/Budgets 评估成本

Identify, define and establish all cost elements to be consider in the Project Lifecycle

为每个 WP 估算成本，最终加上整个项目的 factored risk impact 风险开销

![image-20241103134133315](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411031341374.png)

cost 分为 direct / indirect

直接开销比如人员，材料，设备等。

间接开销比如租房费，保险费，同时用在多个项目的费用。

评估主要分为如下步骤：

- prepare estimating： Define/refine assumptions and quantifying the main parameters 估计量化主要参数；Choose the estimate techniques 选择合适的评估技术
- Develop estimate：用选定的评估技术计算，分析 cost impact of Risks，分析 confidencee in the estimates，并降低不确定度，确定最终的 risk 和 cost。
- aggregate duration 计算整个过程的资源花费并最终确定 estimate
- review
- monitor estimating process
- record, report, manage

#### Risks 风险

A risk is an uncertain event, that, should it occur, would have an adverse effect  on the course of the project. 一旦发生会对项目造成不利影响。

risk 主要分为：

- Risk Identification 
- Risk Characterisation and Prioritisation 
- Risk Handling
- Risk Monitoring

#### Establish Resource Needs & Schedule

Specify a baseline for task durations, deliverables/milestones, dependencies and  expected resources to be allocated.

![image-20241103145329682](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411031453759.png)

#### Finalise Project Execution Baseline

![image-20241103145602198](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411031456267.png)

#### Project Proposal

Bid Manager 把各个提案部分**整合 integration** 起来变成一个用户文档。

### Proposal Submission Review 提案审核与提交

Bid Team 把最终的相关文档发给高层 Senior Management，等待其和  peer reviewers 的建议。确保 GR1 阶段决策基本都完成后进入下一阶段。

#### Technical review of the proposal 技术审核

Reviewer 应该采纳用户建议 Customer Review Board，并且假设自己对项目没有任何先验知识 proir knowledge 地考虑一系列问题：

- 提案是否符合招标文件（RFP）中的要求和标准？
- 提案内容是否完整？
- 所提出的方法是否合理，即方法和逻辑是否清晰、可靠？
- 所交付的成果是否物有所值？
- 完成该工作的时间（小时）是否被评估为可行和现实的？
- 所提出的方法是否详细说明以便于理解？
- 提案是否能够交付所需的成果？

reviewer 应当在一定期限内考虑这些问题的解决方法和项目的改进方案，再发送给 technical lead。

#### Proposal Submission Review GR2

完成风险审核和技术审核后进入 GR2。总结如下内容：

![image-20241103153039506](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411031530574.png)

#### Proposal Hearing &  Negotiation Review GR3 听证会

用户可能会提问以及协商，bid team 需要准备召开听证会来获取用户授权许可签合同。

签合同需要的条件：

- Define milestones/deliverables: 投标经理定义了项目里程碑和可交付产品
- Compliance and export controls 符合出口管制需求规定
- Declare background intellectual property: 后台知识产权用来保护公司
- Manage Price and contract: 销售经理确定可以协商的价钱范围，别给我砍一半我再不挣钱就完蛋了
- Establish the contractual terms of the commercial proposal：采购主管 capture leader 在 bid manager, financial controller 和 contract manager 投标经理，财务总监，合同经理的帮助下确定商业计划书的合同条款

#### Handover – GR4 交接

提案现在就当交完了，也和用户协商通过签合同了。接下来就不是 bid manager 主要负责的事情了，要交接给 project manager 开始干项目了，所以要把现有文件进行交接。

bid team 需要做的有：

- ensure smooth transition 在所有部门合力工作下尽量确保交接丝滑进行
- update the bid data repository 协商后可能投标数据库会有改动，所以记得更新
- present the project context and their bid knowledge to the projec manager 和项目经理讲讲项目背景和投标信息
- provide the access to bid data repository to project manager 给项目经理访问投标数据库的权限
- closing administrative activities 结束行政活动（文件和数据）
- closing the spending authorisations 结清支出授权（投标的预算，剩下的要平账）
- analysing lessons learnt and recording them 吸取教训
- updating the commercial opportunity data 更新商业机会数据，后续投标有用（这个公司这次采纳了我们的xx项目投标，说不定下次也很有机会继续合作）
- handover!

## Managing Risks and Estimates 风险和评估

![image-20241116042026518](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411160420760.png)

### Risks 风险

风险是不确定是否真的会发生但是可以预见的事件。

风险管理的整体步骤：

- risk identification：找到可以影响项目的事件。
- Risk Analysis & Prioritisation：分析风险严重性（潜在影响和发生可能性 potential impact and likelihood）
- Risk Handling (Actions)：制定行动计划，记录了解决 risk 的 action 和其实现方式，相关开销，以及 risk register.
- Risk Monitoring & Control：观察风险，采取缓解措施 mitigation actions，控制 actions 管理风险，并且检验记录这些方法对解决风险和风险产生的根本原因的有效性。

#### 建立风险管理策略

- establishing the risk management strategy 建立风险管理策略：通过一个结构化且连贯的方法来**动态地**管理风险；深入到具体细节（如股东，技术等）；定期根据项目的近期发展，重新评估方法以及采取新方法。
- Compiling a Risk Register 风险登记单：记录了风险源，风险严重程度，风险类型（技术类，顾客金融类等），相应的解决措施；而且定期重新审阅风险登记单，删除不再有效的风险。

#### Identification of Risks 识别风险

主要分为四步：

1. BM 和 RM **reviews** 项目的关键元素，比如客户的技术和非技术需求，法律法规，不确定的部分，过去经验等。
2. BM PM 把相关领域的专家，同行，股东拉过来一块做风险识别。
3. BM RM 通过一系列方法筛选出能影响项目的开销，周期，资源的风险。
4. 记录识别的风险。

收集风险信息的方法有：头脑风暴，砖家判断，股东建议， Root Cause Analysis 根本原因分析，常见公司风险表，以及未证实的 assumption analysis.

风险源有：

![image-20241116180027359](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411161800507.png)

![image-20241116180032263](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411161800333.png)

#### Risk Prioritisation 风险优先级分析

基于：发生概率，影响（如经济损失，时间损失，项目表现结果下降，公司形象受损）进行分类评级。两个维度是独立事件，求交集是分别的概率直接相乘。

![image-20241116180239736](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411161802801.png)

#### Risk Handling 风险处理

避免 avoid，转移 transfer，减少 reduce，接受 accept / tolerate。

一般 low 用 tolerate 处理方式，high 和 medium 用 reduce 处理方式。以防万一，还有 contingency plan 紧急预案。

我们使用 Risk Register 记录风险和要采取的措施：

![image-20241116224702124](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411162247195.png)

Severity = Impact \* Likelihood

#### Risk Monitoring and Control 风险检测控制

由 RM PM 负责。

制定标书阶段，要制定出缓解风险措施和相应预算。

项目执行阶段，监控风险，检查其是否处于控制之下；采取风险应对措施并检测其效果；定期重新审阅并更新风险，风险处理方案等内容。

### Estimate 评估

在项目整个生命周期都会进行，评估成本、时间周期、资源等。

1. 选取合适的评估方法和参数。
2. 估算评估值，尽可能减少不确定性。
3. 在项目过程中记录成本，时间周期，资源等，完成项目估算。
4. 复盘评估，分析置信度 confidence level of estimates.，总结。

#### 待评估项

- resources：人力资源，材料，设备，供应等。使用 work breakdown structure 分解每个结构。

- time：从活动信息和活动资源开始考虑，将其拆为 wp 或者 tasks 以及相应需要使用的工具。人们一般都会过度乐观，高估自己完成任务的速度，所以建议是找没做过类似工作的人评估时间，并且考虑只有80%的时间是有效工作的，再加上对突发事件的容错。
- costs：人力，材料，设备，风险等直接开销；公共资源（如电话费，邮费等）开销，非直接员工开销，非直接设备开销（如电费，房费，保险）等非直接开销。

#### 准备评估

需要选出一个 estimate manager 评估经理。先确定评估范围，然后逐步细化到项目每个阶段每个部分，项目外部依赖等，给每个 WP 创建一个 Estimate Package，并且发给对应的 WP leaders。

#### 评估方法

- top-bottom 自顶向下：适合项目具体细节不清楚或者需要在短时间内完成评估的场景，不太精细，大致算出总体的花费和总体解决方式即可。图像大致呈倒三角。
- bottom-top 自下向上：具体细化到每一个 WP，Tasks 的花费。正三角。

这两种方法都可以应用一些评估技术：

![image-20241117090615613](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411170906695.png)

参数 Parametric；专家建议 Expertise；整合专家建议 consensus or Delphi；对比 analogy；拆解 engineering

参数化：自顶向下常用，基于一些项目参数进行评估（如代码行数，产品重量……）缺点在于参数太多可能过于复杂，也总需要随着参数改变而更新；参数太少评估又不一定准确。

专家判断：某领域的专家的看法，主观意见不一定准确。

类比：如果存在和本项目相似的以往项目就比较适合使用。但是缺点在于不同团队运营起来效果不同，而且可能影响因素随着时间推移发生了变化。

共识：由 co-ordinator 协调员和多位专家一起制定。协调员单独和每位专家提供信息，专家之间彼此不沟通，制定出自己的评估计划。然后专家们依次展示分享自己的评估和原因，互相学习后再继续单独评估再讨论，直到达成共识。可能比较费时间，而且共识也可能带有偏见。

Playing Poker 打扑克：也是一种共识方法，用于估计项目工作量规模。专家们抽取面朝下的扑克牌，基于抽取结果进行讨论，避免偏见。

工程评估：基于工程知识进一步细分，比如开发板的原材料的具体开销，工时具体到开发某一部分软件的花费等。需要开发者的基础知识足够扎实，输入信息准确且充分才能实施，而且也要花很多时间完成。

#### Aggregate & Review 汇总

汇总总数据，记录以便后续项目过程中回顾。

#### 三点评估法（处理不确定性）

当然肯定我们的评估预测不可能百分之百准确。三点评估法是一种处理工期和成本不确定性的方法，基于：输入数据的不确定性；历史数据的不确定性；评估过程中的方法的不准确性进行预测。

预测最终目的是找到三个点：

1. optimistic 乐观点：所有预测都准确情况下的工期。
2. pessimistic 悲观点：大多数预测都不准确，有较大误差。
3. most likely 最可能点：最可能发生的情况。

基于这三点，有许多种评估值计算方法：

- triangular distribution 三角评估：三者求期望。
- beta distribution (PERT - Program Evaluation and Review Technique) 加权平均：$$PERT\,Estimate\,=\,[(Optimistic+(4*Most\,Likely)+Pessimistic]/6$$

- PERT Standard Derivation 标准差：正态分布的 activity 在 PERT 的平均值左右两侧n个标准差范围内。n 被称作 confident level 可信度。
  $$
  \begin{aligned}
  \sigma&=(Pessimistic – Optimistic) / 6\\
  \mu&:\,mean\\
  Task \,Activity\, Duration &= Estimated\,PERT ± (n * \sigma);
  \end{aligned}
  $$
  ![image-20241117210457670](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411172104797.png)

#### 蒙特卡洛法

信息非常有限时使用，否则优先使用三点评估法。

根据事件发生的概率生成随机事件计算评估值，最后再整合。
