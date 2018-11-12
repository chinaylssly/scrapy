# _*_ coding:utf-8 _*_
import json
path='highlight.json'
with open(path,'r') as f:
	r=f.read()
	
	j=json.loads(r)
	print type(j)
	for i in j:
		print type(i)
		# break
		for key,values in i.items():
			print key,values
			print u'\n'
