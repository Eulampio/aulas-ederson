for req, item in df.groupby("Requisicao"):
    # item é do tipo DataFrame
    for index, row in item.iterrows():
        # row é do tipo Series
        print(row)    # Substitua estas duas linhas pelo o que você
        print("---")  # precisa para o cadastro.