# Preface

项目 project: 简单来说就是一部分人，为了一个共同的目标，利用有限的时间和其他资源制定计划来达到目标。

It is a piece of planned work completed over a period of time or an activity that is and intended to achieve a particular purpose.

程序 Program：关联多个项目来达到大目标，可能涉及到不同领域的项目，比如造一个飞机，要审批，竞标，科研，生产等等。项目的结果可能更加注重成品，而程序的结果注重多个项目的效益（除了成品，还有花费的时间金钱等）。

Project Structure, work package, task, activity 是逐步细化的概念。比如 project structure 是“后端开发”，work package 是“设计后端数据库”，task 是“设计数据库接口”，activity是“编写单元测试代码”。

project和business operations的区别在于introduces business change.

# 项目模型

## Waterfall 瀑布模型

瀑布模型的特点在于专门化，每个阶段都只基于之前的阶段，考虑这个阶段的任务（因果性？）。

<div align="center">

<img src="https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410032132696.png" alt=" " style="zoom:67%;" />

</div>

## V 模型

也叫 Verification and Validation 验证确认模型，客户的最终反馈可以让我们反过来从头修改迭代计划。

![ ](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410032133598.png)

## Agile 敏捷开发模型

持续集成/持续交付（CI/CD）。rapid delivery

打个比方，瀑布模型可能是做一道菜，我先准备食材，下锅，加调料，炒完出锅再给客户品尝，客户才能反馈做得如何。敏捷开发可以拆成一些小任务持续地交付，比如煮一点，尝一口，看看咸淡，及时调整。不需要整个大项目组一起做几个月做出全部成果再等反馈。

![ ](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410032135489.png)

# 项目管理概述

## 基本概念

Project Management: Project Management (PM): is the Application of knowledge, skills,  tools and techniques to the project activities in order to meet stakeholders needs and expectations from the project. 利用所学知识管理项目来达到预期结果。

- Bid Manager 投标经理：主要协调客户和项目组，制定工作计划和提案达到客户预期。
- Project Manager 项目经理：主要管他负责的一块进度。

Project Management Context：为了完成项目需求的一系列活动，包括 initiating, planning, organizing, executing, monitoring  and controlling the project activities （启动，计划，组织，执行，监控）

Project Life Cycle (PLC)：项目生命周期。定义了项目运行过程中的不同阶段 distinct phases，这些阶段需要哪些人，花多长时间。

比如瀑布模型，大致分为：

1. 初始化阶段，分析客户需求，研究可行性。
2. 计划阶段，选择合适的人，制定计划。
3. 执行和交付阶段，下达指令，监控执行情况，提出新方案，发给客户。

## 技术对项目管理的促进

技术指的是科技产物，比如有形的工具（计算机），无形的软件，算法等。

## 成熟度

Readiness Level 是衡量项目的指标之一。

- Customer Readiness Level：比如低成熟度，用户需要自己百度才能用明白对方的产品。高成熟度，产品非常好懂，易于操作。
- Business Readiness Level：市场需求，是否可扩展到其他项目。
- Technology Readiness Level TRL：从简单的技术概念，到可交付的系统。

随着项目发展，成熟度会越来越高，比如项目前期可能会提出一些新技术概念，项目后期新概念经过多次迭代后已经成熟许多。

## Bid & Proposal B&P 投标提案

向客户证明：我们有能力能完成你的目标，我们的初步计划，公司价值等。

在提案开始的过程中会进行两个操作（**PROSPECT PHASE**）：

- Horizon Scanning：对新兴技术和威胁的早期检测评估。Aims to spot changes in the world, so that we can plan on how to  exploit these changes
- Technology Watch：获取有用信息用于制定策略。Systematic process of capturing, analysing and exploiting useful  information for strategic decision making in the company

招标方会发布 Request For Proposal （RFP）由招标方发布，发布自己的需求，让感兴趣的投标方提供解决方案，报价等。

## Sources of Project Initiation 项目启动来源

- **客户请求 (Customer Requests)**: 基于客户的具体需求启动项目。
- **高层管理指令 (Top Management Directives)**: 由战略决策推动的新项目。
- **已有系统 (Existing systems)**：进一步迭代。
- **外部因素 (External Factors)**: 市场趋势、新技术或监管变化促发项目创意。

##  Project Organization Structure 项目组织结构

项目组织是项目和上级组织之间的中间者 Project organisation is defined as the interface  between the project and its parent organisation.

| 组织类型                                         | 描述                                                         | 优点                               | 缺点                                                     |
| ------------------------------------------------ | ------------------------------------------------------------ | ---------------------------------- | -------------------------------------------------------- |
| Functional Organisation 职能组织                 | 项目由多个组织部门组成，每个部门管理特定职能，如研发，市场，HR等。项目经理通常是其中的成员，由职能部门经理控制该职能。 | 资源利用率高；同专业人员沟通方便   | 跨部门沟通困难；过度关注自身目标可能偏离项目目标         |
| Pure Project Organisation 纯项目组织             | 每个项目有独立的组织实体；项目经理控制整个项目；团队成员不受其他组织影响 | 减少层级审批，效率高；大家目标一致 | 可能导致资源浪费（每个项目都是独立团队，行政管理成本大） |
| Matrix Organisation 矩阵组织                     | 结合两者，在不同项目间共享人力物资等资源。不同部门的人为了这个项目临时组成一个纯项目组织，项目完成后解散 | 有效利用资源，平衡目标             | 可能权责不清，沟通不便；决策效率降低                     |
| Collaborative Projects Organisation 合作项目组织 | 项目成员分布在不同地点甚至国家                               | 融会贯通，促进学习创新，扩展视野   | 沟通交流可能存在问题；知识产权界限                       |

# 项目人员组成

## Stakeholders 股东

股东可以影响项目 having potential influence on the project

但是只有内部股东需要担责 Only Internal stakeholders are responsible/accountable  towards the project.

**两种重要的股东**：

- 赞助者 sponsors / customers: 拥有项目，能管理项目，能提供资源给项目（比如资金，技术）。**top level management**

- 使用者 users

![ ](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410111320043.png)

在项目过程中，首先我们需要 identify stakeholders，因为这些人会制定一些需求，项目最终目标就是满足他们的这些需求。同时项目过程中缺什么资源也可以和他们要。

