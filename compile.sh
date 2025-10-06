#!/bin/bash
echo "Compiling SSB modules..."

# Python include path
PYTHON_INCLUDE=$(python -c "import sysconfig; print(sysconfig.get_path('include'))")
echo "Python include: $PYTHON_INCLUDE"

# 64-bit compile
echo "🔨 Compiling 64-bit version..."
cython -3 ssb_64.pyx
gcc -shared -fPIC -O2 -I$PYTHON_INCLUDE ssb_64.c -o ssb_64.so

# 32-bit compile
echo "🔨 Compiling 32-bit version..."  
cython -3 ssb_32.pyx
gcc -shared -fPIC -m32 -O2 -I$PYTHON_INCLUDE ssb_32.c -o ssb_32.so

echo "✅ Compilation attempted!"