# CCNet_PyTorch

- 论文链接：[CCNet: Criss-Cross Attention for Semantic Segmentation](http://cn.arxiv.org/pdf/1811.11721.pdf)

- CCNet网络结构图：
![](https://blog-1258986886.cos.ap-beijing.myqcloud.com/paper/18-3.jpg)

## Installation
- 环境: Python3.6, Pytorch1.0
- CCNet网络代码: CC.py, ccnet.py

## 实验数据集介绍
- 一副无人机拍摄的高分辨率矿区影像图
- 实验室进行标注的对应label
- 进行裁剪后的320 x 320的图像与label数据

## 实验代码说明

## 实验版本及结果记录
- CCNet_v0403版本：参考大佬代码，使用了辅助loss，对结果的两个输出分别求loss，得到的模型效果很差。
  - ps：应该是自己对该代码实验的理解有误，后期改为论文中的样例，cat[x,x_dsn]，进行分割
