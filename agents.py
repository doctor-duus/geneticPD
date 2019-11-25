# GeneticPDModel agents. 

from mesa import Agent
import random

debug=True

if debug:


    def actionnum(n):
        if n=="C":
            return 1
        else:
            if n=="D":
                return 0
            else:
                return None

    def history_to_entry(hist):
        val = 0
        temp=hist.copy()
        temp.reverse()
        for a in temp:
            val = val * 2 + actionnum(a)
        return val




class GeneticPDAgent(Agent):

    probs = [0, .25, .5, .75, 1]

    def __init__(self, unique_id, model=None,playertype="Random"):
        super().__init__(unique_id,model)

        if playertype=="Genetic":
            self.prob_cooperate=None
            self.make_fake_history(self.model.history_length)
        else:
            self.prob_cooperate = random.choice(self.probs)

        self.wealth=0

        if self.model.verbose:
            print("Agent " + str(self.unique_id) + " created, prob:", self.prob_cooperate)

    def make_fake_history(self,histlen):
        self.hist=[]
        for i in range(histlen):
            ranhist=random.choice("C","D")
            self.hist.append(ranhist)


    def action(self):
        if random.uniform(0,1) < self.prob_cooperate:
            return "C"
        else:
            return "D"

    def choose_opponent(self):
        other_agents= self.model.agents.copy()
        other_agents.remove(self)
        return random.choice(other_agents)

    def actionnum(self,n):
        if n=="C":
            return 1
        else:
            if n=="D":
                return 0
            else:
                return None

    def history_to_entry(self):
        val = 0
        temp=self.hist.copy()
        temp.reverse()
        for a in temp:
            val = val * 2 + actionnum(a)
        return val

    def play(self,n_times=1):
        oppo = self.choose_opponent()
        #self.wealth=0
        #oppo.wealth=0

        for t in range( n_times ):
            my_action=self.action()
            oppo_action=oppo.action()

            my_payoff = self.model.PDpayoff(my_action, oppo_action)
            self.wealth += my_payoff
            oppo_payoff = self.model.PDpayoff(oppo_action,my_action)
            oppo.wealth += oppo_payoff

            if self.model.verbose:
                print( "Agent", self.unique_id, "played against Agent", oppo.unique_id)
                print( "I played", my_action, "and she played", oppo_action)
                print( "Payoffs were:", my_payoff, ",", oppo_payoff)
                print( "Wealths are: ", self.wealth, ", ", oppo.wealth)

    def step(self):
        self.play(self.model.rounds_per_play)
