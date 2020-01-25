squad={'Batsman':{'Rohit Sharma':{'Matches':10,'Runs':2324,'Average':333,'Top Score':242},'Virat Kohli':{'Matches':20,'Runs':85948,'Average':2020,'Top Score':142},
'Shikhar Dhawan':{'Matches':30,'Runs':74857,'Average':444,'Top Score':333}}}
lst=[]
[lst.append((str(value),x)) for x,y in squad['Batsman'].items() for key,value in y.items() if(key=="Top Score")]
lst=max(lst)
print("Highest Score: {0} Name: {1}".format(lst[0],lst[1]))



		