![ ](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410111323177.png)

methodology（制定需求）-> capture requirements（实现需求）-> consolodate requirements（评估结果）

### Capture requirements 实现股东需求

Validation: Checks the proposed concept/solution  stakeholders’ requirements  **against the  and needs** 确保股东需求能实现

Verification：Check the implemented solution (prototype/service) **meet  design specifications** 验证股东的需求如何实现

Performance:  **meet certain  performance (KPI) characteristics** 评估结果

### Categorisation of Stakeholders and Engagement 股东分类

然后需要对**股东**进行优先级排序，判断谁说的话更有分量。主要有两种分类方式：

Stakeholder Power-Interest Matrix: 根据功能和股东兴趣两个维度制定优先级。

![ ](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410111409382.png)

Salience Model:  power, legitimacy, urgency 三个维度。（Power 影响力，比如我能给更多的钱，更能影响项目；Legitimacy 正当性，比如项目发起人，或者某些价值观的代表者；Urgency 紧迫性，比如我对这个项目的需求很急）

![ ](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410111416805.png)

- Dormant stakeholders 休眠利益相关者: no need for major communication，你有权力，那就用权帮我执行项目就完事了，少交流。
- Discretionary stakeholders 裁量型利益相关者：regular project updates . 也不需要过多交流，给他们项目更新进度就行。
- Demanding stakeholders 要求型利益相关者：Only keep them informed，他们比较急。
- Dominant stakeholders 支配型利益相关者：consider their communication and their involvement **needs at all times** 要保持沟通和参与。
- Dangerous stakeholders 危险利益相关者：有权，且需求很急，所以很危险。**Must meet their needs**. 
- Dependent stakeholders 依存型利益相关者：他们有需求和正当性，但是没有权力执行项目，依存于其他人执行项目。**Keep them informed** when I **need their helps** 需要他们帮忙的时候才通知他们。
- Definitive stakeholders 决定型利益相关者：Always keep them **informed, satisfied and involved**。

### Monitoring 评估股东

股东部分先不讲怎么实现项目了（后面项目部分才会展开叙述），直接讲如何监控评估股东：

![image-20241011144022366](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410111440485.png)

**Communicate with key stakeholders to  discover and manage their expectations upfront and during the project.**

## Project Teams 项目团队

![ ](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410111444012.png)

核心执行团队： conducting the works on a continuous basis, and are required for decision making 负责持续工作，以及下决定。

项目团队：负责贡献自己的部分，比如技术，人力。

项目支持团队：负责支持核心团队。

Characteristics of good team members:

- Credible and possess a high level of technical skill 技术能力强
- Resilient to pressures 抗压能力强
- Have an interest and ability in solving problems 解决问题兴趣高
- Should be robust 够强壮？？
- Should have a strong result/goal orientation 目标性强

##  Bid / Project Manager 投标经理 / 项目经理

Bid Manger：做计划，拉人组建团队， 筹备资源，在项目执行中确保足够的细节等等。

Project Manager：执行，监控，控制（可能还会改团队人员或者计划），报告（和 top management, 各个功能部门，other stakeholders）等等。

# Managing Bid & Proposal 标书管理

主要目的是创建优的投标提案，满足公司和客户需求。

标书管理阶段和项目管理阶段关联紧密，比如对项目的组织规划，风险管理，各个阶段的评审等。

整体结构图如下：

![image-20241103131320088](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411031313153.png)

## Prospect Phase 前景阶段

调研现有市场数据进行分析（如竞品分析），评估**是否值得为某个项目准备投标**。

![image-20241018132641835](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410181326926.png)

## Project Evaluation & Selection 项目评估选择

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

- **The Sacred Cow 神圣的奶牛？**（英语俚语，意为 神圣不可侵犯的思想、机构、制度等）: Project suggested by a senior and influential person 老板说选啥项目我就选啥
- **The Operating/Competitive Necessity Model 运营/竞争必要性模型**: Project is necessary for continued operation of the company or for maintaining a competitive  position. 项目对公司的持续运营或者确保公司的竞争力的重要性
- **The Comparative Benefit Model 比较效益模型**: A selection committee arranges projects in a ranked order and the projects will be selected 比较项目优先级。

### Project Selection Review GR1

接下来，要进行 Review 环节。有外部客户的 Review 如下：

- B/P 负责人先建立一个 B&P Data Repository 投标数据库。
- 考虑项目可行性和收益 feasible & benefits
- 根据外部客户需求（如果涉及到外部客户的话）制定解决方案
- 再重新考虑一下是否要投标

这就引入了评估项目的优劣势、机会与威胁的重要方法：SWOT

![image-20241018135743001](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202410181357066.png)

以及分析政治、经济、社会、技术、环境、法律等外部因素评估对项目的影响：PESTEL。

**Political, Economic, Social, Technological,  Environmental and Legal**

## Prepare B&P 准备提案

评估完成后就开始准备提案了。首先需要根据客户需求创建 project 并制定项目计划。

### Define project charter 定义项目章程

主要作用是让大家尽早达成一致，别做着做着发现大家目标不同。

- 项目定义 Project identification
- 项目背景
- 利益相关者 stakeholders
- 项目描述
- goals, objectives, constraints
- 等等……

#### Requirements & Requirements baseline 需求和需求基线

**注意下面的部分会提到一些概念，ppt 中强调务必不能搞混。Requirements, Goals, Objectives, Deliverables**

A requirement is a specific need or want defined in  unambiguous, abstract, clear, unique, consistent, atomic and verifiable terms and  identifies what is needed for stakeholder acceptance.

需求有几大特点：

- abstract：不包括具体的技术实现方法，就只是需求。
- unambiguous：必须没有歧义，清晰描述需求。
- Traceable：需求描述 requirement description，system requirement，solution 这三者之间有关联性。
- Testable：必须有方法可以测试需求是否满足。

需求基线：建立一个需求表格，对其中的需求分析是否保留，要采取什么样的措施解决这些需求。

![image-20241103122003256](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411031220378.png)

#### Goals and Objectives 目标和具体目标

Goal is  an overarching long-term clear aim. 项目的总体方向和预期成果，是一个长期、清晰、覆盖整个项目的目标。*比如：开发一个可用于自动驾驶车辆认证的模拟器。*

