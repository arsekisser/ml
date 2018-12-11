
import csv
hypo=['%','%','%','%','%','%']
with open('Train.csv') as csv_file:
    readcsv=csv.reader(csv_file,delimiter=',')
    print(readcsv)
    data=[]
    print("\n The given training example are:");
    for row in readcsv:
        print(row)
        if row[len(row)-1].upper()=="Y":
            data.append(row)
print("The positive exa are");
for x in data:
    print(x);
print("\n");
TotalExample=len(data);
i=0;
j=0;
k=0;
print("The steps of the find-s algorithm are:\n",hypo);
list=[];
p=0;
d=len(data[p])-1;
for j in range(d):
         list.append(data[i][j]);
hypo=list;
i=1;
for i in range(TotalExample):
    for k in range(d):
        if hypo[k]!=data[i][k]:
            hypo[k]='?';
            k=k+1;
        else:
            hypo[k];
    print(hypo);

print("\n The maximize specific find-s hypothesis for the given training examples is");
print(hypo);