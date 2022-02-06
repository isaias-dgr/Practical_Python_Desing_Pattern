import csv


class UserFetcher:

    def __init__(self, source):
        self.source = source

    def fetch_users(self):
        with open(self.source, 'r') as cvs_file:
            reader = csv.DictReader(csv_file)
            users = [x for row in reader]

        return users
