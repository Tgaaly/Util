import scipy.io

def loadMat(path, varname):
    
    print 'loading mat file' 
    datasets = scipy.io.loadmat(path)
    
    data = datasets[varname]
    data = data[0]
    
    print data[0]
    print data[0][0]
    print data[0][1]
    
    x = data[0][0]
    y = data[0][1]

    print 'loaded'