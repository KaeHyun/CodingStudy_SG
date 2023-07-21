# 성적이 낮은 순서로 학생 출력하기
n = int(input())
students = []

for i in range(n):
    name, scrore = input().split()
    students.append([name, int(scrore)])

students.sort(key=lambda x : x[1])

print(students)

for i in students:
    print(i[0], end=' ')