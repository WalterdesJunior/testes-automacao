.PHONY: install-api install-web test-api test-web test-all clean

install-api:
	cd api_tests && python3 -m venv venv && venv/bin/pip install -r requirements.txt

install-web:
	cd web_tests && python3 -m venv venv && venv/bin/pip install -r requirements.txt

test-api:
	cd api_tests && venv/bin/pytest

test-web:
	cd web_tests && venv/bin/pytest

test-all: test-api test-web

clean:
	rm -rf api_tests/venv web_tests/venv api_tests/report.html web_tests/report.html
