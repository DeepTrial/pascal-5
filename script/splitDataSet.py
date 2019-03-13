from config import config
from .txtSolver import solver
from matplotlib import pyplot as plt

from glob import glob


def generate_datalist():
    datalist_train={}
    datalist_test={}
    for subclass in config.pascal5_classlist:
        filename=subclass+'_train.txt'
        datalist_train[subclass]=solver(config.txt_path+filename)

        filename = subclass + '_val.txt'
        datalist_test[subclass] = solver(config.txt_path + filename)
    return datalist_train,datalist_test


def set_i(index):
    config.current_index=index
    config.pascal5_classlist = config.class_list[config.current_index * 5:config.current_index + 5]
    config.pascal5_colormap = config.color_map[config.current_index * 5:config.current_index + 5]





#image=plt.imread('../SegmentationClass/2008_002032.png')

#datalist=generate_datalist()
#print(datalist["aeroplane"])
