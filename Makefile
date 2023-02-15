run:
	python Client.py
	python Server.py
setup: 
	pip install -r socket
	pip install -r sys
	pip install -r os
clean:
	rm -rf __pycache__
