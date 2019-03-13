
from script.imgProcess import *
from script.splitDataSet import *

def generate_dataset(index):

    set_i(index)
    datalist_train,datalist_test=generate_datalist()
    vanishBg_batch(datalist_train,"train")
    vanishBg_batch(datalist_test,"test")

def generate_all():
    for i in range(4):
        print("generating pascal5-%d..."%i)
        generate_dataset(i)

if __name__=="__main__":
    generate_all()