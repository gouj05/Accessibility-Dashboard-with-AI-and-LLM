fetch("http://127.0.0.1:8000/use-extension", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        name: "translator"
    })
});