'''
DESCRIBE
'''

from mesa import Model
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from mesa.time import RandomActivation

from agents import GeneticPDAgent

#### MODEL

class GeneticPDModel(Model):

    description = 'A model which does nothing'

    def __init__(self, numagents=10,verbose=False, rounds_per_play=1,history_length=2):
        super().__init__()
        # Set parameters
        self.numagents=numagents
        self.verbose=verbose
        self.rounds_per_play = rounds_per_play
        self.history_length=history_length


        self.agents=[]


        # Build basic objects
        self.schedule = RandomActivation(self)
        self.datacollector = DataCollector(
            model_reporters= {"Agents": lambda m: len(m.schedule.agents)},
            agent_reporters={"wealth": lambda a: a.wealth}
            )



        # Create agents:
        for i in range(self.numagents):
            newagent=GeneticPDAgent(unique_id=self.next_id(),model=self)
            self.schedule.add(newagent)
            self.agents.append(newagent)

    def step(self):
        if self.verbose:
            print("Tick number:", self.schedule.time)
        self.schedule.step()
        # collect data
        self.datacollector.collect(self)



    def run_model(self, step_count=200):
        if self.verbose:
            print('Initial number agents: ',
                  self.schedule.get_agent_count())

        for i in range(step_count):
            self.step()

        if self.verbose:
            print('')
            print('Final number agents: ',
                  self.schedule.get_agent_count())

    def PDpayoff(self, my_action, your_action):
        if my_action == "C" and your_action == "C":
            return 3
        if my_action == "C" and your_action == "D":
            return 0
        if my_action == "D" and your_action == "C":
            return 4
        if my_action == "D" and your_action == "D":
            return 1
