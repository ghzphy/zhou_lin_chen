# -- coding:utf-8
import os

# f2 = open('test.txt','w')
# files = os.listdir('D:\\文档\\Github\\ghzphy.github.io\\Relax\\music\\music_files\\')
# file_list = []
# files.sort()
# print(len(files),files)
# files.remove('新建文件夹')
# num = 0
# f2.write('<tr>\n')
# for file in files:
#     num += 1
#     name = file.strip('.mp3').split('_')[-1]
#     f2.write('<td>{0:}{1:}\n\t<audio controls="controls">\
#              \n\t<source src="./music_files/{2:}" type="audio/mp3" />\
#              \n\t<embed height="100" width="100" src="./music_files/{2:}" />\
#              \n</audio>\n</td>\n'.format('&nbsp;'*(7-len(name)),name,file))
#     if num%3 ==0 : f2.write('</tr>\n\n<tr>\n')

# f2.close()


# f2 = open('test.txt','w')
files1 = os.listdir('.\\other_music\\music')
# files2 = os.listdir('.\\image')
ls1 = [i.split('.mp3')[0] for i in files1]
# ls2 = [i.split('.png')[0] for i in files2]

print(ls1)
# os.chdir('.\\image')


# f2 = open('林俊杰.png','r',encoding='utf-8')
# content2 = f2.readlines()

# f3 = open('陈奕迅.png','r',encoding='utf-8')
# content3 = f3.readlines()

import sys
for i in ls1:
    if i not in ls2:
        print(i)
        # os.system('copy 周杰伦.png 周杰伦 - 林俊杰.png')
        # sys.exit()
        # if i.split(' - ')[0] == '林俊杰': 

        #     with open('{}.png'.format(i),'w') as ff2:
        #         ff2.writelines(content2)
        # if i.split(' - ')[0] == '陈奕迅': 
        #     with open('{}.png'.format(i),'w') as ff3:
        #         ff3.writelines(content3)