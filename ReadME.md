# PASCAL-5 DataSet

This is a python tool which help developers to extract pascal-5i dataset from pascal voc 2012 according to the paper `One-Shot Learning for Semantic Segmentation`This dataset is used to train the one-shot segmentation model.

## Requirements

- python 3.6
- packages:
	- glob
	- matplotlib
	- numpy
	- easydict

I highly recommend to install Anaconda instead of the original python

## Usage

organize the project like this,VOC2012 is the PASCAL VOC 2012 Dataset,PASCAL-5i is this project.

![](https://i.imgur.com/YSdzZAD.jpg)


Or you can change the datapath in `config.py`

For more specific information,please see `createDataSet.py`
