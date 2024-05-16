// Init
const uploadDir = '/files/';
const fileOwner = 'user1'; //moet endpoint worden dat owner van het project ophaalt
const projectNaam = 'project1'; //moet endpoint worden dat projectnaam ophaalt

// Event listener for the upload button
document.getElementById('uploadButton').addEventListener('click', function() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];

    if (file) {
        const formData = new FormData();
        formData.append('file', file);

        // Send file to upload.php
        fetch('upload.php', {
            method: 'POST',
            body: formData
        })
            .then(response => {
                if (response.ok) {
                    // Clear file input
                    fileInput.value = '';

                    // Prepare data for API call
                    const fileName = file.name;
                    const filePath = uploadDir + fileOwner + '/' + projectNaam + '/' + fileName;

                    const postData = {
                        filename: fileName,
                        path: filePath,
                        username: fileOwner
                    };

                    // Send data to API endpoint
                    fetch('http://10.0.99.141:8000/upload/', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(postData)
                    })
                        .then(apiResponse => {
                            if (apiResponse.ok) {
                                console.log('Data successfully sent to API');
                                // Fetch and display files list after successful upload and API call
                                fetchFilesList();
                            } else {
                                console.error('Error sending data to API:', apiResponse.statusText);
                            }
                        })
                        .catch(apiError => {
                            console.error('Error sending data to API:', apiError);
                        });
                } else {
                    console.error('Error uploading file:', response.statusText);
                }
            })
            .catch(uploadError => {
                console.error('Error uploading file:', uploadError);
            });
    }
});

// Function to fetch and display files list
function fetchFilesList() {
    fetch('http://10.0.99.141:8000/files/')
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error('Failed to fetch files list');
            }
        })
        .then(files => {
            const filesListContainer = document.getElementById('filesList');
            filesListContainer.innerHTML = ''; // Clear previous content

            // Display each file's data as it comes from the API endpoint
            files.forEach(file => {
                const fileData = document.createElement('div');
                fileData.textContent = JSON.stringify(file);
                filesListContainer.appendChild(fileData);
            });
        })
        .catch(error => {
            console.error('Error fetching files list:', error);
        });
}

// Call the fetchFilesList function when the page loads
window.addEventListener('load', fetchFilesList);

