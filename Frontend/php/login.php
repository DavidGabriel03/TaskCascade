<?php
$localhost = "127.0.0.1";
$user = "root";
$database = "TaskFlow";
$connect = mysqli_connect($localhost, $user, "", $database);
if(!$connect){
    echo "Eroare de conexiune la server MySql";
    exit;
}else echo "Conexiunea la base de database";
$username = $_POST['username'];
$password = $_POST['password'];

$query = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
$result = mysqli_query($connect, $query);
if (mysqli_num_rows($result) > 0) {
    echo "User found.";
} else {
    echo "No user found.";
}

