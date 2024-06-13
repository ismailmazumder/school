import requests
from bs4 import BeautifulSoup
import os
import random,subprocess
import string,os,re
main_path = os.getcwd()
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
def folder_file(school_name):
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
	 	os.rmdir(new_folder_path)
def main_function(link):
	url =str(link) +  f'/Views/profile/profile_staff_single.php?type=Teacher&id='
	school_name = fetch_school_name(url)
	print(school_name,url)
	folder_file(school_name)
	subprocess.Popen(["python",f"{main_path}\\{school_name}",f"{url}"])
with open("school_link.txt") as file:
	lines = []
	for new in file:
		# print(new.strip())
		main_function(new.strip())
