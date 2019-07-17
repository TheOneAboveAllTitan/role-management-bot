# Defines criteria for segregation
def classify(nick_name):
    #nick_name = user.nick
    role_name = nick_name.split('|')[0]        # Splits nick name of user around '|' and take first word
    role_name = role_name.strip()              # remove white spaces
    return role_name


# Returns what name has to be given in newly create role
def get_role_name(user):
    return classify(user)

def is_role_int(role):
    try:
        int(role)
        return True
    except:
        return False

async def create_role(Guild,Role,Permission):
    return await Guild.create_role(name=Role,permissions=Permission)

def role_names(Guild):
    temp = []
    for role in Guild.roles:
        temp+=role.name
    return temp

def get_role_by_name(Guild,role_name):
    for role in role_name(Guild):
        if role.name == role_name:
            return role