import os 
from os import listdir
from os.path import isfile, join

# COMMAND: 
# python src_joint/main.py parse 
#     --model-path-base ./models/joint_bert_dev=95.55_devuas=96.67_devlas=94.86.pt 
#     --input-path ./input.txt  
#     --output-path-synconst output_synconst.txt 
#     --output-path-syndep output_syndephead.txt 
#     --output-path-synlabel output_syndeplabel.txt

## Exemple of OUTPUT: 2_4045_CLASS_0_synconst.txt
    #[0] 2 - Train / Test
    #[1] 4045 - File Number
    #[2] CLASS - Class indicator
    #[3] 0 - Class id
    #[4] synconst - Type of content

def create_ohsumed():
    OUTPUT = './Output/R8/'
    DEFAULT_PATH='./PreProcess/Output/R8-'
    TEST_TRAIN=['test/','train/']


    command_list = []
    for _type in TEST_TRAIN:
        INPUT_PATH = DEFAULT_PATH + _type  
        onlyfiles = [f for f in listdir(INPUT_PATH) if isfile(join(INPUT_PATH, f))]
        for _file in onlyfiles:
            FILE =  INPUT_PATH + _file + " "
            CMD = FILE[:-1]
            CMD = "python src_joint/main.py parse --model-path-base ./models/joint_bert_dev=95.55_devuas=96.67_devlas=94.86.pt "
            CMD = CMD + "--input-path " + FILE
            CMD = CMD + "--output-path-synconst " + OUTPUT + _type + _type[:-1] + '_' + _file.split(".")[0] + '_synconst.txt' + " "
            CMD = CMD + "--output-path-syndep " + OUTPUT + _type + _type[:-1] + '_' + _file.split(".")[0] + '_syndep.txt' + " "
            CMD = CMD + "--output-path-synlabel " + OUTPUT + _type + _type[:-1] + '_' + _file.split(".")[0] + '_synlabel.txt'
            command_list.append(CMD)
            # Fix files
 
    return command_list

print("Creating command list")
commands = create_ohsumed()
len_commnads = str(len(commands))
print("Command list created. There are", len_commnads, "commands to run")
i = 1
for command in commands:
    print("\t>> Running", str(i), "/", len_commnads)
    os.system(command)
    i = i + 1

print(commands[0])
# print("------------ Finished Processing ------------")
