student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_alturas = 0
for alturas in (student_heights):
   total_alturas += alturas
print(total_alturas)

total_alunos = 0
for quantidade in (student_heights):
    total_alunos += 1
print(total_alunos)

media = round(total_alturas/ total_alunos)
print(media)
