# -*- coding: utf-8 -*-
import json
import time
import hashlib

class BCHCashFusionMerchant:
    def __init__(self, merchant_address: str, token_category: str):
        self.merchant_address = merchant_address
        self.token_category = token_category

    def generate_bip21_invoice(self, amount_bch: float, token_amount: int, order_desc: str) -> dict:
        invoice_id = hashlib.sha256(f"{self.merchant_address}:{amount_bch}:{time.time()}".encode()).hexdigest()[:12]
        bip21_uri = f"bitcoincash:{self.merchant_address}?amount={amount_bch}&category={self.token_category}&token={token_amount}&desc={order_desc}"
        return {
            "invoice_id": f"bch_inv_{invoice_id}",
            "merchant_address": self.merchant_address,
            "bip21_uri": bip21_uri,
            "amount_bch": amount_bch,
            "token_amount": token_amount,
            "token_category": self.token_category,
            "order_description": order_desc,
            "qr_payload": bip21_uri,
            "timestamp": int(time.time())
        }

if __name__ == "__main__":
    merchant = BCHCashFusionMerchant("bitcoincash:qp3wjpa3tjlj042z2wv7hahsldgwhwy0rq9sywjpyy", "d3adb33f00000000000000000000000000000000000000000000000000000000")
    inv = merchant.generate_bip21_invoice(0.045, 100, "Enterprise Cloud Compute Subscription")
    print("BCH Merchant Invoice:", json.dumps(inv, indent=2))
