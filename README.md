Проект был создан для того, чтобы облегчить подсчет итоговых оценок.

Многие из нас сталкиваются с тем, что теряют чувство контроля из-за системы накопленной оценки в Вышке: непонятно, как хорошо ты уже поработал и приходится постоянно искать формулы и заниматься подсчетом оценки. Я долгое время вела такие "таблицы оценок" в экселе, но решила, что раз уж я теперь программист, пора это автоматизировать. Теперь оценки считать намного проще!

Приложение представляет из себя набор страниц, на каждой из которой вас ждут готовые формы для вставки туда своей оценки по какой-то форме контроля. После постановки всех оценок автоматически подсчитывается итоговая оценка (без округления, в силу того что правила округления везде разные). Кроме того, на главной странице есть возможность посидеть и почитать анекдотов, чтобы не расстраиваться так сильно из-за оценок (это всего лишь цифры!)

Реализовано приложение на Python с использованием Flask, кроме этого я занималась написанием html-кода, задействовав готовые конструкции Bootstrap. Отбор анекдота происходит путем Web scrapping html-кода страницы с помощью BeaBeautifulSoup.
