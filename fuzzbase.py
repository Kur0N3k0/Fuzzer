#-*- coding: utf-8 -*-
import subprocess
import glob
import random
import time
import json
import hashlib
import zipfile
import shutil
import os

from configurebase import *

class FuzzBase(object):
    def __init__(self, config, mutator = None):
        config_json = ""
        with open(config, "r") as f:
            config_json = json.loads(f.read())

        self.config = ConfigureBase(config_json)
        self.mutator = mutator

    def default_mutator(self, fuzzbase):
        try:
            directory = fuzzbase.config.directory
            seed = fuzzbase.config.seed
            fuzzdepth = float(fuzzbase.config.fuzzdepth) / 100 # percentage

            r = glob.glob(directory + "*")
            fn = random.choice(r)
            extension = fn[fn.rfind(".") + 1:]

            with open(fn, "rb") as f:
                data = f.read()

            flen = len(data)
            data = list(data)
            for i in range(int(flen * fuzzdepth)):
                data[random.randint(0, flen) % flen] = chr(random.randint(0, 0x100) % 256)
            data = "".join(data)

            filename = hashlib.sha256(data).hexdigest()
            filename += ".{}".format(extension)

            with open(seed + filename, "wb") as f:
                f.write(data)

            return seed + filename
        except:
            return ""

    def run(self):
        dbg = self.config.dbg
        dbgopt = self.config.dbgopt
        target = self.config.target
        timeout = self.config.timeout

        if self.mutator == None:
            mutator = self.default_mutator
        else:
            mutator = self.mutator

        while True:
            testcase = mutator(self)
            cmd = "\"{}\" {} \"{}\" \"{}\"".format(dbg, dbgopt, target, testcase)
            fp = subprocess.Popen(cmd, shell=False)
            time.sleep(timeout)
            fp.kill()