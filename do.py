import requests
from bs4 import BeautifulSoup
import os
import random,sys
import string,re
arg_url = sys.argv[1]
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
scl_name = fetch_school_name(arg_url)
path_with_school = os.path.join(main_path,scl_name)
os.chdir(path_with_school)
with open('count.txt', 'r') as file:
    count = int(file.read().strip())
while True:
    try:
        url = f'{arg_url}/Views/profile/profile_staff_single.php?type=Teacher&id={count}'
        response = requests.get(url)
        # if "Nothing found" in response.text:
        #     break
        if response.status_code != 200:
            break
        soup = BeautifulSoup(response.text, 'html.parser')
        # print(soup.get_text())
        main_part = soup.find(id='id_card')
        # print(main_part.prettify())
        def remove_html_tags(text):
            try:
                soup = BeautifulSoup(text, "html.parser")
                stripped_text = ' '.join(soup.get_text().split())
                return stripped_text
            except:
                stripped_text = BeautifulSoup(text, "html.parser")
                return stripped_text
        try:
            print(remove_html_tags(str(main_part.prettify())))
        except:
            pass

        pic =  soup.find("div", class_="profile_photo")
        # print(pic.prettify())
        img_tag = pic.find("img")
        import re
        match = re.search(r'<img alt="Image" src="([^"]*)', str(img_tag))

        # print(match.group(1))
        folder_name = str(count)
        os.makedirs(folder_name, exist_ok=True)
        def remove_prefix(text, prefix):
            return text.replace(prefix, '')
        pic_path = f"{arg_url}/"+remove_prefix(str(match.group(1)), '../../')
        without_space_pic_path = str(pic_path).replace(" ", "")
        with open(f"{folder_name}/pic.jpg", "wb") as f:
            f.write(requests.get(without_space_pic_path).content)
        print(without_space_pic_path)
        with open(f"{folder_name}/info.txt", "w", encoding='utf-8') as f:
            try:
                f.write(remove_html_tags(str(main_part.prettify())))
            except Exception as e:
                print(f"Error removing HTML tags: {e}")
                f.write(str(BeautifulSoup(response, 'html.parser')))

        count = count + 1
        with open('count.txt', 'w', encoding='utf-8') as file:
            file.write(str(count))
    except:
        count = count + 1