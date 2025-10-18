const TabTestData = [
  {
    "title": "项目管理系统设计与实现",
    "nickname": "Alice"
  },
  {
    "title": "基于Vue的组件化开发实践",
    "nickname": "Bob"
  },
  {
    "title": "大数据可视化技术研究",
    "nickname": "Charlie"
  },
  {
    "title": "人工智能在医疗诊断中的应用",
    "nickname": "David"
  },
  {
    "title": "深度学习模型优化探索",
    "nickname": "Eve"
  },
  {
    "title": "移动端用户体验（UX）分析报告",
    "nickname": "Frank"
  },
  {
    "title": "Go语言高并发服务器架构",
    "nickname": "Grace"
  },
  {
    "title": "现代前端工程化CI/CD流程",
    "nickname": "Henry"
  },
  {
    "title": "区块链技术与供应链金融",
    "nickname": "Ivy"
  },
  {
    "title": "WebAssembly性能提升研究",
    "nickname": "Jack"
  },
  {
    "title": "云原生应用容器化部署",
    "nickname": "Kelly"
  },
  {
    "title": "Rust语言安全编程实践",
    "nickname": "Liam"
  },
  {
    "title": "跨平台桌面应用开发指南",
    "nickname": "Mia"
  },
  {
    "title": "物联网设备数据安全传输",
    "nickname": "Noah"
  },
  {
    "title": "产品需求文档（PRD）撰写规范",
    "nickname": "Olivia"
  },
  {
    "title": "敏捷开发Scrum方法论实践",
    "nickname": "Peter"
  },
  {
    "title": "Python异步编程与性能调优",
    "nickname": "Quinn"
  },
  {
    "title": "5G网络切片技术综述",
    "nickname": "Riley"
  },
  {
    "title": "虚拟现实（VR）交互设计原则",
    "nickname": "Sophia"
  },
  {
    "title": "服务器less架构与FaaS应用",
    "nickname": "Tom"
  },
  {
    "title": "金融科技风控模型设计",
    "nickname": "Uma"
  },
  {
    "title": "React Hooks深度解析",
    "nickname": "Victor"
  },
  {
    "title": "智能家居系统集成方案",
    "nickname": "Willow"
  },
  {
    "title": "图数据库Neo4j实战应用",
    "nickname": "Xavier"
  },
  {
    "title": "自动化测试框架Selenium进阶",
    "nickname": "Yara"
  },
  {
    "title": "前端微服务架构实践",
    "nickname": "Zane"
  },
  {
    "title": "用户行为路径分析方法论",
    "nickname": "Amy"
  },
  {
    "title": "强化学习在游戏AI中的应用",
    "nickname": "Ben"
  },
  {
    "title": "Kubernetes集群管理与运维",
    "nickname": "Chloe"
  },
  {
    "title": "TypeScript类型系统高级技巧",
    "nickname": "Daniel"
  },
  {
    "title": "DevOps工具链与自动化部署",
    "nickname": "Emma"
  },
  {
    "title": "边缘计算数据处理优化",
    "nickname": "Finn"
  },
  {
    "title": "分布式事务解决方案对比",
    "nickname": "Gia"
  },
  {
    "title": "CSS Grid布局实战教程",
    "nickname": "Hugo"
  },
  {
    "title": "云计算资源调度策略优化",
    "nickname": "Iris"
  },
  {
    "title": "自然语言处理（NLP）情感分析",
    "nickname": "Jake"
  },
  {
    "title": "网络安全渗透测试流程",
    "nickname": "Kara"
  },
  {
    "title": "性能监控与APM系统建设",
    "nickname": "Leo"
  },
  {
    "title": "低代码平台技术架构研究",
    "nickname": "Mila"
  },
  {
    "title": "设计模式在Java项目中的应用",
    "nickname": "Nico"
  },
  {
    "title": "物联网操作系统FreeRTOS分析",
    "nickname": "Owen"
  },
  {
    "title": "A/B测试设计与结果评估",
    "nickname": "Penny"
  },
  {
    "title": "WebRTC实时通信技术栈",
    "nickname": "Quentin"
  },
  {
    "title": "数据仓库建模方法论",
    "nickname": "Ruby"
  },
  {
    "title": "SaaS产品定价策略分析",
    "nickname": "Sam"
  },
  {
    "title": "Docker镜像优化与瘦身",
    "nickname": "Tara"
  },
  {
    "title": "前端动画性能优化技巧",
    "nickname": "Uriel"
  },
  {
    "title": "机器学习模型可解释性（XAI）",
    "nickname": "Vera"
  },
  {
    "title": "微前端Single-SPA实践",
    "nickname": "Wyatt"
  },
  {
    "title": "AR增强现实交互界面设计",
    "nickname": "Yuna"
  },
  {
    "title": "分布式缓存Redis集群部署",
    "nickname": "Zoe"
  },
  {
    "title": "用户画像构建与应用",
    "nickname": "Alex"
  },
  {
    "title": "微服务间通信模式对比",
    "nickname": "Beth"
  },
  {
    "title": "前端状态管理Pinia vs Vuex",
    "nickname": "Chris"
  },
  {
    "title": "C++ 内存管理与性能优化",
    "nickname": "Dina"
  },
  {
    "title": "GraphQL API 设计与实践",
    "nickname": "Ethan"
  },
  {
    "title": "推荐系统算法综述",
    "nickname": "Fiona"
  },
  {
    "title": "云计算成本优化策略",
    "nickname": "Gabe"
  },
  {
    "title": "WebGL 3D图形渲染入门",
    "nickname": "Holly"
  },
  {
    "title": "Elasticsearch全文检索优化",
    "nickname": "Ivan"
  },
  {
    "title": "Rust Web框架Actix-web实战",
    "nickname": "Jade"
  },
  {
    "title": "项目风险管理与应急预案",
    "nickname": "Kyle"
  },
  {
    "title": "Vue Router 深度配置与技巧",
    "nickname": "Lara"
  },
  {
    "title": "Linux内核参数调优指南",
    "nickname": "Max"
  },
  {
    "title": "敏捷测试与自动化集成",
    "nickname": "Nora"
  },
  {
    "title": "TypeScript Monorepo 最佳实践",
    "nickname": "Oscar"
  },
  {
    "title": "网络协议TCP/IP详解",
    "nickname": "Paige"
  },
  {
    "title": "设计系统规范制定与落地",
    "nickname": "Quincy"
  },
  {
    "title": "Serverless DevSecOps 流水线",
    "nickname": "Rose"
  },
  {
    "title": "Web Worker与多线程应用",
    "nickname": "Saul"
  },
  {
    "title": "Java虚拟机（JVM）性能监控",
    "nickname": "Tess"
  },
  {
    "title": "产品经理用户访谈技巧",
    "nickname": "Ulysses"
  },
  {
    "title": "前端单元测试Jest配置",
    "nickname": "Violet"
  },
  {
    "title": "Kubernetes Helm包管理",
    "nickname": "Walter"
  },
  {
    "title": "数据库索引设计与优化",
    "nickname": "Xena"
  },
  {
    "title": "React Native跨端性能比较",
    "nickname": "Yuji"
  },
  {
    "title": "日志分析ELK Stack实践",
    "nickname": "Zach"
  },
  {
    "title": "Web性能指标 Lighthouse 优化",
    "nickname": "Aaron"
  },
  {
    "title": "AIGC内容生成算法概述",
    "nickname": "Bella"
  },
  {
    "title": "React Server Components工作原理",
    "nickname": "Caleb"
  },
  {
    "title": "鸿蒙OS开发框架与生态",
    "nickname": "Doris"
  },
  {
    "title": "SvelteKit全栈开发实践",
    "nickname": "Edwin"
  },
  {
    "title": "事件驱动架构Kafka应用",
    "nickname": "Flora"
  },
  {
    "title": "数据脱敏与隐私保护技术",
    "nickname": "Gavin"
  },
  {
    "title": "前端打包工具Webpack/Vite对比",
    "nickname": "Hannah"
  },
  {
    "title": "微服务 API Gateway 选型",
    "nickname": "Isaac"
  },
  {
    "title": "低延迟直播推流技术研究",
    "nickname": "Jasmine"
  },
  {
    "title": "Web安全XSS/CSRF防御机制",
    "nickname": "Kevin"
  },
  {
    "title": "Git Flow与GitHub Flow工作流",
    "nickname": "Lily"
  },
  {
    "title": "DDD领域驱动设计实践",
    "nickname": "Marco"
  },
  {
    "title": "移动端性能监控SDK开发",
    "nickname": "Nelly"
  },
  {
    "title": "RESTful API 设计最佳实践",
    "nickname": "Omar"
  },
  {
    "title": "PostgreSQL高级查询优化",
    "nickname": "Pam"
  },
  {
    "title": "SRE站点可靠性工程实践",
    "nickname": "Rex"
  },
  {
    "title": "Web组件Shadow DOM应用",
    "nickname": "Ruby"
  },
  {
    "title": "Serverless数据库FaunaDB",
    "nickname": "Sean"
  },
  {
    "title": "前端异常监控与报警系统",
    "nickname": "Tina"
  },
  {
    "title": "产品迭代与版本管理策略",
    "nickname": "Vince"
  }
]

