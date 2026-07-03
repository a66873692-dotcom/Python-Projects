evaluation_count=0
def evaluate_candidate(name, score):
    global evaluation_count
    evaluation_count+=1
    if score == 100:
        return f"[{name}]: Masterpiece detected."," RETAINED."
    elif score >= 90:
        return f"[{name}]: Passed standard. "," RETAINED."
    else:
        return f"[{name}]: Insufficient adaptation.","DISPOSED."

msg1, status1 = evaluate_candidate("Kiyotaka", 100)
msg2, status2 = evaluate_candidate("Ryuen", 45)
print(msg1)
print(msg2)
print("Totla operations run:",evaluation_count)