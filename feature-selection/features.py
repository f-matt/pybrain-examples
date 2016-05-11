from random import random

def create_feature_vectors():
    
    ds = []
    
    # Four classes
    for c in range(4):
        # 20 vectors for each class
        for i in range(20):
            v = []
            # 10 features for each vector
            for i in range(10):
                # First two features provide data separation
                if i == 0:
                    if c == 0 or c == 3:
                        v.append(0.5 * random())
                    else:
                        v.append(0.5 + 0.5 * random())
                elif i == 1:
                    if c == 0 or c == 1:
                        v.append(0.5 * random())
                    else:
                        v.append(0.5 + 0.5 * random())         
                else:
                    v.append(random())    
            
            ds.append((v, c))
    
    print len(ds)
    
    lines = []
    for k, v in ds:
        line = ';'.join(map(str,k)) + ";" + str(v) + "\n"
        lines.append(line)
        
    fid = open("data/features.csv", "w")
    fid.writelines(lines)
    fid.close();
        
                    
            
            
    
    