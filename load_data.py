import pandas as pd

DATA_PATH = "../data"

def load_logs():
    logon = pd.read_csv(f"{DATA_PATH}/logon.csv")
    device = pd.read_csv(f"{DATA_PATH}/device.csv")
    http = pd.read_csv(
    f"{DATA_PATH}/http.csv",
    header=None,
    names=["id", "date", "user", "pc", "url"]
    )

    return logon, device, http


if __name__ == "__main__":
    logon, device, http = load_logs()
    print("Logon rows:", len(logon))
    print("Device rows:", len(device))
    print("HTTP rows:", len(http))