from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Subject, Commendation
from random import choice


def find_schoolkid(name):
    try:
        return Schoolkid.objects.get(full_name__contains=name)
    except Schoolkid.MultipleObjectsReturned:
        if name:
            print(f'В базе больше одного ученика с именем, содержащим {name}')
        else:
            print('Введено пустое имя')
    except Schoolkid.DoesNotExist:
        print(f'В базе отсутствуют ученики с именем {name}')


def fix_marks(schoolkid):
    marks = Mark.objects.filter(schoolkid=schoolkid)
    bad_marks = marks.filter(points__lte=3)
    for bad_mark in bad_marks:
        bad_mark.points = 5
        bad_mark.save()


def delete_chastisements(schoolkid):
    Chastisement.objects.filter(schoolkid=schoolkid).delete()


def create_commendation(schoolkid, subject_name):
    schoolkid_year_of_study = schoolkid.year_of_study

    try:
        subject = Subject.objects.get(title=subject_name,
                                      year_of_study=schoolkid_year_of_study)
    except Subject.DoesNotExist:
        print(f'Предмет с названием {subject_name} не найден')

    schoolkid_group_letter = schoolkid.group_letter
    lessons = Lesson.objects.filter(year_of_study=schoolkid_year_of_study,
                                    group_letter=schoolkid_group_letter,
                                    subject=subject)
    lesson = choice(lessons)
    teacher = lesson.teacher
    last_lesson_date = lesson.date
    texts = ['Хвалю!', 'Отлично!', 'Молодец!', 'Так держать!',
            'Один из лучших!', 'Великолепно!', 'Гордимся!', ]
    Commendation.objects.create(text=choice(texts),
                                created=last_lesson_date,
                                schoolkid=schoolkid,
                                subject=subject,
                                teacher=teacher)
