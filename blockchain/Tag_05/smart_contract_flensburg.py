class SmartContract:

    # ohne Konstruktor bzw. OHNE Eigenschaften
    # NUR mit Methode, um "intelligenten" Vertrag einzusetzen bzw. anzuwenden
    # an offene Transaktionen bevor diese in den Mempool abgelegt werden
    # in Rücksprache mit vorrherigen Transaktionen der Blockchain

    def apply(self, current_transaction, blocks):

        print("apply!")

        for block in blocks: # jeden Block der Blockchain durchlaufen

            for transaction in block.transactions: # jede einzelne Transaktion eines jew. Blocks

                # Check ob die Führerschein-ID bereits vorhanden in vorherigen Transaktionen
                if current_transaction.driving_license_id == transaction.driving_license_id:

                    print("driving_license_id bereits bekannt")

                    # Anzahl der Verstöße wird um 1 erhöht
                    current_transaction.number_of_violations += 1

                    # weiterer Check, ob Füherschein entzogen werden soll
                    # hier: mehr 1 Verstoß: Füherschein weg!
                    if current_transaction.number_of_violations > 1:

                        current_transaction.is_driver_license_suspended = True
                        print("Füherschein entzogen")

                        """
                        a)
                        transaktion(zu schnell, 24.Mai, 5645645475475)
                        b) SmartContract ausgeführt BEVOR Transaktion in den Mempool

                        # Mempool
                        transaktionen.append(transaktion)
                        c)

                        Block(transaktionen)
                        """
