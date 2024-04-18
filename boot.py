import os
from dotenv import load_dotenv

load_dotenv()
boot_choice = os.getenv("BOOT_DEFAULT_STARTUP")
boot_recover = os.getenv("BOOT_RECOVER")
python_version = os.getenv("PYTHON_COMMAND")

boot = True
boot_fail = True
boot_recover_fail = True

for file in os.listdir("."):
    if file.endswith(".py") and file == boot_choice:
        boot_fail = False

if boot_fail and boot:
    for file in os.listdir("."):
        if file.endswith(".py") and file == boot_recover:
            boot_recover_fail = False

if boot_recover_fail and boot:
    print("BOOT RECOVERY HAS FAILED! PLEASE CHECK YOUR .env SETTINGS!!")

if not boot_recover_fail and boot:
    print("STARTING RECOVER SYSTEM")
    os.system(python_version + " " + boot_recover)

if not boot_fail and boot:
    os.system(python_version + " " +  boot_choice)