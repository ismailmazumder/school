import requests
from bs4 import BeautifulSoup
import os
import random,subprocess
import string,os,re
from threading import Thread
main_path = os.getcwd()
schools = []
def the_file_runner(path,link__):
	do_py = path + "\\do.py"
	subprocess.run(["python",do_py,link__])
def fetch_school_name(url):
 
  # Check if the URL starts with "http://" or "https://"
  if not re.match(r"^(http|https)://", url):
    return None

  # Use regular expression to capture everything before the first dot or path separator
  match = re.search(r"(https?://)?(www\d?\.)?([^/\.]+)", url)

  # Check if there's a match
  if not match:
    return None

  # Return the captured main name
  return match.group(3)
def folder_file(school_name,link):
	try:
	 	new_folder_path = os.path.join(main_path,school_name)
	 	os.mkdir(new_folder_path)
	 	with open(f"{new_folder_path}\\count.txt","w") as f:
	 		f.write("0")
	 	# do file 
	 	with open(f"{main_path}//do.py" , "r") as d:
	 		do_txt = d.read()
	 	with open(f"{new_folder_path}\\do.py","w") as f:
	 		f.write(do_txt)
	 	# search
	 	with open(f"{main_path}//search.py" , "r") as d:
	 		do_txt = d.read()
	 	with open(f"{new_folder_path}\\search.py","w") as f:
	 		f.write(do_txt)
	except Exception as e:
		pass
		try_again = Thread(target=the_file_runner,args=(new_folder_path,link))
		try_again.start() # last added after this check do stop req or break
	 	# os.rmdir(new_folder_path)
def main_function(link):
	# url =str(link) +  f'/Views/profile/profile_staff_single.php?type=Teacher&id='
	school_name = fetch_school_name(link)
	# print(school_name,link)
	folder_file(school_name,link)
	schools.append(school_name)
	# subprocess.Popen(["python",f"{main_path}\\{school_name}\\do.py",f"{link}"])
links = []
with open("school_link.txt") as file:
	lines = []
	for new in file:
		# print(new.strip())
		main_function(new.strip())
		links.append(new.strip())

threads = []
countt = 0

for new in schools:
	now_link = links[countt]
	countt = countt + 1
	print(now_link+":)")
	full_path = os.path.join(main_path,new)
	thread_ = Thread(target=the_file_runner,args=(full_path,now_link))
	threads.append(thread_)
	thread_.start()