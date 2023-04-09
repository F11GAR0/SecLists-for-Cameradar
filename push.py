import os
import json
import sys

def push_front(cred, username, password):
    print("Pushing front...\n")
    cred_json = json.loads(open(cred, "r+").read())
    if not username in cred_json["usernames"]:
        cred_json["usernames"].insert(0, username)
    if not password in cred_json["passwords"]:
        cred_json["passwords"].insert(0, password)
    cred_file = open(cred, "w+")
    cred_file.write(json.dumps(cred_json))
    cred_file.close()
    print("Successfuly pushed front.")
def push_back(cred, username, password):
    print("Pushing back...\n")
    cred_json = json.loads(open(cred, "r+").read())
    if not username in cred_json["usernames"]:
        cred_json["usernames"].append(username)
    if not password in cred_json["passwords"]:
        cred_json["passwords"].append(password)
    cred_file = open(cred, "w+")
    cred_file.write(json.dumps(cred_json))
    cred_file.close()
    print("Successfuly pushed back.")


if __name__ == "__main__":
    if len(sys.argv) > 4:
        if str(sys.argv[1]).startswith("-f"):
            push_front(sys.argv[2], sys.argv[3], sys.argv[4])
        elif str(sys.argv[1]).startswith("-b"):
            push_front(sys.argv[2], sys.argv[3], sys.argv[4])
        else:
            print(f"Unknown option {sys.argv[1]}.")
    else:
        print("Not enough arguments. (python push.py <-f(ront),-b(ack)> <credentials.json> <Username> <Password>)")