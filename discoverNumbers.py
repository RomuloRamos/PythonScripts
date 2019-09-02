def isNumberChecker(charElement):
    
    try:
        float(charElement)
        
    except:
        return False
        
    return True    

def main():
    print("Please, enter with your string:")
    
    strList = input()
    print("Your string was: ", strList)
    
    intSequenceDelimiter = 4
    intElementCount = 0
    intCounterPos = 0
    listAllPositions = []
    
    for element in strList:
        
        if(isNumberChecker(element)):
            intCounterPos = intCounterPos+1
        else:
            if(intCounterPos >= intSequenceDelimiter):
                intFirst = (intElementCount-intCounterPos)
                listAllPositions.append((intFirst,(intElementCount-1)))

            intCounterPos = 0
        
        intElementCount = intElementCount + 1    
    #To the case that there are a sequence number on the final
    if(intCounterPos >= intSequenceDelimiter):
        intFirst = (intElementCount-intCounterPos)
        listAllPositions.append((intFirst,(intElementCount-1)))            
    print(listAllPositions)


if __name__ == "__main__":
    
    main()
