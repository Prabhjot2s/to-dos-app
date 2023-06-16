content=['hello','how','bye']

files=['file1.txt','file2.txt','file3.txt']

for i,j in zip(content,files):
    file=open(j,'w')
    file.writelines(i)
    file.close()


filename=["1.doc","2.report","3.presentation"]

filename=[filenam.replace('.','-') for filenam in filename]


#print(filename)