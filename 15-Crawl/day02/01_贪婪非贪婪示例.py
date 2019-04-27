import re 

html = '''
<div><p>仰天大笑出门去</p></div>
<div><p>我辈岂是蓬蒿人</p></div>
'''
# 贪婪匹配 .*
p = re.compile('<div><p>.*</p></div>',re.S)
rList = p.findall(html)
print(rList)

# 非贪婪匹配 : .*?
p = re.compile('<div><p>.*?</p></div>',re.S)
rList = p.findall(html)
# print(rList)

str = '<p><img src="/media/goods/images/image_20190423153430_818.png" title="" alt="image.png"/> </p><p><img src="/media/goods/desc/微信图片_20190315113106_20190423155554_317.jpg" title="" alt="微信图片_20190315113106.jpg"/> </p><p><img src="/media/goods/images/image_20190423153502_255.png" title="" alt="image.png"/> </p><p><img src="/media/goods/images/image_20190423153516_460.png" title="" alt="image.png"/> </p><p><img src="/media/goods/images/image_20190423153532_622.png" title="" alt="image.png"/> </p>'
p = re.compile('<p><img src="(.*?)" title',re.S)
rList = p.findall(str)
# print(rList)

rList1 = []
for str1 in rList:
    str1 = 'http:127.0.0.1:8000' + str1
    rList1.append(str1)
print(rList1)    
    



new = ''
for image in rList1:
    str = '<p><img src="{image}" title="" alt="image.png"/> '.format(image=image)
    new = new+str
print(new)
    





