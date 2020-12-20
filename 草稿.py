files = ['0000000000.txt', '0000000004.txt', '0000000002.txt', '0000000001.txt', '0000000003.txt', '0000000006.txt',
         '0000000005.txt']
files.sort(key=lambda x:int(x[:-4]))
print(files)