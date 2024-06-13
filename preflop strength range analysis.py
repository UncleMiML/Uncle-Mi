
sorted_hand_strength_file = open ('d:/Python Projects/sorted_hand_strength_file','r')
hand_strength_range1_file = open('d:/Python Projects/hand_strength_range1_file','w')
hand_strength_range2_file = open('d:/Python Projects/hand_strength_range2_file','w')
hand_strength_range3_file = open('d:/Python Projects/hand_strength_range3_file','w')
hand_strength_range4_file = open('d:/Python Projects/hand_strength_range4_file','w')
hand_strength_range5_file = open('d:/Python Projects/hand_strength_range5_file','w')
hand_strength_range6_file = open('d:/Python Projects/hand_strength_range6_file','w')
hand_strength_range7_file = open('d:/Python Projects/hand_strength_range7_file','w')
hand_strength_range8_file = open('d:/Python Projects/hand_strength_range8_file','w')
hand_strength_range9_file = open('d:/Python Projects/hand_strength_range9_file','w')
hand_strength_rangeT_file = open('d:/Python Projects/hand_strength_rangeT_file','w')
hand_strength_rangeJ_file = open('d:/Python Projects/hand_strength_rangeJ_file','w')
hand_strength_rangeQ_file = open('d:/Python Projects/hand_strength_rangeQ_file','w')
hand_strength_rangeK_file = open('d:/Python Projects/hand_strength_rangeK_file','w')

RANGES = 13

