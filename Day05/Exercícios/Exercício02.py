student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

maior_pontuacao = 0
for score in student_scores:
    if score > maior_pontuacao:
        maior_pontuacao = score
print(f"The highest score in the class is: {maior_pontuacao}")
