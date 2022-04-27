probability = {
 'R_T' : 0.2,
 'R_F' : 0.8,
 'SR_T': 0.01,
 'SR_F': 0.99,
 'S_T' : 0.4,
 'S_F' : 0.6,
 'GSR_T' : 0.99,
 'GSR_F' : 0.01,
 'GS_T' : 0.9,
 'GS_F' : 0.1,
 'GR_T' : 0.8,
 'GR_F' : 0.2,
 'G_T' : 0.0,
 'G_F' : 1.0
}

def prob_rain(R):
    if(R==1):
        return probability['R_T']
    else:
        return probability['R_F']

def prob_sprinkler(S,R):
    if(S==1 and R==1):
        return probability['SR_T']
    elif(S==1 and R==0):
        return probability['S_T']
    elif(S==0 and R==1):
        return probability['SR_F']
    else:
        return probability['S_F']

def prob_grasswet(S,R,G):
    if(S==1 and R==1 and G==1):
        return probability['GSR_T']
    elif(S==1 and R==1 and G==0):
        return probability['GSR_F']
    elif(S==0 and R==1 and G==1):
        return probability['GR_T']
    elif(S==0 and R==1 and G==0):
        return probability['GR_F']
    elif(S==1 and R==0 and G==1):
        return probability['GS_T']
    elif(S==1 and R==0 and G==0):
        return probability['GS_F']
    elif(S==1 and R==1 and G==1):
        return probability['G_T']
    else:
        return probability['G_F']


R = int(input("Enter if rain or not : "))
S = int(input("Enter if sprinkler was on or not :"))
G = int(input("Enter if grass wet or not : "))

PR = prob_rain(R)
PS = prob_sprinkler(S,R)
PG = prob_grasswet(S,R,G)

probability_final = PR*PS*PG
print("Probability = ",probability_final)