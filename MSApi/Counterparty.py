from typing import Optional

from MSApi import Employee
from MSApi.ObjectMS import ObjectMS, check_init


class Counterparty(ObjectMS):
    def __init__(self, json):
        super().__init__(json)

    @check_init
    def get_id(self) -> str:
        return self._json.get('id')

    @check_init
    def get_account_id(self) -> str:
        return self._json.get('accountId')

    @check_init
    def get_owner(self) -> Optional[Employee]:
        return Employee(self._json.get('owner'))

    @check_init
    def get_shared(self) -> bool:
        return self._json.get('shared')

    @check_init
    def get_name(self) -> str:
        return self._json.get('name')

    @check_init
    def get_actual_address(self) -> Optional[str]:
        return self._json.get('actualAddress')


# meta	Meta	Метаданные Контрагента	—	да	нет
#  ! id	UUID	ID Контрагента	Только для чтения	да	нет
#  ! accountId	UUID	ID учетной записи	Только для чтения	да	нет
#  ! owner	Meta	Владелец (Сотрудник)	—	нет	да
#  ! shared	Boolean	Общий доступ	—	да	нет
# group	Meta	Отдел сотрудника	—	да	да
# syncId	UUID	ID синхронизации	После заполнения недоступен для изменения	нет	нет
# updated	DateTime	Момент последнего обновления Контрагента	Только для чтения	да	нет
#  ! name	String(255)	Наименование Контрагента	Необходимое при создании	да	нет
# description	String(4096)	Комментарий к Контрагенту	—	нет	нет
# code	String(255)	Код Контрагента	—	нет	нет
# externalCode	String(255)	Внешний код Контрагента	—	да	нет
# archived	Boolean	Добавлен ли Контрагент в архив	—	да	нет
# created	DateTime	Момент создания	—	да	нет
# email	String(255)	Адрес электронной почты	—	нет	нет
# phone	String(255)	Номер городского телефона	—	нет	нет
# fax	String(255)	Номер факса	—	нет	нет
#  ! actualAddress	String(255)	Фактический адрес Контрагента	—	нет	нет
# actualAddressFull	Object	Фактический адрес Контрагента с детализацией по отдельным полям. Подробнее тут	—	нет	нет
# accounts	MetaArray	Массив счетов Контрагентов. Подробнее тут	—	да	да
# companyType	Enum	Тип Контрагента. В зависимости от значения данного поля набор выводимых реквизитов контрагента может меняться. Подробнее тут	—	да	нет
# discountCardNumber	String(255)	Номер дисконтной карты Контрагента	—	нет	нет
# state	Meta	Метаданные Статуса Контрагента	—	нет	да
# salesAmount	Int	Сумма продаж	Только для чтения	да	нет
# bonusProgram	Meta	Метаданные активной Бонусной программы	—	нет	да
# bonusPoints	Int	Бонусные баллы по активной бонусной программе	Только для чтения	нет	нет
# files	MetaArray	Метаданные массива Файлов (Максимальное количество файлов - 100)	—	да	да