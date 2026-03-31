# 🚗 Awesome Deep Learning based Radar Perception

[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![ stars](https://img.shields.io/github/stars/nacayu/awesome-deeplearning-based-radar-perception.svg)](https://github.com/nacayu/awesome-deeplearning-based-radar-perception/stargazers)
[![ forks](https://img.shields.io/github/forks/nacayu/awesome-deeplearning-based-radar-perception.svg)](https://github.com/nacayu/awesome-deeplearning-based-radar-perception/network/members)

> 面向自动驾驶的深度学习雷达感知论文、代码、数据集精选

## 📌 目录

- [📖 综述 (Surveys)](#1-综述-surveys)
- [🎯 目标检测 (Detection)](#2-目标检测-detection)
  - [2.1 单模态雷达检测](#21-单模态雷达检测)
  - [2.2 多模态融合检测](#22-多模态融合检测)
  - [2.3 4D雷达检测](#23-4d雷达检测)
- [🗺️ 分割 (Segmentation)](#3-分割-segmentation)
- [📏 深度估计 (Depth Estimation)](#4-深度估计-depth-estimation)
- [🔄 跟踪 (Tracking)](#5-跟踪-tracking)
- [🌐 世界模型 (World Models)](#6-世界模型-world-models)
- [🎨 3DGS/4DGS](#7-3dgs4dgs)
- [🤖 VLA (Vision-Language-Action)](#8-vla-vision-language-action)
- [📊 数据集 (Datasets)](#9-数据集-datasets)
- [🔧 工具 (Tools)](#10-工具-tools)

---

## 1. 综述 (Surveys)

| 年份 | 论文 | 摘要 | 中文解读 | 代码 |
| :--- | :--- | :--- | :--- | :--- |
| 2024 | [MmWave Radar and Vision Fusion for Object Detection in Autonomous Driving: A Review](https://arxiv.org/) | 自动驾驶中毫米波雷达与视觉融合的综述 | - | - |
| 2022 | [Towards Deep Radar Perception for Autonomous Driving: Datasets, Methods, and Challenges](https://arxiv.org/) | 面向自动驾驶的深度雷达感知:数据集、方法和挑战 | - | - |

---

## 2. 目标检测 (Detection)

### 2.1 单模态雷达检测

| 年份 | 论文 | 任务 | 代码 | 中文解读 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2025 | [TransRAD: Retentive Vision Transformer for Enhanced Radar Object Detection](https://arxiv.org/abs/2501.17977) | 3D检测 | - | - | [4D雷达] 利用Retentive Vision Transformer改进雷达目标检测 |
| 2025 | [SpikingRTNH: Spiking Neural Network for 4D Radar Object Detection](https://arxiv.org/abs/2502.00074) | 3D检测 | - | - | [4D雷达] 首个用于4D雷达目标检测的脉冲神经网络 |
| 2024 | [RadarNeXt: Real-Time and Reliable 3D Object Detector Based On 4D mmWave Imaging Radar](https://arxiv.org/abs/2501.02314) | 3D检测 | [GitHub](https://github.com/Pay246-git468/RadarNeXt) | - | [4D雷达] 实时可靠的4D毫米波成像雷达3D目标检测器 |
| 2021 | [Radar-PointGNN: Graph Based Object Recognition for Unstructured Radar Point-cloud Data](https://arxiv.org/) | 3D检测 | - | [知乎](https://zhuanlan.zhihu.com/p/549641548) | 基于GNN |
| 2019 | [2D Car Detection in Radar Data with PointNets](https://arxiv.org/) | 3D检测 | - | [知乎](https://zhuanlan.zhihu.com/p/568160922) | 改进PointNets |
| 2021 | [Improved Orientation Estimation and Detection with Hybrid Object Detection Networks for Automotive Radar](https://arxiv.org/) | BEV 2D检测 | - | - | 结合网格和点方法 |

### 2.2 多模态融合检测

| 年份 | 论文 | 任务 | 代码 | 中文解读 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026 | [RadarXFormer: Robust Object Detection via Cross-Dimension Fusion of 4D Radar Spectra and Images for Autonomous Driving](https://arxiv.org/abs/2603.14822) | 3D检测 | - | - | [4D雷达] 跨维度融合4D雷达频谱与图像的鲁棒3D目标检测 |
| 2026 | [Boosting Instance Awareness via Cross-View Correlation with 4D Radar and Camera for 3D Object Detection](https://arxiv.org/abs/2602.20632) | 3D检测 | - | - | [4D雷达] 通过跨视角相关性增强实例感知 |
| 2026 | [R4Det: 4D Radar-Camera Fusion for High-Performance 3D Object Detection](https://arxiv.org/abs/2603.09805) | 3D检测 | - | - | [4D雷达] 高性能4D雷达-相机融合3D检测 |
| 2026 | [Wavelet-based Multi-View Fusion of 4D Radar Tensor and Camera for Robust 3D Object Detection](https://arxiv.org/abs/2512.22972) | 3D检测 | - | - | [4D雷达] 基于小波的多视角融合 |
| 2025 | [RadarMP: Motion Perception for 4D mmWave Radar in Autonomous Driving](https://arxiv.org/abs/2511.12117) | 3D检测 | - | - | [4D雷达] 4D毫米波雷达运动感知 |
| 2025 | [All You Need for Object Detection: From Pixels, Points, and Prompts to Next-Gen Fusion and Multimodal LLMs](https://arxiv.org/abs/2510.10753) | 3D检测 | - | - | 多模态LLM融合 |
| 2025 | [MLF-4DRCNet: Multi-Level Fusion with 4D Radar and Camera for 3D Object Detection in Autonomous Driving](https://arxiv.org/abs/2509.18613) | 3D检测 | - | - | [4D雷达] 多层级融合 |
| 2025 | [SpaRC-AD: A Baseline for Radar-Camera Fusion in End-to-End Autonomous Driving](https://arxiv.org/abs/2508.10567) | 端到端 | - | - | [4D雷达] 端到端融合基线 |
| 2025 | [Zfusion: An Effective Fuser of Camera and 4D Radar for 3D Object Perception in Autonomous Driving](https://arxiv.org/abs/2504.03438) | 3D检测 | - | - | [4D雷达] 有效融合器 |
| 2025 | [Revisiting Radar Camera Alignment by Contrastive Learning](https://arxiv.org/abs/2504.02267) | 3D检测 | - | - | 对比学习对齐 |
| 2025 | [HGSFusion: Radar-Camera Fusion with Hybrid Generation and Synchronization for 3D Object Detection](https://arxiv.org/abs/2412.11489) | 3D检测 | - | - | [4D雷达] 混合生成同步融合 |
| 2025 | [Depth-aware Fusion Method based on Image and 4D Radar Spectrum for 3D Object Detection](https://arxiv.org/abs/2502.15516) | 3D检测 | - | - | [4D雷达] 深度感知融合 |
| 2023 | [RADIANT: Radar-Image Association Network for 3D Object Detection](https://arxiv.org/) | 3D检测 | [GitHub](https://github.com/longyunf/radiant) | [知乎](https://zhuanlan.zhihu.com/p/597739906) | 雷达-图像关联网络 |
| 2023 | [CRAFT: Camera-Radar 3D Object Detection with Spatio-Contextual Fusion Transformer](https://arxiv.org/) | 3D检测 | - | [知乎](https://zhuanlan.zhihu.com/p/581055339) | 空间-语义信息互补 |
| 2022 | [A frustum proposal-based 3D object detection network for multi-stage fusion in autonomous driving](https://arxiv.org/) | 3D检测 | [GitHub](https://github.com/brandesjj/centerfusionpp) | [知乎](https://zhuanlan.zhihu.com/p/603398636) | 基于CenterFusion改进 |
| 2021 | [CenterFusion: Center-based Radar and Camera Fusion for 3D Object Detection](https://arxiv.org/) | 3D检测 | [GitHub](https://github.com/mrnabati/CenterFusion) | [知乎](https://zhuanlan.zhihu.com/p/508905129) | 基于CenterNet |
| 2021 | [Bridging the View Disparity of Radar and Camera Features for Multi-modal Fusion 3D Object Detection](https://arxiv.org/) | 3D检测 | - | [知乎](https://zhuanlan.zhihu.com/p/568160922) | Conv-LSTM融合多帧 |
| 2021 | [CRFNet: Camera and Radar Fusion Network](https://arxiv.org/) | 2D检测 | [GitHub](https://github.com/nacayu/CRFNet_Tensorflow2.4.1) | [知乎](https://zhuanlan.zhihu.com/p/112578232) | 基于YOLOv3经典网络 |
| 2021 | [SAF-FCOS: Spatial Attention Fusion for Obstacle Detection using MmWave Radar and Vision Sensor](https://arxiv.org/) | 2D检测 | [GitHub](https://github.com/Singingkettle/SAF-FCOS) | [CSDN](https://blog.csdn.net/weixin_43253464/article/details/124376444) | 基于FCOS |
| 2021 | [GRIF Net: Gated Region of Interest Fusion Network for Robust 3D Object Detection](https://arxiv.org/) | 3D检测 | - | - | 二阶段检测，自适应融合 |
| 2022 | [CramNet: Camera-Radar Fusion with Ray-Constrained Cross-Attention](https://arxiv.org/) | 3D检测 | - | - | 射线约束交叉注意力 |
| 2022 | [DeepFusion: A Robust and Modular 3D Object Detector](https://arxiv.org/) | 3D检测 | - | [知乎](https://zhuanlan.zhihu.com/p/578655032) | 模块化设计 |
| 2021 | [TransFuser: Multi-Modal Fusion Transformer for End-to-End Autonomous Driving](https://arxiv.org/) | 路径预测 | [GitHub](https://github.com/autonomousvision/transfuser) | [知乎](https://zhuanlan.zhihu.com/p/508898376) | Transformer融合 |

### 2.3 4D雷达检测

| 年份 | 论文 | 任务 | 代码 | 中文解读 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026 | [4D-CAAL: 4D Radar-Camera Calibration and Auto-Labeling for Autonomous Driving](https://arxiv.org/abs/2601.21454) | 标定 | - | - | 自动标注 |
| 2026 | [Doracamom: Joint 3D Detection and Occupancy Prediction with Multi-view 4D Radars and Cameras for Omnidirectional Perception](https://arxiv.org/abs/2501.15394) | 检测+占用 | - | - | 全向感知 |
| 2025 | [RQR3D: Reparametrizing the regression targets for BEV-based 3D object detection](https://arxiv.org/abs/2505.17732) | 3D检测 | - | - | 回归目标重参数化 |
| 2025 | [Efficient On-Chip Implementation of 4D Radar-Based 3D Object Detection on Hailo-8L](https://arxiv.org/abs/2505.00757) | 3D检测 | - | - | 芯片实现 |
| 2025 | [L2RDaS: Synthesizing 4D Radar Tensors for Model Generalization via Dataset Expansion](https://arxiv.org/abs/2503.03637) | 数据增强 | - | - | 数据集扩展 |
| 2022 | [K-Radar: 4D Radar Object Detection for Autonomous Driving](https://arxiv.org/) | 3D检测 | [GitHub](https://github.com/kaist-avelab/k-radar) | - | 4D雷达，各种天气条件 |

### 2.4 雷达+3DGS检测

| 年份 | 论文 | 任务 | 代码 | 中文解读 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2025 | [RaGS: Unleashing 3D Gaussian Splatting from 4D Radar and Monocular Cues for 3D Object Detection](https://arxiv.org/abs/2507.19856) | 3D检测 | - | - | 3DGS+4D雷达 |

---

## 3. 分割 (Segmentation)

| 年份 | 论文 | 任务 | 代码 | 中文解读 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2022 | [A Simple Baseline for BEV Perception Without LiDAR](https://arxiv.org/) | BEV分割 | [GitHub](https://github.com/aharley/simple_bev) | [知乎](https://zhuanlan.zhihu.com/p/568160922) | 基于nuScenes |
| 2021 | [RadSegNet: A Reliable Approach to Radar Camera Fusion](https://arxiv.org/) | 语义分割 | - | [知乎](https://zhuanlan.zhihu.com/p/568160922) | RADIATE数据集 |
| 2021 | [NVRadarNet: Real-Time Radar Obstacle and Free Space Detection](https://arxiv.org/) | Freespace | - | [知乎](https://zhuanlan.zhihu.com/p/575385783) | 实时(1.5ms)BEV多任务 |
| 2021 | [Radar Occupancy Prediction With Lidar Supervision](https://arxiv.org/) | Freespace | - | [知乎](https://zhuanlan.zhihu.com/p/568160922) | LiDAR监督生成 |
| 2021 | [See Through Smoke: Robust Indoor Mapping with Low-cost mmWave Radar](https://arxiv.org/) | 稠密点云 | - | [知乎](https://zhuanlan.zhihu.com/p/568160922) | 室内建图 |

---

## 4. 深度估计 (Depth Estimation)

| 年份 | 论文 | 任务 | 代码 | 中文解读 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2021 | [Depth Estimation From Monocular Images and Sparse Radar](https://arxiv.org/) | 深度估计 | [GitHub](https://github.com/lochenchou/DORN_radar) | [知乎](https://zhuanlan.zhihu.com/p/568160922) | 序数回归，改进DORN |
| 2022 | [RCDPT: RADAR-CAMERA FUSION DENSE PREDICTION TRANSFORMER](https://arxiv.org/) | 深度估计 | - | - | 密集预测Transformer |

---

## 5. 跟踪 (Tracking)

| 年份 | 论文 | 任务 | 代码 | 中文解读 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2022 | [CFTrack: Center-based Radar and Camera Fusion for 3D Multi-Object Tracking](https://arxiv.org/) | 3D跟踪 | - | - | 端到端，基于CenterFusion |
| 2021 | [Radar-PointGNN: Graph Based Object Recognition for Unstructured Radar Point-cloud Data](https://arxiv.org/) | 跟踪 | - | [知乎](https://zhuanlan.zhihu.com/p/549641548) | 基于GNN |

---

## 6. 世界模型 (World Models)

| 年份 | 论文 | 任务 | 代码 | 中文解读 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026 | [Video Generation Models as World Models: Efficient Paradigms, Architectures and Algorithms](https://arxiv.org/abs/2603.14125) | 世界模型 | - | - | 视频生成作为世界模型 |
| 2026 | [Collision-Aware Vision-Language Learning for End-to-End Driving](https://arxiv.org/abs/2603.09746) | 端到端 | - | - | 碰撞感知VLM |
| 2026 | [Toward Physically Consistent Driving Video World Models](https://arxiv.org/abs/2603.17249) | 世界模型 | - | - | 物理一致性 |
| 2026 | [X-World: Controllable Ego-Centric Multi-Camera World Models](https://arxiv.org/abs/2603.08703) | 世界模型 | - | - | 多相机可控世界模型 |
| 2026 | [DriveVLM-RL: Neuroscience-Inspired Reinforcement Learning with Vision-Language Models](https://arxiv.org/abs/2603.06328) | 强化学习 | - | - | 神经科学启发的RL |
| 2026 | [VectorWorld: Efficient Streaming World Model via Diffusion Flow on Vector Graphs](https://arxiv.org/abs/2603.06820) | 世界模型 | - | - | 向量图扩散流 |
| 2026 | [From Virtual Environments to Real-World Trials: Emerging Trends in Autonomous Driving](https://arxiv.org/abs/2603.04708) | 综述 | - | - | 虚拟到现实趋势 |

---

## 7. 3DGS/4DGS

| 年份 | 论文 | 任务 | 代码 | 中文解读 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026 | [R-PGA: Robust Physical Adversarial Camouflage Generation via Relightable 3D Gaussian Splatting](https://arxiv.org/abs/2603.26067) | 对抗攻击 | - | - | [物理对抗] 利用可重光照3DGS生成鲁棒对抗纹理，抵御复杂动态场景 |
| 2026 | [StreetForward: Perceiving Dynamic Street with Feedforward Causal Attention](https://arxiv.org/abs/2603.19552) | 动态场景 | - | - | 前馈因果注意力 |
| 2026 | [Reconstruction Matters: Learning Geometry-Aligned BEV Representation through 3D Gaussian Splatting](https://arxiv.org/abs/2603.06223) | BEV表示 | - | - | 几何对齐BEV |
| 2026 | [LiDAR-EVS: Enhance Extrapolated View Synthesis for 3D Gaussian Splatting with Pseudo-LiDAR Supervision](https://arxiv.org/abs/2603.14763) | 视图合成 | - | - | LiDAR监督 |
| 2026 | [DynamicVGGT: Learning Dynamic Point Maps for 4D Scene Reconstruction](https://arxiv.org/abs/2603.04044) | 4D重建 | - | - | 动态点云图 |
| 2026 | [ReconDrive: Fast Feed-Forward 4D Gaussian Splatting for Autonomous Driving](https://arxiv.org/abs/2603.03906) | 场景重建 | - | - | 前馈4DGS |
| 2026 | [VG3S: Visual Geometry Grounded Gaussian Splatting for Semantic Occupancy Prediction](https://arxiv.org/abs/2603.05704) | 语义占用 | - | - | 几何 grounded |
| 2026 | [Transforming Omnidirectional RGB-LiDAR data into 3D Gaussian Splatting](https://arxiv.org/abs/2603.05395) | 数据转换 | - | - | 全向数据转GS |
| 2026 | [DiffusionHarmonizer: Bridging Neural Reconstruction and Photorealistic Rendering](https://arxiv.org/abs/2603.02789) | 重建+渲染 | - | - | 神经重建桥接 |

---

## 8. VLA (Vision-Language-Action)

| 年份 | 论文 | 任务 | 代码 | 中文解读 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026 | [Understanding Behavior Cloning with Action Quantization](https://arxiv.org/abs/2603.05887) | 行为克隆 | - | - | 动作量化 |
| 2026 | [Utonia: Toward One Encoder for All Point Clouds](https://arxiv.org/abs/2603.03438) | 点云编码 | - | - | 统一点云编码器 |
| 2025 | [VLA-R: Vision-Language Action Retrieval toward Open-World End-to-End Autonomous Driving](https://arxiv.org/abs/2511.12405) | 端到端 | - | - | [VLA] 开放世界端到端自动驾驶视觉语言动作检索 |
| 2025 | [ADVEDM: Fine-grained Adversarial Attack against VLM-based Embodied Agents](https://arxiv.org/abs/2509.15768) | 对抗攻击 | - | - | VLM对抗攻击 |
| 2025 | [TA-VLA: Elucidating the Design Space of Torque-aware Vision-Language-Action Models](https://arxiv.org/abs/2509.04637) | 机器人操作 | - | - | 力矩感知VLA |
| 2025 | [Unified Vision-Language-Action Model](https://arxiv.org/abs/2506.13935) | 统一模型 | - | - | 统一VLA |
| 2026 | [Out-of-Sight Embodied Agents: Multimodal Tracking, Sensor Fusion, and Trajectory Forecasting](https://arxiv.org/abs/2603.09719) | 多模态跟踪 | - | - | 具身智能体 |

---

## 9. 数据集 (Datasets)

### 9.1 传统毫米波雷达

| 数据集 | 传感器 | 场景 | 链接 | 备注 |
| :--- | :--- | :--- | :--- | :--- |
| [CRUW](http://www.cruwdataset.org/) | radar | 自动驾驶 | [GitHub](https://github.com/qian0105/CRUW_dataset) | 支持tracking |
| [CARRADA](https://github.com/valeoai/carrada_dataset) | camera radar | 道路 | - | 支持tracking, segmentation |
| [RADDet](https://github.com/ZhangAoCanada/RADDet) | radar | - | - | 雷达点云 |
| [nuScenes](https://nuscenes.org/) | radar camera lidar | 1000 scenes | - | 包含雷达数据 |
| [RadarScenes](https://radar-scenes.com/) | radar camera | 驾驶 | - | 点级别细粒度标注 |
| [RADIATE](http://pro.hw.ac.uk/radiate/) | radar camera lidar | 多种天气 | - | 支持tracking |
| [Pointillism](https://github.com/Kshitizbansal/pointillism-multi-radar-data) | radar camera lidar | - | - | 多雷达数据 |
| [Zendar](https://storage.googleapis.com/www.archive.zendar.io/dataset.html) | radar camera lidar | - | - | 支持tracking |

### 9.2 4D雷达

| 数据集 | 传感器 | 场景 | 链接 | 备注 |
| :--- | :--- | :--- | :--- | :--- |
| [TJ4DRadSet](https://github.com/TJRadarLab/TJ4DRadSet) | radar camera lidar | 驾驶 | [博客](https://blog.csdn.net/u013019296/article/details/127219137) | 支持tracking |
| [K-Radar](https://github.com/kaist-avelab/K-Radar) | camera lidar radar | 各种天气 | - | 4D tensor数据 |
| [OmniHD-Scenes](https://arxiv.org/abs/2412.13274) | 多模态 | 下一代 | - | 多模态数据集 |

---

## 10. 工具 (Tools)

### 雷达数据处理

- [RADDet](https://github.com/ZhangAoCanada/RADDet) - 雷达点云表示
- [mmWave Radar Camera Fusion](https://github.com/nacayu/CRFNet_Tensorflow2.4.1) - 雷达-相机融合基线

---

## 📝 更新日志

- **2026-04-01**: 新增World Models、3DGS/4DGS、VLA三个类别，更新2023-2026年新论文
- **2026-04-01**: 重构项目结构，按任务类型分类，增加目录导航
- 原始项目: [awesome-deeplearning-based-radar-perception](https://github.com/nacayu/awesome-deeplearning-based-radar-perception)

---

## 🤝 贡献

欢迎提交PR更新最新论文！请按以下格式提交:

```markdown
| 年份 | 论文标题 | 任务 | 代码链接 | 中文解读 | 备注 |
```

---

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=nacayu/awesome-deeplearning-based-radar-perception&type=Date)](https://star-history.com/#nacayu/awesome-deeplearning-based-radar-perception)

---

<p align="center">基于 <a href="https://github.com/nacayu">nacayu</a> 整理 | 自动更新</p>