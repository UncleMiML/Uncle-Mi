unzip_hand_strength_file = open ('d:/Python Projects/unzip_hand_strength_file','r')
sorted_hand_strength_file = open ('d:/Python Projects/sorted_hand_strength_file','w')

def main ():
    
    from_list = unzip_hand_strength_file.readlines() 
    hand_strength = list(from_list)
    hand_strength_dictionary = {}
    for i in range (len(hand_strength)) :
        #print (hand_strength[i])
        dic_item = hand_strength [i]
        dic_hand = dic_item[0:4]
        dic_equity = dic_item[6:10]
        hand_strength_dictionary [dic_hand] = dic_equity
    
 
    sorted_hand_strength_dictionary = sorted(hand_strength_dictionary.items(), key=lambda x: x[1], reverse=True)
    sorted_hand_strength_dictionary = dict(sorted_hand_strength_dictionary)
 
    
    print_old_list (sorted_hand_strength_dictionary)

def print_old_list (sorted_hand_strength_dictionary) :
    for key,value in sorted_hand_strength_dictionary.items():
        print (str (key)+"->"+str(value))
        sorted_hand_strength_file.write (str (key)+"->"+str(value)+'\n')
    total_hands = len (sorted_hand_strength_dictionary)
    print ("Total hands = ", total_hands)


main()
unzip_hand_strength_file.close()  
sorted_hand_strength_file.close()