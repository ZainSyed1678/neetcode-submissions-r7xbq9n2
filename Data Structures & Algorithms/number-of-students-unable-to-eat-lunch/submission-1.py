class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        while students and count != len(students):
            if students[0] != sandwiches[0]:
                count += 1
                
                students.append(students.pop(0))
            else:
                count = 0
                students.pop(0)
                sandwiches.pop(0)
        return count