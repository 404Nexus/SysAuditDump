import subprocess

def list_smb_shares():
    print("[+] Checking shared folders on this system...\n")
    try:
        result = subprocess.check_output("net share", shell=True, text=True)
        print(result)

        risky_shares = []
        lines = result.splitlines()
        for line in lines:
            if any(share in line for share in ["C$", "ADMIN$", "IPC$", "Users", "Public"]):
                risky_shares.append(line.strip())

        if risky_shares:
            print("\n[!] Risky or default shares found:")
            for share in risky_shares:
                print("[-]", share)
        else:
            print("[+] No risky shares found.")
    except Exception as e:
        print("[-] Failed to enumerate shares:", e)

if __name__ == "__main__":
    list_smb_shares()
