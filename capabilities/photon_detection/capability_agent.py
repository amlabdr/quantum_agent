import yaml, logging
from utils.source import CLD1015
class capability_agent():
    def __init__(self):
        super(capability_agent, self).__init__()
        self.capabilities = {"capabilities/measurement_capability.json"}
        #read configuration file
        yf    = open('capabilities/photon_detection/config/config.yaml','r')
        config = yaml.load(yf, Loader=yaml.SafeLoader)
        yf.close()
        self.serialNumber = config["detector"]["serial"]
    def run(self,specification,parameters):
        return ["ok"]
        ####CODE HERE