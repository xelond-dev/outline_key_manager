from outline_vpn.outline_vpn import OutlineVPN as OutlineVPN


class debug:
    def info(message) -> None:
        if debug_keys == True:
            print(f"[Outline Key Manager] [INFO] {message}")
        

    def error(message) -> None:
        print(f"[Outline Key Manager] [ERROR] {message}")


def init(api_url, cert_sha256 = None, debug = False) -> str:
    global client
    global debug_keys
    client = OutlineVPN(api_url, cert_sha256)
    debug_keys = debug
    return client


def init_check() -> int:
    if not 'client' in globals():
        debug.error("Outline Key Manager is not definded. Use Outline_Key_Manager.init(<your_api_key>, debug=<True/False>)")
        return 43 # Exit or Return???


def get_all_keys() -> str:
    init_check()
    all_keys = client.get_keys()
    debug.info(all_keys)
    return all_keys


def get_key(key_to_find) -> str | int:
    init_check()
    for key in client.get_keys():
        if key.name == key_to_find:
            debug.info(key)
            return key
    return 44


def new_key(name = None, renew = False) -> int:
    init_check()
    if get_key(name) == 44 or renew == True:
        debug.info(client.create_key(name))
        return 0
    return 40


def rename_key(old_name, new_name) -> int:
    init_check()
    key_to_rename = get_key(old_name)
    if key_to_rename != 44:
        if client.rename_key(get_key(old_name).key_id, new_name):
            debug.info(f"Key `{old_name}` successfully renamed to `{new_name}`")
            return 0
        else:
            debug.error("Unnamed error. Return status is `-1`.")
            return -1
    else:
        debug.info(f"Key `{old_name}` is not founded.")
        return 44


def set_limit(name, limit_MB) -> int:
    init_check()
    if name != 44:
        if client.add_data_limit(get_key(name).key_id, 1000 * 1000 * limit_MB):
            debug.info(f"Limit {limit_MB}MB is set for `{name}` key.")
            return 0
        else:
            debug.error("Unnamed error. Return status is `-1`.")
            return -1
    else:
        debug.info(f"Key `{name}` is not founded.")
        return 44


def remove_limit(name) -> int:
    init_check()
    if name != 44:
        if client.delete_data_limit(get_key(name).key_id):
            debug.info(f"Limit is unset for `{name}` key.")
            return 0
        else:
            debug.error("Unnamed error. Return status is `-1`.")
            return -1
    else:
        debug.info(f"Key `{name}` is not founded.")
        return 44


def remove_key(name) -> int:
    init_check()
    if name != 44:
        if client.delete_key(get_key(name).key_id):
            debug.info(f"Key `{name}` deleted.")
            return 0
        else:
            debug.error("Unnamed error. Return status is `-1`.")
            return -1
    else:
        debug.info(f"Key `{name}` is not founded.")
        return 44