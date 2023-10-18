from django.db import models


class Users(models.Model):
    surname = models.CharField('Фамилия', max_length=50)
    name = models.CharField('Имя', max_length=50)
    middleName = models.CharField('Отчество', max_length=50)
    fullname = models.CharField('Полное имя', max_length=50)
    structuralDivision = models.CharField('Структурное подразделение', max_length=50)
    department = models.CharField('Отдел', max_length=50)
    heldPost = models.CharField('Должность', max_length=50)

    def __str__(self):
        return self.surname + " " + self.name + " " + self.middleName

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'