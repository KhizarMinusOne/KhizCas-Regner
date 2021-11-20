#KhizCas Calculator
KhizCas_Value = int(input("Giv mig n! og jeg vi give KhizCas af n!: "))

x=1000
NewKhizCas = KhizCas_Value;

if KhizCas_Value == 1:
    print("Både 1 og 0, videre forklaringer i artiklen...")
    quit
    exit()


for i in range(1,x):
    x+=10000
    if NewKhizCas == 1:
       print("KhizCas af " +str(KhizCas_Value)+" er "+str(NewKhizCas*(i-1)))
       
       break
       exit()
    x += 5
    NewKhizCas = NewKhizCas/i
    

