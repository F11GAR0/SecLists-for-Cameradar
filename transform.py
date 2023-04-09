import os
import json
import sys

def trim_arr(arr):
    i = 0
    for el in arr:
        arr[i] = el.rstrip()
        i += 1
    return arr

def main(usernames_file, passwords_file, output_file):
    print(f"un: {usernames_file}, pwd: {passwords_file}, out: {output_file}")
    un_lines = trim_arr(open(usernames_file, "r+").readlines())
    pw_file = trim_arr(open(passwords_file, "r+").readlines())
    out_file = open(output_file, "w+")

    jj = json.dumps({ "usernames" : un_lines, "passwords" : pw_file })
    
    out_file.write(jj)
    out_file.close()
    print(f"Succesfully completed. Saved to:{out_file.name}")

if __name__ == "__main__":
    if len(sys.argv) > 3:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Not enough arguments. (python transform.py <usernames.txt> <passwords.txt> <outcredentials.json>")