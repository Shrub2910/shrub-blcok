class Player:
    def __init__(self, data):
        self._player_data = data["player"]

        self.uuid = self._player_data.get("uuid")
        self.displayname = self._player_data.get("displayname")
        self.package_rank = self._player_data.get("packageRank")
        self.new_package_rank = self._player_data.get("newPackageRank")
        self.monthly_package_rank = self._player_data.get("monthlyPackageRank")
        self.first_login = self._player_data.get("firstLogin")
        self.last_login = self._player_data.get("lastLogin")
        self.last_logout = self._player_data.get("lastLogout")
        self.stats = self._player_data.get("stats")
