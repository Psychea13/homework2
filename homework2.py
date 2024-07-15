homework_count = 12
hour_count = 1.5
minute_count = hour_count * 60
course_name = 'Python'
time_for_one_exercise = minute_count / homework_count

print('Курс:', course_name+',', ' всего задач:', (str(homework_count))+',', ' затрачено часов:', (str(hour_count))+',', ' среднее время выполнения:', time_for_one_exercise, 'минут')