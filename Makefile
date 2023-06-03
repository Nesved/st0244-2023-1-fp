.PHONY: all

SRC_DIR := src
TEST_DIR := test
MAIN_FILE := main.py

all: run

run:
	python $(SRC_DIR)/$(MAIN_FILE)
