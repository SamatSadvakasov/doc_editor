from django.db import models
from simple_history.models import HistoricalRecords
import pandas as pd

class Table(models.Model):
    id = models.AutoField(primary_key=True)
    col_1 = models.CharField(max_length=250, blank=True, null=True, verbose_name="№")
    col_2 = models.CharField(max_length=250, blank=True, null=True, verbose_name="ФИО")
    col_3 = models.CharField(max_length=250, blank=True, null=True, verbose_name="ИИН")
    col_4 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Дата рождения")
    col_5 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Номер паспорта")
    col_6 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Гражданство")
    col_7 = models.CharField(max_length=250, blank=True, null=True, verbose_name="прошли проверку ИИН")
    col_8 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Номер мобильного телефона")
    col_9 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Номер2")
    col_10 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Место и сроки пребывания в последние 14 дней до прибытия в Казахстан (укажите страну, область, штат и т.д.)")
    col_11 = models.CharField(max_length=250, blank=True, null=True, verbose_name="номер по базе")
    col_12 = models.CharField(max_length=250, blank=True, null=True, verbose_name="поставлен на учет в прогу")
    col_13 = models.CharField(max_length=250, blank=True, null=True, verbose_name="дата постановки в прогу")
    col_14 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Регион")
    col_15 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Место жительство, либо предпологаемое место проживания")
    col_16 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Место работы")
    col_17 = models.CharField(max_length=250, blank=True, null=True, verbose_name="заражен")
    col_18 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Госпитализирован (да/нет)")
    col_19 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Место госпитализации")
    col_20 = models.CharField(max_length=250, blank=True, null=True, verbose_name="ИИН, ФИО, моб. тел проживающие вместе в домашнем карантине")
    col_21 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Найден (да/нет)")
    col_22 = models.CharField(max_length=250, blank=True, null=True, verbose_name="находится на дозвоне (да/нет)")
    col_23 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Выбыл из РК")
    history = HistoricalRecords()

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['id']
        verbose_name = 'Таблица'
        verbose_name_plural = 'Таблица'



class Document(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание")
    document = models.FileField(upload_to='documents/', verbose_name="Документ")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Время загрузки")
    document_status = [
        ('0', 'Провал'),
        ('1', 'Успеч'),
    ]
    status = models.CharField(max_length=1, choices=document_status, default='0',  verbose_name="Статус документа")
    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        update = kwargs.pop('update', None)
        super(Document, self).save(*args, **kwargs)

        if not update:
            try:

                res = Document.objects.latest('id')
                if str(res.document)[-5:] == '.xlsx':
                    df = pd.read_excel('media/' + str(res.document))
                    df.columns = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
                    for i in range(len(df)):
                        b = Table(
                            col_1 = df[1][i],
                            col_2 = df[2][i],
                            col_3 = df[3][i],
                            col_4 = df[4][i],
                            col_5 = df[5][i],
                            col_6 = df[6][i],
                            col_7 = df[7][i],
                            col_8 = df[8][i],
                            col_9 = df[9][i],
                            col_10 = df[10][i],
                            col_11 = df[11][i],
                            col_12 = df[12][i],
                            col_13 = df[13][i],
                            col_14 = df[14][i],
                            col_15 = df[15][i],
                            col_16 = df[16][i],
                            col_17 = df[17][i],
                            col_18 = df[18][i],
                            col_19 = df[19][i],
                            col_20 = df[20][i],
                            col_21 = df[21][i],
                            col_22 = df[22][i],
                            col_23 = df[23][i]
                        )
                        b.save()

                    tt = Document.objects.get(id=res.id)
                    tt.status='1'
                    tt.save(update=True)
            except:
                print('something wrong')
        else:
            print('not xslx')


    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['id']
        verbose_name = 'Загрузка документа'
        verbose_name_plural = 'Загрузка документа'
