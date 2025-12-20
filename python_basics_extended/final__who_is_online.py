def who_is_online(friends: list) -> dict:
    status_list = {}
    # iterar user de um em um
    for user in friends:
        # se status for online
        if user["status"] == "online":
        # se lastActivity > 10
            if user["lastActivity"] > 10:
                # adiciona a chave caso não exista e faz append de valores.
                status_list.setdefault("away", []).append(user["username"])
            else:
                status_list.setdefault("online",[]).append(user["username"])
        else:
            status_list.setdefault("offline", []).append(user["username"])
    return status_list
