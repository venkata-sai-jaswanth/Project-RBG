import json
# To load the colours2.json file
with open("colours2.json","r") as colours:
    loaded_colours = json.load(colours)
    print("colours loaded!")
#To take the input from  the user of the two colours that he wants to mix!

while True :  
    user_c1 = input("Enter the name of the first colour(eg:red(or)green):").strip().lower()
    user_c2 = input("Enter the name of the second colour(eg:orange(or)blue):").strip().lower()
    if user_c1 in loaded_colours and user_c2 in loaded_colours :
        c1 = loaded_colours.get(user_c1)
        c2 = loaded_colours.get(user_c2)
        break 
    else :
        print("please enter the name of the colour withount any typo !")
    

    #doing the average of the colour values

average_list = []    

for x,y in zip(c1,c2):  
    average=x/2+y/2
    average_list.append(average)
dict_differences={}
smallest_difference=9999

for key,value in loaded_colours.items():
    difference_list=[]
    for y,z in zip(average_list,value):
        difference = abs(y-z)
        difference_list.append(difference)
    sum_differences = sum(difference_list)
    dict_differences[key]=sum_differences
    if sum_differences < smallest_difference:
        smallest_difference=sum_differences
        final_colour = key
print(f"by mixing the colours {user_c1} and {user_c2} is {final_colour}")



        


 
