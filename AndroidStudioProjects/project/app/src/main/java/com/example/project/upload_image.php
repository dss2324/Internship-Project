<?php
$servername = "2409:4080:9e09:6b43:a361:263d:540e:417e"; // Correctly formatted IPv6 address
$username = "username";
$password = "password";
$database = "internshipproject";

// Create connection
$conn = new mysqli($servername, $username, $password, $database);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Create table if it doesn't exist
$table_sql = "CREATE TABLE IF NOT EXISTS Images (
    id INT AUTO_INCREMENT PRIMARY KEY,
    file_name VARCHAR(255) NOT NULL,
    file_path VARCHAR(255) NOT NULL,
    file_type VARCHAR(10) NOT NULL,
    file_size INT NOT NULL,
    date_uploaded DATETIME NOT NULL,
    description TEXT
)";

if ($conn->query($table_sql) === TRUE) {
    echo "Table created successfully<br>";
} else {
    echo "Error creating table: " . $conn->error . "<br>";
}

// Check if the table exists
$tableCheck = $conn->query("SHOW TABLES LIKE 'Images'");

if ($tableCheck->num_rows > 0) {
    echo "Table 'Images' exists.<br>";
} else {
    echo "Table 'Images' does not exist.<br>";
}

// Handling file upload
$target_dir = "uploads/";
$file_name = basename($_FILES["file"]["name"]);
$target_file = $target_dir . $file_name;
$imageFileType = strtolower(pathinfo($target_file, PATHINFO_EXTENSION));
$file_size = $_FILES["file"]["size"];
$date_uploaded = date('Y-m-d H:i:s');
$description = $_POST['description'] ?? '';

// Check if image file is an actual image or fake image
if (isset($_POST["submit"])) {
    $check = getimagesize($_FILES["file"]["tmp_name"]);
    if ($check !== false) {
        if (move_uploaded_file($_FILES["file"]["tmp_name"], $target_file)) {
            // Save file path to database
            $stmt = $conn->prepare("INSERT INTO Images (file_name, file_path, file_type, file_size, date_uploaded, description) VALUES (?, ?, ?, ?, ?, ?)");
            $stmt->bind_param("sssiss", $file_name, $target_file, $imageFileType, $file_size, $date_uploaded, $description);
            if ($stmt->execute()) {
                echo json_encode(["message" => "The file " . $file_name . " has been uploaded and path saved to database."]);
            } else {
                echo json_encode(["message" => "Error saving file information to database: " . $stmt->error]);
            }
            $stmt->close();
        } else {
            echo json_encode(["message" => "Sorry, there was an error uploading your file."]);
        }
    } else {
        echo json_encode(["message" => "File is not an image."]);
    }
}

$conn->close();
?>
