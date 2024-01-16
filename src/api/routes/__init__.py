from api.routes.r_users import RUsers

def init(api_ref):
    api_ref.add_resource(RUsers, *RUsers.paths)
