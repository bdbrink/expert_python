class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        votes = []
        for char in senate:
            votes.append(char)
        
        if len(votes) <= 2:
            first_vote = votes[0]
            if first_vote == "R":
                return "Radiant"
            else:
                return "Dire"
        else:
            last_vote = votes[-1]
            if last_vote == "R":
                return "Radiant"
            else:
                return "Dire"

radiant = deque()
        dire = deque()
        
        # Step 1: Add the indices of the senators to the respective queues
        for i, s in enumerate(senate):
            if s == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        
        # Step 2: Process the voting and banning until one side wins
        while radiant and dire:
            r_index = radiant.popleft()
            d_index = dire.popleft()
            
            # The senator with the lower index bans the other
            if r_index < d_index:
                # Radiant wins this round, push the Radiant senator to the end of the queue (new index is current index + total senators)
                radiant.append(r_index + len(senate))
            else:
                # Dire wins this round, push the Dire senator to the end of the queue
                dire.append(d_index + len(senate))
        
        # Step 3: Check which party has remaining senators
        return "Radiant" if radiant else "Dire"
