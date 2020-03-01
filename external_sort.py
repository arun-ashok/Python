import os
def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0
        
def ext_sort():
    fh=open("temp_words_1.txt","rb",64*1024)
    i=0
    file_name="out"+str(i)+".txt"
    f2=open(file_name,"wb")
    for line in fh:
        f2.write(line)
        file_info = os.stat(file_name)
        size=convert_bytes(file_info.st_size)
        l1=size.split(' ')
        l2=l1[0].split('.')
        if(int(l2[0])>=300 and l1[1]=='MB'):
            f2.close()
            i=i+1            
            file_name="out"+str(i)+".txt"
            f2=open(file_name,"wb")
    fh.close()
    f2.close()


if __name__=="__main__":
    ext_sort()
