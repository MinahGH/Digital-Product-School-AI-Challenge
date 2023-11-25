import pickle
import os 

def load_pickle_file(path):
    file_name = os.path.join(os.getcwd(),path)
    loaded_pickle = pickle.load(open(file_name, "rb"))
    return loaded_pickle