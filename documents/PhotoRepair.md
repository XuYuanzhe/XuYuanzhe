# Photo Repair 老照片修复
# **1、Bringing Old Photo Back to Life**

### 项目地址：

https://github.com/microsoft/Bringing-Old-Photos-Back-to-Life

项目依赖于「Synchronized-BatchNorm-PyTorch」，按照教程配置即可。

#### 第一步，clone 工程：

```
git clone https://github.com/microsoft/Bringing-Old-Photos-Back-to-Life.git
```

#### 第二步，进入工程目录，clone 依赖项目：

```
cd Face_Enhancement/models/networks/git clone https://github.com/vacancy/Synchronized-BatchNorm-PyTorchcp -rf Synchronized-BatchNorm-PyTorch/sync_batchnorm .cd ../../../
cd Global/detection_modelsgit clone https://github.com/vacancy/Synchronized-BatchNorm-PyTorchcp -rf Synchronized-BatchNorm-PyTorch/sync_batchnorm .cd ../../
```

#### 第三步，下载预训练模型。

```
cd Face_Detection/wget http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2bzip2 -d shape_predictor_68_face_landmarks.dat.bz2cd ../
```

然后分别下载 Global 和 Face_Enhancement 的训练好的模型，并解压，放在对应目录下：

Global：

https://facevc.blob.core.windows.net/zhanbo/old_photo/pretrain/Global/checkpoints.zip

Face_Enhancement：

https://facevc.blob.core.windows.net/zhanbo/old_photo/pretrain/Face_Enhancement/checkpoints.zip

**下载速度极慢，建议百度云**

```
网盘链接（提取码：jack）：

https://pan.baidu.com/s/1jVjd8dS0j0AnWeFI-7l-eA
```

#### 使用方法：

没有裂痕的图像修复，就是图片不清晰，可以用如下指令：

```
python run.py --input_folder [test_image_folder_path] \
              --output_folder [output_path] \
              --GPU 0
```

将你想修复的图片放到 [test_image_folder_path] 目录下（自己指定），生成的图片会放到 [output_path] 目录中。

对于裂痕的图片，需要额外增加一个参数，指令如下：

```
# 这里需要注意的是，指定的路径需要使用绝对路径
python run.py --input_folder [test_image_folder_path] \
              --output_folder [output_path] \
              --GPU 0 \
	      --with_scratch
```

# **2、DeOldify**

「DeOldify」是一个图片上色算法。

曾经上过热搜的修复百年前老北京的影像，就是用的这个算法。

一切都是现成的，用起来很简单。

DeOldify 就是一种对抗生成网络的应用。

其原理是使用 NoGAN 技术，它结合了 GAN 训练的优点，比如出色的上色效果，同时也消除了一些副作用，比如画面着色不稳定、闪烁的现象。

算法出了很久，算法原理教程应该很多，这里就不再累述，我们直接看怎么用吧。

## 项目地址：

https://github.com/jantic/DeOldify

**下载速度极慢，建议百度云**

```
网盘链接（提取码：jack）：

https://pan.baidu.com/s/17sma_a1ICJMY07KLnDpiww
```
