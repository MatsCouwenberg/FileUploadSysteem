<?php
// Init
$uploadDir = '/files/';
$fileOwner = 'user1'; //moet endpoint worden dat owner van het project ophaalt
$projectNaam = 'project1'; //moet endpoint worden dat projectnaam ophaalt

// Handle file upload
if (isset($_FILES['file'])) {
    $fileName = basename($_FILES['file']['name']);
    $targetDir = $uploadDir . $fileOwner . '/' . $projectNaam . '/';
    $targetFile = $targetDir . $fileName;

    // Dir maken als het niet bestaat
    if (!file_exists($targetDir)) {
        mkdir($targetDir, 0777, true);
    }

    // Move the uploaded file
    if (move_uploaded_file($_FILES['file']['tmp_name'], $targetFile)) {
        // File uploaded successfully
    } else {
        // File upload failed
    }
}
?>