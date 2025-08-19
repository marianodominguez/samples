Role

you are a logical analyzer, your task is to find a path from an initial state to a final state, following a set of rules.

Problem description:

Three missionaries and three cannibals are stranded on a riverbank. They need to cross the river to the opposite bank. Any person can operate the raft, but the raft must be returned to the original side after every crossing. At no point can there be more cannibals than missionaries on either side of the river. The goal is to safely transport all three missionaries and three cannibals to the destination bank. 


Initial state.

3 missionary and 3 Cannibals have to cross a river, using a raft.

 this is represented by this string:

¨MMMCCCR|”

where M is a missionary , C is a Cannibal , R is the Raft and | is the river     

Final state

|MMMCCCR   

All cannibals and missionaries are in the other side of the river.   

Rules:

    - only 2 People can cross at a time in rthe raft
    - After crossing , someone in that side has to bring the raft back, e.g. after MMCC|RCM, MMCCR|CM is invalid, but MMMCCR|C is valid
    - There cannot be more cannibals than missionaries at any time in any side, this is a critical resriction  
    - the raft cannot cross alone
     

Output:
return a a table with a sequence of valid movements that goes from the inital state to the final state 


Let’s finalize the rules and problem definition: 

Finalized Rules of the Puzzle: 

     The Goal: All three missionaries and three cannibals must cross the river safely.
     The Riverbanks: There are two riverbanks – one starting bank and one destination bank.
     The raft: Any person can operate the raft.
     The Restriction: At no point can there be more cannibals than missionaries on either side of the river.
     The Return: The raft must be returned to the original side after every crossing.
     

Re-defined Problem: 


