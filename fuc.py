import os
import ssb  # import your x86 .so module

# Portable directory
dir_path = os.path.join(os.getcwd(), "data")
os.makedirs(dir_path, exist_ok=True)

print(f"✅ Directory created at: {dir_path}")

# Test ssb functions
try:
    if hasattr(ssb, "test_function"):
        result = ssb.test_function()
        print(f"ssb.test_function() output: {result}")
    else:
        print("⚠️ ssb module loaded, but test_function() not found. Available names:", dir(ssb))
except Exception as e:
    print("❌ Error running ssb functions:", e)

