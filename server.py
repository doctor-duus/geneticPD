from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import  ChartModule
from mesa.visualization.UserParam import UserSettableParameter

from model import GeneticPDModel


def  my_model_portrayal(agent):
    if agent is None:
        return

    portrayal = {}
    portrayal["Color"] = ["Red"]
    portrayal["Shape"] = "circle"
    portrayal["r"] = ".75"
    portrayal["Filled"] = "true"
    portrayal["Layer"] = 0
    portrayal["w"] = 1
    portrayal["h"] = 1

    return portrayal

chart_element = ChartModule([{"Label": "Agents", "Color": "#AA0000"}])

model_params = {"numagents": UserSettableParameter('slider', 'Initial # Agents', 10, 0, 100),
                "verbose" : UserSettableParameter('checkbox', 'verbose', True),
                "height" : gridheight,
                "width" : gridwidth
                }

server = ModularServer(GeneticPDModel, [chart_element], "My Model", model_params)
server.port = 8521
