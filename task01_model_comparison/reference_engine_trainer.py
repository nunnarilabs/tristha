# Reference engine to GENERATE the verified answer key for the harder Task 1.
FX = {"INR":1, "USD":84, "EUR":90}
CHAN_LIMIT = {"POS":50000, "ECOM":30000, "ATM":25000}
DAILY_CAP = 80000      # per account, cumulative approved INR
VEL_WINDOW = 60        # minutes
VEL_MAX = 3            # max approved per card within any rolling 60-min window

accounts = {"ACC1":100000, "ACC2":40000, "ACC3":500000}
cum = {"ACC1":0,"ACC2":0,"ACC3":0}
cards = {
 "A":{"acc":"ACC1","num_ok":True,"status":"ACTIVE","exp":(2027,12),"debit":True,"intl":True},
 "B":{"acc":"ACC1","num_ok":True,"status":"ACTIVE","exp":(2026,11),"debit":True,"intl":False},
 "C":{"acc":"ACC2","num_ok":True,"status":"ACTIVE","exp":(2028,12),"debit":True,"intl":True},
 "D":{"acc":"ACC1","num_ok":False,"status":"ACTIVE","exp":(2027,12),"debit":True,"intl":True},
 "E":{"acc":"ACC3","num_ok":True,"status":"ACTIVE","exp":(2026,9),"debit":True,"intl":False},
 "F":{"acc":"ACC2","num_ok":True,"status":"STOLEN","exp":(2028,1),"debit":True,"intl":True},
 "G":{"acc":"ACC3","num_ok":True,"status":"ACTIVE","exp":(2025,3),"debit":True,"intl":True},
 "H":{"acc":"ACC3","num_ok":True,"status":"ACTIVE","exp":(2027,1),"debit":False,"intl":True},
}
vel = {k:[] for k in cards}      # list of minutes of approved txns
appt = {k:0 for k in cards}      # approved count today
approved_log = {}                # txn_id -> (card, inr) for reversals

TODAY=(2026,6)
def expired(exp): return exp < TODAY   # (yyyy,mm) before June 2026

def to_min(hhmm):
    h,m=hhmm.split(":"); return int(h)*60+int(m)

def authorize(tid, t, ck, chan, cur, amt):
    c=cards[ck]; acc=c["acc"]
    inr = round(amt*FX[cur])
    intl = cur!="INR"
    # precedence
    if not c["num_ok"]: return dec(tid,ck,"14","Invalid card number",inr)
    if c["status"]=="LOST": return dec(tid,ck,"41","Card lost",inr)
    if c["status"]=="STOLEN": return dec(tid,ck,"43","Card stolen",inr)
    if expired(c["exp"]): return dec(tid,ck,"54","Card expired",inr)
    if intl and not c["intl"]: return dec(tid,ck,"62","International txn blocked on card",inr)
    if amt<=0: return dec(tid,ck,"13","Invalid amount",inr)
    if not c["debit"]: return dec(tid,ck,"57","Debit not permitted",inr)
    if inr > CHAN_LIMIT[chan]: return dec(tid,ck,"61",f"Over {chan} per-txn limit ({inr}>{CHAN_LIMIT[chan]})",inr)
    win=[x for x in vel[ck] if x> t-VEL_WINDOW]
    if len(win)>=VEL_MAX: return dec(tid,ck,"65",f"Velocity: {len(win)} approved in last 60min",inr)
    if cum[acc]+inr > DAILY_CAP: return dec(tid,ck,"61",f"Over account daily cap ({cum[acc]+inr}>{DAILY_CAP})",inr)
    if inr > accounts[acc]: return dec(tid,ck,"51",f"Insufficient ({inr}>{accounts[acc]})",inr)
    # approve
    accounts[acc]-=inr; cum[acc]+=inr; vel[ck].append(t); appt[ck]+=1
    approved_log[tid]=(ck,inr,t)
    return row(tid,ck,chan,cur,amt,inr,"Approved","00","Approved",acc)

def dec(tid,ck,code,reason,inr):
    c=cards[ck]
    return row(tid,ck,None,None,None,inr,"Declined",code,reason,c["acc"])

def reverse(tid, ref):
    ck,inr,tt = approved_log[ref]; acc=cards[ck]["acc"]
    accounts[acc]+=inr; cum[acc]-=inr; vel[ck].remove(tt); appt[ck]-=1
    return {"tid":tid,"card":ck,"dec":"Processed","code":"REV","reason":f"Reversal of {ref} (+{inr})","acc":acc}

def row(tid,ck,chan,cur,amt,inr,d,code,reason,acc):
    return {"tid":tid,"card":ck,"inr":inr,"dec":d,"code":code,"reason":reason,"acc":acc}

txns=[
 ("T1","09:00","A","POS","INR",20000),
 ("T2","09:05","D","POS","INR",5000),
 ("T3","09:10","F","POS","INR",5000),
 ("T4","09:15","G","POS","INR",5000),
 ("T5","09:20","E","ECOM","USD",100),
 ("T6","09:25","H","POS","INR",5000),
 ("T7","09:30","A","ECOM","INR",35000),
 ("T8","09:40","B","POS","INR",50000),
 ("T9","09:45","A","POS","INR",20000),
 ("REV","09:50","REV-T8",None,None,None),
 ("T11","09:55","A","POS","INR",20000),
 ("T12","10:00","C","ECOM","INR",5000),
 ("T13","10:10","C","ECOM","INR",5000),
 ("T14","10:20","C","ECOM","INR",5000),
 ("T15","10:30","C","ECOM","INR",5000),
 ("T16","11:05","C","ECOM","USD",360),
 ("T17","11:10","C","POS","INR",30000),
]
print(f"{'Txn':4}{'Card':5}{'INR':>8}  {'Dec':10}{'Code':5} Reason")
for tid,tm,ck,chan,cur,amt in txns:
    if tid=="REV":
        r=reverse(tid,"T8")
        print(f"{tid:4}{r['card']:5}{'':>8}  {r['dec']:10}{r['code']:5} {r['reason']}")
        continue
    r=authorize(tid,to_min(tm),ck,chan,cur,amt)
    print(f"{tid:4}{r['card']:5}{r['inr']:>8}  {r['dec']:10}{r['code']:5} {r['reason']}")
print()
print("FINAL ACC1 balance:",accounts["ACC1"],"cum:",cum["ACC1"])
print("FINAL ACC2 balance:",accounts["ACC2"],"cum:",cum["ACC2"])
print("Approved counts:",{k:appt[k] for k in ['A','B','C']})
