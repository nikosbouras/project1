import math


def calculate_averages(students_scores):
    return {
        'Μαθηματικά': sum([students_score[1] for students_score in students_scores]) / len(students_scores),
        'Φυσική': sum([students_score[2] for students_score in students_scores]) / len(students_scores),
        'Αγγλικά': sum([students_score[3] for students_score in students_scores]) / len(students_scores)
    }

def top_students(students_scores):
    res = {
        'Μαθηματικά': ('', 0),
        'Φυσική': ('', 0),
        'Αγγλικά': ('', 0)
    }
    for students_score in students_scores:
        if students_score[1] > res['Μαθηματικά'][1]:
            res['Μαθηματικά'] = (students_score[0], students_score[1])
        if students_score[2] > res['Φυσική'][1]:
            res['Φυσική'] = (students_score[0], students_score[2])
        if students_score[3] > res['Αγγλικά'][1]:
            res['Αγγλικά'] = (students_score[0], students_score[3])

    return {
        'Μαθηματικά': res['Μαθηματικά'][0],
        'Φυσική': res['Φυσική'][0],
        'Αγγλικά': res['Αγγλικά'][0],
    }

def students_above_threshold(students_scores, threshold):
    count = 0
    for students_score in students_scores:
        if students_score[1] > threshold and students_score[2] > threshold and students_score[3] > threshold:
            count += 1
    return count

def unique_scores(students_scores):
    return {
        'Μαθηματικά': set([students_score[1] for students_score in students_scores]),
        'Φυσική': set([students_score[2] for students_score in students_scores]),
        'Αγγλικά': set([students_score[3] for students_score in students_scores]),
    }

def calculate_std_deviation(students_scores):
    averages = calculate_averages(students_scores)
    return {
        'Μαθηματικά': math.sqrt(sum([(students_score[1] - averages['Μαθηματικά']) ** 2 for students_score in students_scores]) / (len(students_scores) - 1)),
        'Φυσική': math.sqrt(sum([(students_score[2] - averages['Φυσική']) ** 2 for students_score in students_scores]) / (len(students_scores) - 1)),
        'Αγγλικά': math.sqrt(sum([(students_score[3] - averages['Αγγλικά']) ** 2 for students_score in students_scores]) / (len(students_scores) - 1))
    }

if __name__ == '__main__':
    students_scores = [ ('Alice', 85, 90, 82),  ('Bob', 78, 76, 88),  ('Charlie', 92, 89, 95),  ('David', 70, 72, 68),  ('Eve', 88, 92, 91)]
    print(calculate_std_deviation(students_scores))
