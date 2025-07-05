import winreg

def check_auto_login():
    print("[+] Checking AutoLogin settings...\n")
    try:
        reg_path = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path)

        auto_login, _ = winreg.QueryValueEx(key, "AutoAdminLogon")
        username, _ = winreg.QueryValueEx(key, "DefaultUserName")
        password, _ = winreg.QueryValueEx(key, "DefaultPassword")

        print(f"[!] AutoAdminLogon: {auto_login}")
        print(f"[!] DefaultUserName: {username}")
        print(f"[!] DefaultPassword: {password}")

        if auto_login == "1":
            print("[-] Auto login is ENABLED — this is a security risk!")
        else:
            print("[+] Auto login is not enabled.")

        winreg.CloseKey(key)

    except FileNotFoundError:
        print("[-] Winlogon key not found.")
    except Exception as e:
        print("[-] Error while checking AutoLogin:", e)

if __name__ == "__main__":
    check_auto_login()
