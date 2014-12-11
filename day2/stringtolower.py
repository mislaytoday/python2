L =['Hello','World','IBM',18,None]
print [s.lower() if isinstance(s,str) else s for s in L]

