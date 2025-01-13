class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        lock , unlock = [], []

        for i in range(len(s)):
            if locked[i] == '1':
                if s[i] == ')':
                    if lock:
                        lock.pop()
                    elif unlock:
                        unlock.pop()
                    else:
                        return False
                
                else:
                    lock.append(i)

            else:
                unlock.append(i)

        if len(lock) > len(unlock):
            return False

        while lock:
            pos1 = lock.pop()
            pos2 = unlock.pop() 
            if pos1 > pos2:
                return False

        if len(unlock) % 2 == 1:
            return False

        return True       
        