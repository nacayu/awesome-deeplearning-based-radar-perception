# awesome-deeplearning-based-radar-perception 项目分析

## 当前项目结构

```
awesome-deeplearning-based-radar-perception/
└── README.md  (14647 bytes)
```

## 现有内容格式

### 1. Recent Papers 表格
| 字段 | 说明 |
|------|------|
| paper | 论文标题+年份 |
| task | 任务类型(3D detection, segmentation, tracking等) |
| sensors | 传感器类型(radar, camera, lidar组合) |
| github link | 代码链接 |
| 中文解读 | 中文解读链接(知乎) |
| remarks | 备注说明 |

### 2. Dataset 表格
| 字段 | 说明 |
|------|------|
| Dataset | 数据集名称 |
| sensor | 传感器配置 |
| 中文解读 | 中文解读链接 |
| link | 官方链接 |
| remarks | 备注 |

---

## 现有分类方式

### 任务类型 (Task)
- 3D detection
- 2D detection / 2D detection in BEV
- segmentation / freespace generation
- depth estimation
- object tracking
- route prediction

### 传感器类型
- radar only
- camera&radar
- lidar&radar
- camera&lidar&radar
- camera&4d radar

---

## 重构建议

### 1. 组织结构优化
建议采用多级分类:
```
├── 1. 综述 (Surveys)
├── 2. 目标检测 (Detection)
│   ├── 2D检测
│   ├── 3D检测
│   └── 多模态融合检测
├── 3. 分割 (Segmentation)
│   ├── BEV分割
│   ├── 语义分割
│   └── 可行驶区域(freespace)
├── 4. 深度估计 (Depth Estimation)
├── 5. 跟踪 (Tracking)
├── 6. 数据集 (Datasets)
└── 7. 传感器 (Sensors)
    ├── 毫米波雷达
    └── 4D雷达
```

### 2. 论文条目增强
每个论文条目建议包含:
- 年份
- 作者/机构
- 主要贡献
- 数据集性能
- 中文解读(如有)

### 3. 页面美化
- 使用GitHub风格的表格
- 添加标签徽章
- 按年份分组
- 添加目录导航

---

## 需要更新的类别

根据README内容，以下类别需要补充2023-2025年新论文:
1. **3D Detection** - 最多，需补充最新SOTA
2. **BEV Perception** - 重要方向
3. **4D Radar** - 新兴领域
4. **多模态融合** - 持续热点
5. **Tracking** - 需补充end-to-end方法