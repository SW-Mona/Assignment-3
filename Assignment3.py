#218435882
#SW MONA
#ASSIGNMENT 3
#Solution 1
s = 'fullstackslp';
print("Solution 1")
print("# '",s[0],"'");
print("")
print("# '",s[11],"'");
print("")
print("# '",s[4:9],"'");
print("")
print("# '",s[9:12],"'");
print("")
print("# '",s[7:10],"'");
print("")
#s.reverse()
print("# '",s[11],s[10],s[9],s[8],s[7],s[6],s[5],s[4],s[3],s[2],s[1],s[0],"'");
print("")

#Solution 2
print("Solution 2")
l = [3,7,[5,[1,4,'hello']]] 
l[2][1][2] = 'goodbye'
print(l)
print("")

#Solution 3
print("Solution 3")
d1 = {'Simple_key':'hello'}
d2 = {'k1':{'k2':'hello'}}
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d1['Simple_key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1][0])
print("")

#Solution 4
print("Solution 4")
mylist =[1,1,1,1,1,2,2,2,2,3,3,3,3]
print(mylist)
new_set = set(mylist)
print(new_set)
print("")

#Solution 5
print("Solution 5")
age = 45
name = "Raptor"

string_1 = "Hello my dog's name is {} and he looks {} years old".format(name,age)
print(string_1)
print("")