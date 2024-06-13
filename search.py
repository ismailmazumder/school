import os
import re

import re

def extract_match(pattern, data, default=""):
    match = re.search(pattern, data)
    return match.group(1).strip() if match else default

def format_profile(data):
    # Extract Basic Information
    profile = {}
    
    profile['ID No'] = extract_match(r'ID No\. (\d+)', data)
    profile['Name'] = extract_match(r'Name: ([\w\s\(\)\.]+)', data)
    profile['Father\'s Name'] = extract_match(r"Father's Name: ([\w\s\.]+)", data)
    profile['Mother\'s Name'] = extract_match(r"Mother's Name: ([\w\s\.]+)", data)
    profile['Gender'] = extract_match(r'Gender: (\w+)', data)
    profile['Religion'] = extract_match(r'Religion: (\w+)', data)
    profile['Date of Birth'] = extract_match(r'Date of birth: (\d{2}/\d{2}/\d{4})', data)
    profile['Academic Qualification'] = extract_match(r'Academic Qualification: ([\w\s]+)', data)
    profile['Type'] = extract_match(r'Type: (\w+)', data)
    profile['Designation'] = extract_match(r'Designation: ([\w\s]+)', data)
    profile['Subject'] = extract_match(r'Subject : ([\w\s]*)', data)
    profile['Date of Joining'] = extract_match(r'Date of Joining: (\d{2}/\d{2}/-?\d{4})', data)
    profile['Blood Group'] = extract_match(r'Blood: ([\w\+]+)', data)

    # Extract Present Address
    present_address = {}
    present_address['Village/Holding No'] = extract_match(r'Present Address[\s\S]*?Village/Holding No: ([\w\s,]+)', data)
    present_address['Post'] = extract_match(r'Post: ([\w\s,]+)', data)
    present_address['Word/ Union'] = extract_match(r'Word/ Union: ([\w\s]+)', data)
    present_address['Upazilla/ Thana'] = extract_match(r'Upazilla/ Thana: ([\w\s]+)', data)
    present_address['Zilla'] = extract_match(r'Zilla: ([\w\s]+)', data)

    # Extract Permanent Address
    permanent_address = {}
    permanent_address['Village/Holding No'] = extract_match(r'Permanent Address[\s\S]*?Village/Holding No: ([\w\s,]+)', data)
    permanent_address['Post'] = extract_match(r'Post: ([\w\s,]+)', data)
    permanent_address['Word/ Union'] = extract_match(r'Word/ Union: ([\w\s]+)', data)
    permanent_address['Upazilla/ Thana'] = extract_match(r'Upazilla/ Thana: ([\w\s]+)', data)
    permanent_address['Zilla'] = extract_match(r'Zilla: ([\w\s]+)', data)

    # Combine the data
    formatted_profile = {
        'Basic Information': profile,
        'Present Address': present_address,
        'Permanent Address': permanent_address
    }

    return formatted_profile

path_base = "D:\\Users\\im087\\OneDrive\\Desktop\\All\\ccsc\\all_files"
folder_count = 5000
content = input("Enter your victim name : ")
for new in range(folder_count):
	try:
		path = os.path.join(path_base,str(new),"info.txt")
		# print(path)
		file_content = open(path,"r").read()
		if content in file_content:
			formatted_profile = format_profile(file_content)
			for section, info in formatted_profile.items():
			    print(section + ":")
			    for key, value in info.items():
			        print(f"  {key}: {value}")
			    print()

			# print(file_content)
	except FileNotFoundError:
		print(f'no file in {path}')