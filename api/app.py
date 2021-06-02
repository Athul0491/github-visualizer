from flask import Flask
from flask import request, jsonify
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)
token = "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"
headers = {
    "Accept":"application/vnd.github.v3+json",
    "Authorization": f"Token {token}"
}
BASE_URL = "https://api.github.com"


@app.route("/github/<username>/<repo>",methods=["GET"])
def github(username, repo):
    r = requests.get(BASE_URL + f"/repos/{username}/{repo}",headers=headers).json()
    # value of r
    # {
    #     "id": 352987175,
    #     "node_id": "MDEwOlJlcG9zaXRvcnkzNTI5ODcxNzU=",
    #     "name": "Vealize",
    #     "full_name": "techguy940/Vealize",
    #     "private": False,
    #     "owner": {
    #         "login": "techguy940",
    #         "id": 51826754,
    #         "node_id": "MDQ6VXNlcjUxODI2NzU0",
    #         "avatar_url": "https://avatars.githubusercontent.com/u/51826754?v=4",
    #         "gravatar_id": "",
    #         "url": "https://api.github.com/users/techguy940",
    #         "html_url": "https://github.com/techguy940",
    #         "followers_url": "https://api.github.com/users/techguy940/followers",
    #         "following_url": "https://api.github.com/users/techguy940/following{/other_user}",
    #         "gists_url": "https://api.github.com/users/techguy940/gists{/gist_id}",
    #         "starred_url": "https://api.github.com/users/techguy940/starred{/owner}{/repo}",
    #         "subscriptions_url": "https://api.github.com/users/techguy940/subscriptions",
    #         "organizations_url": "https://api.github.com/users/techguy940/orgs",
    #         "repos_url": "https://api.github.com/users/techguy940/repos",
    #         "events_url": "https://api.github.com/users/techguy940/events{/privacy}",
    #         "received_events_url": "https://api.github.com/users/techguy940/received_events",
    #         "type": "User",
    #         "site_admin": False
    #     },
    #     "html_url": "https://github.com/techguy940/Vealize",
    #     "description": "My Submission for Timathon 2021 (Mar-Apr)",
    #     "fork": False,
    #     "url": "https://api.github.com/repos/techguy940/Vealize",
    #     "forks_url": "https://api.github.com/repos/techguy940/Vealize/forks",
    #     "keys_url": "https://api.github.com/repos/techguy940/Vealize/keys{/key_id}",
    #     "collaborators_url": "https://api.github.com/repos/techguy940/Vealize/collaborators{/collaborator}",
    #     "teams_url": "https://api.github.com/repos/techguy940/Vealize/teams",
    #     "hooks_url": "https://api.github.com/repos/techguy940/Vealize/hooks",
    #     "issue_events_url": "https://api.github.com/repos/techguy940/Vealize/issues/events{/number}",
    #     "events_url": "https://api.github.com/repos/techguy940/Vealize/events",
    #     "assignees_url": "https://api.github.com/repos/techguy940/Vealize/assignees{/user}",
    #     "branches_url": "https://api.github.com/repos/techguy940/Vealize/branches{/branch}",
    #     "tags_url": "https://api.github.com/repos/techguy940/Vealize/tags",
    #     "blobs_url": "https://api.github.com/repos/techguy940/Vealize/git/blobs{/sha}",
    #     "git_tags_url": "https://api.github.com/repos/techguy940/Vealize/git/tags{/sha}",
    #     "git_refs_url": "https://api.github.com/repos/techguy940/Vealize/git/refs{/sha}",
    #     "trees_url": "https://api.github.com/repos/techguy940/Vealize/git/trees{/sha}",
    #     "statuses_url": "https://api.github.com/repos/techguy940/Vealize/statuses/{sha}",
    #     "languages_url": "https://api.github.com/repos/techguy940/Vealize/languages",
    #     "stargazers_url": "https://api.github.com/repos/techguy940/Vealize/stargazers",
    #     "contributors_url": "https://api.github.com/repos/techguy940/Vealize/contributors",
    #     "subscribers_url": "https://api.github.com/repos/techguy940/Vealize/subscribers",
    #     "subscription_url": "https://api.github.com/repos/techguy940/Vealize/subscription",
    #     "commits_url": "https://api.github.com/repos/techguy940/Vealize/commits{/sha}",
    #     "git_commits_url": "https://api.github.com/repos/techguy940/Vealize/git/commits{/sha}",
    #     "comments_url": "https://api.github.com/repos/techguy940/Vealize/comments{/number}",
    #     "issue_comment_url": "https://api.github.com/repos/techguy940/Vealize/issues/comments{/number}",
    #     "contents_url": "https://api.github.com/repos/techguy940/Vealize/contents/{+path}",
    #     "compare_url": "https://api.github.com/repos/techguy940/Vealize/compare/{base}...{head}",
    #     "merges_url": "https://api.github.com/repos/techguy940/Vealize/merges",
    #     "archive_url": "https://api.github.com/repos/techguy940/Vealize/{archive_format}{/ref}",
    #     "downloads_url": "https://api.github.com/repos/techguy940/Vealize/downloads",
    #     "issues_url": "https://api.github.com/repos/techguy940/Vealize/issues{/number}",
    #     "pulls_url": "https://api.github.com/repos/techguy940/Vealize/pulls{/number}",
    #     "milestones_url": "https://api.github.com/repos/techguy940/Vealize/milestones{/number}",
    #     "notifications_url": "https://api.github.com/repos/techguy940/Vealize/notifications{?since,all,participating}",
    #     "labels_url": "https://api.github.com/repos/techguy940/Vealize/labels{/name}",
    #     "releases_url": "https://api.github.com/repos/techguy940/Vealize/releases{/id}",
    #     "deployments_url": "https://api.github.com/repos/techguy940/Vealize/deployments",
    #     "created_at": "2021-03-30T12:07:28Z",
    #     "updated_at": "2021-05-27T07:07:56Z",
    #     "pushed_at": "2021-03-31T08:11:54Z",
    #     "git_url": "git://github.com/techguy940/Vealize.git",
    #     "ssh_url": "git@github.com:techguy940/Vealize.git",
    #     "clone_url": "https://github.com/techguy940/Vealize.git",
    #     "svn_url": "https://github.com/techguy940/Vealize",
    #     "homepage": None,
    #     "size": 11236,
    #     "stargazers_count": 37,
    #     "watchers_count": 37,
    #     "language": "HTML",
    #     "has_issues": True,
    #     "has_projects": True,
    #     "has_downloads": True,
    #     "has_wiki": True,
    #     "has_pages": False,
    #     "forks_count": 15,
    #     "mirror_url": None,
    #     "archived": False,
    #     "disabled": False,
    #     "open_issues_count": 0,
    #     "license": None,
    #     "forks": 15,
    #     "open_issues": 0,
    #     "watchers": 37,
    #     "default_branch": "main",
    #     "permissions": {
    #         "admin": False,
    #         "push": False,
    #         "pull": True
    #     },
    #     "temp_clone_token": "",
    #     "network_count": 15,
    #     "subscribers_count": 2
    # }

    if r.get('private') or r.get("message") == "Not Found":
        return jsonify({"success": False, "error":r})
    data = {}
    data["archived"] = r["archived"]
    branch_data = requests.get(r['branches_url'].replace("{/branch}", ""), headers=headers).json()
    data["branch_count"] = len(branch_data)
    commit_data = requests.get(r['commits_url'].replace("{/sha}", ""),headers=headers).json()
    data["commit_count"] = len(commit_data)
    contributor_data = requests.get(r['contributors_url'],headers=headers).json()
    data["contributors"] = {}
    for i in contributor_data:
        data["contributors"][i['login']] = i['contributions']
    data['contributor_count'] = len(contributor_data)
    data['createdAt'] = r['created_at'].replace("T"," ")[:-4]
    data['defaultBranch'] = r['default_branch']
    data['description'] = r['description'] or "No Description Provided"
    data['isForked'] = r['fork']
    data['forksCount'] = r['forks_count']
    # can add the data of whoever forked
    issues_data = requests.get(r['issue_events_url'].replace("{/number}",""), headers=headers).json()
    data['issuesCount'] = len(issues_data)
    # can add info about issues: closed or opened
    data['name'] = r['name']
    data['owner'] = {}
    data['owner']['name'] = r['owner']['login']
    data['owner']['avatarUrl'] = r['owner']['avatar_url']
    data['private'] = r['private']
    data['stargazers']= r['stargazers_count']
    data['url'] = r['url']
    data['success'] = True
    return jsonify(data)