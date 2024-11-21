#Program 3 – Girl Guide Cookies
#Description:   The organizers of the annual Girl Guide cookie sale event want to raise 
#               the stakes on the number of cookies sold and are offering cool prizes to
#               those guides who go above and beyond in their sales efforts. The organizers
#               want a program to print the guide list and their prizes.

#Student #:     
#Student Name:Lucas  


    # YOUR CODE STARTS HERE, each line must be indented (one tab)
def guidenumber(numguides): 
    guides = [] #makes the list for guides 
   
    guides=int(input("enter the number of guides")) #inputs the guide number
    if ValueError:
                    print("error please try again. ") #return if there is a error
                    return guides
            
    for i in range(guides):
                   name=input(f"enter the name of your guide {i+1}")
                   boxsales =int(input(f"enter the number of boxes sold by your guide{name}"))
                   guides[name]= boxsales
                   averagesales= sum(guides/numguides)
                   averagesales
                  
                   highestsales=max(guides)
                   print("{averagesales}")
                   

       for name, sales in numguides:       
        if sales == highestsales:         
            prize = "you won a Trip to the Jamboree!"
        elif sales >averagesales:
            prize = "you get a Badge!"
        elif sales > 0:
            prize = "you get to Split the remaining cookies.."
        else:
            prize = "you get nothing"

                                
print(f"{name:,prizes}")

      






    # YOUR CODE ENDS HERE
def main():
        
        main()