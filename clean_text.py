import os,re

#directory = r'/home/dale/Documents/Code/news_releases/data/1962-1967_2019-22_Box_36_File_268-274/'
#directory = r'/home/dale/Documents/Code/news_releases/data/1974-2002_2012-42_Box_1-3_File_1-27/'
#directory = r'/home/dale/Documents/Code/news_releases/data/1968-1974_2019-3_Box_56-57_File_570-578/'

base_dir = r'data/'

input_dir = base_dir + 'txt/'
output_dir = base_dir + 'cleaned/'

for filename in os.listdir(input_dir):

	filepath = os.path.join(input_dir, filename)

	base_file = os.path.splitext(filename)[0]
	output_file = base_file + '.txt'
	output_path = os.path.join(output_dir, output_file)
	#print(output_path)
	
	outfile = open(output_path,'a')

	file = open(filepath)	
	#text = file.read()	
	
	text = file.readlines()	
	for line in text: 	
		if re.match('\.\.\.MORE',line):
			line = ''
		if re.match('UNIV\. OF SASK',line):
			line = ''
		line = re.sub('•|\*','',line)
		line = re.sub('-30-|- 30 -|— 30 —','',line)
		line = re.sub('(-|¬)\s','',line)
		line = re.sub('[^[:alnum:]\s.:,?!\'\";]','',line)
		line = line.strip('\f')
		endline = re.search('[a-zA-Z0-9,]\n',line)
		if endline:
			line = re.sub('\n',' ',line)
		if line == '\n':
			continue
		outfile.write(line)
	outfile.close()	
			


