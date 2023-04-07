<?php
?>

<!doctype html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.rtl.min.css" integrity="sha384-WJUUqfoMmnfkBLne5uxXj+na/c7sesSJ32gI7GfCk4zO4GthUKhSEGyvQ839BC51" crossorigin="anonymous">
    <!-- Font Awesome (красивые иконки)-->
    <script src="https://kit.fontawesome.com/8f637f460a.js" crossorigin="anonymous"></script>
    <!-- Путь к стилям -->
    <link rel="stylesheet" href="front/CSS/style.css">
    <!--Google Fonts-->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Jura:wght@300;400;500;600;700&family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">

    <title>SMART-генератор</title>
</head>
<body>
<!--Header-->
<?php
include("back/include/header.php");
?>
<!--Панель ввода данных-->

<form class="row justify-content-center" method="post" action="post.php">
    <div class="mb-3 col-12 col-md-4">
        <label for="exampleInput" class="form-label"><h3>Введите ключевые слова</h3><label>
        </div>
    <div class="w-100"></div>
    <div class="mb-3 col-12 col-md-4">
         <input  name="technology" type="text" class="form-control" placeholder="Ваши ключевые слова">
    </div>
    <div class="w-100"></div>
    <button type="submit" class="btn btn-success col-12 col-md-4">Готово</button>
</form>

<!--<div class="container reg_form">-->
<!--    <h2>Введите основную информацию</h2>-->
<!--    <form class="row justify-content-center" method="post" action="index.php">-->
<!--        <div class="mb-3 col-12 col-md-4 err">-->
<!--            <p>--><?php ////=$errMsg?><!--</p>-->
<!--       </div>-->
<!--        <div class="w-100"></div>-->
<!--        <div class="mb-3 col-12 col-md-4">-->
<!--            <label for="exampleInpuTechnology" class="form-label">Введите технологии</label>-->
<!--            <input  name="technology" type="text" class="form-control">-->
<!--            </div>-->
<!--        <div class="w-100"></div>-->
<!--        <div class="mb-3 col-12 col-md-4">-->
<!--            <label for="exampleInputLogin" class="form-label">Фамилия, Имя, Отчество</label>-->
<!--            <input name="FIO" type="FIO" class="form-control">-->
<!--        </div>-->
<!--        <div class="w-100"></div>-->
<!--        <div class="mb-3 col-12 col-md-4">-->
<!--            <label for="exampleInputOMS" class="form-label">Выбор филиала</label>-->
<!--            <select name="filial" class="form-select" aria-label="Выбор филиала">-->
<!--                <option value="0" selected>Выберите филиал</option>-->
<!--                <option value="1">Москва</option>-->
<!--                <option value="2">Ангарск</option>-->
<!--                <option value="3">Владимир</option>-->
<!--                <option value="4">Глазов</option>-->
<!--                <option value="5">Зеленогорск</option>-->
<!--                <option value="6">Ковров</option>-->
<!--                <option value="7">Нижний Новгород</option>-->
<!--                <option value="8">Новосибирск</option>-->
<!--                <option value="9">Новоуральск</option>-->
<!--                <option value="10">Подольск</option>-->
<!--                <option value="11">Санкт-Петербург</option>-->
<!--                <option value="12">Саров</option>-->
<!--                <option value="13">Северск</option>-->
<!--                <option value="14">Электросталь</option>-->
<!--                <option value="15">Волгодонск</option>-->
<!--                <option value="16">Димитровград</option>-->
<!--                <option value="17">Екатеринбург</option>-->
<!--                <option value="18">Железногорск</option>-->
<!--                <option value="19">Заречный</option>-->
<!--                <option value="20">Краснокаменск</option>-->
<!--                <option value="21">Мурманск</option>-->
<!--                <option value="22">Петрозаводск</option>-->
<!--            </select>-->
<!--        </div>-->
<!--        <div class="w-100"></div>-->
<!--        <div class="mb-3 col-12 col-md-4">-->
<!--            <label for="exampleInputOMS" class="form-label">Должность</label>-->
<!--            <select name="job" class="form-select" aria-label="Выбор должности">-->
<!--                <option value="0" selected>Выберите должность</option>-->
<!--                <option value="1">Специалист</option>-->
<!--                <option value="2">Верстальщик</option>-->
<!--            </select>-->
<!--        </div>-->
<!--        <div class="w-100"></div>-->
<!--        <div class="mb-3 col-12 col-md-4">-->
<!--            <label for="exampleInputOMS" class="form-label">Грейд</label>-->
<!--            <select name="grade" class="form-select" aria-label="Выбор грейда">-->
<!--                <option value="0" selected>Выберите грейд</option>-->
<!--                <option value="1">Стажёр</option>-->
<!--                <option value="2">Младший специалист</option>-->
<!--                <option value="3">Специалист</option>-->
<!--                <option value="4">Старший специалист</option>-->
<!--                <option value="5">Ведущий специалист</option>-->
<!--                <option value="6">Эксперт</option>-->
<!--                <option value="7">Старший эксперт</option>-->
<!--                <option value="8">Ведущий эксперт</option>-->
<!--                <option value="9">Архитектор</option>-->
<!--            </select>-->
<!--        </div>-->
<!--        <div class="w-100"></div>-->
<!--        <button type="submit" class="btn btn-success col-12 col-md-4" name="btn-post">Отправить</button>-->
<!--        <div class="w-100"></div>-->
<!--    </form>-->
<!--</div>-->