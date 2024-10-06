run:
	@read -s -p "Password: " password; echo ""; python3 example.py $$password

req:
	pip3 install -r requirements.txt

req-dev:
	pip3 install -r requirements-dev.txt
