#!/usr/bin/python3

import json
# import argparse

with open("/tmp/board.jsonl", 'r') as file:
    data = json.load(file)
    print(json.dumps(data, indent=4))

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
