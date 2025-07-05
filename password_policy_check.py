import subprocess

def check_password_policy():
    print("[+] Checking password policy...\n")
    try:
        result = subprocess.check_output("net accounts", shell=True, text=True)
        print(result)

        # Basic Analysis
        if "Minimum password length" in result:
            lines = result.splitlines()
            for line in lines:
                if "Minimum password length" in line:
                    length = int(line.split(":")[1].strip())
                    if length < 8:
                        print("[-] Weak password policy: Minimum length is less than 8")
                    else:
                        print("[+] Password length policy looks good.")
    except Exception as e:
        print("[-] Failed to check password policy:", e)

if __name__ == "__main__":
    check_password_policy()
