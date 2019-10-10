class calldetail:
    def __init__(self,a,b,c,d):
        self.calledfrom=a
        self.calledto=b
        self.duration=c
        self.type=d
    def printout(self):
        print("called from:",self.calledfrom)
        print("called to:",self.calledto)
        print("duration:",self.duration)
        print("type:",self.type)
class util:
    def __init__(self):
        self.li=None
    def parse_customer(self,li):
        l=[]
        for i in range(len(li)):
            a=li[i].split(",")
            b=calldetail(a[0],a[1],a[2],a[3])
            b.printout()
            l.append(b)
call1="9934560182,98673627123,23,STD"
call2="9934560182,98673627123,33,Local"
call3="9934560182,98673627123,43,ISD"
list_of_call_string=[call1,call2,call3]
util().parse_customer(list_of_call_string)

            