Objectives are concrete measurable achievements to be made following a certain  number of steps. 为了实现目标而设立的具体行动步骤，需要在一定时间预算质量要求内完成。相比 Goals 是可以衡量的，所以采用**SMART标准**，即**具体（Specific）、可衡量（Measurable）、可实现（Achievable）、相关性（Relevant）和时间限制（Time-bound）**。*比如：构建一个可扩展的架构，实现自动化单域的服务级协议（SLA）谈判。*

需求是项目必须满足的特定条件，用于判断项目是否成功。具体目标是为了实现项目总体目标制定的短期步骤，有助于项目逐步达成预期成果。比如需求规定系统响应时间必须小于1秒，那么具体目标可能会是“优化代码和数据库查询，在6个月内将系统响应时间减少到1秒以内”。*主要区别可能是具体目标有特定的步骤，时间金钱等限制？*

#### Deliverable 可交付物

 the outcome/result of a project’s task/activity. 在 execution phase 产生，交给股东衡量是否和 proposal phase 阶段的 objectives 相符。

### Define Project Structures 定义项目结构

####  Organisational Breakdown Structure 组织分解结构

to Organize the people who will be working on the project 所有要给这个项目打工的人。下图是一个 OBS 的示例，细化到每个层次的人，以及他们要向谁汇报。

![image-20241103125335269](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411031253335.png)

####  Work Breakdown Structure 工作分解结构

把整体大工作分解为许多小工作（并且包含交付 deliverables 部分）。

![image-20241103125915339](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411031259405.png)

并且每个 WP（Work package，第一章的概念）都需要细致的描述：

- SMART 目标
- scope, requirements, descriptions, dependencies, inputs 前置条件
- schedule 时间表
- deliverables, milestones 产出
- resources estimates 资源评估

#### Responsibility Assignment Matrix (RAM)

这部分有点像之前的股东分类。列出每个 WP 有谁参与，这些人的参与度。

![image-20241103131021874](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411031310967.png)

### Create Management Plans (PMP) 准备管理计划

 defines how the project is executed,  monitored, and controlled.

![image-20241103133651829](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411031336900.png)

### Estimates - Develop Costs/Budgets 评估成本

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

### Risks 风险

A risk is an uncertain event, that, should it occur, would have an adverse effect  on the course of the project. 一旦发生会对项目造成不利影响。

risk 主要分为：

- Risk Identification 
- Risk Characterisation and Prioritisation 
- Risk Handling
- Risk Monitoring

### Establish Resource Needs & Schedule

Specify a baseline for task durations, deliverables/milestones, dependencies and  expected resources to be allocated.

![image-20241103145329682](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411031453759.png)

#### Finalise Project Execution Baseline

![image-20241103145602198](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411031456267.png)

### Project Proposal

Bid Manager 把各个提案部分**整合 integration** 起来变成一个用户文档。

## Proposal Submission Review 提案审核与提交

Bid Team 把最终的相关文档发给高层 Senior Management，等待其和  peer reviewers 的建议。确保 GR1 阶段决策基本都完成后进入下一阶段。

### Technical review of the proposal 技术审核

Reviewer 应该采纳用户建议 Customer Review Board，并且假设自己对项目没有任何先验知识 proir knowledge 地考虑一系列问题：

- 提案是否符合招标文件（RFP）中的要求和标准？
- 提案内容是否完整？
- 所提出的方法是否合理，即方法和逻辑是否清晰、可靠？
- 所交付的成果是否物有所值？
- 完成该工作的时间（小时）是否被评估为可行和现实的？
- 所提出的方法是否详细说明以便于理解？
- 提案是否能够交付所需的成果？

reviewer 应当在一定期限内考虑这些问题的解决方法和项目的改进方案，再发送给 technical lead。

### Proposal Submission Review GR2

完成风险审核和技术审核后进入 GR2。总结如下内容：

![image-20241103153039506](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411031530574.png)

### Proposal Hearing &  Negotiation Review GR3 听证会

用户可能会提问以及协商，bid team 需要准备召开听证会来获取用户授权许可签合同。

签合同需要的条件：

- Define milestones/deliverables: 投标经理定义了项目里程碑和可交付产品
- Compliance and export controls 符合出口管制需求规定
- Declare background intellectual property: 后台知识产权用来保护公司
- Manage Price and contract: 销售经理确定可以协商的价钱范围，别给我砍一半我再不挣钱就完蛋了
- Establish the contractual terms of the commercial proposal：采购主管 capture leader 在 bid manager, financial controller 和 contract manager 投标经理，财务总监，合同经理的帮助下确定商业计划书的合同条款

### Handover – GR4 交接

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

# Managing Risks and Estimates 风险和评估

![image-20241116042026518](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411160420760.png)

## Risks 风险

风险是不确定是否真的会发生但是可以预见的事件。

风险管理的整体步骤：

- risk identification：找到可以影响项目的事件。
- Risk Analysis & Prioritisation：分析风险严重性（潜在影响和发生可能性 potential impact and likelihood）
- Risk Handling (Actions)：制定行动计划，记录了解决 risk 的 action 和其实现方式，相关开销，以及 risk register.
- Risk Monitoring & Control：观察风险，采取缓解措施 mitigation actions，控制 actions 管理风险，并且检验记录这些方法对解决风险和风险产生的根本原因的有效性。

### 建立风险管理策略

- establishing the risk management strategy 建立风险管理策略：通过一个结构化且连贯的方法来**动态地**管理风险；深入到具体细节（如股东，技术等）；定期根据项目的近期发展，重新评估方法以及采取新方法。
- Compiling a Risk Register 风险登记单：记录了风险源，风险严重程度，风险类型（技术类，顾客金融类等），相应的解决措施；而且定期重新审阅风险登记单，删除不再有效的风险。

### Identification of Risks 识别风险

主要分为四步：

1. BM 和 RM **reviews** 项目的关键元素，比如客户的技术和非技术需求，法律法规，不确定的部分，过去经验等。
2. BM PM 把相关领域的专家，同行，股东拉过来一块做风险识别。
3. BM RM 通过一系列方法筛选出能影响项目的开销，周期，资源的风险。
4. 记录识别的风险。

收集风险信息的方法有：头脑风暴，砖家判断，股东建议， Root Cause Analysis 根本原因分析，常见公司风险表，以及未证实的 assumption analysis.

