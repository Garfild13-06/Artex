from django.db import models


class Account(models.Model):
    accountId = models.CharField(max_length=255, primary_key=True)
    number = models.CharField(max_length=255, help_text='номер счета')

    class Meta:
        managed = False
        db_table = 'account'
        indexes = [
            models.Index(fields=['number'], name='accountNumber'),
        ]

    def __str__(self):
        return f'{self.accountId}||{self.number}'


class Asset(models.Model):
    id = models.BigAutoField(primary_key=True)
    dateFromCash = models.DateTimeField(null=True, default=None, help_text='время проведения операции на кассе')
    amount = models.BigIntegerField(default=0, help_text='сумма операции')
    date = models.DateTimeField(null=True, default=None, help_text='время создания операции на сервере')
    lastStatus = models.CharField(max_length=100, null=True, default=None, help_text='актуальный статус операции')
    sessionId = models.CharField(max_length=255, null=True, default=None, help_text='идентификатор сессии')
    status = models.CharField(max_length=100, null=True, default=None, help_text='тип операции')
    accountNumber = models.CharField(max_length=255, null=True, default=None, help_text='номер счета')
    assetGroupId = models.CharField(max_length=255, null=True, default=None, help_text='идентификатор группы')
    cardNumber = models.CharField(max_length=255, null=True, default=None, help_text='номер карты')
    terminalNumber = models.CharField(max_length=255, null=True, default=None, help_text='номер терминала')
    additionalInfo = models.CharField(max_length=1024, null=True, default=None,
                                      help_text='дополнительная информация по операции (сериализованный json)')
    update_time = models.DateTimeField(auto_now_add=True, help_text='Для сохранения момента изменения операции')
    lastSource = models.CharField(max_length=255, null=True, default=None,
                                  help_text='Последний источник начисления бонусов')
    lastReason = models.CharField(max_length=255, null=True, default=None,
                                  help_text='Последняя причина начисления бонусов')

    class Meta:
        managed = False
        db_table = 'asset'
        indexes = [
            models.Index(fields=['assetGroupId'], name='assetGroupIdIndex'),
            models.Index(fields=['cardNumber'], name='cardNumberIndex'),
            models.Index(fields=['terminalNumber'], name='terminalNumberIndex'),
            models.Index(fields=['sessionId'], name='sessionIdIndex'),
            models.Index(fields=['update_time'], name='update_timeIndex'),
            models.Index(fields=['accountNumber', 'date'], name='accountNumberAndDateIndex'),
        ]

    def __str__(self):
        return f'{self.id}||{self.dateFromCash}||{self.amount}||{self.date}||{self.lastStatus}||{self.sessionId}||{self.status}||{self.accountNumber}||{self.assetGroupId}||{self.cardNumber}||{self.terminalNumber}||{self.additionalInfo}||{self.update_time}||{self.lastSource}||{self.lastReason}'


class AssetGroup(models.Model):
    internalId = models.CharField(max_length=255, primary_key=True)
    begin = models.DateTimeField(null=True, default=None, help_text='начало действия группы')
    end = models.DateTimeField(null=True, default=None, help_text='окончание действия группы')
    groupId = models.CharField(max_length=255, null=True, default=None, help_text='идентификатор группы')
    weight = models.IntegerField(null=True, default=None, help_text='вес группы')

    class Meta:
        managed = False
        db_table = 'assetGroup'
        indexes = [
            models.Index(fields=['groupId'], name='group_idIndex'),
        ]

    def __str__(self):
        return f'{self.internalId}||{self.begin}||{self.end}||{self.groupId}||{self.weight}'


class AssetGroupTransaction(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=50, help_text='тип изменяемых данных')
    date = models.DateTimeField(null=True, default=None, help_text='новое значение времени')
    dateOfOperation = models.DateTimeField(null=True, default=None, help_text='время изменения')
    weight = models.IntegerField(null=True, default=None, help_text='новое значение веса')
    group_id = models.CharField(max_length=255, null=True, default=None, help_text='идентификатор группы')
    terminalNumber = models.CharField(max_length=255, null=True, default=None, help_text='номер терминала')

    class Meta:
        managed = False
        db_table = 'assetGroupTransaction'
        indexes = [
            models.Index(fields=['group_id']),
            models.Index(fields=['terminalNumber']),
        ]

    def __str__(self):
        return f'{self.id}||{self.type}||{self.date}||{self.dateOfOperation}||{self.weight}||{self.group_id}||{self.terminalNumber}'


class AssetTransactionStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=50, help_text='тип изменяемых данных')
    date = models.DateTimeField(null=True, default=None, help_text='новое значение времени')
    dateOfOperation = models.DateTimeField(null=True, default=None, help_text='время изменения')
    weight = models.IntegerField(null=True, default=None, help_text='новое значение веса')
    group_id = models.CharField(max_length=255, null=True, default=None, help_text='идентификатор группы')
    terminalNumber = models.CharField(max_length=255, null=True, default=None, help_text='номер терминала')

    class Meta:
        managed = False
        db_table = 'assetTransactionStatus'
        indexes = [
            models.Index(fields=['group_id']),
            models.Index(fields=['terminalNumber']),
        ]

    def __str__(self):
        return f'{self.id}||{self.type}||{self.date}||{self.dateOfOperation}||{self.weight}||{self.group_id}||{self.terminalNumber}'


class CardAccounting(models.Model):
    idcard = models.CharField(max_length=255, primary_key=True, unique=True)
    number = models.CharField(max_length=255, null=True, default=None, unique=True, help_text='номер карты')
    status = models.CharField(max_length=255, null=True, default=None, help_text='тип операции')
    accountNumber = models.CharField(max_length=255, null=True, default=None, help_text='номер аккаунта')
    lastKnownBonusBalance = models.DecimalField(max_digits=8, decimal_places=2, null=True, default=None,
                                                help_text='Последний известный актуальный баланс')
    lastKnownBonusBalanceDate = models.DateTimeField(null=True, default=None,
                                                     help_text='Дата и время последнего известного актуального баланса')
    additionalStatus = models.TextField(null=True, default=None)

    class Meta:
        managed = False
        db_table = 'cardAccounting'
        indexes = [
            models.Index(fields=['number']),
            models.Index(fields=['accountNumber']),
        ]

    def __str__(self):
        return f'{self.idcard}||{self.number}||{self.status}||{self.accountNumber}||{self.lastKnownBonusBalance}||{self.lastKnownBonusBalanceDate}||{self.additionalStatus}'


class CardTransaction(models.Model):
    id = models.BigAutoField(primary_key=True)
    operationDate = models.DateTimeField(null=True, default=None, help_text='время изменений')
    status = models.CharField(max_length=255, null=True, default=None, help_text='новый статус карты')
    card_id = models.CharField(max_length=255, null=True, default=None, help_text='идентификатор карты')
    terminalNumber = models.CharField(max_length=255, null=True, default=None, help_text='номер терминала')
    accountNumber = models.CharField(max_length=255, null=True, default=None, help_text='номер счета карты')

    class Meta:
        managed = False
        db_table = 'cardTransaction'
        indexes = [
            models.Index(fields=['card_id']),
            models.Index(fields=['terminalNumber']),
        ]

    def __str__(self):
        return f'{self.id}||{self.operationDate}||{self.status}||{self.card_id}||{self.terminalNumber}||{self.accountNumber}'
