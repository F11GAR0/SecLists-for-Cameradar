import os
import json
import sys


def create(cred):
    print("Creating blank credentials file...\n")
    blank = json.dumps({"usernames" : ["admin"], "passwords" : ["admin"]})
    cred_file = open(cred, "w+")
    cred_file.write(blank)
    cred_file.close()
    print("Successfuly created.")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        create(sys.argv[1])
    else:
        print("Not enough arguments. (python create.py <filename.json>)")