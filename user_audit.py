import os
import subprocess

def get_local_users():
    print("[+] Getting local user accounts...\n")
    try:
        output = subprocess.check_output('net user', shell=True, text=True)
        print(output)
    except Exception as e:
        print("[-] Failed to get users:", e)

def get_user_details(user):
    print(f"\n[+] Details for user: {user}")
    try:
        output = subprocess.check_output(f'net user {user}', shell=True, text=True)
        print(output)
    except Exception as e:
        print("[-] Failed to get user details:", e)

if __name__ == "__main__":
    get_local_users()
