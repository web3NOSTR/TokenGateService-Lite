<?php
// API endpoint
$url = 'http://your-flask-app-url/verify-token';

// The message and signature to verify
$data = array(
    'message' => 'Your message to sign',
    'signature' => '0xYourSignature'
);

// Use json_encode to format data as JSON
$options = array(
    'http' => array(
        'header'  => "Content-Type: application/json\r\n",
        'method'  => 'POST',
        'content' => json_encode($data),
    ),
);

$context  = stream_context_create($options);
$result = file_get_contents($url, false, $context);

if ($result === FALSE) {
    // Handle error
    echo 'Error contacting the server.';
}

$response = json_decode($result, true);

if ($response['success']) {
    if ($response['holding']) {
        echo 'The recovered address holds the token.';
    } else {
        echo 'The recovered address does not hold the token.';
    }
} else {
    echo 'Error: ' . $response['error'];
}
?>
