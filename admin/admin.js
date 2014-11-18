function init() {
    var ROOT = 'https://practical-well-728.appspot.com/_ah/api';
    gapi.client.load('devfest_cdh_api', 'v1', function () {
        console.log("loaded")

        refresh();

        //handlers
        document.getElementById('userAdd').addEventListener("submit", addUser, false);
        document.getElementById('questAdd').addEventListener("submit", addQuest, false);
    }, ROOT);
}

function addQuest(e) {
    e.preventDefault();
    gapi.client.devfest_cdh_api.quests.addQuest({
        "name": document.querySelector('#questAdd input[name=name]').value,
        "points": document.querySelector('#questAdd input[name=points]').value,
        "faction": document.querySelector('#questAdd select[name=faction]').value
    }).execute(function (resp) {
        if(resp.code && resp.code != 200)
             emitMessage("Quest not added " + JSON.stringify(resp), "danger");
        else {
            emitMessage("Added quest " + JSON.stringify(resp), "success");
            refresh();
        }
    });
}

function addUser(e) {
    e.preventDefault();
    gapi.client.devfest_cdh_api.users.addUser({
        "name": document.querySelector('#userAdd input[name=name]').value,
        "email": document.querySelector('#userAdd input[name=email]').value
    }).execute(function (resp) {
        if(resp.code && resp.code != 200)
             emitMessage("User not added " + JSON.stringify(resp), "danger");
        else {
            emitMessage("Added user " + JSON.stringify(resp), "success");
            refresh();
        }
    });
}

function setFaction(e) {
    e.preventDefault();

    gapi.client.devfest_cdh_api.users.setFaction({
        "user_id": e.target.querySelector('input[name=userId]').value,
        "faction_id": e.target.querySelector('select[name=factionId]').value
    }).execute(function (resp) {
        if(resp.code && resp.code != 200)
             emitMessage("faction NOT set " + JSON.stringify(resp), "danger");
        else {
            emitMessage("faction set " + JSON.stringify(resp), "success");
            refresh();
        }
    });
}


function refresh() {
    gapi.client.devfest_cdh_api.users.list().execute(function (resp) {
        var tableBody = document.querySelector('#userTable tbody');
        while (tableBody.firstChild) {
            tableBody.removeChild(tableBody.firstChild);
        }

        for (userId in resp.user) {
            var userRow = document.createElement('tr');

            var nameTd = document.createElement("td");
            nameTd.innerText = resp.user[userId].name;
            var emailTd = document.createElement("td");
            emailTd.innerText = resp.user[userId].email;
            var factionTd = document.createElement("td");
            factionTd.innerText = resp.user[userId].faction;
            var formTd = document.createElement("td");

            var form = document.createElement("form");
            form.setAttribute("id", "setFraction"+resp.user[userId].id);
            form.className = "setFactionForm form-inline";

            var select = document.createElement("select");
            select.setAttribute('name',"factionId");
            select.className = "form-control input-sm";
            var factions = [1, 2, 3];
            for(option in factions) {
                var opt = document.createElement("option");
                opt.setAttribute('value', factions[option]);
                opt.innerText = factions[option];
                select.appendChild(opt);
            }
            form.appendChild(select);

            var hidden = document.createElement("input");
            hidden.setAttribute('type',"hidden");
            hidden.setAttribute('name',"userId");
            hidden.setAttribute('value',resp.user[userId].id);
            form.appendChild(hidden);

            var submit = document.createElement("input");
            submit.setAttribute('type',"submit");
            submit.setAttribute('value',"Set");
            submit.className = "btn btn-default";
            form.appendChild(submit);

            formTd.appendChild(form);

            userRow.appendChild(nameTd);
            userRow.appendChild(emailTd);
            userRow.appendChild(factionTd);
            userRow.appendChild(formTd);

            document.querySelector('#userTable tbody').appendChild(userRow);
        }

        var forms = document.querySelectorAll('.setFactionForm');

        for(form in forms) {
            if(!isNaN(form))
                forms[form].addEventListener("submit", setFaction, false);
        }
    });
}

var msgCounter = 0;

function emitMessage(text, type) {
    var msgBox = document.querySelector("#messageBox");
    var msgElm = document.createElement('div');
    msgElm.setAttribute('id', "message" + msgCounter);
    msgElm.className = "alert alert-" + type;
    msgElm.innerText = text;
    msgBox.appendChild(msgElm);

    setTimeout(function (msgId) {
        document.querySelector("#messageBox").removeChild(
            document.querySelector("#message" + msgId)
        );
    }, 1000, msgCounter);

    msgCounter++;
}
