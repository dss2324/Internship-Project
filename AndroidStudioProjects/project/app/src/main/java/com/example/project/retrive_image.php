<?php
$conn = new mysqli("2409:4080:9e09:6b43:a361:263d:540e:417e192.0.0.4", "username", "password", "database");
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$result = $conn->query("SELECT path FROM Images");
$images = [];
while ($row = $result->fetch_assoc()) {
    $images[] = $row['path'];
}
$conn->close();

echo json_encode($images);
?>
