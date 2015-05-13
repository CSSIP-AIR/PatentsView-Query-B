<?php
require 'H:/share/Science Policy Portfolio/PatentsView III/Query tool development/Development/Code/PHPMailer/PHPMailerAutoload.php';

$mail = new PHPMailer;

$mail->isSMTP();        
$mail->SMTPDebug = 2;                              // Set mailer to use SMTP
$mail->Host = 'smtp.gmail.com';
$mail->Port = 465;
 // Specify main and backup SMTP servers
$mail->SMTPAuth = true;                               // Enable SMTP authentication
$mail->Username = 'ahmademad@gmail.com';                 // SMTP username
$mail->Password = 'katrinakaif';                           // SMTP password
$mail->SMTPSecure = 'ssl';                            // Enable encryption, 'ssl' also accepted

// $mail->From = 'ahmademad@gmail.com';
$mail->SetFrom("example@gmail.com");
$mail->addAddress('aemad@air.org', 'Ahmad Emad');     // Add a recipient
// $mail->addReplyTo('replyto@example.com', 'First Last');
// $mail->addCC('cc@example.com');
// $mail->addBCC('bcc@example.com');

$mail->WordWrap = 50;                                 // Set word wrap to 50 characters
// $mail->addAttachment('/var/tmp/file.tar.gz');         // Add attachments
// $mail->addAttachment('/tmp/image.jpg', 'new.jpg');    // Optional name
$mail->isHTML(true);                                  // Set email format to HTML

$mail->Subject = 'Here is a test email for PatentsView';
$mail->Body    = 'This is the HTML message body <b>in bold!</b>';
$mail->AltBody = 'This is the body in plain text for non-HTML mail clients';

if(!$mail->send()) {
    echo 'Message could not be sent.';
    echo 'Mailer Error: ' . $mail->ErrorInfo;
} else {
    echo 'Message has been sent';
}