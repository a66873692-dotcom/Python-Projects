total_processed=0
registry_ledger={}
def evaluate_subject(name,rank):
    global total_processed
    total_processed+=1
    if rank>=90:
        return f"Elite status secured.","SECURE"
    elif rank>=50 and rank<89:
        return f"Standard clearance granted","HOLD"
    elif rank<50:
        return f"Critcal failure.Purge required","PURGE"
while True:
    name = input("enter the name of the candidate")
    if name=="EXIT":
         break
    try:
        rank=int(input("Enter the rank of the candidate"))  
    except ValueError :
        print("System error: Rank must be an integer")
        continue
    log_msg,status_msg=evaluate_subject(name,rank) 
    print(log_msg) 
    registry_ledger[name]=status_msg
print("----------")
print("Total subjects processed:",total_processed)
print("Final registry ledger:",registry_ledger)
            
