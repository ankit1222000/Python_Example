s=input("Enter a String: ")
a=s.split(',')
for i in range(1,len(a)):
    a[i]=int(a[i])
sumsub=sum(a[1:6])
sumprac=sum(a[6:])
percent=((sumsub+sumprac)/(len(a)-1))*100
print('{0} obtained {1} marks out of 500 in theory and {2} marks out of 30 in practical and successfully passed the exam with {3}% in aggregate. Many Congratulations to {0}'.format(a[0],sumsub,sumprac,percent))