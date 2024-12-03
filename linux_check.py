import os
import json
import subprocess

for dp, dn, filenames in os.walk('./'):
    for f in filenames:
        if os.path.splitext(f)[1] == '.json':
            with open(os.path.join(dp, f), 'r') as file:
                print(file.read())
        if os.path.splitext(f)[1] == '.so':
            try:
                result = subprocess.run(['ldd', os.path.join(dp, f)], capture_output = True, text = True)
                print(result)
                print(result.stdout)
                print(result.stderr)
            except Exception as e:
                print("Error:", e)