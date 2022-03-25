class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        num_people = len(people)

        # Create two pointers to track how many people left.
        ptr1 = 0
        ptr2 = num_people - 1

        # After sorting the list.
        # people[ptr1] will be the minimum weight, and
        # people[ptr2] will be the maximum weight in the list
        people.sort()

        ans = 0

        # check if the list is still valid
        while ptr1 <= ptr2:
            # people[ptr1] + people[ptr2] is the minimum weight of two people
            # if that minimum weight is less than limit, we can save two in one boat
            # incrememt ptr1 so that people[ptr1] will be the next minimum,
            # decrement ptr2 so that people[ptr2] will be the next maximum
            if people[ptr2] + people[ptr1] <= limit:
                ptr1 += 1
                ptr2 -= 1
            # if one boat cannot save two people, then save the maximum in the list
            else:
                ptr2 -= 1
            ans += 1
        
        return ans
        
                
            
            
            