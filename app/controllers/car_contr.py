import datetime

def get_car(json_data,tr,wt):
    output={'Cars':[]}
    year = datetime.date.today().year
    cy=int(year)
    my=int(json_data["cr_year"])
    cat=str(json_data['cr_category'])
    price=int(json_data['cr_newprice'])
    dep=cy-my

    if dep == 0:
        crv=price * 0.8
    elif dep==1:
        crv=price * 0.8
    elif dep==2:
        crv=price * 0.8
    elif dep==3:
        crv=price * 0.7
    elif dep == 4:
        crv=price * 0.6
    elif dep == 5:
        crv=price * 0.5
    elif dep == 6:
        crv=price * 0.45
    elif dep == 7:
        crv=price * 0.4
    elif dep == 8:
        crv=price * 0.35
    elif dep == 9:
        crv=price * 0.3
    elif dep>=10:
        crv=price * 0.25


    rat=810
    cif=crv+int(tr)
    rcv=cif * rat

#VAT
    vat=rcv * 0.18


#IMPORT DUTY TAX
    if cat == "B":
        imd=rcv * 0.25
    elif cat == "C":
        imd=rcv * 0.25
    elif cat == "E":
        imd=rcv * 0.25
    elif cat == "F":
        imd=rcv * 0.1
    elif cat == "H":
        imd=rcv * 0.1
    elif cat == "G":
        imd=rcv * 0.25


#WITHHOLDING TAX


#EXERCISE DUTY TAX

    if cat == "B":
        edt=(rcv+imd+(int(wt)*10))*0.1
    elif cat == "C":
        edt=(rcv+imd+(int(wt)*10))*0.15
    elif cat == "E":
        edt=0
    elif cat == "F":
        edt=0
    elif cat == "G":
        edt=0
    elif cat == "H":
        edt=0

    tam= rcv+vat+imd+edt

    data={'Brand':json_data['cr_brand'],'Mark':json_data['cr_mark'],'MadeYear':json_data['cr_year'],'DeprYears':dep,'NewPrice':json_data['cr_newprice'],'CurrentResValue':crv,'Transport':tr,'Cif':cif,'Rate':rat,'Value in Kigali':rcv,'VAT':vat,'Import Duty':imd,'Exercise Duty':edt,'Total Amount':tam}
    #data={'CRV':crv,'CIF':cif,'RCV':rcv,'EDT':edt}
    output['Cars'].append(data)
    return output