def main ():
    
    from_list = sorted_hand_strength_file.readlines() 
    hand_strength = list(from_list)
    hand_strength_range1 = {}
    hand_strength_range2 = {}
    hand_strength_range3 = {}
    hand_strength_range4 = {}
    hand_strength_range5 = {}
    hand_strength_range6 = {}
    hand_strength_range7 = {}
    hand_strength_range8 = {}
    hand_strength_range9 = {}
    hand_strength_rangeT = {}
    hand_strength_rangeJ = {}
    hand_strength_rangeQ = {}
    hand_strength_rangeK = {}
    
    hands_in_range = int (len(hand_strength) / RANGES )
    

    for i in range (hands_in_range) :
        dic_item1 = hand_strength [i]
        dic_hand1 = dic_item1[0:4]
        dic_equity1 = dic_item1[6:10]
        hand_strength_range1 [dic_hand1] = dic_equity1
        dic_item2 = hand_strength [i + hands_in_range]
        dic_hand2 = dic_item2[0:4]
        dic_equity2 = dic_item2[6:10]
        hand_strength_range2 [dic_hand2] = dic_equity2
        dic_item3 = hand_strength [i + 2*hands_in_range]
        dic_hand3 = dic_item3[0:4]
        dic_equity3 = dic_item3[6:10]
        hand_strength_range3 [dic_hand3] = dic_equity3
        dic_item4 = hand_strength [i + 3*hands_in_range]
        dic_hand4 = dic_item4[0:4]
        dic_equity4 = dic_item4[6:10]
        hand_strength_range4 [dic_hand4] = dic_equity4
        dic_item5 = hand_strength [i + 4*hands_in_range]
        dic_hand5 = dic_item5[0:4]
        dic_equity5 = dic_item5[6:10]
        hand_strength_range5 [dic_hand5] = dic_equity5
        dic_item6 = hand_strength [i + 5*hands_in_range]
        dic_hand6 = dic_item6[0:4]
        dic_equity6 = dic_item6[6:10]
        hand_strength_range6 [dic_hand6] = dic_equity6
        dic_item7 = hand_strength [i + 6*hands_in_range]
        dic_hand7 = dic_item7[0:4]
        dic_equity7 = dic_item7[6:10]
        hand_strength_range7 [dic_hand7] = dic_equity7
        dic_item8 = hand_strength [i + 7*hands_in_range]
        dic_hand8 = dic_item8[0:4]
        dic_equity8 = dic_item8[6:10]
        hand_strength_range8 [dic_hand8] = dic_equity8
        dic_item9 = hand_strength [i + 8*hands_in_range]
        dic_hand9 = dic_item9[0:4]
        dic_equity9 = dic_item9[6:10]
        hand_strength_range9 [dic_hand9] = dic_equity9
        dic_itemT = hand_strength [i + 9*hands_in_range]
        dic_handT = dic_itemT[0:4]
        dic_equityT = dic_itemT[6:10]
        hand_strength_rangeT [dic_handT] = dic_equityT
        dic_itemJ = hand_strength [i + 10*hands_in_range]
        dic_handJ = dic_itemJ[0:4]
        dic_equityJ = dic_itemJ[6:10]
        hand_strength_rangeJ [dic_handJ] = dic_equityJ
        dic_itemQ = hand_strength [i + 11*hands_in_range]
        dic_handQ = dic_itemQ[0:4]
        dic_equityQ = dic_itemQ[6:10]
        hand_strength_rangeQ [dic_handQ] = dic_equityQ
        dic_itemK = hand_strength [i + 12*hands_in_range]
        dic_handK = dic_itemK[0:4]
        dic_equityK = dic_itemK[6:10]
        hand_strength_rangeK [dic_handK] = dic_equityK
        
        

    
    for key,value in hand_strength_range1.items():
        print (str (key)+"->"+str(value))
        hand_strength_range1_file.write (str (key)+"->"+str(value)+'\n')
    
    print ("number of hands in range1: ", hands_in_range)

    for key,value in hand_strength_range2.items():
        print (str (key)+"->"+str(value))
        hand_strength_range2_file.write (str (key)+"->"+str(value)+'\n')
    
    print ("number of hands in range2: ", hands_in_range)

    for key,value in hand_strength_range3.items():
        print (str (key)+"->"+str(value))
        hand_strength_range3_file.write (str (key)+"->"+str(value)+'\n')
    
    print ("number of hands in range3: ", hands_in_range)

    for key,value in hand_strength_range4.items():
        print (str (key)+"->"+str(value))
        hand_strength_range4_file.write (str (key)+"->"+str(value)+'\n')
    
    print ("number of hands in range4: ", hands_in_range)

    for key,value in hand_strength_range5.items():
        print (str (key)+"->"+str(value))
        hand_strength_range5_file.write (str (key)+"->"+str(value)+'\n')
    
    print ("number of hands in range5: ", hands_in_range)

    for key,value in hand_strength_range6.items():
        print (str (key)+"->"+str(value))
        hand_strength_range6_file.write (str (key)+"->"+str(value)+'\n')
    
    print ("number of hands in range6: ", hands_in_range)

    for key,value in hand_strength_range7.items():
        print (str (key)+"->"+str(value))
        hand_strength_range7_file.write (str (key)+"->"+str(value)+'\n')
    
    print ("number of hands in range7: ", hands_in_range)

    for key,value in hand_strength_range8.items():
        print (str (key)+"->"+str(value))
        hand_strength_range8_file.write (str (key)+"->"+str(value)+'\n')
    
    print ("number of hands in range8: ", hands_in_range)

    for key,value in hand_strength_range9.items():
        print (str (key)+"->"+str(value))
        hand_strength_range9_file.write (str (key)+"->"+str(value)+'\n')
    
    print ("number of hands in range9: ", hands_in_range)

    for key,value in hand_strength_rangeT.items():
        print (str (key)+"->"+str(value))
        hand_strength_rangeT_file.write (str (key)+"->"+str(value)+'\n')
    
    print ("number of hands in range 10: ", hands_in_range)

    for key,value in hand_strength_rangeJ.items():
        print (str (key)+"->"+str(value))
        hand_strength_rangeJ_file.write (str (key)+"->"+str(value)+'\n')
    
    print ("number of hands in range 11: ", hands_in_range)

    for key,value in hand_strength_rangeQ.items():
        print (str (key)+"->"+str(value))
        hand_strength_rangeQ_file.write (str (key)+"->"+str(value)+'\n')
    
    print ("number of hands in range 12: ", hands_in_range)

    for key,value in hand_strength_rangeK.items():
        print (str (key)+"->"+str(value))
        hand_strength_rangeK_file.write (str (key)+"->"+str(value)+'\n')
    
    print ("number of hands in range 13: ", hands_in_range)

    

main()

sorted_hand_strength_file.close()
hand_strength_range1_file.close()
hand_strength_range2_file.close()
hand_strength_range4_file.close()
hand_strength_range5_file.close()
hand_strength_range6_file.close()
hand_strength_range7_file.close()
hand_strength_range9_file.close()
hand_strength_rangeT_file.close()
hand_strength_rangeJ_file.close()
hand_strength_rangeQ_file.close()
hand_strength_rangeK_file.close()