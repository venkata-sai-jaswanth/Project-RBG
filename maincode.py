import json
import time 

#To print title of the project

print("\033[5;3;38;2;255;0;128m---------------------------------\033[0m\033[5;3;38;2;255;255;255mPROJECT  RGB\033[0m\033[5;3;38;2;0;255;255m-------------------------------\033[0m")




# To load the colours2.json file
print("loading database please wait....")
time.sleep(1)


with open("colours.json","r") as colours:
    loaded_colours = json.load(colours)
 



print(f"\033[A\033[K✔ colours loaded successfully! ({len(loaded_colours)} colors available)")

#we create a fuction to use it later to display the colours

def colour(c1,c2,average_list):
    R ,G,B = c1
    c1_colour= f"\033[38;2;{R};{G};{B}m █████ \033[0m"
    R,G,B= c2 
    c2_colour=f"\033[38;2;{R};{G};{B}m █████ \033[0m"
    R,G,B = average_list 
    average_list_colour= f"\033[38;2;{R};{G};{B}m █████ \033[0m"
    return c1_colour,c2_colour,average_list_colour

#To take the input from  the user of the two colours that he wants to mix!

while True :  
    user_c1 = input("Enter the name of the first colour(eg:red(or)green.....):").strip().lower()
    user_c2 = input("Enter the name of the second colour(eg:orange(or)blue.....):").strip().lower()
    if user_c1 in loaded_colours and user_c2 in loaded_colours :
        c1 = loaded_colours.get(user_c1)
        c2 = loaded_colours.get(user_c2)
        break 
    else :
        print("\033[5;3;38;2;255;0;128m----------\033[0m\033[3;38;2;255;255;255m please enter the name of the colour withount any typo! \033[0m\033[5;3;38;2;0;255;255m----------\033[0m")

        
    
#doing the average of the colour values

average_list = []    

for x,y in zip(c1,c2):  
    sum_value=x+y
    average=sum_value//2
     

    average_list.append(int(average))
dict_differences={}
smallest_difference=9999


#to check the colour matched to the average value 

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

box1,box2,box3=colour(c1,c2,average_list)

#To print out the result

print(f"By mixing the colours '{user_c1} {box1}' and '{user_c2} {box2}' gives '{final_colour} {box3}' ")

print("\033[5;3;38;2;255;0;128m-------------------------- \033[0m\033[5;3;38;2;255;255;255m--------------------- \033[0m\033[5;3;38;2;0;255;255m---------------------------\033[0m")      


 
