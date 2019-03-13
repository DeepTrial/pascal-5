import numpy as np
import operator,os
from config import config
from matplotlib import pyplot as plt
from .txtSolver import record

def bg_vanish(groundtruth,objective_color):
    assert(groundtruth.shape[2])
    height,width=groundtruth.shape[:2]
    for hi in range(height):
        for wj in range(width):
            temp=(groundtruth[hi,wj]*256).astype(np.uint8).tolist()
            if not operator.eq(temp,objective_color):
                groundtruth[hi, wj]=[0,0,0]
            else:
                groundtruth[hi, wj] = [255, 255, 255]
    return groundtruth/255.0


def vanishBg_batch(dataDict,datatype):
    for subclass,datalist in dataDict.items():
        imglist = []
        for imgindex in datalist:
            image=plt.imread(config.img_path+imgindex+'.jpg')
            if os.path.exists(config.annotations_path+imgindex+'.png'):
                groundtruth=plt.imread(config.annotations_path+imgindex+'.png')
                gt_vanish=bg_vanish(groundtruth,config.color_map[config.class_list.index(subclass)])
                save_pair(imgindex,image,gt_vanish,datatype)
                imglist.append(imgindex)
            else:
                continue
        record(config.save_dir+str(config.current_index)+'/'+datatype+'/'+subclass,imglist)

def save_pair(name,image,groundtruth,datatype):
    if not os.path.exists(config.save_dir+str(config.current_index)+'/'+datatype):
        os.makedirs(config.save_dir+str(config.current_index)+'/'+datatype+'/')
        os.makedirs(config.save_dir + str(config.current_index) + '/' + datatype+'/origin/')
        os.makedirs(config.save_dir + str(config.current_index) + '/' + datatype+ '/groundtruth/')

    plt.imsave(config.save_dir+str(config.current_index)+ '/' + datatype+'/origin/'+name+'.jpg',image)
    plt.imsave(config.save_dir + str(config.current_index)+ '/' + datatype + '/groundtruth/' + name + '.jpg',groundtruth)



