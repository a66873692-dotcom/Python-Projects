class SecurityPayload:
    def __init__(self,endpoint:str,funds:float,threat_values:int):
        self.endpoint=endpoint
        self._funds=funds
        self._threat_values=threat_values
    def get_risk(self):
        return (self._funds*self._threat_values)/100
    def __gt__(self,other):
        return self.get_risk()>other.get_risk()
    def __eq__(self,other):
        return self.get_risk()==other.get_risk()
    def __str__(self):
        return f"[SECURE LOG] Endpoint:{self.endpoint}|Risk level:{self.get_risk()}"            
class NetworkGate:
    def __init__(self):
        self.ledger=[]
    def add_payload(self,payload:SecurityPayload):
        self.ledger.append(payload)
    def get_highest_threat(self):
        if not self.ledger:
            return None 
        highest=self.ledger[0]
        for current in self.ledger:
            if current>highest:
                highest=current
        return highest        
if __name__=="__main__":
    gate=NetworkGate()
    p1=SecurityPayload("/api/standard_checkout",15000,30)
    p2=SecurityPayload("/api/root_access",5000,95)
    p3=SecurityPayload("/api/micro_payment",80000,5)
    gate.add_payload(p1)
    gate.add_payload(p2)
    gate.add_payload(p3)
    print("------Running Validation------") 
    most_dangerous=gate.get_highest_threat()
    print(f"Intercepted Threat Vector:\n{most_dangerous}")