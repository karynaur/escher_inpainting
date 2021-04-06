from glob import glob
import os
import shutil



images = glob('./Escher Images/0/*')
for i in range(1,7):
   for j in glob(f'./Escher Images/{i}/*'):images.append(j)

print(len(images))
count=0
print(images[0])
for i in images:
   shutil.move(i,f'./Escher Images/{count}.png')
   count+=1
print(count)


