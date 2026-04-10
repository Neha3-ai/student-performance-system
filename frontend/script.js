function predict() {
    console.log("Button clicked");

    let data = {
        study_hours: document.getElementById("study_hours").value,
        sleep_hours: document.getElementById("sleep_hours").value,
        play_hours: document.getElementById("play_hours").value,
        attendance: document.getElementById("attendance").value
    };

    fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(result => {
        console.log(result);

        localStorage.setItem("result", JSON.stringify(result));
        window.location.href = "result.html";
    })
    .catch(err => console.error(err));
}

function exportPDF() {
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF();

    let result = JSON.parse(localStorage.getItem("result"));

    let y = 20;

    doc.setFontSize(16);
    doc.text("Student Performance Report", 20, y);
    y += 10;

    doc.setFontSize(12);
    doc.text("Status: " + result.status, 20, y);
    y += 10;

    // Input values
    doc.text("Input Data:", 20, y);
    y += 10;

    for(let key in result.input){
        doc.text(`${key}: ${result.input[key]}`, 20, y);
        y += 8;
    }

    y += 5;
    doc.text("Suggestion:", 20, y);
    y += 10;

    doc.text(result.suggestion, 20, y);

    // Download
    doc.save("Student_Report.pdf");
}