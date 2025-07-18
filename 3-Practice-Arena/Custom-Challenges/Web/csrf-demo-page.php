<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $new_email = $_POST['email'];
    echo "Email berhasil diganti menjadi: " . htmlspecialchars($new_email);
}
?>

<form method="POST" action="csrf-demo-page.php">
  <label>Ganti Email:</label>
  <input type="email" name="email" required>
  <input type="submit" value="Submit">
</form>