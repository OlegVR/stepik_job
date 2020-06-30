""" Вакансии """

jobs = [

    {"title": "Разработчик на Python", "cat": "backend", "company": "staffingsmarter", "salary_from": "100000",
     "salary_to": "150000", "posted": "2020-03-11", "desc": "Потом добавим",
     "skills": "Django, SQL(PostgreSQl), Unix/Linux, опыт коммерческой разработки на Python от 3 лет"},
    {"title": "Разработчик в проект на Django", "cat": "backend", "company": "swiftattack", "salary_from": "80000",
     "salary_to": "90000", "posted": "2020-03-11", "desc": "Потом добавим",
     "skills": "Linux, Bash, Docker, Git, SQL, уверенные знания Python"},
    {"title": "Разработчик на Swift в аутсорс компанию", "cat": "backend", "company": "swiftattack",
     "salary_from": "120000", "salary_to": "150000", "posted": "2020-03-11", "desc": "Потом добавим",
     "skills": "Git, IOS, Scrum, SQL, Swift, Viper"},
    {"title": "Мидл программист на Python", "cat": "backend", "company": "workiro", "salary_from": "80000",
     "salary_to": "90000", "posted": "2020-03-11", "desc": "Потом добавим",
     "skills": "Python, Django, MySQL, Git, Docker, Flask, SOAP, REST, Linux"},
    {"title": "Питонист в стартап", "cat": "backend", "company": "primalassault", "salary_from": "120000",
     "salary_to": "150000", "posted": "2020-03-11", "desc": "Потом добавим",
     "skills":"Python, HTML, CSS, Git, Docker, HTTP, REAT, Flask"}

]

""" Компании """

companies = [

    {"title": "workiro", "location": "Москва", "description": "Самая класная компания", "employee_count": 233,
     "logo": "../static/logo1.png"},
    {"title": "rebelrage", "location": "Казань", "description": "Наша компания ценит своих сотрудников",
     "employee_count": 2122,
     "logo": "../static/logo2.png"},
    {"title": "staffingsmarter", "location": "Рязань",
     "description": "Молодой стартап приглашает завоевать мир программирования", "employee_count": 10,
     "logo": "../static/logo3.png"},
    {"title": "evilthreat h", "location": "Санкт-Петербург", "description": "Крупная компания с большим именем",
     "employee_count": 2233,
     "logo": "../static/logo4.png"},
    {"title": "hirey", "location": "Нижний Новгород", "description": "Компания по разработке компьютерных игр",
     "employee_count": 541,
     "logo": "../static/logo5.png"},
    {"title": "swiftattack", "location": "Москва", "description": "Занимаемся разработкой beckend-а",
     "employee_count": 197,
     "logo": "../static/logo6.png"},
    {"title": "troller", "location": "Владимир", "description": "Молодой стартап, занимаемся разработкой сайтов",
     "employee_count": 8,
     "logo": "../static/logo7.png"},
    {"title": "primalassault", "location": "Санкт-Петербург", "description": "Выполняем разработку frontend-а",
     "employee_count": 67,
     "logo": "../static/logo8.png"}

]

""" Категории """

specialties = [

    {"code": "frontend", "title": "Фронтенд",
     "picture": "../static/specty_frontend.png"},
    {"code": "backend", "title": "Бэкенд",
     "picture": "../static/specty_backend.png"},
    {"code": "gamedev", "title": "Геймдев",
     "picture": "../static/specty_gamedev.png"},
    {"code": "devops", "title": "Девопс",
     "picture": "../static/specty_devops.png"},
    {"code": "design", "title": "Дизайн",
     "picture": "../static/specty_design.png"},
    {"code": "products", "title": "Продукты",
     "picture": "../static/specty_products.png"},
    {"code": "management", "title": "Менеджмент",
     "picture": "../static/specty_management.png"},
    {"code": "testing", "title": "Тестирование",
     "picture": "../static/specty_testing.png"}

]

""" Статусы в формате Enum """

#
#
# class EducationChoices(Enum):
#     missing = 'Отсутствует'
#     secondary = 'Среднее'
#     vocational = 'Средне-специальное'
#     incomplete_higher = 'Неполное высшее'
#     higher = 'Высшее'
#
#
# class GradeChoices(Enum):
#     intern = 'intern'
#     junior = 'junior'
#     middle = 'middle'
#     senior = 'senior'
#     lead = 'lead'
#
#
# class SpecialtyChoices(Enum):
#     frontend = 'Фронтенд'
#     backend = 'Бэкенд'
#     gamedev = 'Геймдев'
#     devops = 'Девопс'
#     design = 'Дизайн'
#     products = 'Продукты'
#     management = 'Менеджмент'
#     testing = 'Тестирование'
#
#
# class WorkStatusChoices(Enum):
#     not_in_search = 'Не ищу работу'
#     consideration = 'Рассматриваю предложения'
#     in_search = 'Ищу работу'
