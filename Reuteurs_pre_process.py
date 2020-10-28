import csv

OUTPUT = './PreProcess/Output/'
DEFAULT_PATH='./PreProcess/'
DATASETS=['R8/','R52/']
FILES=['test.txt','train.txt']



## dict_keys(['R8-test', 'R8-train', 'R52-test', 'R52-train'])
data = {}
for dataset in DATASETS:
    dset = dataset.split("/")[0]
    for f in FILES:
        tsv_file = open(DEFAULT_PATH + dataset + f)        
        read_tsv = csv.reader(tsv_file, delimiter="\t")        
        aux = []
        for row in read_tsv:
          aux.append(row)

        data[dset+'-'+f.split(".")[0]] = aux



for key in data.keys():    
    print(key)
    i = 0
    dict_size = len(data[key])
    out = OUTPUT+key+"/"
    while i < dict_size:
        file_name = str(i) + "-" + data[key][i][0] + ".txt"
        f = open(out + file_name, "w")
        f.write(data[key][i][1])
        f.close()
        i = i + 1
