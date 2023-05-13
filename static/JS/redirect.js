document.addEventListener("DOMContentLoaded", function() {
    const response_log = document.getElementById('responselog').textContent
    console.log(response_log)
    const temp = document.getElementById('redirect').textContent;
    document.location.href = temp
})