class UndergroundSystem:

    def __init__(self):
        self.ans={}
        self.enter={}
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.enter[id]=(stationName,t)
        if stationName not in self.ans:
            self.ans[stationName]={}
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        end = stationName
        start = self.enter[id][0]
        t1 = self.enter[id][1]
        if end not in self.ans[start]:
            self.ans[start][end]=[t-t1,1]
        else:
            self.ans[start][end][0]+=t-t1
            self.ans[start][end][1]+=1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.ans[startStation][endStation][0]/self.ans[startStation][endStation][1]
list1 = ["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
list2 = [[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]
obj = UndergroundSystem()
for i in range(len(list1)):
    if list1[i]=='checkIn':
        obj.checkIn(list2[i][0],list2[i][1],list2[i][2])
    if list1[i]=='checkOut':
       obj.checkOut(list2[i][0],list2[i][1],list2[i][2]) 
    if list1[i]=='getAverageTime':
        obj.getAverageTime(list2[i][0],list2[i][1])