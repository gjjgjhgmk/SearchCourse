import requests

class SearchCourse:
    def __init__(self, token):
        self.token = token

    def search_course(self, key):
        headers = {"Authorization": "token " + self.token}
        search = 'ustc course ' + key  # 在搜索关键字中添加用户输入的关键字
        search = search.replace(' ', '+')
        url_list = []
        for page in range(1, 11):
            repo = requests.get("https://api.github.com/search/repositories?q=" + search + "&per_page=100&page=" + str(page), headers=headers).json()
            if (len(repo['items']) == 0):
                break
            for item in repo['items']:
                full_name = item['full_name']
                branch = item['default_branch']
                tree_url = 'https://api.github.com/repos/' + full_name + '/git/trees/' + branch + '?recursive=1'
                content = requests.get(tree_url, headers=headers)
                if 'tree' not in content.json().keys():
                    continue
                files = full_name.lower()
                keys=[key] # 改成用户输入的关键字
                for file in content.json()["tree"]:
                    files += file['path'].lower()
                for key in keys:
                    if key in files:
                        url_list.append('https://github.com/' + full_name)

        return url_list