from easydict import EasyDict as edict

config=edict()
config.class_list=['aeroplane','bicycle','bird','boat','bottle','bus','car','cat','chair','cow','diningtable','dog','horse','motorbike','person','pottedplant','sheep','sofa','train','tvmonitor']
config.color_map=[[128,0,0],[0,128,0],[128,128,0],[0,0,128],[128,0,128],[0,128,128],[128,128,128],[64,0,0],[192,0,0],[64,128,0],[192,128,0],[64,0,128],[192,0,128],[64,128,128],[192,128,128],[0,64,0],[128,64,0],[0,192,0],[128,192,0],[0,64,128]]

config.txt_path='../voc2012/ImageSets/Main/'
config.img_path='../voc2012/JPEGImages/'
config.annotations_path='../voc2012/SegmentationClass/'
config.save_dir='./pascal-5/'

config.current_index=0    #0,1,2,3
config.pascal5_classlist=config.class_list[config.current_index*5:config.current_index+5]
config.pascal5_colormap=config.color_map[config.current_index*5:config.current_index+5]

