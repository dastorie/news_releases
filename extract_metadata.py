import os,re
import csv
from datetime import datetime
import calendar
from titlecase import titlecase

directory = r'data/1962-1967_2019-22_Box_36_File_268-274/'
accession_id = '2019-22 Box 36 File 268-274'
uid_part = '-2019-22-36'

# directory = r'data/1974-2002_2012-42_Box_1-3_File_1-27/'
# accession_id = '2012-42 Box 1-3 File 1-27'
# uid_part = '-2012-42-1'

# directory = r'data/1968-1974_2019-3_Box_56-57_File_570-578/'
# accession_id = '2019-3 Box 56-57 File 570-578'
# uid_part = '-2019-3-570'

with open('news_release_metadata.csv', 'a') as csvFile:
	writer = csv.writer(csvFile)
	header = ['pid','filename','accession_id','date','year','month','day','decade','label','title','author']
	#writer.writerow(header)
	for filename in os.listdir(directory):
		if filename.endswith(".pdf"):

			base_file = os.path.splitext(filename)[0]
			text_path = 'data/txt/' 
			text_file = base_file + '.txt'
			filepath = os.path.join(text_path + text_file)
			file = open(filepath)	
			text = file.read()

			d = re.search("(\d{4}-\d{2}-\d{2})",filename)
			if d:
				date = d[0]
				real_date = datetime.strptime(date, '%Y-%m-%d')	
				year = real_date.year
				month = real_date.month
				day = real_date.day

			else:
				date = None
				year = None
				month = None
				day = None	

			if year:	
				if year > 1959 and year < 1970:
					decade = '1960s'
				elif year > 1969 and year < 1980:
					decade = '1970s'
				elif year > 1979 and year < 1990:
					decade = '1980s'
				elif year > 1989 and year < 2000:
					decade = '1990s'
				elif year > 1999:
					decade = '2000s'
			else: 
				decade = None

				# <1968-01-31 "News from the University of Saskatchewan"
				# 1968-02-01 - 1973-07-11 - "News from the University of Saskatchewan, Regina Campus"
				# 1973-07-12 - 1974-06-30 - "News Release - University of Saskatchewan, Regina Campus"
				# 1974-07-01 - 1985-06-30 - "News Release - University of Regina"
				# 1985-07-01 - 1988-03-03 - "Information"
				# 1985-03-04 - 1989-03-20 - "Info"
				# 1989-03-21 - 1993-10-15 - "News"
				# > 1993-10-16 - "University of Regina: News Release"
			
			#real titles start in Oct. 1985	

			if real_date:
				if real_date <= datetime(year = 1968, month = 1, day = 31):
					label = "News from the University of Saskatchewan"
				elif real_date <= datetime(year = 1973, month = 7, day = 11):
					label = "News from the University of Saskatchewan, Regina Campus"
				elif real_date <= datetime(year = 1974, month = 6, day = 30):
					label = "News Release - University of Saskatchewan, Regina Campus"
				elif real_date <= datetime(year = 1985, month = 6, day = 30):
					label = "News Release - University of Regina"
				elif real_date <= datetime(year = 1988, month = 3, day = 3):
					label = "Information"
				elif real_date <= datetime(year = 1989, month = 3, day = 20):
					label = "Info"
				elif real_date <= datetime(year = 1993, month = 10, day = 15):
					label = "News"
				else:
					label = "University of Regina: News Release"

			#authors
				#< 1962-07-01 - "News Services Office"
				#  1962-07-01 to 1968-01-31 - "University News Services"	
				#  1968-02-01 to 1972-09-30 - "Publicity and Public Relations Office"
				#  1972-10-01 to 1973-02-02 - "Information Office"
				#  1972-02-03 to 1977-12-31 - "News and Information Services"
				#  1978-01-01 to 1983-06-02 - "Publicity and Information Services"
				#  1983-06-03 to 1985-06-30 - "Public Relations Office"
				#  1985-07-01 to 1988-03-03 - "University of Regina Public Relations"
				#  1988-03-04 to 1989-05-27 - "University of Regina News and Communications"
				#  > 1989-05-28 "University of Regina Communications Office"		

			if real_date:
				if real_date <= datetime(year = 1962, month = 7, day = 1):
					author = "News Services Office"
				elif real_date <= datetime(year = 1968, month = 1, day = 31):
					author = "University News Service"
				elif real_date <= datetime(year = 1972, month = 9, day = 30):
					author = "Publicity and Public Relations Office"
				elif real_date <= datetime(year = 1973, month = 2, day = 2):
					author = "Information Office"
				elif real_date <= datetime(year = 1977, month = 12, day = 31):
					author = "News and Information Services"
				elif real_date <= datetime(year = 1983, month = 6, day = 2):
					author = "Publicity and Information Services"
				elif real_date <= datetime(year = 1985, month = 6, day = 30):
					author = "Public Relations Office"
				elif real_date <= datetime(year = 1988, month = 3, day = 3):
					author = "University of Regina Public Relations"	
				elif real_date <= datetime(year = 1989, month = 5, day = 27):
					author = "University of Regina News and Communications"	
				else:
					author = "University of Regina Communications Office"

			title = None

			if year:
				if year > 1985:
					title_block = re.search(r'(\d{4}.?\n+)([^a-z]+)(\n+)',text)
					if title_block:
						if title_block.group(2):
							extract = title_block.group(2)
							stop_words = re.search(r'RELEASE|MEDIA ADVISORY|IMMEDIATELY|\d{4}',extract)
							if stop_words:
								title = None
							elif len(extract) < 8:
								title = None
							else: 
								extract = re.sub(r'\n',' ',extract)
								title = re.sub(r' +',' ',extract)
								title = titlecase(title)

			old_base = os.path.splitext(filename)[0]
			base = re.sub('Release_','',old_base)
			base = re.sub('_RE-DO','-1',base) 
			uid = base + uid_part
			
			#rename file
			old_name = r'data/cleaned/' + old_base + '.txt'
			new_name = r'data/cleaned/' + uid + '.txt'
			#os.rename(old_name,new_name)
			row = [uid,new_name,accession_id,date,year,month,day,decade,label,title,author]
			writer.writerow(row)
csvFile.close()		