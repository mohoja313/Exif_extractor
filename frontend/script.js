document.getElementById('uploadButton').addEventListener('click', function() {
    const file = document.getElementById('imageInput').files[0];
    if (file) {
        const formData = new FormData();
        formData.append('image', file);

        // Replace with your server's IP address and port
        const serverIP = 'your_servet_ip';
        const serverPort = '5000'; // Or your desired port

        fetch(`http://${serverIP}:${serverPort}/upload`, {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('exifData').innerHTML = JSON.stringify(data, null, 2);
        });
    }
});
