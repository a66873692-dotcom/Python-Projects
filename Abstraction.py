from abc import ABC, abstractmethod
class Candidate(ABC):
    def __init__(self,name,rank):
        self.name=name
        self._rank=rank
    def display_status(self):
        print(f"System node:{self.name}|Rank level:{self._rank}") 
    @abstractmethod
    def evaluate(self):
        pass 
class PremiumCandidate(Candidate):
    def evaluate(self):
        if self._rank>=95:
            print(f"STATUS ALERT: Premium node {self.name} is SECURE")
        else:
            print(f"STATUS ALERT:Premium node {self.name} is on HOLD (Elite Threshold Failed)")
Candidate_A=PremiumCandidate("Alex",92)
Candidate_B=PremiumCandidate("Vance",42) 
Candidate_C=PremiumCandidate("Zack",94)   
Candidate_A.display_status()
Candidate_A.evaluate()
Candidate_B.display_status()
Candidate_B.evaluate()
Candidate_C.display_status()
Candidate_C.evaluate()
print("---------------------")

