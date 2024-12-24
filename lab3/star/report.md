# Lab 3 Star

1. Прокачаем предыдущее приложение выводом переменной в браузере. Если переменная не указана, то выводится default. 

![alt text](image.png)

![alt text](image-1.png)

2. Был создан helm chart для приложения из предыдущей лабораторной 

![alt text](image-2.png)

3. Укажим переменную в шаблоне

![alt text](image-3.png)

4. Зададим значение переменной 

![alt text](image-4.png)

5. Запустим приложение через команы helm. Перед этим нужно сначала установить helm. 

![alt text](image-5.png)

6. В итоге получаем вывод нашей переменной, которую мы задали.

![alt text](image-6.png)

7. Теперь изменим эту же переменную, создадим еще один файлик с values, где заменим переменную на helm_upgradeю 

8. Введем команду

```bash
helm upgrade app helm/ --values helm/value_upgrade.yaml
```

9. Получим результат

![alt text](image-7.png)

10. Причины использовать helm, чем использовать классический k8s.

1) Чтобы изменить что-то в деплойменте или другом манифесте не нужно создавать новые файлы
2) Есть аналоги dockerhub, только для helm чартов, например https://artifacthub.io/. То есть можно пользоваться чужими чартами
3) Использование возможностей jinja, то есть возможность использования if, for и возможно макросов