import os

def read_csv(filename):
    try:
        with open(filename, 'r') as f:
            raw_data = f.readlines()
            
        for line in range(len(raw_data)):
            raw_data[line] = list(map(int,raw_data[line].strip().split(',')))
            
        return raw_data
    except:
        print("Data wasn't processed correctly")
        raise
        
            
        
def read_folder(path : str,delimiter = -1):
    imagenes = {}
    try:
        for files in os.listdir(path)[:delimiter]:
            imagenes[files] = read_csv(path + "/" + files) 
        return imagenes
    except:
        print("A file might have a problem")
        

sanosx = read_folder("datasets\csv\enfermo_csv",2)
print(sanosx)

            
            
    