风险源有：

![image-20241116180027359](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411161800507.png)

![image-20241116180032263](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411161800333.png)

### Risk Prioritisation 风险优先级分析

基于：发生概率，影响（如经济损失，时间损失，项目表现结果下降，公司形象受损）进行分类评级。两个维度是独立事件，求交集是分别的概率直接相乘。

![image-20241116180239736](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411161802801.png)

### Risk Handling 风险处理

避免 avoid，转移 transfer，减少 reduce，接受 accept / tolerate。

一般 low 用 tolerate 处理方式，high 和 medium 用 reduce 处理方式。以防万一，还有 contingency plan 紧急预案。

我们使用 Risk Register 记录风险和要采取的措施：

![image-20241116224702124](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411162247195.png)

Severity = Impact \* Likelihood

### Risk Monitoring and Control 风险检测控制

由 RM PM 负责。

制定标书阶段，要制定出缓解风险措施和相应预算。

项目执行阶段，监控风险，检查其是否处于控制之下；采取风险应对措施并检测其效果；定期重新审阅并更新风险，风险处理方案等内容。

## Estimate 评估

在项目整个生命周期都会进行，评估成本、时间周期、资源等。

1. 选取合适的评估方法和参数。
2. 估算评估值，尽可能减少不确定性。
3. 在项目过程中记录成本，时间周期，资源等，完成项目估算。
4. 复盘评估，分析置信度 confidence level of estimates.，总结。

### 待评估项

- resources：人力资源，材料，设备，供应等。使用 work breakdown structure 分解每个结构。

- time：从活动信息和活动资源开始考虑，将其拆为 wp 或者 tasks 以及相应需要使用的工具。人们一般都会过度乐观，高估自己完成任务的速度，所以建议是找没做过类似工作的人评估时间，并且考虑只有80%的时间是有效工作的，再加上对突发事件的容错。
- costs：人力，材料，设备，风险等直接开销；公共资源（如电话费，邮费等）开销，非直接员工开销，非直接设备开销（如电费，房费，保险）等非直接开销。

### 准备评估

需要选出一个 estimate manager 评估经理。先确定评估范围，然后逐步细化到项目每个阶段每个部分，项目外部依赖等，给每个 WP 创建一个 Estimate Package，并且发给对应的 WP leaders。

### 评估方法

- top-bottom 自顶向下：适合项目具体细节不清楚或者需要在短时间内完成评估的场景，不太精细，大致算出总体的花费和总体解决方式即可。图像大致呈倒三角。
- bottom-top 自下向上：具体细化到每一个 WP，Tasks 的花费。正三角。

这两种方法都可以应用一些评估技术：

![image-20241117090615613](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202411170906695.png)

- 参数化 Parametric：自顶向下常用，基于一些项目参数进行评估（如代码行数，产品重量……）缺点在于参数太多可能过于复杂，也总需要随着参数改变而更新；参数太少评估又不一定准确。

- 专家建议 Expertise：某领域的专家根据经验的看法。

- 类比 analogy：如果存在和本项目相似的以往项目就比较适合使用。但是缺点在于不同团队运营起来效果不同，而且可能影响因素随着时间推移发生了变化，很难完全一致。

- 共识 Consensus or Delphi：由 co-ordinator 协调员和多位专家一起制定。协调员单独和每位专家提供信息，专家之间彼此不沟通，制定出自己的评估计划。然后专家们依次展示分享自己的评估和原因，互相学习后再继续单独评估再讨论，直到达成共识。可能比较费时间，而且共识也可能带有偏见。

*Playing Poker 打扑克：也是一种共识方法，用于估计项目工作量规模。专家们抽取面朝下的扑克牌，基于抽取结果进行讨论，避免偏见。*

- 工程评估 engineering：基于工程知识进一步细分，比如开发板的原材料的具体开销，工时具体到开发某一部分软件的花费等。需要开发者的基础知识足够扎实，输入信息准确且充分才能实施，而且也要花很多时间完成。
- 三点评估法 3-point：见下。
- 蒙特卡洛法 monte-carlo：见下。

### Aggregate & Review 汇总

汇总总数据，记录以便后续项目过程中回顾。

### 三点评估法（处理不确定性）

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

### 蒙特卡洛法

信息非常有限时使用，否则优先使用三点评估法。

根据事件发生的概率生成随机事件计算评估值，最后再整合。

# Structuring and Scheduling 组织计划

项目结构包括：

- introduction
- management / implementation
- technical
- other complimentary sections
- summary and conclusions

## Work

指明了项目中必做的 tasks and jobs

###  Work Breakdown Structure (WBS)

把工作进行细分：

project, sub-project, work package, task, activity （之前了解过，这些是逐步细化的）。

WPs 在逻辑上依靠前一个 WPs，比如：场地准备，购买材料，建造，清理，这种细分程度是4个 WPs。

WPs 是成本和进度的基础，每个 WPs 对一定的资源和管理责任负责。在项目执行过程中用项目预定进度和每个 WPs 的实际进度进行对比核实，并以 WPs 为单位采取相应的调整措施。

## Scheduling

将项目计划转换成图表等形式，典型的例子是甘特图。

甘特图可以显示项目的起止日期，相互之间的依赖情况，以及所需资源等。

### Project schedule

项目管理人员通过 Project schedule 来计划和审查项目。

呈现出主要的项目活动，但是不会具体展开其细节。自顶向下地制定，自下向上（从细节到整体）地修改。

比如：WP Schedule，

### Scheduling Process & Challenges 流程和挑战

scheduling 的过程包括：

1. Organize tasks concurrently 并发组织任务，有点像小时候做过的那种“淘米需要x分钟，煮饭需要x分钟，洗菜需要x分钟，如何让做好饭的总时间最短”问题。
2. Minimize task dependencies 最小化任务之间的依赖，减少依赖后很多任务就不用等着其他任务先完成再做了。
3. Estimated duration and resources 评估每个 tasks 所需时间和资源。

挑战：

1. 任务优先级划分；
2. 任务重叠问题；
3. 资源有限；
4. 复杂任务的处理。

### Schedule Development Activities 制定计划的12步活动

1.  Identify the WPs/tasks 判断此项目中哪些是 WP，哪些是 tasks。

