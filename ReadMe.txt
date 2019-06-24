Launch Instructions:
1. Download Docker
2. Launch docker and login:
	docker login
3. Get Image
	docker pull philipschen/neuroflow
4. Launch Docker image:
	docker run -p 8000:8000 philipschen/neuroflow
5. Go to 
	http://192.168.99.100:8000


API Guide: Navigation is through urls
Login and logout:
http://192.168.99.100:8000/Login 
http://192.168.99.100:8000/Logout

admin interface:
http://192.168.99.100:8000/admin 

Mood endpoint:
http://192.168.99.100:8000/mood

Notes:
1. Go to admin page to see and edit mood models and users
2. 3 users included as test data
	1. Login: admin 
	   pass: admin
	2. Login: admin2
	   pass: adminadmin
	3. Login: user3 
	   pass: adminadmin