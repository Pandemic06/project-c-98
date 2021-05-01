def swapFileData():
    name1=input("Write first file")
    name2=input("Write second file")
    f1=open(name1,"r")
    read1=f1.read()
    f2=open(name2,"r")
    read2=f2.read()

    w1=open(name1,"w")
    w1.write(read2)
    w2=open(name2,"w")
    w2.write(read1)

swapFileData()