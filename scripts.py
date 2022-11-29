from random import choice

from datacenter.models import Chastisement, Commendation, Lesson, Mark, Schoolkid, Subject


COMMENDATION_TEXTS = ['Хвалю!', 'Отлично!', 'Молодец!', 'Так держать!',
                      'Один из лучших!', 'Великолепно!', 'Гордимся!', ]


def find_schoolkid(name):
    try:
        return Schoolkid.objects.get(full_name__contains=name)
    except Schoolkid.MultipleObjectsReturned:
        print(f'В базе больше одного ученика с именем, содержащим {name}')
        return
    except Schoolkid.DoesNotExist:
        print(f'В базе отсутствуют ученики с именем {name}')
        return


def fix_marks(schoolkid):
    marks = Mark.objects.filter(schoolkid=schoolkid)
    marks.filter(points__lte=3).update(points=5)


def delete_chastisements(schoolkid):
    Chastisement.objects.filter(schoolkid=schoolkid).delete()


def create_commendation(schoolkid, subject_name):
    schoolkid_year_of_study = schoolkid.year_of_study

    try:
        subject = Subject.objects.get(title=subject_name,
                                      year_of_study=schoolkid_year_of_study)
    except Subject.DoesNotExist:
        print(f'Предмет с названием {subject_name} не найден')
        return

    schoolkid_group_letter = schoolkid.group_letter
    lessons = Lesson.objects.filter(year_of_study=schoolkid_year_of_study,
                                    group_letter=schoolkid_group_letter,
                                    subject=subject)

    if not lessons:
        lesson = choice(lessons)
    else:
        print('Уроки не найдены')
        return

    teacher = lesson.teacher
    last_lesson_date = lesson.date
    Commendation.objects.create(text=choice(COMMENDATION_TEXTS),
                                created=last_lesson_date,
                                schoolkid=schoolkid,
                                subject=subject,
                                teacher=teacher)
