def get_succeded_file(file_name):
    return file_name.split("_")[1]

def create_array(file_name):
    with open(file_name, 'r+') as f:
        lines = [line[:-1] for line in f]
        f.close()
    return lines 

def fix_done(file):
    return_array = []
    for f in file:
        return_array.append(get_succeded_file(f))
    return return_array

def compare(done, _all):
    sDone = set(done)
    sAll = set(_all)
    return list(sAll.difference(sDone))

done_training = create_array('./training_atual.txt')
done_testing = create_array('./test_atual.txt')
all_training = create_array('./Lista_train2.txt')
all_testing = create_array('./Lista_test2.txt')

missing_training = compare(fix_done(done_training), all_training)
missing_testing = compare(fix_done(done_testing), all_testing)

print("________________________________________________________")
print(">>>>>>>>>>>>>>>>>>> TEST <<<<<<<<<<<<<<<<<<<")
print(missing_testing)
print("________________________________________________________")
print(">>>>>>>>>>>>>>>>>>> TRAIN <<<<<<<<<<<<<<<<<<<")
print(missing_training)
print("________________________________________________________")
print("LEN MISSING_TESTING >> ", len(missing_testing))
print("LEN DONE_TESTING >> ", len(done_testing))
print("LEN ALL_TESTING >> ", len(all_testing))
print("________________________________________________________")
print("LEN MISSING_TRAINING >> ", len(missing_training))
print("LEN DONE_TRAINING >> ", len(done_training))
print("LEN ALL_TRAINING >> ", len(all_training))