folder = lambda path: path + "\\" if path[:-1] != "\\" else path

class ConfigureBase:
    def __init__(self, config):
        self.directory = folder(config["directory"])
        self.seed = folder(config["seed"])
        self.target = config["target"]
        self.dbg = config["dbg"]
        self.dbgopt = config["dbgopt"]
        self.fuzzdepth = config["fuzzdepth"] # percentage
        self.timeout = config["timeout"]