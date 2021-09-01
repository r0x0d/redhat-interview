PYTHON_INTERPRETER=python
SOURCE_PROJECT=redhat_interview_interview

all:
	$(PYTHON_INTERPRETER) redhat_interview_interview/main.py

test: 
	pytest tests/

clean:
	find . -name '__pycache__' -exec rm -rf  {} +