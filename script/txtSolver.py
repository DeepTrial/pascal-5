
def solver(filepath):
    valid_data=[]
    with open(filepath) as txtfile:
        lines=txtfile.readlines()
        for single_line in lines:
            line_data=single_line.replace('\n',' ').split(' ')
            line_data.remove('')
            if line_data[1]=='1':
                valid_data.append(line_data[0])
    return valid_data

def record(filename,content):
    with open(filename+'.txt','w+') as writer:
        for index in content:
            writer.write(index+'\n')


#data=solver('../ImageSets/Main/aeroplane_train.txt')
