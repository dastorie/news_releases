import os,re



#directory = r'/home/dale/Documents/Code/news_releases/data/1962-1967_2019-22_Box_36_File_268-274/'
#directory = r'/home/dale/Documents/Code/news_releases/data/1974-2002_2012-42_Box_1-3_File_1-27/'
#directory = r'/home/dale/Documents/Code/news_releases/data/1968-1974_2019-3_Box_56-57_File_570-578/'

base_dir = r'/home/dale/Documents/Code/news_releases/data/'

input_dir = base_dir + 'txt/'
output_dir = base_dir + 'cleaned/'

def find_breakline(file):
	break_line = 0
	text = file.readlines()
	for idx,line in enumerate(text):
		release_point = re.search('RELEASE',line)
		if release_point:
			if idx < 40:
				break_line = idx
	return(break_line)


for filename in os.listdir(input_dir):
	#print(filename)
	filepath = os.path.join(input_dir, filename)

	base_file = os.path.splitext(filename)[0]
	output_file = base_file + '_clean.txt'
	output_path = os.path.join(output_dir, output_file)
	#print(output_path)
	
	outfile = open(output_path,'a')

	with open(filepath) as file:
		#print(filepath)
		break_line = find_breakline(file)	
		text = file.readlines()	
		for idx,line in enumerate(text):
			if idx < break_line:
				continue
				#print(line)
			if idx >= break_line: 
				#line.decode('utf8').encode('ascii', errors='ignore')
				line = line.strip('\n')	
				#remove the dot patterns
				line = re.sub('•|\*', '', line)
				#remove page numbers	
				line = re.sub('-+ ?\d{1,4} ?-+', '', line)
				#remove intro
				intro = re.search('^(SASKATOON.+SASK.+|ADMINISTRATION BUILDING|EXT|UNIVERSITY NEWS|NEWS AND INFORMATION|PHONE.+|\d{1,3}|UNIV.+OF.+SASK.+|...MORE)',line)
				if intro:
					continue
				#strip blank lines
				if line == '':
					continue
				not_upper = re.search('[a-z]',line)
				if not_upper:
					outfile.write(line + ' ')
					#print(line) 			
					
	outfile.close()	
			


