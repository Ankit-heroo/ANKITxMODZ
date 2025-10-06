def get_fb_ua():
    android_versions = ["13", "12", "11", "10"]
    devices = ["SM-G998B", "SM-G991B", "SM-A736B", "Redmi Note 12", "Pixel 7 Pro", "OnePlus 11"]
    builds = ["TP1A.220624.014", "SP1A.210812.016", "RP1A.200720.012", "QP1A.190711.020"]
    chrome_versions = ["119.0.6045.163", "118.0.5993.111", "117.0.5938.153", "116.0.5845.114"]
    
    android = random.choice(android_versions)
    device = random.choice(devices)
    build = random.choice(builds)
    chrome = random.choice(chrome_versions)
    fb_version = "428.0.0.32.120"
    
    ua = f"Mozilla/5.0 (Linux; Android {android}; {device} Build/{build}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_version};]"
    return ua    