from components.tokens import Token


def trial():

    tokens = []
    file_path = ["./architecture/tokens/asn.json", "./architecture/tokens/esn.json"]

    for fp in file_path:
        with open(fp, "r") as file:
            file_content = file.read()

        tokens.append(Token.generateFromJson(json_definition=file_content))

    for t in tokens:
        print(
            t.id,
            t.name,
            t.type,
            t.description,
        )


if __name__ == "__main__":
    trial()
