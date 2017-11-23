# Оценки

# Создать список с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
# Посчитать и вывести средний балл по всей школе.
# Посчитать и вывести средний балл по каждому классу.


journal = [
   {'school_class': '1a', 'scores': [5, 4, 4, 5, 3]},
   {'school_class': '1b', 'scores': [3, 4, 5, 2]}, 
   {'school_class': '2a', 'scores': [3, 3, 4, 5, 3]},
   {'school_class': '2b', 'scores': [5, 5, 5, 5, 5]},
   {'school_class': '3a', 'scores': [3, 3, 4, 3]}, 
   {'school_class': '3b', 'scores': [4, 2, 2, 3, 2]}
]

total_sum = 0
total_count = 0

for c in journal:
    c_sum = sum(c['scores'])
    c_count = len(c['scores'])
    c['avg'] = c_sum / c_count
    total_sum += c_sum
    total_count += c_count
    
total_avg = total_sum / total_count
print('Средний балл по школе: ' + str(total_avg))
    
for c in journal:
    print(c['school_class'] + ': ' + str(c['avg']))
