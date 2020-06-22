#Leet Code Problems
# Linked List Cycle
#return true if the linked list contains a cycle, false if not

#use whitespace to make code clearer
#comment describing the part of the problem solved by that bit of code
    #comments help explain why not what

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycleFlag(self, head: ListNode) -> bool:
        cur = head
        #walk the entire linked list
        while cur is not None:

            #check to see if we found a loop
            if hasattr(cur, 'visited'):
                return True

            #mark as visited to move to the next
            cur.visited = True
            cur = cur.next

        #if we get here, no loop was detected
        return False


    #slightly slower with more memory, but we don't have to alter the definition of the list node
    def hasCycleDict(self, head: ListNode) -> bool:
        cur = head
        visited = set()
        #walk the entire linked list
        while cur is not None:

            #check to see if we found a loop
            if cur in visited:
                return True

            #mark as visited to move to the next
            visited.add(cur)
            cur = cur.next

        #if we get here, no loop was detected
        return False


#how to solve with O(1) space?
    #walking the list multiple times keeping track of how many times we come across it


'''
Technical Interviewing
-----------------------
1. Hack your mindset
2. Use UPER
3. Teach the problem


Hack your mindset
-relax
-pretend interviewer is a coworker who has just come to you for help on a difficult problem
    -teaching a problem is the right level of a detail for an interview
    -makes you think out loud
    -shows you can systematically solve problems
    -causes you to act like you're part of the team

UPER
-understand: teach the problem to the interviewer
    -start with inputs and outputs
    -ask clarifying questions
-plan: teach the plan to the interviewer
    -conceptually, as little code as possible
    -draw diagrams
    -walk through examples
-execute: code it up (or go over your code if you wrote earlier)
    -separated logical blocks of code with blank space
    -comment
-reflect: look on ways to improve it, or future directions
    -if you thought of a better solution afterwards, talk about this
    -look at alternate solutions and mention why you rejected them
    -talk about things that are out of scope, but might be good
        -how to make more general, modifications to work with different data structures, etc

If truly stuck - start talking about methods that you know won't work. Think out loud. May be given a hint.
-if they give you the answer, show that you understand it - explain it back to them or relate it to past work
'''

#Sample question
#Can you show me how you'd reverse a linked list
#This problem was to reverse a linked list. Can you tell me how you solved it


#U - single or double? Reference to tail node?
#P - iterate through list setting next to point to previous
#  - add each node to a stack then pop them off (t hey will come out in reverse order)


'''

Make your code look sharp
-------------------------
good comments
good use of whitespace
consistent spacing around punctuation and operators
consistent indentation
good variable and function names



Summary
-----------
-teach the problem
-UPER is your best friend
-Make your code look sharp


fastest way to reverse the bits in a byte?

'''