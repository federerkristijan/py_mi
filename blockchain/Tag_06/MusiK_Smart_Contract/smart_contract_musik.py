class SmartContract:

    def apply(self, current_transactions, blocks):

        print("Apply Smart Contract")

        # Block in BC
        for block in blocks:

            # all transactions in a Block
            for transaction in block.transaction:

                # check if artist and track exist
                if current_transactions.artist_id and current_transactions.track_id == True:

                    # check if buyer has balance is greater or equal 10
                    if current_transactions.buyer.account.balance >= 10:

                        # check if the record is sold
                        if current_transactions.track_id == transaction.track_id:
                            current_transactions.sold = True
