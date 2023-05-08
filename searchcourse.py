import requests

class SearchCourse:
    keys = ['编译', 'compile'] 

    def __init__(self, token):
        self.token = token
        self.headers = {"Authorization": "token " + token}

    # Set the keyword list
    def set_keys(self, keys):
        SearchCourse.keys = keys

    # Search repositories by keyword and return a list of URLs
    def search(self):
        url_list = []
        for page in range(1, 11):
            # Each page returns up to 100 repositories
            repo = requests.get("https://api.github.com/search/repositories?q=ustc+course&per_page=100&page=" + str(page), headers=self.headers).json()

            # If there are no repositories, stop searching
            if (len(repo['items']) == 0):
                break

            # Search the file list of each repository
            for item in repo['items']:
                full_name = item['full_name']
                branch = item['default_branch']
                tree_url = 'https://api.github.com/repos/' + full_name + '/git/trees/' + branch + '?recursive=1'
                content = requests.get(tree_url, headers=self.headers)

                # If the repository has no files, continue to the next one
                if 'tree' not in content.json().keys():
                    continue

                # Convert file paths to lowercase
                files = full_name.lower()
                for file in content.json()["tree"]:
                    files += file['path'].lower()

                # Check if the file contains any of the keywords, and if so, add the URL of the repository to the URL list
                for key in SearchCourse.keys:
                    if key in files:
                        url_list.append('https://github.com/' + full_name)

        return url_list
