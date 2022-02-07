from searoth_rigs_lib import *

if __name__ == "__main__":
    print("Starting")
    rigs_mining = get_mining_rigs()
    if len(rigs_mining) == 0:
        print("WARNING: There are curently no running rigs")
    for r in rigs_mining:
        request_body = {
            "rigId": r,
            "action": "STOP"
        }
        reply = api_call(
            "POST", "/main/api/v2/mining/rigs/status2", "", request_body)
        if reply.status_code == 200:
            print(log_time() + "Stop rig requested for {}".format(r))
            print(json.loads(reply.content))
        else:
            print(log_time() + "WARNING: did not stop rig {}".format(r))
            print(reply)
