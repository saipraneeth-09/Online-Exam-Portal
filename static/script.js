function startTimer() {
    let timeLeft = 60;  // 60 seconds timer
    const timeDisplay = document.getElementById("time");
    
    const timer = setInterval(function() {
        if (timeLeft <= 0) {
            clearInterval(timer);
            alert("Time's up!");
            document.querySelector('form').submit();  // Automatically submit the form after time runs out
        } else {
            timeDisplay.textContent = timeLeft;
            timeLeft--;
        }
    }, 1000);
}
