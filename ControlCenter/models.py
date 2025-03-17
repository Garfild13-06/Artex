from django.db import models


class CardTemp(models.Model):
    idcard = models.CharField(max_length=100, primary_key=True, default='')
    idcardgroup = models.IntegerField(null=True, default=None)
    idclient = models.CharField(max_length=100, null=True, default=None)
    number = models.CharField(max_length=200, unique=True, null=True, default=None)
    validitydatebeg = models.DateField(null=True, default=None, help_text='начало периода валидности')
    validitydateend = models.DateField(null=True, default=None, help_text='окончание периода валидности')
    cardSum = models.DecimalField(max_digits=20, decimal_places=2, null=True, default=None,
                                  help_text='Сумма накоплений')
    blocked = models.SmallIntegerField(null=True, default=None)
    multiplicator = models.DecimalField(max_digits=15, decimal_places=2, null=True, default=None)
    multiplicatorbeg = models.DateTimeField(null=True, default=None)
    multiplicatorend = models.DateTimeField(null=True, default=None)
    multiplicatorcurrent = models.DecimalField(max_digits=15, decimal_places=2, null=True, default=None)
    lastKnownBonusBalance = models.DecimalField(max_digits=15, decimal_places=2, null=True, default=None)
    lastKnownBonusBalanceDate = models.DateTimeField(null=True, default=None,
                                                     help_text='Дата и время последнего известного актуального баланса')
    pincode = models.CharField(max_length=100, null=True, default=None,
                               help_text='пароль для доступа к данным пользователя')
    cardstatus = models.IntegerField(null=True, default=None,
                                     help_text='статус карты 0-Анонимная 1-Зарегистрированная 2-Заблокированная')
    discountpercent = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None,
                                          help_text='процент скидки')
    purchases = models.IntegerField(null=True, default=None, help_text='количество покупок')
    crc = models.BigIntegerField(null=True, default=None, help_text='контрольная сумма')
    ownerStoreId = models.CharField(max_length=10, null=True, default=None, help_text='код родительского магазина')
    update_time = models.DateTimeField(auto_now=True, help_text='Для сохранения момента модификации поля')
    shopcode = models.CharField(max_length=255, null=True, default=None, help_text='Код домашнего магазина')

    class Meta:
        managed = False
        db_table = 'cardTemp'
        indexes = [
            models.Index(fields=['idclient']),
            models.Index(fields=['update_time']),
        ]

    def __str__(self):
        return f'{self.idcard}||{self.idclient}||{self.number}||{self.update_time}'


class ClientTemp(models.Model):
    idclient = models.CharField(max_length=100, primary_key=True, default='')
    name = models.CharField(max_length=200, null=True, default=None, help_text='имя клиента')
    text = models.CharField(max_length=200, null=True, default=None, help_text='текст')
    sex = models.IntegerField(null=True, default=None, help_text='пол')
    birthday = models.DateField(null=True, default=None, help_text='день рождения')
    specialdate1 = models.DateField(null=True, default=None, help_text='особая дата 1')
    specialdate2 = models.DateField(null=True, default=None, help_text='особая дата 2')
    specialdate3 = models.DateField(null=True, default=None, help_text='особая дата 3')
    specialdate1name = models.CharField(max_length=200, null=True, default=None, help_text='название особой даты 1')
    specialdate2name = models.CharField(max_length=200, null=True, default=None, help_text='название особой даты 2')
    specialdate3name = models.CharField(max_length=200, null=True, default=None, help_text='название особой даты 3')
    zipcode = models.CharField(max_length=200, null=True, default=None, help_text='почтовый индекс')
    address = models.CharField(max_length=200, null=True, default=None, help_text='адрес')
    email = models.CharField(max_length=200, null=True, default=None, help_text='email')
    webpage = models.CharField(max_length=200, null=True, default=None, help_text='web-страничка')
    phonenumber = models.CharField(max_length=200, null=True, default=None, help_text='номер телефона')
    inn = models.CharField(max_length=200, null=True, default=None, help_text='ИНН')
    document = models.CharField(max_length=200, null=True, default=None, help_text='документ')
    okpo = models.CharField(max_length=200, null=True, default=None, help_text='ОКПО')
    okpd = models.CharField(max_length=200, null=True, default=None, help_text='ОКПД')
    occupation = models.CharField(max_length=200, null=True, default=None, help_text='род занятий')
    childrencount = models.IntegerField(null=True, default=None, help_text='количество детей')
    extendedoptions = models.TextField(null=True, default=None, help_text='тэги')
    codeword = models.CharField(max_length=100, null=True, default=None, help_text='кодовое слово клиента')
    userid = models.CharField(max_length=100, unique=True, null=True, default=None,
                              help_text='идентификатор пользователя')
    update_time = models.DateTimeField(auto_now=True, help_text='Для сохранения момента модификации поля')
    createdate = models.DateTimeField(null=True, default=None)
    organizationcode = models.CharField(max_length=255, null=True, default=None, help_text='код организации')
    subscriptionadj = models.IntegerField(null=True, default=None, help_text='согласие на рассылку')
    crc = models.BigIntegerField(null=True, default=None, help_text='контрольная сумма')
    ownerStoreid = models.CharField(max_length=10, null=True, default=None, help_text='код родительского магазина')
    options = models.IntegerField(null=True, default=None, help_text='дополнительные опции')

    class Meta:
        managed = False
        db_table = 'clientTemp'
        indexes = [
            models.Index(fields=['birthday']),
            models.Index(fields=['codeword']),
            models.Index(fields=['phonenumber']),
            models.Index(fields=['update_time']),
        ]

    def __str__(self):
        return f'{self.idclient}||{self.name}||{self.birthday}||{self.specialdate1}||{self.specialdate1name}||{self.address}||{self.email}||{self.phonenumber}'
