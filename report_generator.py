import subprocess
import os
import sys

SAVE_TO_FILE = False
REPORT_FILE = "report/audit_report.txt"

def run_module(module_name, description, save=False):
    print(f"\n========== {description} ==========")
    try:
        output = subprocess.check_output(f"python audit/{module_name}", shell=True, text=True)
        print(output)

        if save:
            with open(REPORT_FILE, "a") as f:
                f.write(f"\n========== {description} ==========\n")
                f.write(output)

    except Exception as e:
        error_msg = f"[{description}] Error: {e}"
        print(error_msg)
        if save:
            with open(REPORT_FILE, "a") as f:
                f.write("\n" + error_msg + "\n")

def clear_previous_report():
    if os.path.exists(REPORT_FILE):
        os.remove(REPORT_FILE)
        print("[+] Old report cleared.")

if __name__ == "__main__":
    # Check if user wants to save to file
    if len(sys.argv) > 1 and sys.argv[1] == "--save":
        SAVE_TO_FILE = True
        print("[+] Save mode enabled — report will be written to file.\n")
        os.makedirs("report", exist_ok=True)
        clear_previous_report()

    run_module("user_audit.py", "Local User Audit", SAVE_TO_FILE)
    run_module("password_policy_check.py", "Password Policy Check", SAVE_TO_FILE)
    run_module("auto_login_check.py", "AutoLogin Check", SAVE_TO_FILE)
    run_module("smb_share_enum.py", "SMB Share Enumeration", SAVE_TO_FILE)
    run_module("hash_dump.py", "Hash Dump (Admin Only)", SAVE_TO_FILE)

    if SAVE_TO_FILE:
        print(f"\n[+] Final report saved to: {REPORT_FILE}")
    else:
        print("\n[+] Report displayed only — not saved.")
