hand_strength_file = open ('d:/Python Projects/hand_strength_file','r')
unzip_hand_strength_file = open ('d:/Python Projects/unzip_hand_strength_file','w')

def main ():
    
    from_list = hand_strength_file.readlines() 
    hand_strength = list(from_list)
    unzip_hand_strength_dictionary = {}
    s = 0
    o = 0
    p= 0
    for i in range (len(hand_strength)) :
        dic_item = hand_strength [i]
        dic_hand = dic_item[0:3]
        dic_equity = dic_item[5:9]
        first_card_num = dic_item[0]
        second_card_num = dic_item [1]
        suited_or_not = dic_item[2]
        
        if suited_or_not == "s" :
            dic_key1 = "s"+str(first_card_num)+"s"+str(second_card_num)
            dic_key2 = "h"+str(first_card_num)+"h"+str(second_card_num)
            dic_key3 = "c"+str(first_card_num)+"c"+str(second_card_num)
            dic_key4 = "d"+str(first_card_num)+"d"+str(second_card_num)
            unzip_hand_strength_dictionary [dic_key1] = dic_equity
            unzip_hand_strength_dictionary [dic_key2] = dic_equity
            unzip_hand_strength_dictionary [dic_key3] = dic_equity
            unzip_hand_strength_dictionary [dic_key4] = dic_equity
            s =s+4
        elif suited_or_not == "o" :
            dic_key1 = "s"+str(first_card_num)+"h"+str(second_card_num)
            dic_key2 = "s"+str(first_card_num)+"c"+str(second_card_num)
            dic_key3 = "s"+str(first_card_num)+"d"+str(second_card_num)
            dic_key4 = "h"+str(first_card_num)+"s"+str(second_card_num)
            dic_key5 = "h"+str(first_card_num)+"c"+str(second_card_num)
            dic_key6 = "h"+str(first_card_num)+"d"+str(second_card_num)
            dic_key7 = "c"+str(first_card_num)+"s"+str(second_card_num)
            dic_key8 = "c"+str(first_card_num)+"h"+str(second_card_num)
            dic_key9 = "c"+str(first_card_num)+"d"+str(second_card_num)
            dic_keyt = "d"+str(first_card_num)+"s"+str(second_card_num)
            dic_keyj = "d"+str(first_card_num)+"h"+str(second_card_num)
            dic_keyq = "d"+str(first_card_num)+"c"+str(second_card_num)
            unzip_hand_strength_dictionary [dic_key1] = dic_equity
            unzip_hand_strength_dictionary [dic_key2] = dic_equity
            unzip_hand_strength_dictionary [dic_key3] = dic_equity
            unzip_hand_strength_dictionary [dic_key4] = dic_equity
            unzip_hand_strength_dictionary [dic_key5] = dic_equity
            unzip_hand_strength_dictionary [dic_key6] = dic_equity
            unzip_hand_strength_dictionary [dic_key7] = dic_equity
            unzip_hand_strength_dictionary [dic_key8] = dic_equity
            unzip_hand_strength_dictionary [dic_key9] = dic_equity
            unzip_hand_strength_dictionary [dic_keyt] = dic_equity
            unzip_hand_strength_dictionary [dic_keyj] = dic_equity
            unzip_hand_strength_dictionary [dic_keyq] = dic_equity
            o = o+12
        else :
            dic_key1 = "s"+str(first_card_num)+"h"+str(second_card_num)
            dic_key2 = "s"+str(first_card_num)+"c"+str(second_card_num)
            dic_key3 = "s"+str(first_card_num)+"d"+str(second_card_num)
            dic_key4 = "h"+str(first_card_num)+"c"+str(second_card_num)
            dic_key5 = "h"+str(first_card_num)+"d"+str(second_card_num)
            dic_key6 = "c"+str(first_card_num)+"d"+str(second_card_num)
            unzip_hand_strength_dictionary [dic_key1] = dic_equity
            unzip_hand_strength_dictionary [dic_key2] = dic_equity
            unzip_hand_strength_dictionary [dic_key3] = dic_equity
            unzip_hand_strength_dictionary [dic_key4] = dic_equity
            unzip_hand_strength_dictionary [dic_key5] = dic_equity
            unzip_hand_strength_dictionary [dic_key6] = dic_equity
            p = p+6
   
    
    print_list (unzip_hand_strength_dictionary,s,o,p)

def print_list (unzip_hand_strength_dictionary,s,o,p) :
    for key,value in unzip_hand_strength_dictionary.items():
        print (str (key)+"->"+str(value))
        unzip_hand_strength_file.write (str (key)+"->"+str(value)+'\n')
    total_hands = len (unzip_hand_strength_dictionary)
    print ("Total hands = ", total_hands)
    print ("s=",s, "   o=",o,"     p=",p)

main()
hand_strength_file.close()  
unzip_hand_strength_file.close()