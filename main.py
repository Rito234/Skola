#vysko, polomer vpisanej opisanej, uhly, taznice, obvod, obsah, druhy trojuholnika
import math
a = int(input("Zadaj stranu a: "))
b = int(input("Zadaj stranu b: "))
c = int(input("Zadaj stranu c: "))            
#testujem ci je to trojuholnik
if (a + b > c) and (a + c > b) and (b + c > a):
    print("Je to trojuholnik")
    #testujem ci je pravouhly
    if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        print("Je to pravouhly trojuholnik")
        #testujem ci je rovnostranny
        if (a==b==c):
            print("Je to rovnostranny trojuholnik")
            #testujem ci je rovnoramenny
        if (a==b and a!=c) or (a==c and b!=c) or (b==c and a!=c):
            print("Je to rovnoramenny trojuholnik")
        o= (a+b+c)
        po= o/2
        S= (po*(po-a)*(po-b)*(po-c))**0.5
        va= (2*S)/a
        vb= (2*S)/b
        vc= (2*S)/c
        p_vpis= S/po
        p_opis= (a*b*c)/(4*S)
        #pocitam uhly
        alpha= round(math.degrees(math.acos((b**2+c**2-a**2)/(2*b*c))),2)
        beta= round(math.degrees(math.acos((a**2+c**2-b**2)/(2*a*c))),2)
        gamma= round(math.degrees(math.acos((a**2+b**2-c**2)/(2*a*b))),2)