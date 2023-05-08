import requests


class SearchCourse:
    keys = ['编译', 'compile'] # 搜索关键字

    def __init__(self, token):
        self.token = token
        self.headers = {"Authorization": "token " + token}

    def set_keys(self, keys):
        SearchCourse.keys = keys

    def search(self):
        url_list = []
        for page in range(1, 11):
            repo = requests.get("https://api.github.com/search/repositories?q=ustc+course&per_page=100&page=" + str(page), headers=self.headers).json()
            if (len(repo['items']) == 0):
                break
            for item in repo['items']:
                full_name = item['full_name']
                branch = item['default_branch']
                tree_url = 'https://api.github.com/repos/' + full_name + '/git/trees/' + branch + '?recursive=1'
                content = requests.get(tree_url, headers=self.headers)
                if 'tree' not in content.json().keys():
                    continue
                files = full_name.lower()
                for file in content.json()["tree"]:
                    files += file['path'].lower()
                for key in SearchCourse.keys:
                    if key in files:
                        url_list.append('https://github.com/' + full_name)

        return url_list