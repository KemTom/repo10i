raw=[]
fbe=open("kep.txt")
for sor in fbe:
    sor=sor.strip("\n")
    sor=sor.split()
    raw.append(sor)
fbe.close()

print("2. feladat")
row=int(input("Kérem egy képpont adatait!\nSor: "))
col=int(input("Oszlop: "))

print("3. feladat")

print("4. feladat")

R=0
G=0
B=0
RGB1=0
RGB2=0
def hatar(R1,G1,B1,R2,G2,B2):
    elter=False
    RGB1=R1+G1+B1
    RGB2=R2+G2+B2
    if RGB1>RGB2+100 or RGB1+100<RGB2:
        elter=True
    return elter

print("6. feladat")