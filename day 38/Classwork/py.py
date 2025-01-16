def manual_difference(sett1, sett2):
    Answer = sett1.copy()  
    Answer -= sett2        
    return Answer
sett1 = {1, 2, 3, 4}
sett2 = {3, 4, 5, 6}

Answer = manual_difference(sett1, sett2)
print(Answer)  












student_giorgi = {
    'სახელი': 'გიორგი',
    'გვარი': 'ჩიღინაძე',
    'ასაკი': 15,
    'საშუალო ქულა': 8.0
}


student_davit = {
    'სახელი': 'დავით',
    'გვარი': 'მენაბდე',
    'ასაკი': 18,
    'საშუალო ქულა': 9.5
}


print("გიორგის ინფორმაცია:", student_giorgi)
print("დავითის  ინფორმაცია:", student_davit)
