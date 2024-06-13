new_hand_strength_file = open ('d:/Python Projects/new_hand_strength_file', 'w')
hand_strength_file = open ('d:/Python Projects/hand_strength_file','r')

def main ():
    
    from_list = hand_strength_file.readlines() 
    hand_strength = list(from_list)
    hand_strength_dictionary = {}
    for i in range (len(hand_strength)) :
        #print (hand_strength[i])
        dic_item = hand_strength [i]
        dic_hand = dic_item[0:3]
        dic_equity = dic_item[5:9]
        hand_strength_dictionary [dic_hand] = dic_equity

    print_old_list (hand_strength_dictionary)
    
    start = input ("Create a hand strength dictionary(1) or check your hand strength(2) ?")
    start = int (start)

    if start == 1 :
       
        hand_strength_list = create_list (hand_strength_dictionary)

        print_new_list (hand_strength_list)
    
    

def create_list (hand_strength_dictionary):
    hand_strength_list = hand_strength_dictionary
    while True :
        your_hand = input("Please input your pre-flop cards (end with s for suited, o for offsuited): ")
        if your_hand == "":
            break
        
        preflop_equity = input ("Run the solver and input the equity (in %): ")
        preflop_equity = float (preflop_equity)

        hand_strength_list [your_hand] = preflop_equity

    return hand_strength_list


def print_old_list (hand_strength_list) :
    for key,value in hand_strength_list.items():
        print (str (key)+"->"+str(value))

def print_new_list (hand_strength_list) :
    for key,value in hand_strength_list.items():
        print (str (key)+"->"+str(value))
        new_hand_strength_file.write (str (key)+"->"+str(value)+'\n')
     


main ()
new_hand_strength_file.close()  
hand_strength_file.close()