2. Identify the project’s Milestones/Deliverables 确定里程碑节点和最终可交付物。

   里程碑的概念不要和其他概念混淆。WPS 和 Tasks 是需要完成的消耗资源的任务；events 是某一个时刻的事；interface event 接口事件是指前一个 tasks 完成，后一个 tasks 开始的时刻。里程碑标志着项目的重要节点，比如完成了一系列重大任务的阶段，就某些重要事情达成共识，以及获取到了重要资源等。如果里程碑没有按预期完成，后果会比较严重，可能会影响后续计划预算。

3. Identify Customer Milestones 客户提出的里程碑节点。

4. Detail the schedule at different levels

5. Estimate Activity/Task Durations 评估活动所需时间，使用前面提到的评估方法，包括处理不确定性的蒙特卡洛法

6. Estimate Resources Needed 评估资源需求

7. Activity Network Diagram 创建活动网络图。如下图：

​	![image-20241207001424352](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412070014474.png)

其中，总用时最长的路径被称作 Critical Path 关键路径，因为其决定了整个项目最早什么时候才能完成。这条路径上的任务如果没有按时完成，延期了，那么整个项目都会延期。所以可以分配给关键路径上的活动更多资源来确保其能够风险最小地尽快完成。

*sub critical paths 是第二长用时的路径。*

而后再使用 PERT 方法进行评估（最优时间+最差时间+最可能情况*4）/6。

下图是每个项目的具体浮动时间情况：

![image-20241207002346054](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412070023167.png)

Total Float，或者叫 Slack，就是该活动的最长可延迟时间（在不影响**该活动结束日期**的前提下）。用最晚可开始时间-最早可开始时间，或者最晚可结束时间-最早可结束时间得到。ES-LS=EF-LF

Duration 是项目的持续时间，用 EF-ES+1 得到。

Free Float：该项目不影响**后续项目**的情况下最大可延迟时间。计算公式是 FF=该活动后续活动的 ES 的最小值 - 该活动的 ES - 该活动的 DU。

比如 Activity P，FF(P)=min(6,8)-1-5=0

Negative Float NF：该项目已经落后了，需要提前几天完成。

8. Incorporate Risk Analysis (Estimates) 分析

9. Incorporate resource constraints – Critical Chain Technique 关键链方法设置资源约束

   找到关键路径的资源和活动依赖，增加其他非工作活动的持续时间（来把其他不要紧的活动的资源分配给关键路径）。

   之前的关键路径方法我们要计算 Float，目的是判断每个项目最晚可以晚完成的时间；关键链方法则是设置缓冲区来留有一些余地。比如下图，非关键路径会设置 Feeding Buffer，这样在项目执行过程中如果发生了一些延迟也不一定会影响原计划。

   Project Buffer 设置在关键路径上，代表因为意外情况整个项目可以推迟完成的时间。

   除此之外还有 Resource Buffer，设置在关键路径上，叫做关键资源，这些资源相当于备用待命确保项目缺少资源的时候不会告急。

   ![image-20241207052220311](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412070522402.png)

   总结来说，Float 是关键路径和非关键路径之间的时间差，代表可以晚完成非关键路径多少天（关键路径不可以推迟完成）。而缓冲 buffer 是估计预留出一个安全期来确保项目的鲁棒性。

10. Incorporate schedule constraints, imposed dates, or other schedule updates： Duration Compression 压缩技术压缩项目总用时。具体做法是：Fast Tracking 尽可能并行执行连续性任务；Crashing 以最小的成本增量获得最大的时间压缩，比如让工人加班（什么地狱笑话）。
11. Resource Levelling 考虑资源因素调整活动的起止时间；常用甘特图，对于有共享资源的项目比较一目了然。
12. Final Approval：制定 schedule baseline；把 schedule 上交给高级管理者批准，后续嵌入到项目中。

# Managing Project 管理计划

## Completing Bid & Proposal

首先我们需要完成投标。包括召开听证会给客户答疑，制定合同，交接到项目执行阶段，以及投标阶段的复盘与关闭。

## Initialise

将从投标阶段递交过来的数据整理存入项目数据库，检查有无缺少部分等。PM 审核后批准项目章程。

PM 需要做的有：

- 开放预算线 budget lines, 团队可以预订项目预算。
- 开启所有的 planned management activities 管理活动，比如文档，配置，数据等。
- 确定管理工具 tools。
- 建立项目数据库。
- 监控项目初始化 monitor and control。

召开会议，确定股东和项目达成一致；解释项目目标；介绍项目的各个主要阶段。

Present the project main parts in particular 呈现项目的主要部分，比如章程，组织，schdule，机制等等，并记录会议时长和事件。

如果可能的话，还需要对项目进一步修改。

## Project Manager Responsibilities

PM 负责的内容：

- organization：管理项目，资源，时间等，预防会导致项目延期或预算不够的风险，决定是否向高级领导汇报进度，**绝对不能让 top management surprised**。

- Project：确保项目完整性；消除误解 misunderstandings；满足客户需求；按时按规定完成项目。
- Project Team：让团队高效工作；倾听团队成员意见；关心团队成员的个人发展和未来规划。
  - 人是一个项目中最重要的资产。PM 的人际交往应该做到：Consistency 一致性，一视同仁；Respect 尊重不同人的技能、文化、性格等；Inclusion 考虑到所有人的想法；Honesty 对项目现状要如实禀报。

PM 必须是一个很好的谈判者，无论是谈判获取资源，和项目成员沟通，和股东，高级管理者汇报进度，解决障碍，这些都需要良好的沟通能力。

风险问题一般源自于低估项目所需资源以及资源分配得不好。如果出现障碍，PM 需要及时提出解决方案并和客户沟通，并吸取经验。

## Project Execution, Monitoring & Control 

### Start  WPs & WGs

启动 WP 工作包和 WG 工作小组。WP 工作包必须要详细确定好其计划，组织，资源分配，和其他工作包的接口。

### Control Project

防止出现偏差；定期更新记录；一旦出现偏差采取补救措施。

### Progress Reviews

与团队成员召开内部会议检查 WPS 进度；

确保沟通质量；

分享遇到的问题，预期解决方式，并在解决问题的过程中持续跟进；

记录工作，采取的措施等；

定期向高层汇报工作。

![image-20241207173309122](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412071733296.png)

