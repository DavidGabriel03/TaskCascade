// script.js
fetch("http://localhost:5000/tasks")
  .then(response => response.json())
  .then(data => {
    console.log(data); // afișează taskurile în consolă
  });

function addTask() {
  fetch('/tasks', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      id: 1,
      name: "Test",
      description: "Test descriere",
      status: "ToDo",
      start_time: "2025-05-20",
      end_time: "2025-05-21"
    })
  })
  .then(response => response.json())
  .then(data => alert(data.message))
  .catch(error => console.error('Eroare:', error));
}