const ContentTestData = `
@: - 395 -
  - 用于同步抖音收藏夹以及我喜欢的视频，解决个人收藏和喜欢的视频容易失效的问题(dysync)

@Edward 庞总: - 402 - 801990
  - 一个轻量的在线 PDF 工具箱，基于 GhostScript 与 OCR 技术，提供浏览器端的 PDF 压缩与文字提取功能。无需复杂配置，挂载输入输出目录即可使用，适合个人与小型团队在本地或私有环境中快速处理 PDF。 (PDF工具箱)
    - File System 是一个面向个人与小团队的轻量级文件服务。它支持在本地或云端以浏览器管理与分发文件，提供图片、视频、音频与文档的直链预览、下载，以及基础的批量操作与目录递归浏览。 (File System)

@天天 韩总: - 496 - 801817
  - 极简自托管卡路里追踪器 - 轻松记录每日饮食，管理餐食和食材库，设置卡路里目标，追踪饮食进度。采用 Nord 主题，界面简洁美观，支持自定义时区偏移和数据库清理功能，是个人健康管理的理想工具。 (Calorific)
    - 自托管的 CalDAV 任务和日历管理系统 - 支持多账户、子任务、甘特图视图、日历视图，提供完整的任务管理解决方案。兼容 Nextcloud 和 Baikal，支持任务过滤、重复任务和 OAuth 认证。 (MMDL)
      - 简洁易用的家庭预算管理系统，支持支出跟踪、预算共享、月度报告，保护您的财务隐私. (Piglet)

@@卓帅 卓总: - 779 - 802883
  - PromptWorks 是一个聚焦 Prompt 资产管理与大模型运营的全栈解决方案，仓库内包含 FastAPI 后端与 Vue + Element Plus 前端。平台支持 Prompt 全生命周期管理、模型配置、版本对比与评估实验，为团队提供统一的提示词协作与测试工作台。 (PromptWorks)

@@yuan 丁总: - 801 - 901912
  - 一个能在远程机器上运行服务端、还能用现代浏览器直接访问的 VS Code 版本。 (OpenVSCode Server)

@@LiuQing 刘总: - 703 - 901839
  - Temporal 是开源的分布式工作流编排平台, 用于构建可靠、可扩展的应用程序。通过工作流和活动的概念, 提供自动重试、状态持久化、长时间运行、分布式事务等核心能力。本应用在 LazyCat 平台部署完整的 Temporal 服务, 包含 Server、Web UI 和 PostgreSQL 数据库, 开箱即用。适用于订单处理、支付流程、数据处理、微服务编排等场景。 (Temporal 工作流引擎)

@ponzS ponzS总: - 559 - 801906
  - 100 % 纯血去中心化分布式通信工具，完美适配懒猫微服硬件平台。 (TalkFlow)

@溴化锂 锂总: - 323 - 800832
  - llm 工作流(Dify)

@: - 2 -
  - 端口映射(局域网端口转发工具)
`