### Manage Customer

定期与客户交换信息达成一致；商务信息必须和商务经理沟通分析。

### Manage QA

确保品质；定期检查应用质量和客户评价。

## Project Closure

PM 确保项目按合同完成所有需求，产出相应交付物，并取得合规文件（如海关出口许可），让财务提出最终费用 final invoices 后准备关闭项目。需要获取客户同意，以及更新项目数据库，Lesson Learnt：在团队成员的帮助下总结项目的优缺点。

## Project Management Methods

### Methods

Project Management Institute (PMI)：一种项目管理标准。

![image-20241207175311009](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412071753104.png)

 PRINCE2：一个面向商业化的项目管理方法，基于产品，强调将项目分为可管理和可控制的阶段。而且非常灵活，可以被应用于相似的项目。

![1733594380554](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412071759598.png)

![image-20241207175949934](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412071759021.png)

### Tool

比如微软的 Microsoft Project Management，还有 Chorus 2.0。

Chorus 2.0 是一个流程框架 process  & procedures framework，所有工具都需要与其兼容。

![image-20241207183515914](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412071835032.png)

B1 是电商套件；Primavera 是 schedule 工具，类似微软 Project 工具（相比微软工具，Primavera 量级更大，需要填写的细节更多，适合大型项目）；OTL Oracle Time and Labour 是时间和考勤管理工具；mTools 接受上述输入，并提供实际进度、预测花费等信息。

# Project Extcution 项目执行

下面介绍一些项目执行模型。

## Waterfall 瀑布模型

就像瀑布顺着台阶留下来一样，一级一级地执行。

![image-20241207185052414](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412071850536.png)

优点在于模型很简单，也很好实现。缺点在于，如果在后续活动执行的时候很难再回去改之前的部分。而且不适用于太复杂的项目。

Change Request 很常见，可能原因有：客户有新的需求；客户希望使用新技术；目前项目耽搁太多时间了；检测到新风险需要避免；等等。PM 在收到 Change Request Form 后必须评估改变请求对项目造成的影响。

## Agile 敏捷开发

实际上在项目过程中，保持需求不变几乎是不可能的。所以没办法在最开始就确保整个项目的所有需求。

敏捷开发是快速，轻量级的项目管理过程，**当项目的目标确定但中间的执行过程不确定时使用**。项目被拆为许多个短而小的的迭代周期，争取每一次迭代都产生一个可以交付给客户的小版本。

敏捷开发有12个原则：

1. 满足客户需求是最高优先事项 satisfy the  customer needs。
2. 大胆地修改需求，哪怕是在项目开发过程晚期 change the requirements.
3. 频繁交付 deliver working software frequently
4. 业务人员 business people 和开发人员 developers 在项目过程中必须每天合作 work together。
5. 信任有动力的员工可以完成工作，给予他们合适的环境和支持 trust。
6. 最有效的沟通方式是面对面交流 face-to-face conversation。
7. working software 是进度的首要衡量标准。
8. 可持续开发，开发者应当维持恒定开发速度 sustainable development。
9. 持续关注优秀的技术和设计方案可以提高敏捷性 agility。
10. 保持简单，最大化未完成工作量 simplicity。
11. 最好的设计来自自组织团队 self-organizing teams.
12. 定期反思 reflects.

4条敏捷宣言：

- individuals and interactions > processes and tools 个体和交互胜过过程和工具
- working > comprehensive documentation 可工作的软件胜过复杂的文档
- customer collaboration > contract negotiations 客户合作胜过客户合同谈判
- responding to change > following a plan 相应变化胜过遵守计划

敏捷开发的优势在于持续快速的工作软件的交付；开发者和客户的关系更近；在项目开发过程中仍然可以更改需求，持续改进项目；高度透明化。

缺点在于：可能相比线性模型更难理解；碎片化交付不一定适合所有项目；如果不恰当地使用敏捷开发，可能会导致更低的效率；文档的重要性被忽视。

两种常见的敏捷开发框架是 Scrum and Kanban。开发流程如下：

1. project planning，但是相比其他模型计划的没有那么详细，因为后续可能会做很多改动。
2. Product Roadmap Creation：将最终产品拆成许多部分，分在不同周期中执行。以及根据需求制定一个 product backlog 产品待办事项列表，一项项执行。
3. (Product) Release Planning 发布计划：在每个周期（sprints）开始都会发布一个新的计划。
4. (Work) Sprint/cycle Planning：每个 Sprint 开始之前股东分配工作到各个团队/个人；以及实时记录工作流状态。
5. Daily Meetings：每天召开15分钟左右的小会议，讨论昨天工作。
6. Sprint Review and Retrospective：Review 是和股东，项目拥有者，团队等人开会检查产品是否达到需求。retrospective 是回顾总结项目开发过程中的问题，改进方案等。

![image-20241207201252884](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412072012009.png)

### Scrum

Product Owner：客户。

Scrum Master：PM。

Development Team：项目团队。

Scrum 需要召开的会议如下：

- Sprint Planning Meeting 将任务分配到周期中。

  Sprint Planning PM 必须出席，而且容不得拖延；质量问题不可以协商……

  周期推荐长度为3周。

  sprint planning 需要确定每个周期的 story points 故事点数，故事点数是一个单位，一般4-12小时的活为一个故事点。Velocity 是下一个 sprint 的故事点数，estimated velocity 是预期完成这个 sprint 需要多少故事点，actually 是实际用的。

- Backlog Refinement Meeting 待办事项会议：定义待办事项。

![image-20241207202522353](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412072025447.png)

- Daily Scrum：每日15分钟的小会，汇报进度。
- Sprint Review / Demo：每个周期结束的时候开，调整待办事项列表。
- Sprint Retrospective：在 Sprint Review 之后开，改进工作方法。

![image-20241207202241097](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412072022191.png)

- sprint review：重审后就可以发布计划了。

### Kanban

看板是一种管理产品创建的方法，强调持续交付且不给开发团队带来太大的负担。

下图是 kanban board：

![image-20241210021841013](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412100218175.png)

上面有多列内容，每一列同时存在的任务数量有限制 Work-in-Progress Limit，并且前置任务有前置平均时间限制 Lead Time（来保证持续地进行转移）。

看板和 scrum 相似之处在于图表中呈现了任务内容和足够的透明度。

