data = {
    "login": "fujohn",
    "id": 42927798,
    "node_id": "MDQ6VXNlcjQyOTI3Nzk4",
    "avatar_url": "https://avatars.githubusercontent.com/u/42927798?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/fujohn",
    "html_url": "https://github.com/fujohn",
    "followers_url": "https://api.github.com/users/fujohn/followers",
    "following_url": "https://api.github.com/users/fujohn/following{/other_user}",
    "gists_url": "https://api.github.com/users/fujohn/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/fujohn/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/fujohn/subscriptions",
    "organizations_url": "https://api.github.com/users/fujohn/orgs",
    "repos_url": "https://api.github.com/users/fujohn/repos",
    "events_url": "https://api.github.com/users/fujohn/events{/privacy}",
    "received_events_url": "https://api.github.com/users/fujohn/received_events",
    "type": "User",
    "site_admin": false,
    "name": "John Fu",
    "company": "Amazon",
    "blog": "https://www.linkedin.com/in/johnfu27/",
    "location": "Bay Area and Seattle Area",
    "email": null,
    "hireable": null,
    "bio": "Data Analyst | Aspiring Software Engineer | Active Coding Dojo Part-Time Software Development Student",
    "twitter_username": null,
    "public_repos": 8,
    "public_gists": 0,
    "followers": 0,
    "following": 0,
    "created_at": "2018-09-03T06:55:39Z",
    "updated_at": "2022-10-09T22:32:51Z"
}

function call_api(username) {
    fetch("https://api.github.com/users/" + username)
    .then(response => response.json() )
    .then(coderData => console.log(coderData) )
    .catch(err => console.log(err) )

    console.log(coderData)
}

async function getCoderData() {
        // The await keyword lets js know that it needs to wait until it gets a response back to continue.
        var response = await fetch("https://api.github.com/users/fujohn");
        // We then need to convert the data into JSON format.
        var coderData = await response.json();
        return coderData;
    }
        
    console.log(getCoderData());
    