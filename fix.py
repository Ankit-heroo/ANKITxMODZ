# fix_indent.py
file = "rd.pyx"
with open(file, "r", encoding="utf-8") as f:
    lines = f.readlines()

with open(file, "w", encoding="utf-8") as f:
    for line in lines:
        f.write(line.replace("\t", "    "))  # tab लाई 4 space मा बदल्छ
print("✅ Tabs replaced with spaces!")
