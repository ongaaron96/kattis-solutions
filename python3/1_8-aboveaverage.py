num_cases = int(input())

for _ in range(num_cases):
  # first element is number of grades
  grades = list(map(int, input().split()))
  num_students = grades[0]
  average = sum(grades[1:]) / num_students
  
  above_average_count = 0
  for grade in grades[1:]:
    if grade > average:
      above_average_count += 1
  
  percentage = above_average_count / num_students * 100
  print(f"{percentage:.3f}%")
