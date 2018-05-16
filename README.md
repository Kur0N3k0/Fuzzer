# Fuzzer
Mutation Fuzzer

# Requirement
windbg

# Usage
## 1. Create a python class that inherits from FuzzBase.
```python
from fuzzbase import *

class testfuzzer(FuzzBase):
    def __init__(self, config):
        super(testfuzzer, self).__init__(config, self.mutator)

    def mutator(self, fuzzer):
        return input_generated_seedfile_path

if __name__ == "__main__":
    fuzzer = testfuzzer("config/test-config.json")
    fuzzer.run()
```
## 2. Copy test-config.json to the config folder and set the path.
```json
{
    "directory" : "target file",
    "seed" : "Seed folder",
    "target" : "target exe",
    "dbg" : "C:\\Program Files (x86)\\Windows Kits\\10\\Debuggers\\x86\\cdb.exe",
    "dbgopt" : "-c \"sxd *;.logopen /t [enter your log folder];u;r;kb;q\" -G -g -o",
    "fuzzdepth" : 1,
    "timeout" : 5
}
```
## 3. Run the python file you created
```
python testfuzzer.py
```
