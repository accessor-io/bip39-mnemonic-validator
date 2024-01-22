from bip_utils import Bip39MnemonicValidator, Bip39WordsNum, Bip39Languages

def validate_mnemonic(mnemonic):
    try:
        Bip39MnemonicValidator(Bip39Languages.ENGLISH).Validate(mnemonic)
        return True
    except:
        return False

def process_mnemonics(file_path):
    valid_mnemonics = []
    with open(file_path, "r") as file:
        mnemonics = file.readlines()

    for mnemonic in mnemonics:
        if validate_mnemonic(mnemonic.strip()):
            valid_mnemonics.append(mnemonic.strip())

    with open(file_path, "w") as file:
        for mnemonic in valid_mnemonics:
            file.write(mnemonic + '\n')

    print(f"Processed {len(mnemonics)} mnemonics. {len(valid_mnemonics)} valid mnemonics written back to the file.")

# Usage
file_path = "mnemonics.txt"
process_mnemonics(file_path)

