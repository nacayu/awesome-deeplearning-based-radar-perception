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
- [📊 数据集 (Datasets)](#6-数据集-datasets)
- [🔧 工具 (Tools)](#7-工具-tools)

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
| 2021 | [Radar-PointGNN: Graph Based Object Recognition for Unstructured Radar Point-cloud Data](https://arxiv.org/) | 3D检测 | - | [知乎](https://zhuanlan.zhihu.com/p/549641548) | 基于GNN |
| 2019 | [2D Car Detection in Radar Data with PointNets](https://arxiv.org/) | 3D检测 | - | [知乎](https://zhuanlan.zhihu.com/p/568160922) | 改进PointNets |
| 2021 | [Improved Orientation Estimation and Detection with Hybrid Object Detection Networks for Automotive Radar](https://arxiv.org/) | BEV 2D检测 | - | - | 结合网格和点方法 |

### 2.2 多模态融合检测

| 年份 | 论文 | 任务 | 代码 | 中文解读 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- |
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
| 2022 | [K-Radar: 4D Radar Object Detection for Autonomous Driving](https://arxiv.org/) | 3D检测 | [GitHub](https://github.com/kaist-avelab/k-radar) | - | 4D雷达，各种天气条件 |

---

## 3. 分割 (Segmentation)

| 年份 | 论文 | 任务 | 代码 | 中文解读 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2022 | [A Simple Baseline for BEV Perception Without LiDAR](https://arxiv.org/) | BEV分割 | [GitHub](https://github.com/aharley/simple_bev) | [知乎](https://zhuanlan.zhihu.com/p/568160922) | 基于nuScenes |
| 2021 | [RadSegNet: A Reliable Approach to Radar Camera Fusion](https://arxiv.org/) | 语义分割 | - | [知乎](https://zhuanlan.zhihu.com/p/568160922) | RADIATE数据集 |
| 2021 | [NVRadarNet: Real-Time Radar Obstacle and Free Space Detection](https://arxiv.org/) | Freespace | - | [知乎](https://zhuanlan.zhihu.com/p/575385783) | 实时(1.5ms)BEV多任务 |
| 2021 | [Radar Occupancy Prediction With Lidar Supervision](https://arxiv.com/) | Freespace | - | [知乎](https://zhuanlan.zhihu.com/p/568160922) | LiDAR监督生成 |
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

## 6. 数据集 (Datasets)

### 6.1 传统毫米波雷达

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

### 6.2 4D雷达

| 数据集 | 传感器 | 场景 | 链接 | 备注 |
| :--- | :--- | :--- | :--- | :--- |
| [TJ4DRadSet](https://github.com/TJRadarLab/TJ4DRadSet) | radar camera lidar | 驾驶 | [博客](https://blog.csdn.net/u013019296/article/details/127219137) | 支持tracking |
| [K-Radar](https://github.com/kaist-avelab/K-Radar) | camera lidar radar | 各种天气 | - | 4D tensor数据 |

---

## 7. 工具 (Tools)

### 雷达数据处理

- [RADDet](https://github.com/ZhangAoCanada/RADDet) - 雷达点云表示
- [mmWave Radar Camera Fusion](https://github.com/nacayu/CRFNet_Tensorflow2.4.1) - 雷达-相机融合基线

---

## 📝 更新日志

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