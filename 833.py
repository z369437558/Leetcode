s = "mhnbzxkwzxtaanmhtoirxheyanoplbvjrovzudznmetkkxrdmr"
indexes = [46,29,2,44,31,26,42,9,38,23,36,12,16,7,33,18]
sources = ["rym","kv","nbzxu","vx","js","tp","tc","jta","zqm","ya","uz","avm","tz","wn","yv","ird"]
targets = ["gfhc","uq","dntkw","wql","s","dmp","jqi","fp","hs","aqz","ix","jag","n","l","y","zww"]
Z = sorted(zip(indexes,sources,targets))
indexes,sources,targets = zip(*Z)

ans=""
lastpoint=0
for i in range(len(sources)):
    if sources[i] in s[indexes[i]:]:
        # print(s[indexes[i]:].index(sources[i]),indexes[i])
        if s[indexes[i]:].index(sources[i])==0:
            ans=ans+s[lastpoint:indexes[i]]+targets[i]
            lastpoint = indexes[i]+len(sources[i])
ans = ans + s[lastpoint:]
print(ans)