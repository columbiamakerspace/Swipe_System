import redis


class RedisConnection():
    def __init__(self, uid_regex, user_privileges, host='127.0.0.1', port=6379):
        self.uid_regex = uid_regex
        self.user_privileges = user_privileges
        self.cli = redis.Redis(host=host, port=port)

    def add_user(self, uid, uni, lastname, firstname):
        self.validate_uid(uid)
        self.validate_uni(uni)
        for x in [firstname, lastname]:
            assert isinstance(x, str) and len(x) > 1
        payload = dict(uni=uni, lastname=lastname, firstname=firstname)
        payload.update(self.user_privileges)
        self.cli.hmset(uid, payload)
        print("add user", uid, uni, lastname, firstname)
        # TODO: write to redis with no perms by default

    def change_permissions(self, uid, **user_privileges):
        print("change perms", uid, user_privileges)
        self.validate_uid(uid)
        self.validate_user_privileges(user_privileges)

    def validate_user_privileges(self, user_privileges):
        assert self.user_privileges.issuperset(user_privileges)
        for k, v in user_privileges.items():
            assert isinstance(self.user_privileges[k], v), \
                "%s should have type %s but was %s" % (
                    k, self.user_privileges[k], type(v))

    def validate_uid(self, uid):
        # TODO
        pass

    def validate_uni(self, uni):
        # TODO
        pass

    def fetch_user_profile_data(self, uid, uni):
        if uid is not None:
            user_profile = self.cli.hgetall(uid)
        else:
            # TODO
            raise NotImplemented("lua script uni2uid lookup table")
        return user_profile