| 比较条目     | Scrum                                                        | Kanban                                               |
| ------------ | ------------------------------------------------------------ | ---------------------------------------------------- |
| 角色和职责   | 每个团队成员都有预定义的角色                                 | 没有预定义的角色（除了 PM），鼓励团队合作            |
| DDL          | 可交付成果由 Sprint 决定                                     | 产品和过程在需要的基础上持续交付                     |
| 授权优先级   | 每次迭代拉取一批新任务                                       | 完成前一个任务再拉取下一个任务                       |
| 修改         | 不建议                                                       | 允许                                                 |
| 生产力的量度 | velocity，每个 sprint 的完成时间都依赖于前一个 sprint 的完成 | cycle time：从开始到结束完成项目的一个完整部分来度量 |
| 最佳应用场景 | 有稳定优先级的工作和团队，优先级不会修改                     | 有广泛不同优先级的项目                               |

## Scrummerfall

混合了瀑布模型和 Agile。

![image-20241210022630433](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412100226532.png)

# Control And Monitoring 检查控制

执行过程中要持续监视项目状态并加以调控。这样让项目在有限的时间等资源范围内，在预期范围内发展，也可以减小风险，提高项目产出质量。

但是需求和目标在项目执行过程中不断变化，控制不及时可能赶不上最佳时间。而且对于复杂项目来说控制难度更大。

## Control Steps

1. 确定要控制的量度 criteria/metrics：选择要被衡量的指标
2. 建立标准 standards for performance analysis
3. 利用测量方法衡量 actual performance
4. 比较计划表现和实际表现
5. 识别不可接受的差异 identify unacceptable variance
6. 评估差异造成的影响 impact of variance
7. 找到差表现的根源 source of poor performance
8. 挑选合适的控制措施 control actions
9. 实施措施
10. 确保差表现不再出现 does not re-appear

## 控制重点

- Scope Control 控制范围：不要超出项目负责的范围，因为会浪费时间预算。
- Schedule 控制时间：和计划的时间表对比，不能超时（如甘特图）。可以在计划阶段加入 time buffers，避免一心多用 multi-tasking，频繁收集活动状态，公布提前完成的好处和晚完成的惩罚。
- cost 控制成本：消除未授权或者不恰当的花费。
- quality 控制质量：采取预防措施，遵循质量计划。
- Procurement 控制采购：控制对采购负责的承包商 contractor；提前列出应急解决措施。

## 控制可能存在的问题

1. 不及时的控制措施可能跟不上变化；
2. 成员对控制了解不到位；尽量人手一本手册。
3. 发生问题时过度反应或者不采取措施。
4. 及时报告问题。

## performance analysis 分析表现

### EVPM 分析时间金钱成本

Earned Value Performance Management 挣值绩效管理方法

三个基本变量:

BCWS：budgeted cost of the work scheduled 计划预算

BCWP：budgeted cost of the work performed 实际预算

ACWP：Actual cost of the work performed 实际开销

例题：

Definition : A company signed £200K fixed cost contract to install 1,000 new parking meters. Cost of removing old parking meters and replacing them with new ones: £200 per meter. 25 meters can be installed each day. Project should take 40 working days to complete.

a) BCWS：就是在规定时间内建造所有新停车计时器的预算，200\*18\*25

b) 假设第18天装了400m，求 BCWP：实际工作量的预算，200\*400（Sv = BCWP – BCWS 相减可知，现在的进度低于预期进度50m，2天的工作量）

c) 实际上每米花费 210 英镑，求 ACWP：210\*400

- 进度偏差：Schedule Deviation **Sv = BCWP – BCWS**，正值表示提前了，负值表示落后了（相当于：固定了单位工作量的开销和理想情况一致的前提下，总工作量低于预期）。

- 花费偏差：Cost Deviation **Cv= BCWP – ACWP**，正值表示实际开销小了，负值表示大了。（SV CV 的正值都是我们期望的结果，都是用 BCWP 作为被减数）

- 进度指数 Schedule Index **SI = BCWP/BCWS**，>1 表示在计划进度之前。
- 花费指数 cost index **CI = BCWP/ACWP**，>1 表示实际开销更小。
- 临界比 Critical Ratio **CR=CPI*SPI**，代表这个项目整体来看（时间和开销）怎么样，>1 表示还可以。

但是如果出现了项目以外的开销影响（比如间接开销太大，影响 CV 为负数，但是对项目性能没影响）或者有没及时更新的数据，EVPM 方法就不一定准确。

## Forcasting 预测是否即将完成/是否完成

BAC：budget at Completion 完成时（计划）预算。**BCWP/BAC 表示工作量完成百分比**

WR：work remaining 剩余工作量，用预算衡量。**WR=BAC-BCWP**

ETC：Estimate to complete 剩余工作成本，**ETC = WP / CI**

EAC：Estimate at Completion 完成时工作成本，**EAC=ACWP+ETC**，相当于现在的成本+按照现在的花费速度，完成剩余部分需要的成本。**EAC=BAC / CI**

# Project Outputs and Managing IP 项目产出；知识产权管理

## Project Outputs 项目产出

首先需要区分一下 Outputs 和 Outcomes 的概念。Outputs 是有形或无形的产出物，而 Outcomes 更接近于“间接价值”，比如价值，社会影响，有用性等。

所以我们讨论的 Outputs 更接近于“产出物”注重结果而不是“意义”。比如有形的有硬件，设备等；无形的有代码，算法等。outputs 被用于衡量项目是否成功。*大多数 Outputs 都有相关联的 reports。*

因此，对于不同类型的产出，也需要定义相关联的指标来衡量其优劣。这部分内容在定义 WP/Tasks 的时候制定。

开发软件指标：

- 方法论 methodology：开发过程需要遵循软件研发方法论，比如计划-分析-设计-实现-测试-维护等流程。
- 合规性 Compliance：符合行业规范。
- 鲁棒性 Risks and vulnerabilities：有风险评估并嵌入使能器 embed enablers。*这里我对于使能器的理解：嵌入式开发的时候经常看到有很多端口需要使能才能启用，给不同的部分嵌入使能器后，当出现风险故障的时候可以确保未使能的部分受影响减轻。*
- 编程 Coding：选择合适的实现平台（linux, windows...）
- 兼容性 Compatibility：软件更新迭代应向旧版本兼容。*延伸：向前兼容的意思是新版本的软件仍然可以与旧版本的硬件、文件格式等兼容；向后兼容则是旧版本的软件可以与新版本的硬件、软件或文件格式兼容。*
- 可升级性 upgradability
- 维护支持 maintenance and support

