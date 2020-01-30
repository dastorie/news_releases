import os, subprocess

base_dir = r'data/'
sub_dir = r'scans/'

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
