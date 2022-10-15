var currentUsername = "";
var cardsDiv = document.querySelector('#cards')

function getUsername(element) {
    console.log(element.value);
    currentUsername = element.value;
}

// function call_api(username) {
//     fetch("https://api.github.com/users/" + username)
//     .then(response => response.json() )
//     .then(coderData => console.log(coderData) )
//     .catch(err => console.log(err) )

//     console.log(coderData)
// }

function makeCoderCard(data) {
    var res =  `<div class="card">
                    <img src="${data.avatar_url}" alt="${data.login}">
                    <h3>${data.login} - ${data.name}</h3>
                    <p>Location: ${data.location}</p>
                    <p>Repositories: ${data.public_repos}</p>
                </div>`;
    console.log(res);
    return res;
}

async function getCoderData() {
        // The await keyword lets js know that it needs to wait until it gets a response back to continue.
        var response = await fetch("https://api.github.com/users/" + currentUsername);
        // We then need to convert the data into JSON format.
        var coderData = await response.json();
        console.log(coderData);
        // makeCoderCard(coderData)
        cardsDiv.innerHTML = makeCoderCard(coderData) + cardsDiv.innerHTML;
        return coderData;
    }
        
    