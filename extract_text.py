import os, subprocess

#sub_dir = r'1962-1967_2019-22_Box_36_File_268-274/'
#sub_dir = r'1968-1974_2019-3_Box_56-57_File_570-578/'
sub_dir = r'1974-2002_2012-42_Box_1-3_File_1-27/'


base_dir = r'data/'

directory = base_dir + sub_dir

output_dir = base_dir + 'txt/'

#for extracting with pdftotext
print('extracting text')
for filename in os.listdir(directory):
	if filename.endswith(".pdf"):
		old_path = os.path.join(directory, filename)
		base_file = os.path.splitext(filename)[0]
		output_file = base_file + '.txt'
		output_path = os.path.join(output_dir, output_file)
		subprocess.call(f'pdftotext {old_path} {output_path}',shell=True)
