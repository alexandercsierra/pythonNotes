#today get working solution
#tomorrow, optimize them

#First-pass Solutions - UPER

    #Overwhelmed? Start asking questions to help UNDERSTAND the problem
        #jot them down
        #write down visualizations of the solution
        #can we solve an easier version of the problem first?
        
        #FBR : Fast, Bad, Wrong (rong)
        #FBI : Fast, Bad, Inefficient?
            #start somewhere, doesn't have to be efficient, good, or right
            #it is easier to start somewhere and improve than to wait to start until it's perfect

            # Code it
            # Make it work
            # Make it performant
            # Review and optimize as needed

    # "If there is a problem you can't solve, then there is an easier problem you can solve. Find it."

#Find middle node of linked list
#https://gist.github.com/seanchen1991/3887a0315ca24fe4459bd704fcc60978

    #could get to last node with counter - 5
        #divide by two - 2
        #find node at "index" 2

    #have two pointers, one moving twice as fast as the other
        #when one is at the end
        #the other will be halfway

        #with an even number you can overshoot the end or stop before, either way will return one of the middle two nodes which is acceptable for this problem

#Find target in 2D matrix