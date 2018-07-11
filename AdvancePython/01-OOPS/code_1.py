class Myset:

    def __init__(self,S):
        self.data = S

    def sortedSet(self):
        return sorted(set(self.data))

if __name__ == '__main__':
    s1 = Myset([4,5,6,5,5])
    print(s1.sortedSet())
    s2 = Myset([2,3,4,5,6,7])
    s3 = s1.sortedSet() + s2.sortedSet()
    print(sorted(set(s3)))
    s1 = s1.sortedSet()
    s1.append(23)
    s4 = s1.copy()
    print(s4)
