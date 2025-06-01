VENV_DIR := .venv
PYTHON := $(VENV_DIR)/bin/python
PIP := $(VENV_DIR)/bin/pip
PYTEST := $(VENV_DIR)/bin/pytest

MODEL_DIR := models
MODEL_NAME := vosk-model-small-en-us
MODEL_VERSION := 0.15
MODEL_URL := https://alphacephei.com/vosk/models/$(MODEL_NAME)-$(MODEL_VERSION).zip
MODEL_PATH := $(MODEL_DIR)/$(MODEL_NAME)

all: venv deps model test

venv:
	@test -d $(VENV_DIR) || python3 -m venv $(VENV_DIR)

deps: venv
	$(PIP) install -U pip
	$(PIP) install -r requirements.txt

model:
	@test -d $(MODEL_PATH) || (\
		mkdir -p $(MODEL_DIR) && \
		curl -L $(MODEL_URL) -o $(MODEL_DIR)/model.zip && \
		unzip -q $(MODEL_DIR)/model.zip -d $(MODEL_DIR) && \
		mv $(MODEL_PATH)-$(MODEL_VERSION) $(MODEL_PATH) && \
		rm $(MODEL_DIR)/model.zip \
	)

test: deps
	$(PYTEST) ./src/tests/

clean:
	rm -rf $(VENV_DIR)
	rm -rf __pycache__ .pytest_cache
	find . -name '*.pyc' -delete
	find . -name '*.pyo' -delete
