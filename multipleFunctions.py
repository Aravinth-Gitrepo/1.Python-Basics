class multipleFunctions:
    def Subfields():
        print('Sub-fields in AI are:')
        print('Machine Learning')
        print('Neural Networks')
        print('Vision')
        print('Robotics')
        print('Speech Processing')
        print('Natural Language Processing')
              

    def Elegible():
        gender=input('Your Gender:')
        age=(int(input('Your Age:')))
        if (gender=='Male' and age>=21):
                message='Eligible'
        elif (gender=='Female' and age>=18):
                message='Eligible'
        else:
                message='NOT ELIGIBLE'
        return message


    def triangle():
        H=int(input("Height:"))
        B=int(input('Breadth:'))
        Area=(H*B)/2
        print('Area of Triangle:',Area)
        H1=int(input('Height1:'))
        H2=int(input('Height2:'))
        H3=int(input('Breadth:'))
        perimeter=H1+H2+H3
        print('Perimeter of Triangle:',perimeter)
        
       
    def oddEven():
        num=int(input("Enter a number:"))
        if num%2==0:
            #print('is Even number')
            message=num ,'is Even number'
        else:
            #print('is Odd number')
            message=num ,'is Odd number'
        return message
    
    def percentage():
        Sub1=(int(input("Subject1=")))
        Sub2=(int(input("Subject2=")))
        Sub3=(int(input("Subject3=")))
        Sub4=(int(input("Subject4=")))
        Sub5=(int(input("Subject5=")))
        total=(Sub1+Sub2+Sub3+Sub4+Sub5)
        #total= ("Total:",scal)
       # return total
        print ("Total:",total)
        percent=(float((total/5)))
        percent1= ("{0:.14f}".format(percent))
        #print("percentage:", percent1)
        percent2=("Percentage:", percent1)
        return percent2
    