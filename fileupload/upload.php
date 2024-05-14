<?php
// Init
$fileOwner = 'user';
$uploadDir = '/files/user/';

// Handle file upload
if (isset($_FILES['file'])) {
    $fileName = basename($_FILES['file']['name']);
    $targetFile = $uploadDir . '/' . $fileName;

    // Move the uploaded file
    if (move_uploaded_file($_FILES['file']['tmp_name'], $targetFile)) {
        // File uploaded successfully
    } else {
        // File upload failed
    }
}
?>
