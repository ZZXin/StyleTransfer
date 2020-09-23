# StyleTransfer in ROS

## Introduction

使用Python+OpenCV+ROS实现图像风格迁移，虽然是4年前的项目，结合这个项目打通从基于深度网络的算法移植到嵌入式平台这条路。

## Environment

python2.7;opencv==4.1.0;ros-melodic;

## Get Start

```bash
# download source code
git clone https://github.com/StrangerZhang/pysot-toolkit
# create workspace
mkdir -p catkin_ws1/src
# move source code to /src
mv ../StyleTransfer/style ./catkin_ws1/src/
# compile
cd catkin_ws1
catkin_make
# source
source devel/setup.bash
# run
rosrun style style.py
# or
rosrun style style_camera.py
```
## References

- 知乎[1](https://zhuanlan.zhihu.com/p/129819763)、[2](https://zhuanlan.zhihu.com/p/129826350)
- csdn[1](https://blog.csdn.net/czp_374/article/details/81185603)
- opencv 官方调用代码[1](https://github.com/opencv/opencv/blob/3.4.0/samples/dnn/fast_neural_style.py)、[2](https://github.com/opencv/opencv/blob/master/samples/dnn/fast_neural_style.py)
- [官方训练代码](https://github.com/jcjohnson/fast-neural-style)

## Contact

Email: ZZXin00016@163.com
