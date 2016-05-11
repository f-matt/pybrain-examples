from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

MAX_EPOCHS = 100
TOLERANCE = 0.01

def create_ann():
    net = buildNetwork(10, 2, 4, bias=True)
    ds = SupervisedDataSet(10, 4)
    
    fid = open("data/features.csv", "r")
    lines = fid.readlines()
    fid.close()
    
    for line in lines:
        fields = map(float, line.rstrip("\n").split(";"))
        ds.addSample(fields[0:10], fields[10:14])
    
    trainer = BackpropTrainer(net, ds)
    
    for i in range(MAX_EPOCHS):
        error = trainer.train()
        print "Epoch: ", i + 1
        print "Error: ", error
        
        if error <= TOLERANCE:
            break 
    
    
    right = 0
    wrong = 0
    
    for s in ds:
        patt = s[0]
        out = s[1]
        
        exp_idx = out.argmax()
        
        output = net.activate(s[0])
        
        max_val = output.max()
        
        if (output.tolist().count(max_val) == 1):
            idx = output.argmax()
        
            if exp_idx == idx:
                right += 1
            else:
                wrong += 1
        else:
            wrong += 1
    
    print float(right) / (right + wrong)
        
#        print s[0]

        
