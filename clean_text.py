import os,re

#directory = r'/home/dale/Documents/Code/news_releases/data/1962-1967_2019-22_Box_36_File_268-274/'
#directory = r'/home/dale/Documents/Code/news_releases/data/1974-2002_2012-42_Box_1-3_File_1-27/'
#directory = r'/home/dale/Documents/Code/news_releases/data/1968-1974_2019-3_Box_56-57_File_570-578/'

base_dir = r'data/'

input_dir = base_dir + 'txt/'
output_dir = base_dir + 'cleaned/'

# def find_breakline(file):
# 	break_line = 0
# 	text = file.readlines()
# 	for idx,line in enumerate(text):
# 		release_point = re.search('RELEASE',line)
# 		if release_point:
# 			if idx < 40:
# 				break_line = idx
# 	return(break_line)


for filename in os.listdir(input_dir):

	filepath = os.path.join(input_dir, filename)

	base_file = os.path.splitext(filename)[0]
	output_file = base_file + '_clean.txt'
	output_path = os.path.join(output_dir, output_file)
	#print(output_path)
	
	outfile = open(output_path,'a')

	file = open(filepath)	
	#text = file.read()	
	
	text = file.readlines()	
	for line in text: 	
		more = re.search('^\.{3,4} +(MORE|more)',line)
		if more:
			continue
		line = re.sub('•|\*','',line)
		line = re.sub('-30-|- 30 -','',line)
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

	# 	#remove page endings?
	# 	line = re.sub('-30-|- 30 -','',line)
	# 	#remove hyphen breaks
	# 	line = re.sub('(-|¬)\s','',line)
	# 	#remove odd characters
	# 	line = re.sub('[^[:alnum:]\s.:,?!\'\";]','',line)	
	# 	#remove odd encoding
	# 	

	# 	# 	para = re.search('\.\n',line)
	# 	# 	if para:	
	# 	# 		line = line
	# 	# 	else:
	# 	# 		line = line.strip('\n')
			
	# 	# 	#intro = re.search('^(SASKATOON.+SASK.+|ADMINISTRATION BUILDING|EXT|UNIVERSITY NEWS|NEWS AND INFORMATION|PHONE.+|\d{1,3}|UNIV.+OF.+SASK.+|...MORE)',line)
	# 	# 	# if intro:
	# 	# 	# 	continue
	# 	# 	# #strip blank lines
	# 	# 	# if line == '':
	# 	# 	# 	continue
	# 	# 	#not_upper = re.search('[a-z]',line)
	# 	outfile.write(line)			
					
	# outfile.close()	
			


