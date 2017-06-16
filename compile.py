# Let's Build a Wonderswan Compiler!
import os
import sys

# Take in path arguments
if len(sys.argv) != 3:
	input = "buildme"
	output = "test"
else:
	input = str(sys.argv[1])
	output = str(sys.argv[2])

# TBD!!! Automatically populate .bmp files based on /gfx directory

bmp2ws_dir = "/Users/maclean/Documents/Programming/Wonderswan/swandriving/wonderswandev/bin/bmp2swan.exe"
#bmp2ws_c = "wine " + bmp2ws_dir 

compile_c = "nasm -f bin -o " + output + ".wsc " + input + ".asm"

runemu_dir = "/Users/maclean/Documents/Programming/Wonderswan/cygne21a-win/cygne.exe"
runemu_c = "wine " + runemu_dir

# TBD!!! Delete old ROM

# TBD!!! Make graphics assets (likely needs a loop, look into other exe)
#os.system(bmp2ws_c)

# Compile ROM
os.system(compile_c)

# Open Emulator
os.system(runemu_c)