<!DOCTYPE html>
<html>
<head>
    <title>Example Table Manager</title>
    <meta charset="UTF-8">
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; }
        input, button { margin: 5px; padding: 8px; }
        table { border-collapse: collapse; width: 100%; margin-top: 20px; }
        th, td { border: 1px solid #ccc; padding: 10px; text-align: left; }
    </style>
</head>
<body>

    <h1>Manage Records</h1>

    <h2>Add New Record</h2>
    <input type="text" id="name" placeholder="Name">
    <input type="email" id="email" placeholder="Email">
    <input type="text" id="status" placeholder="Status">
    <button onclick="addRecord()">Add</button>

    <h2>Update Record</h2>
    <input type="number" id="updateId" placeholder="ID">
    <input type="text" id="updateName" placeholder="New Name">
    <input type="email" id="updateEmail" placeholder="New Email">
    <input type="text" id="updateStatus" placeholder="New Status">
    <button onclick="updateRecord()">Update</button>

    <h2>Delete Record</h2>
    <input type="number" id="deleteId" placeholder="ID">
    <button onclick="deleteRecord()">Delete</button>

    <h2>All Records</h2>
    <button onclick="loadData()">Refresh</button>
    <table id="dataTable">
        <thead>
            <tr>
                <th>ID</th><th>Name</th><th>Email</th><th>Status</th>
            </tr>
        </thead>
        <tbody></tbody>
    </table>

    <script>
        function addRecord() {
            const name = document.getElementById("name").value;
            const email = document.getElementById("email").value;
            const status = document.getElementById("status").value;

            fetch("/insert_record", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ name, email, status })
            })
            .then(response => response.json())
            .then(data => {
                alert(data.message || data.error);
                loadData();
            });
        }

        function updateRecord() {
            const id = document.getElementById("updateId").value;
            const name = document.getElementById("updateName").value;
            const email = document.getElementById("updateEmail").value;
            const status = document.getElementById("updateStatus").value;

            fetch(`/update_record/${id}`, {
                method: "PUT",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ name, email, status })
            })
            .then(response => response.json())
            .then(data => {
                alert(data.message || data.error);
                loadData();
            });
        }

        function deleteRecord() {
            const id = document.getElementById("deleteId").value;

            fetch(`/delete_record/${id}`, {
                method: "DELETE"
            })
            .then(response => response.json())
            .then(data => {
                alert(data.message || data.error);
                loadData();
            });
        }

        function loadData() {
            fetch("/data")
                .then(response => response.json())
                .then(data => {
                    const tbody = document.querySelector("#dataTable tbody");
                    tbody.innerHTML = "";
                    data.forEach(row => {
                        const tr = document.createElement("tr");
                        tr.innerHTML = `<td>${row.id}</td><td>${row.name}</td><td>${row.email || ""}</td><td>${row.status || ""}</td>`;
                        tbody.appendChild(tr);
                    });
                });
        }

        // Initial load
        window.onload = loadData;
    </script>

</body>
</html>