const MoenyTestData = [
  { "name": "科技实践第1篇科技实践第1篇", "type": "应用", "author": "刘静", "price": "602.51" },
  { "name": "创新探索第2篇", "type": "文章", "author": "杨军", "price": "459.88" },
  { "name": "未来指南第3篇", "type": "文章", "author": "赵洋", "price": "928.64" },
  { "name": "AI科技第4篇", "type": "应用", "author": "吴强", "price": "172.49" },
  { "name": "艺术未来第5篇", "type": "文章", "author": "张秀英", "price": "357.29" },
  { "name": "探索艺术第6篇", "type": "应用", "author": "李敏", "price": "789.12" },
  { "name": "编程指南第7篇", "type": "文章", "author": "陈磊", "price": "84.77" },
  { "name": "科技创新第8篇", "type": "应用", "author": "黄芳", "price": "605.39" },
  { "name": "未来实践第9篇", "type": "文章", "author": "王洋", "price": "201.46" },
  { "name": "艺术AI第10篇", "type": "应用", "author": "赵军", "price": "948.33" },
  { "name": "创新编程第11篇", "type": "文章", "author": "杨秀英", "price": "563.12" },
  { "name": "指南科技第12篇", "type": "应用", "author": "周伟", "price": "236.90" },
  { "name": "探索未来第13篇", "type": "文章", "author": "刘敏", "price": "705.81" },
  { "name": "AI实践第14篇", "type": "应用", "author": "陈军", "price": "427.36" },
  { "name": "科技艺术第15篇", "type": "文章", "author": "黄洋", "price": "159.75" },
  { "name": "创新探索第16篇", "type": "应用", "author": "张磊", "price": "384.09" },
  { "name": "未来指南第17篇", "type": "文章", "author": "李娜", "price": "971.42" },
  { "name": "编程创新第18篇", "type": "应用", "author": "赵强", "price": "518.00" },
  { "name": "科技未来第19篇", "type": "文章", "author": "吴军", "price": "232.76" },
  { "name": "艺术编程第20篇", "type": "应用", "author": "刘洋", "price": "807.67" },
  { "name": "探索实践第21篇", "type": "文章", "author": "王磊", "price": "141.89" },
  { "name": "创新AI第22篇", "type": "应用", "author": "周静", "price": "915.43" },
  { "name": "指南科技第23篇", "type": "文章", "author": "陈伟", "price": "329.66" },
  { "name": "未来探索第24篇", "type": "应用", "author": "黄军", "price": "758.02" },
  { "name": "AI艺术第25篇", "type": "文章", "author": "张秀英", "price": "691.17" },
  { "name": "创新实践第26篇", "type": "应用", "author": "李磊", "price": "279.55" },
  { "name": "科技探索第27篇", "type": "文章", "author": "赵娜", "price": "602.22" },
  { "name": "未来指南第28篇", "type": "应用", "author": "吴芳", "price": "956.84" },
  { "name": "艺术创新第29篇", "type": "文章", "author": "刘伟", "price": "354.50" },
  { "name": "探索未来第30篇", "type": "应用", "author": "王强", "price": "177.29" },
  { "name": "编程科技第31篇", "type": "文章", "author": "周洋", "price": "802.13" },
  { "name": "创新指南第32篇", "type": "应用", "author": "陈敏", "price": "224.41" },
  { "name": "科技实践第33篇", "type": "文章", "author": "黄磊", "price": "994.00" },
  { "name": "未来探索第34篇", "type": "应用", "author": "张静", "price": "187.03" },
  { "name": "艺术AI第35篇", "type": "文章", "author": "李军", "price": "905.61" },
  { "name": "探索艺术第36篇", "type": "应用", "author": "赵洋", "price": "643.48" },
  { "name": "科技创新第37篇", "type": "文章", "author": "吴伟", "price": "571.62" },
  { "name": "未来实践第38篇", "type": "应用", "author": "刘秀英", "price": "298.75" },
  { "name": "艺术AI第39篇", "type": "文章", "author": "王敏", "price": "459.19" },
  { "name": "创新编程第40篇", "type": "应用", "author": "周磊", "price": "886.84" },
  { "name": "指南科技第41篇", "type": "文章", "author": "陈军", "price": "514.36" },
  { "name": "探索未来第42篇", "type": "应用", "author": "黄洋", "price": "748.66" },
  { "name": "AI实践第43篇", "type": "文章", "author": "张伟", "price": "318.79" },
  { "name": "科技艺术第44篇", "type": "应用", "author": "李芳", "price": "707.95" },
  { "name": "创新探索第45篇", "type": "文章", "author": "赵军", "price": "642.04" },
  { "name": "未来指南第46篇", "type": "应用", "author": "吴静", "price": "276.55" },
  { "name": "编程创新第47篇", "type": "文章", "author": "刘磊", "price": "557.09" },
  { "name": "科技未来第48篇", "type": "应用", "author": "王洋", "price": "865.67" },
  { "name": "艺术编程第49篇", "type": "文章", "author": "周军", "price": "322.58" },
  { "name": "探索实践第50篇", "type": "应用", "author": "陈秀英", "price": "423.90" },
  { "name": "创新AI第51篇", "type": "文章", "author": "黄敏", "price": "293.44" },
  { "name": "指南科技第52篇", "type": "应用", "author": "张磊", "price": "176.32" },
  { "name": "未来探索第53篇", "type": "文章", "author": "李娜", "price": "568.13" },
  { "name": "AI艺术第54篇", "type": "应用", "author": "赵军", "price": "312.64" },
  { "name": "创新实践第55篇", "type": "文章", "author": "吴洋", "price": "726.78" },
  { "name": "科技探索第56篇", "type": "应用", "author": "刘伟", "price": "972.93" },
  { "name": "未来指南第57篇", "type": "文章", "author": "王强", "price": "214.05" },
  { "name": "艺术创新第58篇", "type": "应用", "author": "周洋", "price": "471.99" },
  { "name": "探索未来第59篇", "type": "文章", "author": "陈敏", "price": "808.56" },
  { "name": "编程科技第60篇", "type": "应用", "author": "黄磊", "price": "596.30" },
  { "name": "创新指南第61篇", "type": "文章", "author": "张静", "price": "473.09" },
  { "name": "科技实践第62篇", "type": "应用", "author": "李军", "price": "850.72" },
  { "name": "未来探索第63篇", "type": "文章", "author": "赵洋", "price": "297.18" },
  { "name": "艺术AI第64篇", "type": "应用", "author": "吴伟", "price": "195.94" },
  { "name": "探索艺术第65篇", "type": "文章", "author": "刘秀英", "price": "998.33" },
  { "name": "科技创新第66篇", "type": "应用", "author": "王敏", "price": "176.50" },
  { "name": "未来实践第67篇", "type": "文章", "author": "周磊", "price": "909.67" },
  { "name": "艺术AI第68篇", "type": "应用", "author": "陈军", "price": "463.07" },
  { "name": "创新编程第69篇", "type": "文章", "author": "黄洋", "price": "782.14" },
  { "name": "指南科技第70篇", "type": "应用", "author": "张伟", "price": "153.62" },
  { "name": "探索未来第71篇", "type": "文章", "author": "李芳", "price": "887.38" },
  { "name": "AI实践第72篇", "type": "应用", "author": "赵军", "price": "569.25" },
  { "name": "科技艺术第73篇", "type": "文章", "author": "吴静", "price": "476.88" },
  { "name": "创新探索第74篇", "type": "应用", "author": "刘磊", "price": "322.14" },
  { "name": "未来指南第75篇", "type": "文章", "author": "王洋", "price": "940.33" },
  { "name": "编程创新第76篇", "type": "应用", "author": "周军", "price": "385.41" },
  { "name": "科技未来第77篇", "type": "文章", "author": "陈秀英", "price": "673.80" },
  { "name": "艺术编程第78篇", "type": "应用", "author": "黄敏", "price": "191.36" },
  { "name": "探索实践第79篇", "type": "文章", "author": "张磊", "price": "552.00" },
  { "name": "创新AI第80篇", "type": "应用", "author": "李娜", "price": "671.45" },
  { "name": "指南科技第81篇", "type": "文章", "author": "赵军", "price": "237.64" },
  { "name": "未来探索第82篇", "type": "应用", "author": "吴洋", "price": "904.51" },
  { "name": "AI艺术第83篇", "type": "文章", "author": "刘伟", "price": "723.76" },
  { "name": "创新实践第84篇", "type": "应用", "author": "王强", "price": "457.10" },
  { "name": "科技探索第85篇", "type": "文章", "author": "周洋", "price": "774.06" },
  { "name": "未来指南第86篇", "type": "应用", "author": "陈敏", "price": "646.87" },
  { "name": "艺术创新第87篇", "type": "文章", "author": "黄磊", "price": "284.40" },
  { "name": "探索未来第88篇", "type": "应用", "author": "张静", "price": "935.67" },
  { "name": "编程科技第89篇", "type": "文章", "author": "李军", "price": "453.28" },
  { "name": "创新指南第90篇", "type": "应用", "author": "赵洋", "price": "734.96" },
  { "name": "科技实践第91篇", "type": "文章", "author": "吴伟", "price": "327.44" },
  { "name": "未来探索第92篇", "type": "应用", "author": "刘秀英", "price": "152.20" },
  { "name": "艺术AI第93篇", "type": "文章", "author": "王敏", "price": "825.10" },
  { "name": "探索艺术第94篇", "type": "应用", "author": "周磊", "price": "614.59" },
  { "name": "科技创新第95篇", "type": "文章", "author": "陈军", "price": "909.08" },
  { "name": "未来实践第96篇", "type": "应用", "author": "黄洋", "price": "566.32" },
  { "name": "艺术AI第97篇", "type": "文章", "author": "张伟", "price": "787.45" },
  { "name": "创新编程第98篇", "type": "应用", "author": "李芳", "price": "635.83" },
  { "name": "指南科技第99篇", "type": "文章", "author": "赵军", "price": "298.24" },
  { "name": "探索未来第100篇", "type": "应用", "author": "吴静", "price": "860.13" }
];

export {
  TabTestData,
  ContentTestData,
  MoenyTestData
}
