def find_duplicates(stores):

    duplicates = []

    for i in range(len(stores)):

        current = stores[i]["store_name"].lower()

    for j in range(i + 1, len(stores)):

        comparison = stores[j]["store_name"].lower()

        if current in comparison or comparison in current:

            duplicates.append(
                (
                    stores[i]["store_name"],
                    stores[j]["store_name"]
                )
            )

return duplicates