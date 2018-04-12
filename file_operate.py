import os
helloFile = open ('c:\\myPython\\abc.txt','r')
oldContent = helloFile.read()
print('The old content was\n' + oldContent + '\n\n\n')
helloFile.close()

helloFile = open ('c:\\myPython\\abc.txt','w')
helloFile.write('This is the first content\n')
helloFile.close()

helloFile = open ('c:\\myPython\\abc.txt','r')
new1Content = helloFile.read()
print('The first new message is\n' + new1Content +'\n\n')
helloFile.close()


helloFile = open ('c:\\myPython\\abc.txt','a')
helloFile.write('This is the second content.\n')
helloFile.close()

helloFile = open ('c:\\myPython\\abc.txt','r')
new2Content = helloFile.read()
helloFile.close()
print('The new + second message is\n' + new2Content)
