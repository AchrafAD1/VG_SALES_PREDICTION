
fetch(`http://127.0.0.1:5000/get_data`)
            .then(response => response.json())
            .then(data => {
                create_thead(data.keys);
                create_tbody(data.records);
            });
var thead = document.querySelector('#thead')
var tbody = document.querySelector('#tbody')



function create_thead(keys) {
    const tr = document.createElement('tr');
    keys.forEach(key => {
        const th = document.createElement('th');
        th.textContent = key
        tr.appendChild(th);
    });
    thead.appendChild(tr);
};

function create_tbody(records, page = 1) {
    for (let i = (page-1)*50; i < (50*page); i++){
        const tr = document.createElement('tr');
        records[i].forEach(champs => {
            const td = document.createElement('td');
            td.textContent = champs
            tr.appendChild(td);
        })
        tbody.appendChild(tr);
    }
};

