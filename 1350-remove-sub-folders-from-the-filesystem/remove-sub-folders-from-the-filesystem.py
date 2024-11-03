class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key = lambda x: len(x))
        lookup = {}

        def parse(key):
            directory = key[1:].split('/')
            return directory

        for key in folder:
            directory = parse(key)
            look = []
            for item in directory:
                look.append(item)
                if tuple(look) in lookup:
                    break
            lookup[tuple(look)] = True

        soln = list(lookup.keys())
        for i in range(len(soln)):
            soln[i] = "/".join(soln[i])
            soln[i] = "/" + soln[i]
    

        return soln