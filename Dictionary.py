candidate={
    "Amasawa":95,
    "Kiyotaka":100,
    "Ryuen":45
}
for name,score in candidate.items():
    if score==100:
        print(f"[{name}]:Masterpiece detected.Retaining.")
    elif score>=90:
        print(f"[{name}]:Passed standard.Retaining.") 
    elif score<90:
        print(f"[{name}]:Insufficient adaptation.Disposed.")
              