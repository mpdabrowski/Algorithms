from typing import List
import math

class MergeSort:
    def sort(self, A: List[int]) -> List[int]:
        if (len(A) < 2):
            return A
        
        mid = math.ceil(len(A) / 2)
        C = self.sort(A[:mid])
        D = self.sort(A[mid:])


        return self.merge(C, D)


    def merge(self, C: List[int], D: List[int]) -> List[int]:
        i = j = 0
        B = []
        while len(C) > i and len(D) > j:
            if C[i] < D[j]:
                B.append(C[i])
                i += 1
            else:
                B.append(D[j])
                j += 1

        while len(C) > i:
            B.append(C[i])
            i += 1

        while len(D) > j:
            B.append(D[j])
            j += 1

        return B


arr = [5, 4, 1, 8, 7, 2, 6, 3]

print(MergeSort().sort(arr))