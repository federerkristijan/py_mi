class SmartContract:

    def apply(self, current_transactions, blocks):

        print("Apply Smart Contract")

        # Block in BC
        for block in blocks:

            # all transactions in a Block
            for transaction in block.transaction:

                # check if artist exist in the existing transactions
                if current_transactions.artist_id == transaction.artist_id:

                    # check if the record is sold
                    if current_transactions.track_id == transaction.track_id:
                        current_transactions.sold = True

