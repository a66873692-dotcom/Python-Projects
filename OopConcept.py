class Candidate:
    def __init__(self,name,rank):
        self.name=name
        self.rank=rank
    def display_status(self):
        print(f"System node:{self.name}|Rank level:{self.rank}") 
    def evaluate(self):
        if self.rank>=90:
            print(f"STATUS ALERT:{self.name} is SECURE")
        else:
            print(f"STATUS ALERT:{self.name} is on HOLD")           
Candidate_A=Candidate("Alex",94)
Candidate_B=Candidate("Vance",42)    
Candidate_A.display_status()
Candidate_B.display_status()
Candidate_A.evaluate()
Candidate_B.evaluate()