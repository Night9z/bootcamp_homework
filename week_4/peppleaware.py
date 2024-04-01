class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        people = [0] * (n+1)
        people[1] = 1  
        mod = 10**9 + 7
        
        for day in range(2, n+1):
            for i in range(day - delay, day - forget, -1):
                if i > 0:
                    people[day] += people[i]
                    people[day] %= mod 
            people[day - forget] = 0

        return sum(people) % mod