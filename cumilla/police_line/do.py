import requests
from bs4 import BeautifulSoup
import os
import random
import string
with open('count.txt', 'r') as file:
    count = int(file.read().strip())
while True:

    url = f'https://plhsc.edu.bd/Views/profile/profile_staff_single.php?type=Teacher&id={count}'
    response = requests.get(url)
    if response.status_code != 200:
        break
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup.get_text())
    main_part = soup.find(id='id_card')
    # print(main_part.prettify())
    def remove_html_tags(text):
        soup = BeautifulSoup(text, "html.parser")
        stripped_text = ' '.join(soup.get_text().split())
        return stripped_text
    print(remove_html_tags(str(main_part.prettify())))

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
    pic_path = "https://cumillacsc.edu.bd/"+remove_prefix(str(match.group(1)), '../../')
    without_space_pic_path = str(pic_path).replace(" ", "")
    with open(f"{folder_name}/pic.jpg", "wb") as f:
        f.write(requests.get(without_space_pic_path).content)
    print(without_space_pic_path)
    with open(f"{folder_name}/info.txt", "w") as f:
        f.write(remove_html_tags(str(main_part.prettify())))
    count = count + 1
    with open('count.txt', 'w') as file:
        file.write(str(count))
