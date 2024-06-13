import os,requests
while True:
	

	res = requests.get("https://cumillacsc.edu.bd/Views/profile/profile_staff_single.php?type=Teacher&id=52700")
	print(res.status_code)
	if "Nothing foundd" in res.text:
		break