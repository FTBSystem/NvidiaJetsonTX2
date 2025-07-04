import cv2

def Scan(Min,Max):
    
    Index = Min
    IndexList=[]
    GoodList=[]
    
    for Index in list(range(Min,Max,1)):
        try:
            print("Testing",Index)
            cap = cv2.VideoCapture(Index)
            
            if cap.isOpened():
                
                ret, frame = cap.read()
                
                if ret:
                                        
                    print("Index=",Index,"State=",ret)
                    IndexList.append(Index)
                    
                    try:
                        #cv2.imshow("Frame", frame)
                        cv2.resize(frame,(100,100)) # test frame resizeable
                        cv2.waitKey(1)
                        GoodList.append(Index)
                    except Exception as e:
                        print(e)
                    
        except Exception as e:
            print(e)
    cv2.destroyAllWindows()    
    return GoodList
    
Max = 100
Min = 0

if __name__=="__main__":
    print("Usable cam:",Scan(Min,Max))
