candidate={} 
while True:
    name=input("Enter the name of the candidates")
    if name=="EXIT":
        break
    try:     
        score=int(input("Enter the scores of each candidates")) 
    except ValueError:
        print("Invalid input. Scores must be in integer values , try again with numbers.")
        continue   
    candidate[name]=score
    for name,score in candidate.items():
        if score==100:
            print(f"[{name}]:Masterpiece detected.Retaining.")
        elif  score>=90:
             print(f"[{name}]:Passed standard.Retaining.")
        elif score<90:
             print(f"[{name}]:Insufficient adaptation.Disposed")      