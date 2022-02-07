from searoth_rigs_lib import *

if __name__ == "__main__":
    print("Starting")
    rigs_stopped = get_stopped_rigs()
    if len(rigs_stopped) == 0:
        print("WARNING: There are curently no stopped rigs")
    for r in rigs_stopped:
        request_body = {
            "rigId": r,
            "action": "START"
        }
        reply = api_call(
            "POST", "/main/api/v2/mining/rigs/status2", "", request_body)
        if reply.status_code == 200:
            print(log_time() + "Start rig requested for {}".format(r))
            print(json.loads(reply.content))
        else:
            print(log_time() + "WARNING: did not start rig {}".format(r))
            print(reply)
