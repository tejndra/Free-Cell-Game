
# coding: utf-8

# In[1]:

from itertools import product
ACE=1
J=11
Q=12
K=13
Heart='H'
Diamond='D'
Club='C'
Spade='S'
class Card:
    def __init__(self):
        self.card_face=[ACE,2,3,4,5,6,7,8,9,10,J,Q,K]
        self.card_suit=[Heart,Diamond,Club,Spade]
        self.card=list(product(self.card_face,self.card_suit))


# In[2]:

from random import shuffle
class Deck:
    def __init__(self, value_start, value_end, number_of_suits):
        self.value_s=value_start
        self.value_e=value_end
        self.num_suit=number_of_suits
        #self.value_s=int(input("Enter value start: "))
        #self.value_e=int(input("Enter value end: "))
        #self.num_suit=int(input("Enter Number of Suits: "))
        self.cards=Card()
        self.face=self.cards.card_face[self.value_s-1:self.value_e]
        self.suit=self.cards.card_suit[0:self.num_suit]
        self.deck=list(product(self.face,self.suit))
        if(self.num_suit>4 or self.value_s<1 or self.value_e>13):
            print("error")
        else:
            pass
            
    def pops(self):
        return self.deck.pop()
    
    def pushs(self,value):
        val=self.pops()
        self.deck.append(val)
        return self.deck
    
    def shuffles(self):
        shuffle(self.deck)
        return self.deck


# In[ ]:

from itertools import zip_longest
import sys
class NotFreecell:
    def __init__(self):
        self.c1=[]
        self.c2=[]
        self.c3=[]
        self.c4=[]
        self.f1=[(0,'H')]
        self.f2=[(0,'D')]
        self.f3=[(0,'C')]
        self.f4=[(0,'S')]
        self.cascade1=[]
    
    def starts(self,start):
        start=input("New Game(1) or Exit(2) :- ")
        if(start=='1'):
            self.display()
        elif(start=='2'):
            sys.exit()
        else:
            print("Please select appropriate Option.")
            self.starts(0)
            
    def display(self):
        self.deck=Deck(1,13,4)
        shuf=self.deck.shuffles()
        while(len(shuf)!=0):
            for times in range(1,5):
                self.cascade1.append(shuf[0:7])
                del shuf[0:7]
            for times in range(1,5):
                self.cascade1.append(shuf[0:6])
                del shuf[0:6]
        print("\nCell Slot: ",self.c1 ,self.c2 ,self.c3 ,self.c4 ," \t\t\t\t\t\tFoundation: ",self.f1[-1] ,self.f2[-1] ,self.f3[-1] ,self.f4[-1])
        print("\n  Cascade1\t Cascade2\t Cascade3\t Cascade4\t Cascade5\t Cascade6\t Cascade7\t Cascade8\n" )
        for cols in zip_longest(self.cascade1[0],self.cascade1[1],self.cascade1[2],self.cascade1[3],self.cascade1[4],self.cascade1[5],self.cascade1[6],self.cascade1[7]):
            cas=list(cols)
            displays=['       ' if i is None else i and ('A',i[1]) if i[0]==1 else (i[0],i[1]) and ('J',i[1]) if i[0]==11 else (i[0],i[1]) and ('Q',i[1]) if i[0]==12 else (i[0],i[1]) and ('K',i[1]) if i[0]==13 else (i[0],i[1]) for i in cas]
            #Upper lines takes 1 and print as 'A' , 11 as 'J' , 12 as 'Q' and 13 as 'K' using for loop
            print(" ",displays[0],"\t",displays[1],"\t",displays[2],"\t",displays[3],"\t",displays[4],"\t",displays[5],"\t",displays[6],"\t",displays[7])
        
        self.check_result()
    
    def check_result(self):
        while((self.f1[-1]!=(13,'H')) or (self.f2[-1]!=(13,'D')) or (self.f3[-1]!=(13,'C')) or (self.f4[-1]!=(13,'S'))):
            self.modes()
        if((self.f1[-1]==(13,'H')) and (self.f2[-1]==(13,'D')) and (self.f3[-1]==(13,'C')) and (self.f4[-1]==(13,'S'))):
            print("You Win")
    
    def fromcas(self):
        fromcas = input('From Where to Pop (Cascade No.): ')

        if fromcas == '1':
            fromcas = self.cascade1[0]
            return fromcas
        elif fromcas == '2':
            fromcas = self.cascade1[1]
            return fromcas
        elif fromcas == '3':
            fromcas = self.cascade1[2]
            return fromcas
        elif fromcas == '4':
            fromcas = self.cascade1[3]
            return fromcas
        elif fromcas == '5':
            fromcas = self.cascade1[4]
            return fromcas
        elif fromcas == '6':
            fromcas = self.cascade1[5]
            return fromcas
        elif fromcas == '7':
            fromcas = self.cascade1[6]
            return fromcas
        elif fromcas == '8':
            fromcas = self.cascade1[7]
            return fromcas
        else:
            print("Please select appropriate Cascade.")
            

    def tocas(self):
        tocas = input('To Where to Append (Cascade No.): ')

        if tocas == '1':
            tocas = self.cascade1[0]
            return tocas
        elif tocas == '2':
            tocas = self.cascade1[1]
            return tocas
        elif tocas == '3':
            tocas = self.cascade1[2]
            return tocas
        elif tocas == '4':
            tocas = self.cascade1[3]
            return tocas
        elif tocas == '5':
            tocas = self.cascade1[4]
            return tocas
        elif tocas == '6':
            tocas = self.cascade1[5]
            return tocas
        elif tocas == '7':
            tocas = self.cascade1[6]
            return tocas
        elif tocas == '8':
            tocas = self.cascade1[7]
            return tocas
        else:
            print("Please select appropriate Cascade.")

    def fromcell(self):
        fromcell = input('From Where to Pop (Cellslot No.) : ')

        if fromcell == '1':
            fromcell = self.c1
            return fromcell
        elif fromcell == '2':
            fromcell = self.c2
            return fromcell
        elif fromcell == '3':
            fromcell = self.c3
            return fromcell
        elif fromcell == '4':
            fromcell = self.c4
            return fromcell
        else:
            print("Please select appropriate Cellslot.")


    def fromfound(self):
        fromfound = input('From Where to Pop (Foundation No.) : ')

        if fromfound == '1':
            fromfound = self.f1
            return  fromfound
        elif fromfound == '2':
            fromfound = self.f2
            return  fromfound
        elif fromfound == '3':
            fromfound = self.f3
            return  fromfound
        elif fromfound == '4':
            fromfound = self.f4
            return  fromfound
        else:
            print("Please select appropriate Foundation.")

        

    def tofound(self):
        tofound = input('To Where to Append (Foundation No.) : ')

        if tofound == '1':
            tofound = self.f1
            return  tofound
        elif tofound == '2':
            tofound = self.f2
            return  tofound
        elif tofound == '3':
            tofound = self.f3
            return  tofound
        elif tofound == '4':
            tofound = self.f4
            return  tofound
        else:
            print('"Please select appropriate Foundation."')

    
    def modes(self):
        mode=input("cascade(1) or foundation(2) or cellslot(3):- ")
        if(mode=='1'):
            modecc=input("cascade to another cascade(1) or cascade to foundation(2) or cascade to cellslot(3):- ")
            if(modecc=='1'):
                self.modecc1()
            elif(modecc=='2'):
                self.modecc2()
            elif(modecc=='3'):
                self.modecc3()
            else:
                print("Please select appropriate Option.")
        elif(mode=='2'):
            modef=input("foundation to cascade(1) or foundation to cellslot(2):- ")
            if(modef=='1'):
                self.modeff1()
            elif(modef=='2'):
                self.modeff2()
            else:
                print("Please select appropriate Option.")
        elif(mode=='3'):
            modecell=input("cellslot to cascade(1) or cellslot to foundation (2):- ")
            if(modecell=='1'):
                self.modec1()
            elif(modecell=='2'):
                self.modec2()
            else:
                print("Please select appropriate Option.")
        else:
            print("Please select appropriate Option.")

        self.output()
    
    
    def modecc1(self):
        first=self.fromcas()
        second=self.tocas()
        if(type(first)==list and type(second)==list):
            if(len(second)!=0 and len(first)!=0):
                lastvalf=(first[-1])
                tempvalf=(lastvalf[0])+(1)
                finalvalf=(tempvalf,lastvalf[1])
                finalvals=(second[-1])
                if(finalvalf[0]==finalvals[0]):
                    if(finalvalf[1]=='H' or finalvalf[1]=='D'):
                        if(finalvals[1]=='C' or finalvals[1]=='S'):
                            first.pop()
                            second.append(lastvalf)
                        else:
                            print("Check Input")
                    elif(finalvalf[1]=='C' or finalvalf[1]=='S'):
                        if(finalvals[1]=='H' or finalvals[1]=='D'):
                            first.pop()
                            second.append(lastvalf)
                        else:
                            print("Check Input")
                    else:
                        print("Check Input")
                else:
                    print("Please select appropriate card.")
            elif(len(first)==0):
                print("Check Input")
            elif(len(second)==0):
                val=first.pop()
                second.append(val)
            else:
                print("Please select appropriate card.")
        else:print("Please select appropriate input.")
                
    def modecc2(self):
        first=self.fromcas()
        second=self.tofound()
        if(type(first)==list and type(second)==list):
            finalvals=second[-1]
            if(len(first)!=0):
                finalvalf=(first[-1])
                if(finalvals[0]==0):
                    if(finalvals[1]==finalvalf[1]):
                        if(finalvalf[1]=='H' and finalvalf[0]==1):
                            val=first.pop()
                            second.append(val)
                        elif(finalvalf[1]=='D' and finalvalf[0]==1):
                            val=first.pop()
                            second.append(val)
                        elif(finalvalf[1]=='C' and finalvalf[0]==1):
                            val=first.pop()
                            second.append(val)
                        elif(finalvalf[1]=='S' and finalvalf[0]==1):
                            val=first.pop()
                            second.append(val)
                        else:
                            print("Please select appropriate card.")
                    else:
                        print("Please give appropriate input.")

                elif(len(second)!=0):
                    finalvals=second[-1]
                    lastvalf=first[-1]
                    tempvalf=(lastvalf[0])-(1)
                    finalvalf=(tempvalf,lastvalf[1])
                    if(finalvalf==finalvals):
                        val=first.pop()
                        second.append(val)
                    else:
                        print("Check Input")

                else:
                    print("Please give appropriate input.")
            elif(len(first)==0):
                print("Please give appropriate input.")
            else:
                print("Please give appropriate input.")
        else:
            print("Please give appropriate input.")

        
    def modecc3(self):
        first=self.fromcas()
        if(type(first)==list):
            if(len(first)!=0):
                if(len(self.c1)==0):
                    val=first.pop()
                    self.c1.append(val)
                elif(len(self.c2)==0):
                    val=first.pop()
                    self.c2.append(val)
                elif(len(self.c3)==0):
                    val=first.pop()
                    self.c3.append(val)
                elif(len(self.c4)==0):
                    val=first.pop()
                    self.c4.append(val)
                else:
                    print("its already full")
            else:
                print("Please give appropriate input.")
        else:
            print("Please give appropriate input.")

        
    def modeff1(self):
        first=self.fromfound()
        second=self.tocas()
        if(type(first)==list and type(second)==list):
            lastvalf=(first[-1])
            if(lastvalf[0]!=0 and len(second)!=0):
                finalvals=(second[-1])
                tempvalf=(lastvalf[0])+(1)
                finalvalf=(tempvalf,lastvalf[1])
                if(finalvalf[0]==finalvals[0]):
                    if(finalvalf[1]=='H' or finalvalf[1]=='D'):
                        if(finalvals[1]=='C' or finalvals[1]=='S'):
                            val=first.pop()
                            second.append(val)
                        else:
                            print("Check Input")
                    elif(finalvalf[1]=='C' or finalvalf[1]=='S'):
                        if(finalvals[1]=='H' or finalvals[1]=='D'):
                            val=first.pop()
                            second.append(val)
                        else:
                            print("Check Input")
                    else:
                        print("Check Input")
                else:
                    print("Check Input")
            elif(lastvalf[0]!=0 and len(second)==0):
                val=first.pop()
                second.append(val)
            elif(lastvalf[0]==0):
                print("Check Input")
            else:
                print("Please select appropriate card.")
        else:
            print("Please select appropriate input.")
        
    def modeff2(self):
        first=self.fromfound()
        if(type(first)==list):
            lastvalf=(first[-1])
            if(lastvalf[0]!=0):
                if(len(self.c1)==0):
                    val=first.pop()
                    self.c1.append(val)
                elif(len(self.c2)==0):
                    val=first.pop()
                    self.c2.append(val)
                elif(len(self.c3)==0):
                    val=first.pop()
                    self.c3.append(val)
                elif(len(self.c4)==0):
                    val=first.pop()
                    self.c4.append(val)
                else:
                    print("its already full")
            elif(lastvalf[0]==0):
                print("Check Input")
        else:
            print("Please select appropriate input.")
        
    def modec1(self):
        first=self.fromcell()
        second=self.tocas()
        if(type(first)==list and type(second)==list):
            if(len(first)!=0):
                lastvalf=(first[-1])
                if(len(second)!=0):
                    finalvals=(second[-1])
                    tempvalf=(lastvalf[0])+(1)
                    finalvalf=(tempvalf,lastvalf[1])
                    if(finalvalf[0]==finalvals[0]):
                        if(finalvalf[1]=='H' or finalvalf[1]=='D'):
                            if(finalvals[1]=='C' or finalvals[1]=='S'):
                                val=first.pop()
                                second.append(val)
                            else:
                                print("Check Input")
                        elif(finalvalf[1]=='C' or finalvalf[1]=='S'):
                            if(finalvals[1]=='H' or finalvals[1]=='D'):
                                val=first.pop()
                                second.append(val)
                            else:
                                print("Check Input")
                        else:
                            print("Check Input")
                    else:
                        print("Check Input")
                elif(len(second)==0):
                    val=first.pop()
                    second.append(val)
                else:
                    print("Check Input")
            else:
                print("Please select appropriate card.")
        else:
            print("Please select appropriate input.")

        
    def modec2(self):
        first=self.fromcell()
        second=self.tofound()
        if(type(first)==list and type(second)==list):
            finalvals=(second[-1])
            if(len(first)!=0 and finalvals[0]!=0):
                lastvalf=(first[-1])
                tempvalf=(lastvalf[0])-(1)
                finalvalf=(tempvalf,lastvalf[1])
                if(finalvalf==finalvals):
                    val=first.pop()
                    second.append(val)
                else:
                    print("Please select appropriate card.")
            elif(len(first)!=0 and finalvals[0]==0):
                lastvalf=(first[-1])
                if(lastvalf[0]==1):
                    if(lastvalf[1]==finalvals[1]):
                        val=first.pop()
                        second.append(val)
                    else:
                        print("Check Input")
                else:
                    print("Please select appropriate card.")

            else:
                print("Please select appropriate card.")
        else:
            print("Please select appropriate input.")
    
    def output(self):
        cf1=[('A',i[1]) if i[0]==1 else (i[0],i[1]) and ('J',i[1]) if i[0]==11 else (i[0],i[1]) and ('Q',i[1]) if i[0]==12 else (i[0],i[1]) and ('K',i[1]) if i[0]==13 else (i[0],i[1]) for i in self.c1]
        cf2=[('A',i[1]) if i[0]==1 else (i[0],i[1]) and ('J',i[1]) if i[0]==11 else (i[0],i[1]) and ('Q',i[1]) if i[0]==12 else (i[0],i[1]) and ('K',i[1]) if i[0]==13 else (i[0],i[1]) for i in self.c2]
        cf3=[('A',i[1]) if i[0]==1 else (i[0],i[1]) and ('J',i[1]) if i[0]==11 else (i[0],i[1]) and ('Q',i[1]) if i[0]==12 else (i[0],i[1]) and ('K',i[1]) if i[0]==13 else (i[0],i[1]) for i in self.c3]
        cf4=[('A',i[1]) if i[0]==1 else (i[0],i[1]) and ('J',i[1]) if i[0]==11 else (i[0],i[1]) and ('Q',i[1]) if i[0]==12 else (i[0],i[1]) and ('K',i[1]) if i[0]==13 else (i[0],i[1]) for i in self.c4]
        ff1=[('A',i[1]) if i[0]==1 else (i[0],i[1]) and ('J',i[1]) if i[0]==11 else (i[0],i[1]) and ('Q',i[1]) if i[0]==12 else (i[0],i[1]) and ('K',i[1]) if i[0]==13 else (i[0],i[1]) for i in self.f1]
        ff2=[('A',i[1]) if i[0]==1 else (i[0],i[1]) and ('J',i[1]) if i[0]==11 else (i[0],i[1]) and ('Q',i[1]) if i[0]==12 else (i[0],i[1]) and ('K',i[1]) if i[0]==13 else (i[0],i[1]) for i in self.f2]
        ff3=[('A',i[1]) if i[0]==1 else (i[0],i[1]) and ('J',i[1]) if i[0]==11 else (i[0],i[1]) and ('Q',i[1]) if i[0]==12 else (i[0],i[1]) and ('K',i[1]) if i[0]==13 else (i[0],i[1]) for i in self.f3]
        ff4=[('A',i[1]) if i[0]==1 else (i[0],i[1]) and ('J',i[1]) if i[0]==11 else (i[0],i[1]) and ('Q',i[1]) if i[0]==12 else (i[0],i[1]) and ('K',i[1]) if i[0]==13 else (i[0],i[1]) for i in self.f4]
        #Upper lines takes 1 and print as 'A' , 11 as 'J' , 12 as 'Q' and 13 as 'K' using for loop
        print("Cell Slot: ",cf1 ,cf2 ,cf3 ,cf4 ," \t\tFoundation: ",ff1[-1] ,ff2[-1] ,ff3[-1] ,ff4[-1])
        print("\n  Cascade1\t Cascade2\t Cascade3\t Cascade4\t Cascade5\t Cascade6\t Cascade7\t Cascade8\n" )
        for cols in zip_longest(self.cascade1[0],self.cascade1[1],self.cascade1[2],self.cascade1[3],self.cascade1[4],self.cascade1[5],self.cascade1[6],self.cascade1[7]):
            cas=list(cols)
            displays=['       ' if i is None else i and ('A',i[1]) if i[0]==1 else (i[0],i[1]) and ('J',i[1]) if i[0]==11 else (i[0],i[1]) and ('Q',i[1]) if i[0]==12 else (i[0],i[1]) and ('K',i[1]) if i[0]==13 else (i[0],i[1]) for i in cas]
            #Upper lines takes 1 and print as 'A' , 11 as 'J' , 12 as 'Q' and 13 as 'K' using for loop
            print(" ",displays[0],"\t",displays[1],"\t",displays[2],"\t",displays[3],"\t",displays[4],"\t",displays[5],"\t",displays[6],"\t",displays[7])
    
    
def main():
    free=NotFreecell()
    free.starts(0)
    
    
    
if __name__=='__main__':
    main()

