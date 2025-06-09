from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        bank = set(bank)  # Faster lookup
        if endGene not in bank:
            return -1
        
        q = deque()
        q.append((startGene, 0))  # (current gene, mutation count)
        
        genes = ['A', 'C', 'G', 'T']
        
        while q:
            current, steps = q.popleft()
            
            if current == endGene:
                return steps
            
            for i in range(len(current)):
                for g in genes:
                    if g != current[i]:  # only mutate one letter
                        mutated = current[:i] + g + current[i+1:]
                        if mutated in bank:
                            q.append((mutated, steps + 1))
                            bank.remove(mutated)  # avoid revisiting
        return -1
