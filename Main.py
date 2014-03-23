#-*- coding:utf-8 -*-
#Main.py
import urllib2
import os

if __name__ == "__main__" :
	urlFile = open('url.txt', 'r')
	outputFile = open('output.csv', 'w')
	outputFile.write("网站名称, 网站链接, 博客总流, 关注人数, 性质/内容, 主题\n")
	urls = urlFile.readlines()
	count = 0
	for url in urls:
		print 'blog %d' %(count)
		content = urllib2.urlopen(url).read()
		titleb = content.find(r'<title>')
		titlee = content.find(r'</title>', titleb)
		title = content[titleb+7:titlee]
		print title 
		outputFile.write(title+',')
		outputFile.write(url+',')
		b1 = content.find(r'comp_901_pv')
		b1 = content.find(r'<strong>', b1)+8
		end1 = content.find(r'</strong>', b1)
		numAccess = content[b1:end1]
		print 'number of Access: ', numAccess
		numAccess.replace(',', '')
		outputFile.write(numAccess+',')
		b2 = content.find(r'comp_901_attention')
		b2 = content.find(r'<strong>', b2)+8
		end2 = content.find(r'</strong>', b2)
		numAttention = content[b2:end2]
		print 'Number of Attention: ', numAttention
		outputFile.write(numAttention+',')
		outputFile.write('新浪博客'+',')
		#pass 1
		tags = []
		tagIndexb = content.find(r'blog_tag')
		if tagIndexb != -1: 
			tagIndexEnd = content.find(r'</td>', tagIndexb)
			h3Index = content.find(r'<h3>', tagIndexb, tagIndexEnd)
			while h3Index != -1:
				blankIndex = content.find(r'"_blank">', h3Index)
				blankEnd = content.find(r'</a>', blankIndex)
				tags.append(content[blankIndex+9:blankEnd])
				h3Index = content.find(r'<h3>', blankEnd, tagIndexEnd)

		#pass 2
		tagIndexb = content.find(r'blog_tag', tagIndexb)
		if tagIndexb != -1:
			tagIndexEnd = content.find(r'</td>', tagIndexb)
			h3Index = content.find(r'<h3>', tagIndexb, tagIndexEnd)
			while h3Index != -1:
				blankIndex = content.find(r'"_blank">', h3Index)
				blankEnd = content.find(r'</a>', blankIndex)
				tags.append(content[blankIndex+9:blankEnd])
				h3Index = content.find(r'<h3>', blankEnd, tagIndexEnd)
		print 'tags'
		for t in tags:
			print t
			outputFile.write(t+" ")
		outputFile.write('\n')
		count += 1
		