开发硬件类似，要遵循一定的硬件开发原则、代码编写规范等，并产出相应文档说明。

### Intangible  Outputs 无形产出

专利发明、创新这一类都属于无形的产出。不是一种技术，而是价值 value。

## Intellectual Property IP

IP 是一种财产，比如人类智力的无形创造。有很多种形式的 IP 用于保护创意，比如“商标” trade marks 用于保护品牌形象 brand；“版权” copyright 用于保护文件，图片，音乐等；专利保护发明；设计权保护产品外观……

如果没有 IP，那么别的公司花费大量时间人力物力研制出新技术应用到产品中，我一声不吭就偷过来了，那没有什么公司想自己耗费时间精力研制新技术了，都等着偷别人的就行。IP 保护了别人不可以从公司的努力、专业知识、投资等 inputs 中获利，确定了该公司的地位，也保护了其技术和未来市场。

在项目执行过程中，要事先调查好是否已经有人生成了相关 IP，如果没有，那本项目成员才应该继续设计新技术方法来解决问题，并且**在这个过程中保护好 IP 不泄露**，避免被他人捷足先登。

对于合作项目，也需要明确其他公司的 IP 范围并保护项目的未来 IP。

业务销售部需要确定哪些关键技术需要 IP 保护，是否被保护了，以及能否使用这些 IP 攻击竞争对手。而法务部则避免发生此类情况（之前的中国乔丹，“乔丹是一种花名”，“我们的中国乔丹拿的是乒乓球拍”一案）。

### IP 保护方法

- 商标 trade marks：比如图标，口号等。
- 设计 Designs：分为外部可见的和内部设计两种。外部可见的设计（比如头盔，网页前端）保护其整体外观，最长注册时间25年，注册成功会有®标志。
- 版权 Copyright：常用于保护文学、艺术、音乐、软件等作品。©符号，不用注册，有效期50年到我挂后70年不等，禁止其他人未经许可复制作品或一种概念的表达方式。另一种版权是著佐权 Copyleft，符号是一个左右相反的 Copyright 符号，意思是：只要遵循一定的规定，就可以使用、修改该作品。
- 专利 Patent：一种地域性权利，主要保护物理设备对象，软件，信号，协议等。专利包含这些东西的功能，是怎么具体实现的，所需材料……禁止其他人未经许可制造、使用、进口、出售你的产品。最长20年。
  - *软件只要对**技术**问题有所改进，比如能耗、效率等，就可以申请专利。但不包括非技术性的管理等方面。*
- 商业机密 Trade Secret：比如配方，设计方法，工具等。相较其他知识产权，商业机密不公开。雇员可以签署合同来保证不泄露商业机密地使用。

## Agreements and Liscences 协议和许可

- 在多方合作项目中，所有人需要达成一致，制定保密协议 Non Disclosure Agreement 明确哪些部分是保密的，并且遵守保密义务。最终，在 B&P 阶段结尾，需要制定**联盟协议 Consortium Agreements (CA)**。

​	Memorandum of Understanding MoU 谅解备忘录：诸方达成一致后的记录文本，没有法律效力，但是代表大家差不多达成一致准备签定合约了。

- Background *& Foreground IP：项目执行前后的 IP，项目开始时就要声明好，不能损害 BIP，并保护好 FIP。
- 软件保护：除了之前提到的 Copyright（复制），Patent（其他人抄袭，创造出同样的软件），Design（界面，图标等），Trademark（商标），还有 License 许可，比如开源软件，闭源软件等，下图往左是开源，往右是闭源。

![image-20241225180148283](https://raw.githubusercontent.com/Jingqing3948/FigureBed/main/mdImages/202412251801392.png)

## Dissemination &  Exploitation 传播推广

Dissemination：确定目标受众 target audience，传播途径 dissemination channels，关注 Stackholders 确保有效传播。

Expliotation：首先确定不同的推广策略，主要分为商业 Commercial、知识 Knowledge、学术 Research/Academic 三种。然后找到其使用场景 Real-life Usage Scenarios 并投放使用，优先确定将有效利用结果的关键参与者  the players who will exploit the results。

# Project Closure 项目关闭

完结撒花！

## Project Success or Failure

对于客户和 PM 来说的项目成功性是有区别的。客户只需要考虑是否达到自己的需求就可以了，PM 要考虑的可就多了。比如预算，时间期限，产品质量，客户满意度，团队关系，公司地位。

## Project Closing

PM 的最后一个任务。关闭项目包括：

- output 被交给 stackholders
- Contractual agreements 合同被正确履行
- 项目记录在库

### Project Termination 项目终止

首先需要停止项目。

- integration 集成终止：常用于成功结束的项目。房地产等资源交还给父组织，项目最终产出作为组织运营的标准组成部分。
- add 添加终止：把项目资源加到其他项目上。
- starvation 饥饿终止：项目因资源枯竭，预算削减或政治因素而结束。
- extinction 灭绝终止：高层管理层停止项目，因为没有达到预期目标，或者觉得效益不好。

### Project Closure Process/Actions

PM 完成项目的其他阶段后，开始准备：

- Conducting project Closure Debrief/Review for closure 项目结案汇报 and Post-mortem 事后分析
- Creating a Project Archive 项目归档

- 如果项目是后续还会持续提供支持，应该新开一个支持项目 support project。
- 记录风险。
- 确保客户验收，获得客户和测试人员的同意。在这个过程中一直记录。
- 通过会议或者电邮通知其他负责人。
- CM 商务经理应当检查是否还有需要解决的商业问题，并执行财务结算。
- PM 释放所有项目成员并将其分配到其他工作中。

当所有要求都完成后，CM 应批准关闭项目。

## Post-Mortem Analysis 事后分析

对项目的成功和不成功点进行总结分析，吸取教训。

- 项目产出质量？

- 时间，花费，行政管理问题是否恰当？

- 开发过程中工具是否有效？遇到了什么技术问题？
- 团队成员表现？

- ……
