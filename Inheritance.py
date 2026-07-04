class Candidate:
    def __init__(self,name,rank):
        self.name=name
        self._rank=rank
    def display_status(self):
        print(f"System node:{self.name}|Rank level:{self._rank}") 
    def evaluate(self):
        if self._rank>=90:
            print(f"STATUS ALERT:{self.name} is SECURE")
        else:
            print(f"STATUS ALERT:{self.name} is on HOLD") 
class PremiumCandidate(Candidate):
    def evaluate(self):
        if self._rank>=95:
            print(f"STATUS ALERT: Premium node {self.name} is SECURE")
        else:
            print(f"STATUS ALERT:Premium node {self.name} is on HOLD (Elite Threshold Failed)")
Candidate_A=Candidate("Alex",92)
Candidate_B=Candidate("Vance",42) 
Candidate_C=PremiumCandidate("Zack",94)   
Candidate_A.display_status()
Candidate_B.display_status()
Candidate_C.display_status()
print("---------------------")
Candidate_A.evaluate()
Candidate_B.evaluate()
Candidate_C.evaluate()
