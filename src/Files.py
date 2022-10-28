class FileHandler:
    def __init__(self,str,InputFormat=0):
        with open(str,'r') as f:
            lines = f.readlines()

        L = len(lines)
                                                                                    #if InputFormat = 0, interpret as HEX, else interpret as text
        if(InputFormat==1):
            data = ''.join(lines[0:L-2]).encode('utf-8')                            #Data stored on 1st line of txt file, Key stored on 2nd Line, IV stored on 3rd Line
            d = list(data)
            d.pop()                                                                 #Assembling list of Data values
        
        else:
            d = []
            data = []
            for line in lines[0:L-2]:
                data.append(line[:-1])
            data = ''.join(data)
            for i in range(0,len(data),2):
                temp = int(data[i:i+2],16)
                d.append(temp)
        
        while(len(d)%16!=0):
            d.append(0)
      
        k = []
        key = lines[L-2][:-1]
        for i in range(0,len(key),2):
            temp = int(key[i:i+2],16)
            k.append(temp)

        IV = []
        IVstr = lines[L-1]
        for i in range(0,len(IVstr),2):
            temp = int(IVstr[i:i+2],16)
            IV.append(temp) 

        self.DK = [d,k,IV]

    def getKey(self):
        return self.DK[1]

    def getIV(self):
        return self.DK[2]

    def getData(self):
        return self.DK[0]
