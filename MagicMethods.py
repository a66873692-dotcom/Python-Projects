class SecurityPayload:
    def __init__ (self,endpoint:str,funds:float,threat_score:int):
        self.endpoint=endpoint 
        self.funds=funds
        self.threat_score=threat_score
    def calculate_risk_index(self):
        return (self.funds*self.threat_score)/100    
    def __gt__(self,other):
        return self.calculate_risk_index()>other.calculate_risk_index()
    def __eq__(self,other):
        return self.calculate_risk_index()==other.calculate_risk_index()
    def __str__(self):
        return f"[SECURE LOG] Endpoint:{self.endpoint}|Risk index:{self.calculate_risk_index()}"    
if __name__=="__main__":
    tx1=SecurityPayload("/api/wire_transfer",50000,85)
    tx2=SecurityPayload("/api/quick_pay",90000,20)
    tx3=SecurityPayload("/api/crypto_vault",42500,100)
    print("----Running Validation----") 
    print(tx1)
    print(f"Is tx1 nore critical than tx2?{tx1>tx2}") 
    print(f"Is tx2 nore critical than tx1?{tx2>tx1}")  
    print(f"Are tx1 and tx3 identical threat values{tx1==tx3}")
